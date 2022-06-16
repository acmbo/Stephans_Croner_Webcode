"""
Classes for SQLAlchemy for using in an orm of geopyDB
Baseclass needs to be used in context of the databases and to create session with geodb.
"""

from sqlalchemy import Column, Integer, Float, DateTime, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Country(Base):
    __bind_key__ = 'geopy'
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    country_name = Column(String, nullable=False)
    _long = Column(Float, nullable=False)
    _lat = Column(Float, nullable=False)
    political_state = Column(String)


class City(Base):
    __bind_key__ = 'geopy'
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    city_name = Column(String, nullable=False)
    _long = Column(Float, nullable=False)
    _lat = Column(Float, nullable=False)
    state = Column(String)
    country = Column(String, nullable=False)
    # Foreign Key optional, at least at right now
    country_id = Column(Integer, ForeignKey(Country.id))
