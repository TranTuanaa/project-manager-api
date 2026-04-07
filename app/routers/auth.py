from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.core.security import get_password_hash, verify_password, create_access_token, create_refresh_token
from app.core.config import settings   # ← Import settings

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# Register
@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    
    db_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Login
@router.post("/login")
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_credentials.email).first()
    
    if not user or not verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.email})
    refresh_token = create_refresh_token(data={"sub": user.email})
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name
        }
    }

# Refresh Token
@router.post("/refresh")
def refresh(token_data: dict, db: Session = Depends(get_db)):
    try:
        refresh_token = token_data.get("refresh_token")
        if not refresh_token:
            raise HTTPException(status_code=400, detail="Refresh token is required")
        
        payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token type")
        
        email: str = payload.get("sub")
        user = db.query(User).filter(User.email == email).first()
        
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        
        new_access_token = create_access_token(data={"sub": user.email})
        
        return {
            "access_token": new_access_token,
            "token_type": "bearer"
        }
        
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")