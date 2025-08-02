from fastapi import Depends
from app.utils.auth_utils import create_access_token
from app.models.user import UserCreate
from app.db.mongo import db
from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
async def login(user: UserCreate):
    db_user = db.users.find_one({"email": user.email})
    if db_user:
        token = create_access_token({"sub": db_user["user_id"]})
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")
