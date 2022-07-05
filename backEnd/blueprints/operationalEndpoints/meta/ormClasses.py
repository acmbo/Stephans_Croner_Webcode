"""
Classes for SQLAlchemy for using in an orm of metaDB
Baseclass needs to be used in context of the databases and to create session with metadb.
"""

from sqlalchemy import Column, Integer, Float, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ScrapperData(Base):
    __tablename__ = 'scrapperdata'

    id = Column(Integer, primary_key=True)
    scrapper_name = Column(String, nullable=False)
    amount_of_db_entries = Column(Float, nullable=False)
    entrydate = Column(DateTime, nullable=False)
    errors = Column(Float, nullable=False)


class UsedKeywords(Base):
    __tablename__ = 'usedKeywords'

    id = Column(Integer, primary_key=True)
    keywords = Column(String, nullable=False)
    amount_of_uses = Column(Float, nullable=False)
