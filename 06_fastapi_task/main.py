from fastapi import FastAPI

from app.configs.database import initialize_tortoise
from app.routers.movies import movie_router
from app.routers.likes import like_router
from app.routers.reviews import review_router
from app.routers.users import user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(movie_router)
app.include_router(review_router)  # 추가됨
app.include_router(like_router)  # 추가됨

initialize_tortoise(app=app)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)
