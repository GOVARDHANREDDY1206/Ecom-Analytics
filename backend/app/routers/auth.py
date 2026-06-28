from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user import UserCreate
from app.schemas.user import UserResponse
from app.services.auth_service import create_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserResponse, status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):

    new_user = create_user(db, user)

    if new_user is None:
        raise HTTPException(status_code=400, detail="Email already registered")

    return new_user
