from pydantic import BaseModel, Field

class ConvertRequest(BaseModel):
    """
    말투 변환 요청을 위한 데이터 모델입니다.
    """
    text: str = Field(..., description="비즈니스 말투로 변환할 원문 텍스트입니다.", min_length=1)
    target_audience: str = Field(..., description="수신 대상 코드 (boss / colleague / client / team)")

class ConvertResponse(BaseModel):
    """
    말투 변환 결과를 반환하기 위한 데이터 모델입니다.
    """
    converted_text: str = Field(..., description="변환된 비즈니스 말투 텍스트입니다.")
    target_audience: str = Field(..., description="선택된 수신 대상 코드")
    original_text: str = Field(..., description="사용자가 입력했던 원문 텍스트")
