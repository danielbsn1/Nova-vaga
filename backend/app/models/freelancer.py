from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Freelancer(Base):
    __tablename__ = "freelancers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, index=True)
    nome = Column(String, nullable=False, index=True)
    cpf = Column(String, unique=True, index=True)
    telefone = Column(String)
    habilidades = Column(String)
    
    user = relationship("User", back_populates="freelancer")
    candidaturas = relationship("Candidatura", back_populates="freelancer")
