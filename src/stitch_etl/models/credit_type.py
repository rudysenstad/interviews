from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

Base = declarative_base()

class CreditType(Base):
    __tablename__ = 'credit_type'
    id = Column(Integer, primary_key=True)
    credit_type = Column(String)
    