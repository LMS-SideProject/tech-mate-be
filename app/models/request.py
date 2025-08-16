from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
    Text,
    DateTime,
    func,
)  # 컬럼/타입/함수 로드
from ..db import Base  # 동일 패키지의 Base(모든 모델 부모)


class Request(Base):  # 수요자 요청(의뢰서) 모델
    __tablename__ = "requests"  # 테이블명: requests
    id = Column(Integer, primary_key=True, autoincrement=True)  # PK(자동증가)
    title = Column(Text)  # 요청 제목
    goal = Column(Text)  # 달성하고 싶은 목표/배경
    budget_range = Column(String)  # 예산 범위(예: "20~40만원")
    schedule_pref = Column(String)  # 일정 선호(예: "주말 오전 2h x 3")
    mode_pref = Column(String)  # 진행 방식(온라인/오프라인)
    region = Column(String)  # 선호 지역(오프라인일 때 유효)
    keywords_json = Column(JSON)  # 키워드 목록(JSON 배열)
    created_at = Column(DateTime, server_default=func.now())  # 생성 시각(서버 기본값)
