import os
import datetime

from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from extensions import Base, Blogpost


def createMetaDb(Base):
    """
    Creates Database for Geopy. Tables for City and Country location. Created in sqlalchemy
    Path is created with working path. Set deopyDBPath to a certain location, if no generic path should be used.
    """
    DBPath = os.path.join(os.getcwd(), "db.sqlite")
    engine = create_engine(f'sqlite:///{DBPath}', echo=True)
    Base.metadata.create_all(engine)


def droptable(Entity=Blogpost):
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
def add_blogpost(session,
             title: str,
             contenthtml: str,
             Tags: str,
             autor: str,
             thumbnailpath: str,
             picdescription: str,
             shortdescription:str):

    arguments = locals()

    date = datetime.datetime.now()

    print("DB: ", thumbnailpath)
    
    post = Blogpost(
        title=title,
        contenthtml=contenthtml,
        date=date,
        Tags=Tags,
        autor=autor,
        thumbnailpath=thumbnailpath,
        picdescription = picdescription,
        shortdescription=shortdescription)

    session.add(post)
    session.commit()
    return 0

# -------------- Read from Database --------------------------------


def get_all_posts(session):

    posts = session.query(Blogpost).all()
    return posts



def get_post_by_id(session, _id):

    posts = session.query(Blogpost).filter_by(id=_id)
    return posts


def get_post_by_title(session, title):

    posts = session.query(Blogpost).filter_by(title=title)
    return posts



# ---------------- Delete from Database --------------------------


def delete_post_by_Id(session, id):
    """deletes meta scrapper data in Table by id of entry


    Args:
        session (sqlalchmey.session): current session to database
    """
    session.query(Blogpost).filter(Blogpost.id == id).delete()
    session.commit()
    return 0




if __name__ == '__main__':
    
    #droptable(Entity=Blogpost)
    
    # create Database
    createMetaDb(Base)

    # Establish connection
    engine = getEngine(Base)
    Session = sessionmaker(bind=engine)
    session = Session()

