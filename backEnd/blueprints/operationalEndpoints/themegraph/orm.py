import os
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from extensions import Base, ThemeGraphWeekly, ThemeGraphMonthly, ThemeGraphDaily


def createMetaDb(Base):
    """
    Creates Database for Geopy. Tables for City and Country location. Created in sqlalchemy
    Path is created with working path. Set deopyDBPath to a certain location, if no generic path should be used.
    """
    DBPath = os.path.join(os.getcwd(), "db.sqlite")
    engine = create_engine(f'sqlite:///{DBPath}', echo=True)
    Base.metadata.create_all(engine)


def droptable(Entity=ThemeGraphDaily):
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


# ------------------ ThemeGraph Functions----------------------------------

def add_edge(session,
             source: str,
             target: str,
             value: float,
             urls: str,
             timeperiod="daily"):

    arguments = locals()

    if timeperiod in ["daily", "weekly", "monthly"]:

        if timeperiod == "daily":
            edge = ThemeGraphDaily(
                source=source,
                target=target,
                value=value,
                urls=urls
            )
        elif timeperiod == "weekly":
            edge = ThemeGraphWeekly(
                source=source,
                target=target,
                value=value,
                urls=urls
            )
        elif timeperiod == "monthly":
            edge = ThemeGraphMonthly(
                source=source,
                target=target,
                value=value,
                urls=urls
            )
        session.add(edge)
        session.commit()
        return 0

    return 1


def get_all_edges(session, timeperiod="daily"):

    edges = None

    if timeperiod == "daily":
        edges = session.query(ThemeGraphDaily).all()

    elif timeperiod == "weekly":
        edges = session.query(ThemeGraphWeekly).all()

    elif timeperiod == "monthly":
        edges = session.query(ThemeGraphMonthly).all()

    return edges


def deleteedges(session, timeperiod="daily"):
    """deletes all meta scrapper data in Table

    Args:
        session (sqlalchmey.session): current session to database
    """

    if timeperiod == "daily":
        edges = session.query(ThemeGraphDaily).delete()

    elif timeperiod == "weekly":
        session.query(ThemeGraphWeekly).delete()

    elif timeperiod == "monthly":
        session.query(ThemeGraphMonthly).delete()

    session.commit()
    return 0


if __name__ == '__main__':
    # create Database
    createMetaDb(Base)

    # Establish connection
    engine = getEngine(Base)
    Session = sessionmaker(bind=engine)
    session = Session()
