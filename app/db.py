import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, echo=False, future=True, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


import os  # 환경변수 사용
from pathlib import Path  # 절대경로 생성
from sqlalchemy import create_engine  # SQLAlchemy 엔진
from sqlalchemy.orm import sessionmaker, declarative_base  # 세션/베이스

BASE_DIR = Path(__file__).resolve().parent.parent  # 프로젝트 루트(app/..)
DEFAULT_SQLITE_URL = (
    f"sqlite:///{(BASE_DIR / 'app.db').as_posix()}"  # 윈도우에서도 안전한 슬래시 경로
)
DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_SQLITE_URL)  # .env 없으면 app.db 사용

connect_args = (
    {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)  # SQLite 스레드 옵션
engine = create_engine(
    DATABASE_URL, echo=False, future=True, connect_args=connect_args
)  # 엔진 생성
SessionLocal = sessionmaker(
    bind=engine, autocommit=False, autoflush=False, future=True
)  # 세션 팩토리
Base = declarative_base()  # 모델 베이스(메타데이터 보관)


def get_db():  # FastAPI 의존성: 요청별 DB 세션
    db = SessionLocal()  # 세션 오픈
    try:
        yield db  # 라우터로 전달
    finally:
        db.close()  # 세션 종료
