import json  # 시드 JSON 로딩
from app.db import SessionLocal  # 세션 팩토리
from app.models import Expert, Request  # 시드 대상 모델


def run():  # 시드 주입 메인 함수
    db = SessionLocal()  # 세션 시작
    try:
        experts = json.load(
            open("seed/experts.json", "r", encoding="utf-8")
        )  # 전문가 시드 로드
        for e in experts:  # 전문가 레코드 반복
            db.add(Expert(**e))  # 키워드 인자를 모델에 맵핑하여 추가
        reqs = json.load(
            open("seed/requests.json", "r", encoding="utf-8")
        )  # 요청서 시드 로드
        for r in reqs:  # 요청서 레코드 반복
            db.add(Request(**r))  # 모델 인스턴스 추가
        db.commit()  # 트랜잭션 커밋
        print(f"Seeded experts={len(experts)}, requests={len(reqs)}")  # 결과 로그 출력
    finally:
        db.close()  # 세션 종료(에러 여부와 무관하게)


if __name__ == "__main__":  # 스크립트 직접 실행 시
    run()  # run() 호출
