from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.auth import auth_router
from app.routers import candidaturas, vagas

app = FastAPI(title="Nova Vaga API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api")
app.include_router(candidaturas.router, prefix="/api")
app.include_router(vagas.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Nova Vaga API"}


