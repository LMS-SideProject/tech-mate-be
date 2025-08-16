from sqlalchemy import (
    Column,
    String,
    JSON,
    Integer,
    Boolean,
)
from ..db import Base


class Expert(Base):  # 전문가(공급자) 모델
    __tablename__ = "experts"  # 테이블명: experts
    id = Column(Integer, primary_key=True, autoincrement=True)  # PK(자동증가)
    name = Column(String, nullable=False)  # 전문가 이름(필수)
    region = Column(String)  # 전문가 활동 지역
    rate_per_hour = Column(Integer)  # 시간당 요율(원)
    offline_ok = Column(Boolean, default=False)  # 오프라인 미팅 가능 여부
    availability_json = Column(JSON)  # 가능 시간대 JSON(요일/시간대 리스트)
    rating_avg = Column(Integer, default=0)  # 평균 평점(간단히 정수로 시작)
