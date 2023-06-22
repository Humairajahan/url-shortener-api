from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    String,
    Integer,
    Identity,
)


def start_session(postgres_url):
    engine = create_engine(postgres_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    return engine, session


PG_URL = "postgresql+psycopg2://username:password@db:5432/urls"
engine, session = start_session(PG_URL)

Base = declarative_base()


class URLs(Base):
    __tablename__ = "urls"

    id = Column(Integer, Identity(start=1, cycle=True), primary_key=True, index=True)
    longURL = Column(String)
    shortURL = Column(String)
    shortcode = Column(String)


Base.metadata.create_all(engine)
