from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

from crud.article.ai_summary import get_summary_from_openai

router = APIRouter()

class ArticleSummaryResponse(BaseModel):
    summary: str

class ArticleSummaryRequest(BaseModel):
    contents: str

@router.get("/article-summary", response_model=ArticleSummaryResponse)
async def read_root(request: ArticleSummaryRequest):
    # OpenAI로 요약
    summary = await get_summary_from_openai(request.contents,5)

    return ArticleSummaryResponse(summary=summary)