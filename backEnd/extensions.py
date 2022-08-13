"""
Classes for SQLAlchemy for using in an orm of DB
Baseclass needs to be used in context of the databases and to create session with DB.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import Column, Integer, Float, DateTime, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()
ma = Marshmallow()


Base = declarative_base()


class Country(Base):

    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    country_name = Column(String, nullable=False)
    _long = Column(Float, nullable=False)
    _lat = Column(Float, nullable=False)
    political_state = Column(String)


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    city_name = Column(String, nullable=False)
    _long = Column(Float, nullable=False)
    _lat = Column(Float, nullable=False)
    state = Column(String)
    country = Column(String, nullable=False)
    # Foreign Key optional, at least at right now
    country_id = Column(Integer, ForeignKey(Country.id))


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
    keyword = Column(String, nullable=False)
    amount_of_uses = Column(Float, nullable=False)


class UsedKeywords_7days(Base):
    __tablename__ = 'usedKeywords_7days'

    id = Column(Integer, primary_key=True)
    keyword = Column(String, nullable=False)
    amount_of_uses = Column(Float, nullable=False)


class Postings_weekly(Base):
    __tablename__ = 'postings_weekly'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    post = Column(Float, nullable=False)


class Postings_montly(Base):
    __tablename__ = 'postings_monthly'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    post = Column(Float, nullable=False)


class Postings_year(Base):
    __tablename__ = 'postings_year'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    post = Column(Float, nullable=False)


class ThemeGraphDaily(Base):
    __tablename__ = 'themeGraphDaily'

    id = Column(Integer, primary_key=True)
    source = Column(String, nullable=False)
    target = Column(String, nullable=False)
    value = Column(Float, default=1.0)
    urls = Column(String)


class ThemeGraphWeekly(Base):
    __tablename__ = 'themeGraphWeekly'

    id = Column(Integer, primary_key=True)
    source = Column(String, nullable=False)
    target = Column(String, nullable=False)
    value = Column(Float, default=1.0)
    urls = Column(String)


class ThemeGraphMonthly(Base):
    __tablename__ = 'themeGraphMontly'

    id = Column(Integer, primary_key=True)
    source = Column(String, nullable=False)
    target = Column(String, nullable=False)
    value = Column(Float, default=1.0)
    urls = Column(String)


class Blogpost(Base):
    __tablename__ = 'blogposts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    contenthtml = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    Tags = Column(String)
    autor = Column(String)
    thumbnailpath = Column(String)
    shortdescription = Column(String)