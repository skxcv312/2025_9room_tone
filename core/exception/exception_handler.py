from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette import status
from core.exception.custom_exception import NewsSummaryError


def error_response(exc: Exception, error_code : str, status_code: int) -> JSONResponse:
    # 로그 출력
    print(f"[ERROR] {exc}")

    return JSONResponse(
        status_code=status_code,
        content={
            "status_code": status_code,
            "error_code" : error_code,
            "message": str(exc)  # 개발용 상세 메시지
        },
    )


def register_exception_handlers(app):
    # 커스텀 예외 핸들러
    @app.exception_handler(NewsSummaryError)
    async def news_summary_exception_handler(request: Request, exc: NewsSummaryError):
        return error_response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error_code=exc.code,
            exc=exc,
        )

    # 일반 예외 핸들러
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        return error_response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error_code="S01",
            exc=exc,
        )

