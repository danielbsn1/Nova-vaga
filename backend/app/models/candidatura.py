from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Candidatura(Base):
    __tablename__ = "candidaturas"

    id = Column(Integer, primary_key=True, index=True)
    vaga_id = Column(Integer, ForeignKey("vagas.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String, default="pendente")
    created_at = Column(DateTime, default=datetime.utcnow)

    vaga = relationship("Vaga", back_populates="candidaturas")
    user = relationship("User", back_populates="candidaturas")

