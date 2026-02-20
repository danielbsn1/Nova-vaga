from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    tipo = Column(String)

    candidaturas = relationship("Candidatura", back_populates="user")
    pagamentos = relationship("Pagamento", back_populates="user")
    freelancer = relationship("Freelancer", back_populates="user", uselist=False)
    notificacoes = relationship("Notificacao", back_populates="user")