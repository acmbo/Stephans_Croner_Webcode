import os
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from extensions import Base, ScrapperData, UsedKeywords


def createMetaDb(Base):
    """
    Creates Database for Geopy. Tables for City and Country location. Created in sqlalchemy
    Path is created with working path. Set deopyDBPath to a certain location, if no generic path should be used.
    """
    DBPath = os.path.join(os.getcwd(), "db.sqlite")
    engine = create_engine(f'sqlite:///{DBPath}', echo=True)
    Base.metadata.create_all(engine)


def getEngine(Base):
    """
    Connection start function for establishing save connections

    Args:
        Base (_type_): Base from orm
    Return:
        Returns: Engine für SQLAlchemy
    """
    metaDBPath = os.path.join(os.getcwd(), "db.sqlite")
    engine = create_engine(f'sqlite:///{metaDBPath}', echo=True)
    return engine


# ----------------------------Add to Database----------------------
def add_meta(session,
             scrapper_name: str,
             amount_of_db_entries: int,
             entrydate: datetime.datetime,
             errors: int):

    arguments = locals()

    scrapperData = ScrapperData(
        scrapper_name=scrapper_name,
        amount_of_db_entries=amount_of_db_entries,
        entrydate=entrydate,
        errors=errors)

    session.add(scrapperData)
    session.commit()
    return 0


# -------------- Read from Database --------------------------------


def get_all_scrappermeta(session):

    scrappermeta = session.query(ScrapperData).all()
    return scrappermeta


# ---------------- Delete from Database --------------------------


def deleteScrapperTable(session):
    """deletes all meta scrapper data in Table

    Args:
        session (sqlalchmey.session): current session to database
    """
    session.query(ScrapperData).delete()
    return 0


def deleteScrapperbyId(session, id):
    """deletes meta scrapper data in Table by id of entry


    Args:
        session (sqlalchmey.session): current session to database
    """
    session.query.filter_by(id=id).delete()
    session.commit()
    return 0


if __name__ == '__main__':
    # create Database
    createMetaDb(Base)

    # Establish connection
    engine = getEngine(Base)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add Entrys
    add_meta(session,
             scrapper_name="Raspberry Pi 2b+",
             amount_of_db_entries=10,
             entrydate=datetime.datetime.now(),
             errors=0)

    # Get all Entrys
    get_all_scrappermeta(session)

    # Remove all Entrys
    deleteScrapperTable(session)
