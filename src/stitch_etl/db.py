from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.ext.declarative import declarative_base
from models.credit import Credit
from models.credit_type import CreditType
from models.genre import Genre
from models.movie_review import MovieReview
from models.movies import Movie
from models.person import Person

class DatabaseHandler():

    def __init__(self):
        self.engine = None
        self.session = None
        self.get_db_session()

    def get_db_session(self, user:str=None, password:str=None, dbname:str=None):
        """
        basic method to get db connection, no error handling for brevity
        """
        self.engine = create_engine(f"postgresql://{os.environ.get('SQL_USER', user)}:{os.environ.get('SQL_PASSWORD', password)}@db:5432/{os.environ.get('SQL_DATABASE', dbname)}")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        return self.session

    def _create_table(self, table:declarative_base):
        """
        table creation
        """
        table.__table__.create(bind=self.engine, checkfirst=True)

    def create_tables(self):
        """
        create all of the tables associated with our model classes
        skipping error checking for brevity of this assignment
        """
        if not self.engine:
            self.get_db_session()
        tables = [CreditType, Person, Genre, Credit, Movie, MovieReview]
        _ = [self._create_table(table) for table in tables]
