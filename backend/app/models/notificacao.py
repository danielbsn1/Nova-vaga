from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class Notificacao(Base):
    __tablename__ = "notificacoes"

    id = Column(Integer, primary_key=True, index=True)


    user_id = Column(Integer, ForeignKey("users.id"))

    
    mensagem = Column(String, nullable=False)


    status = Column(String, default="nao_lida")

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")