from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.crud import create_user
from app.schemas import UserSchema

app = FastAPI(name="auth", description="Auth service")
app.title = "Auth service"


@app.get("/connection/")
async def root():
    return {"message": "Connected to auth service"}

@app.post("/register/", response_model=UserSchema)
async def register_user(user: UserSchema, db: AsyncSession = Depends(get_db)):
    return await create_user(db=db, user=user)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
