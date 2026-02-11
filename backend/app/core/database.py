from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from .config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    jobs = relationship("Job", back_populates="company", cascade="all, delete-orphan")
    candidaturas = relationship("Candidatura", back_populates="company", cascade="all, delete-orphan")


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))

    company = relationship("Company", back_populates="jobs")

    candidaturas = relationship("Candidatura", back_populates="job", cascade="all, delete-orphan")
    pagaments = relationship("Pagament", back_populates="job", cascade="all, delete-orphan")


class Freelancer(Base):
    __tablename__ = "freelancers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    candidaturas = relationship("Candidatura", back_populates="freelancer", cascade="all, delete-orphan")


class Pagament(Base):
    __tablename__ = "pagaments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    currency = Column(String)
    status = Column(String)

    job_id = Column(Integer, ForeignKey("jobs.id"))
    job = relationship("Job", back_populates="pagaments")


class Candidatura(Base):
    __tablename__ = "candidaturas"

    id = Column(Integer, primary_key=True, index=True)
    freelancer_id = Column(Integer, ForeignKey("freelancers.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))

    freelancer = relationship("Freelancer", back_populates="candidaturas")
    job = relationship("Job", back_populates="candidaturas")
    company = relationship("Company", back_populates="candidaturas")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
