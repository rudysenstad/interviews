from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import mapped_column, relationship
from models.genre import Genre

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    genre_id = Column(Integer, ForeignKey(Genre.id))
    movie_title = Column(String)
    movie_info = Column(String)
    runtime = Column(Integer)
    theatrical_release_date = Column(Date)
    streaming_release_date = Column(Date)
    rating = Column(String)
    production_company = Column(String)
    genre = relationship("Genre", foreign_keys="Movie.genre_id")

