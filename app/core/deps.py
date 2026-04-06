from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.core.config import settings

security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    print("=== DEBUG: Token received:", credentials.credentials[:50] + "...")  # Debug

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        token = credentials.credentials
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        print("=== DEBUG: Email from token:", email)   # Debug

        if email is None:
            raise credentials_exception
    except JWTError as e:
        print("=== DEBUG: JWT Error:", str(e))   # Debug
        raise credentials_exception
    
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        print("=== DEBUG: User not found in database")
        raise credentials_exception
    
    print("=== DEBUG: User authenticated successfully:", user.email)
    return user