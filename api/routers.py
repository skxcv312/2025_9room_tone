from fastapi import FastAPI, APIRouter
from api.endpoints import article_summary

api_router = APIRouter() # 라우터 연결


api_router.include_router(article_summary.router)
