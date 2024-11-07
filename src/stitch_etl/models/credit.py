from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import mapped_column, relationship
from models.person import Person
from models.credit_type import CreditType
from models.movies import Movie

Base = declarative_base()

class Credit(Base):
    __tablename__ = 'credit'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey(Person.id))
    credit_type_id = Column(Integer, ForeignKey(CreditType.id))
    movie_id = Column(Integer, ForeignKey(Movie.id))
    person = relationship('Person', foreign_keys='Credit.person_id')
    credit_type = relationship("CreditType", foreign_keys="Credit.credit_type_id")
    movie = relationship("Movie", foreign_keys="Credit.movie_id")
