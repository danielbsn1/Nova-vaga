from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime
from app.core.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum 

class StatusPagamento(str, enum.Enum):
    PENDENTE = "pendente"
    PAGO = "pago"
    CANCELADO = "cancelado"
    FALHOU = "falhou"

class Pagamento(Base):
    __tablename__ = "pagamentos"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    empresa_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    plano_id = Column(Integer, nullable=False)
    status = Column(String, default=StatusPagamento.PENDENTE.value)
    stripe_session_id = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    vagas_total = Column(Integer)
    vagas_usadas = Column(Integer, default=0)
    
    user = relationship("User", foreign_keys=[user_id], back_populates="pagamentos")
    empresa = relationship("User", foreign_keys=[empresa_id])