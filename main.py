from fastapi import FastAPI,HTTPException
import uvicorn
from uuid import uuid4,UUID
from models import User, Gender
from typing import List

app = FastAPI()

users: List[User] = [
    User(id=uuid4(),
         name='Arslan',
         gender=Gender.male,
         age=20
         ),
    User(id=uuid4(),
         name='Dayanch',
         gender=Gender.male,
         age=21
         ),
]


@app.get('/')
async def get_main():
    return {"Welcome"}


@app.get('/api/v1/users')
async def get_users():
    return users


@app.post('/api/v1/users')
async def add_user(user: User):
    users.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id:UUID):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Use with id:{user_id} does not exists"
    )


if __name__ == "__main__":
    uvicorn.run(app)
