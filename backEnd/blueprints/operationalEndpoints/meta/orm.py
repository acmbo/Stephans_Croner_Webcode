import os
import datetime

from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from extensions import Base, ScrapperData, UsedKeywords, UsedKeywords_7days, Postings_montly, Postings_weekly, Postings_year


def createMetaDb(Base):
    """
    Creates Database for Geopy. Tables for City and Country location. Created in sqlalchemy
    Path is created with working path. Set deopyDBPath to a certain location, if no generic path should be used.
    """
    DBPath = os.path.join(os.getcwd(), "db.sqlite")
    engine = create_engine(f'sqlite:///{DBPath}', echo=True)
    Base.metadata.create_all(engine)


def droptable(Entity=UsedKeywords):
    DBPath = os.path.join(os.getcwd(), "db.sqlite")
    engine = create_engine(f'sqlite:///{DBPath}', echo=True)
    Entity.__table__.drop(engine)


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


def add_keyword(session,
                keyword: str,
                amount_of_uses: int):

    arguments = locals()
    print("HERE")
    kwData = UsedKeywords(
        keyword=keyword,
        amount_of_uses=amount_of_uses
    )

    session.add(kwData)
    session.commit()
    return 0


def add_keyword_7days(session,
                      keyword: str,
                      amount_of_uses: int):

    arguments = locals()

    kwData = UsedKeywords_7days(
        keyword=keyword,
        amount_of_uses=amount_of_uses
    )

    session.add(kwData)
    session.commit()
    return 0


def add_posting_7days(session,
                      post: int,
                      date:  datetime.datetime):

    arguments = locals()

    post = Postings_weekly(
        date=date,
        post=post
    )

    session.add(post)
    session.commit()
    return 0


def add_posting_month(session,
                      post: int,
                      date:  datetime.datetime):

    arguments = locals()

    post = Postings_montly(
        date=date,
        post=post
    )

    session.add(post)
    session.commit()
    return 0


def add_posting_year(session,
                     post: int,
                     date:  datetime.datetime):

    arguments = locals()

    post = Postings_year(
        date=date,
        post=post
    )

    session.add(post)
    session.commit()
    return 0

# -------------- Read from Database --------------------------------


def get_all_scrappermeta(session):

    scrappermeta = session.query(ScrapperData).all()
    return scrappermeta


def get_all_scrappermeta_by_timeframe(session, days: int):
    """Get scrapperdata from a certain timeframe starting from now till the given days as integer subatracted from now"""
    timepoint = datetime.datetime.today() - datetime.timedelta(days=days)

    scrappermeta = session.query(ScrapperData).filter(
        ScrapperData.entrydate >= timepoint)

    return scrappermeta


def get_all_keywords(session):
    # Montly
    kwdata = session.query(UsedKeywords).all()
    return kwdata


def get_all_keywords_7days(session):

    kwdata = session.query(UsedKeywords_7days).all()
    return kwdata


def get_all_postings_7days(session):

    posts = session.query(Postings_weekly).all()
    return posts


def get_all_postings_Month(session):

    posts = session.query(Postings_montly).all()
    return posts


def get_all_postings_Year(session):

    posts = session.query(Postings_year).all()
    return posts

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
    session.query(ScrapperData).filter(ScrapperData.id == id).delete()
    session.commit()
    return 0


def delete_all_keywords(session):

    session.query(UsedKeywords).delete()
    session.commit()
    return 0


def delete_all_keywords_7days(session):

    session.query(UsedKeywords_7days).delete()
    session.commit()
    return 0


def delete_all_postings_7days(session):

    session.query(Postings_weekly).delete()
    session.commit()
    return 0


def delete_all_postings_month(session):

    session.query(Postings_montly).delete()
    session.commit()
    return 0


def delete_all_postings_year(session):

    session.query(Postings_year).delete()
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

    get_all_scrappermeta_by_timeframe(session, days=200)
