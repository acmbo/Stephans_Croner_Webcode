"""
Functions for creating and working with the geopy Database
for ORM Classes see, ormClasses.py

"""

#import re
import os
#import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .ormClasses import Base, City, Country


def createGeopyDb(Base):
    """
    Creates Database for Geopy. Tables for City and Country location. Created in sqlalchemy
    Path is created with working path. Set deopyDBPath to a certain location, if no generic path should be used.
    """
    geopyDBPath = os.path.join(os.getcwd(), "geopydb.sqlite")
    engine = create_engine(f'sqlite:///{geopyDBPath}', echo=True)
    Base.metadata.create_all(engine)


def getEngine(Base):
    """
    Connection start function for establishing save connections

    Args:
        Base (_type_): Base from orm
    Return:
        Returns: Engine für SQLAlchemy
    """
    geopyDBPath = os.path.join(os.getcwd(), "geopydb.sqlite")
    engine = create_engine(f'sqlite:///{geopyDBPath}', echo=True)
    return engine


# ----------------------------Add to Database----------------------
def add_city(session,
             city_name: str,
             _long: float,
             _lat: float,
             state: str,
             country: str,
             country_id: int = None):
    """Add city to database. Controll for duplicates through cityname. Country_id is optional and should be checked through database internally in this function.

    Args:
        session (sqlalchmey.session): session with database
        city_name (str): cityname
        _long (float): longitude
        _lat (float): latitude
        state (str): nema of state
        country (str): name of country
        country_id (int): foreign_key to other db. (Optional)
    """
    arguments = locals()
    city = City(city_name=city_name,
                _long=_long,
                _lat=_lat,
                state=state,
                country=country,
                )
    if country_id:
        setattr(city, "country_id",  country_id)

    if city.city_name not in [cit.city_name for cit in get_all_citys(session)]:
        session.add(city)
        session.commit()
        return 0
    else:
        return 1


def add_country(session,
                country_name: str,
                _long: float,
                _lat: float,
                political_state: str = None):

    arguments = locals()
    country = Country(country_name=country_name,
                      _long=_long,
                      _lat=_lat,
                      political_state=political_state,
                      )

    if country.country_name not in [count.country_name for count in get_all_countrys(session)]:
        session.add(country)
        session.commit()
        return 0
    else:
        return 1


# -------------- Read from Database --------------------------------


def get_all_citys(session):
    """Gets all citys from database

    Args:
        session (sqlalchmey.session): current session to database

    Returns:
         list: returns list of orm classes of citys found in db
    """
    citys = session.query(City).all()
    return citys


def get_city_by_name(city_name: str, session):
    """Gets all citys with cityname as name

    Args:
        city_name(str): name of city to search in db
        session (sqlalchmey.session): current session to database

    Returns:
         list: returns list of orm classes of citys found in db
    """
    findings = session.query(City).filter_by(city_name=city_name).all()
    return findings


def get_all_countrys(session):
    """Gets all citys from database

    Args:
        session (sqlalchmey.session): current session to database

    Returns:
         list: returns list of orm classes of citys found in db
    """
    countrys = session.query(Country).all()
    return countrys


def get_country_by_name(country_name: str, session):
    """Gets all citys with cityname as name

    Args:
        city_name(str): name of city to search in db
        session (sqlalchmey.session): current session to database

    Returns:
         list: returns list of orm classes of citys found in db
    """
    findings = session.query(Country).filter_by(
        country_name=country_name).all()
    return findings


# ---------------- Delete from Database --------------------------


def deleteCitysInTable(session):
    """deletes all cities in table

    Args:
        session (sqlalchmey.session): current session to database
    """
    session.query(City).delete()
    return 0


def deleteCityByName(session, city_name):
    """delets city by name

    Args:
        city_name(str): name of city to search in db
        session (sqlalchmey.session): current session to database
    """
    session.query(City).filter_by(city_name=city_name).delete()
    return 0


def deleteCountryInTable(session):
    """deletes all country in table

    Args:
        session (sqlalchmey.session): current session to database
    """
    session.query(Country).delete()
    return 0


def deleteCountryByName(session, country_name):
    """delets country by name

    Args:
        country_name(str): name of country to search in db
        session (sqlalchmey.session): current session to database
    """
    session.query(Country).filter_by(country_name=country_name).delete()
    return 0


if __name__ == "__main__":

    """Mainfunctionality of the script:
    Can also be used for testing purposes:
    -Create Database
    -Create Connection (engine, session)
    -Add Entrys
    -Delete entrys
    """

    # create Database
    createGeopyDb(Base)

    # Establish connection
    engine = getEngine(Base)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add Entrys
    add_city(session,
             city_name="Düsseldorf",
             _long=51.233334,
             _lat=6.783333,
             state="NRW",
             country="Germany")

    # Read database through query of orm
    citys = session.query(City).first()
    print(citys.city_name)

    # Add functions
    allCitiesInDb = get_all_citys(session)
    findCity = get_city_by_name("Düsseldorf", session)

    add_country(session,
                country_name="Germany",
                _long=51.165691,
                _lat=10.451526,
                political_state="Bundesrepublik Deutschland")

    add_country(session,
                country_name="France",
                _long=48.864716,
                _lat=2.349014,
                political_state="Bundesrepublik Deutschland")

    countrys = get_all_countrys(session)

    get_country_by_name("Germany", session)

    deleteCountryInTable(session)

    #deleteCountryByName(session, "France")
