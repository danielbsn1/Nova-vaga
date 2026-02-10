from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime
from app.core.database import Base

class Pagamento(Base):
    __tablename__ = "pagamentos"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    valor = Column(Float, nullable=False)
    status = Column(String, default="pendente")
    stripe_session_id = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
