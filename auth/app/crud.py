from fastapi import HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .models import User
from .schemas import UserSchema


async def create_user(user: UserSchema, db: AsyncSession):
    result = await db.execute(select(User).filter(User.email == user.email))
    if exists_user := result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким email уже существует"
        )

    db_user = User(username=user.username, email=user.email,
                   password=user.password)

    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
