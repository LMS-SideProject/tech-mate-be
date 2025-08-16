from pathlib import Path  # 경로 계산을 위한 표준 라이브러리
import sys  # 파이썬 모듈 검색 경로 조작

# (핵심) 현재 파일의 상위 디렉터리(프로젝트 루트)를 import 경로에 추가
sys.path.append(str(Path(__file__).resolve().parents[1]))

import json  # 시드 JSON 로딩
from app.db import SessionLocal
from app.models import Expert, Request


def run():  # 시드 주입 메인 함수
    db = SessionLocal()  # 세션 시작
    try:
        experts = json.load(
            open("seed/experts.json", "r", encoding="utf-8-sig")
        )  # utf-8-sig: BOM 유무 상관없이 읽기
        for e in experts:  # 전문가 레코드 반복
            db.add(Expert(**e))  # 키워드 인자를 모델에 맵핑하여 추가
        reqs = json.load(
            open("seed/requests.json", "r", encoding="utf-8-sig")
        )  # PowerShell이 만든 BOM 파일 대응
        for r in reqs:  # 요청서 레코드 반복
            db.add(Request(**r))  # 모델 인스턴스 추가
        db.commit()  # 트랜잭션 커밋
        print(f"Seeded experts={len(experts)}, requests={len(reqs)}")  # 결과 로그 출력
    finally:
        db.close()  # 세션 종료(에러 여부와 무관하게)


if __name__ == "__main__":  # 스크립트 직접 실행 시
    run()  # run() 호출
