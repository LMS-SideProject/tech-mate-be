from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import Expert, Request

router = APIRouter(prefix="/api", tags=["api"])


@router.get("/seed-check")
def seed_check(db: Session = Depends(get_db)):
    experts = db.query(Expert).count()
    requests = db.query(Request).count()
    return {"experts": experts, "requests": requests}
