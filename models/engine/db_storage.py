#!/usr/bin/python3
"""This is the DBStorage module"""

from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv


class DBStorage:
    """The DBStorage class"""

    __engine = None
    __session = None

    def __init__(self):
        """initialize a connection with MySQL"""

        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, db), pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""

        obj = {}
        classes = [User, State, City, Amenity, Place, Review]

        if cls is not None:
            classes = [cls]

        for c in classes:
            result = self.__session.query(c)

            for i in result:
                key = '{}.{}'.format(i.__class__.__name__, i.id)
                obj[key] = i
        return obj

    def new(self, obj):
        """ add the object to the current database session"""

        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""

        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and create the session"""

        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)

        self.__session = Session()

    def close(self):
        """close the current session"""

        self.__session.close()
