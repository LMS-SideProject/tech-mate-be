import os, sys  # 경로/환경
from logging.config import fileConfig  # 로깅 설정
from sqlalchemy import engine_from_config, pool  # 엔진 유틸
from alembic import context  # Alembic 컨텍스트

config = context.config  # alembic.ini 로딩

# (중요) 프로젝트 루트를 파이썬 경로에 추가해서 app.* 임포트 가능하게 만듦
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.db import Base, DATABASE_URL  # 앱과 동일한 Base/DB URL 사용
import app.models  # (매우 중요) 모델을 실제로 import해야 autogenerate가 테이블을 인식

# alembic.ini 내부 sqlalchemy.url 값을 런타임에 앱과 동일하게 주입
if DATABASE_URL:
    config.set_main_option("sqlalchemy.url", DATABASE_URL)  # 앱과 마이그 DB URL 통일

# 자동 생성 기준이 되는 메타데이터(=모델들의 스키마)
target_metadata = Base.metadata


def run_migrations_offline():  # 오프라인 모드 (SQL만 생성)
    url = config.get_main_option("sqlalchemy.url")  # DB URL 읽기
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,  # 컬럼 타입 변경도 감지
    )
    with context.begin_transaction():  # 트랜잭션 시작
        context.run_migrations()  # 마이그 실행


def run_migrations_online():  # 온라인 모드 (DB에 직접 적용)
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),  # alembic.ini 섹션 로드
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:  # DB 연결
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # 타입 비교 활성화
        )
        with context.begin_transaction():  # 트랜잭션 시작
            context.run_migrations()  # 마이그 실행


if context.is_offline_mode():  # 실행 모드 분기
    run_migrations_offline()
else:
    run_migrations_online()
