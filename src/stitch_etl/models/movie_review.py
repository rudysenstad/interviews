from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import mapped_column, relationship
from models.movies import Movie

Base = declarative_base()

class MovieReview(Base):
    __tablename__ = 'movie_review'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movie.id"))
    critics_consensus = Column(String)
    audience_count = Column(Float)
    tomatometer_status = Column(String)
    tomatometer_count = Column(Float)
    tomatometer_rating = Column(Float)
    audience_status = Column(String)
    audience_rating = Column(Float)
    audience_count = Column(Float)
    tomatometer_top_critics_count = Column(Integer)
    tomatometer_fresh_critics_count = Column(Integer)
    tomatometer_rotten_critics_count = Column(Integer)
    movie = relationship("Movie", foreign_keys="MovieReview.movie_id")

