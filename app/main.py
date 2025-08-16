from fastapi import FastAPI
from .routers import main_router as main_router

app = FastAPI(title="tech-mate-api")


@app.get("/health")
def health():
    return {"ok": True}


app.include_router(main_router.router)
