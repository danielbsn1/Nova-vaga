from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Freelancer(Base):
    __tablename__ = "freelancers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True)
    telefone = Column(String)
    habilidades = Column(String)
    
    user = relationship("User")
    candidaturas = relationship("Candidatura", back_populates="freelancer")
