class NewsSummaryError(RuntimeError):
    """뉴스 요약 생성 중 발생하는 커스텀 예외"""
    def __init__(self, message: str):
        self.message = message
        self.code = "A01"
        super().__init__(self.message)