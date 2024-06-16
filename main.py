from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


class TelegramUser(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str = None
    photo_url: str = None
    auth_date: int
    hash: str

@app.post("/auth/telegram")
async def auth_telegram(user: TelegramUser):
    # Валидация данных пользователя (например, проверка подписи hash)
    # Сохранение данных в базу или другая обработка
    return {"message": "User data received successfully"}


@app.get("/")
async def read_root():
    return {"Hello": "World"}
