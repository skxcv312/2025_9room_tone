import uvicorn
from fastapi import FastAPI
from api.routers import api_router
from core.config import settings
from core.exception import exception_handler
from core.exception.exception_handler import register_exception_handlers

app = FastAPI()

app.include_router(api_router, prefix="/api")


# 전역 예외 핸들러 등록
register_exception_handlers(app)

# 실행 진입점
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
