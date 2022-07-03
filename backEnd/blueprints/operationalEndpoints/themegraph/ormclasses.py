"""
Classes for SQLAlchemy for using in an orm of graphDB
Baseclass needs to be used in context of the databases and to create session with graphdb.
"""

from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ThemeGraphDaily(Base):
    __bind_key__ = 'graphdb'
    __tablename__ = 'themeGraphDaily'

    id = Column(Integer, primary_key=True)
    edge_partA = Column(String, nullable=False)
    edge_partB = Column(String, nullable=False)
    weigth = Column(Float, default=1.0)
    urls = Column(String)


class ThemeGraphWeekly(Base):
    __bind_key__ = 'graphdb'
    __tablename__ = 'themeGraphWeekly'

    id = Column(Integer, primary_key=True)
    edge_partA = Column(String, nullable=False)
    edge_partB = Column(String, nullable=False)
    weigth = Column(Float, default=1.0)
    urls = Column(String)


class ThemeGraphMonthly(Base):
    __bind_key__ = 'graphdb'
    __tablename__ = 'themeGraphMontly'

    id = Column(Integer, primary_key=True)
    edge_partA = Column(String, nullable=False)
    edge_partB = Column(String, nullable=False)
    weigth = Column(Float, default=1.0)
    urls = Column(String)
