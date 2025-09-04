from openai import OpenAI
from core.config import settings
from core.exception.custom_exception import NewsSummaryError

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=settings.openai_api_key)


async def get_summary_from_openai(text: str, sentence_count : int) -> str:
    """
    OpenAI GPT 모델을 호출하여 뉴스 기사를 요약합니다.

    Args:
        text (str): 요약할 뉴스 기사 본문

    Returns:
        str: 요약된 텍스트 (5문장 정도)
    """
    try:
        # 요약 프롬프트
        prompt = (
            f"다음 뉴스 기사를 {sentence_count}문장 내외로 요약하고, "
            "중요한 수치나 날짜는 그대로 유지하며, "
            "출처가 있으면 표시해줘.\n\n"
            f"{text}"
        )

        response = client.chat.completions.create(
            model="gpt-5-mini-2025-08-07",
            messages=[
                {"role": "system", "content": "당신은 뉴스 요약 전문가입니다."},
                {"role": "user", "content": prompt},
            ],
        )

        # 응답 추출
        summary = response.choices[0].message.content.strip()
        return summary

    except Exception as e:
        raise NewsSummaryError("AI 뉴스 생성중 오류 발생")