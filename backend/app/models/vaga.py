from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Vaga(Base):
    __tablename__ = "vagas"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    valor = Column(Float)
    status = Column(String, default="aberta")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    empresa = relationship("Empresa", back_populates="vagas")
    candidaturas = relationship("Candidatura", back_populates="vaga")
