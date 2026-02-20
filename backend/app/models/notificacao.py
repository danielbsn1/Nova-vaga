from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base
import enum


class StatusNotificacao(str, enum.Enum):
    LIDA = "lida"
    NAO_LIDA = "nao_lida"


class Notificacao(Base):
    __tablename__ = "notificacoes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    mensagem = Column(String, nullable=False)
    status = Column(String, default=StatusNotificacao.NAO_LIDA.value, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="notificacoes")