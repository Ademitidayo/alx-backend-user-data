#!/usr/bin/env python3
""" doc doc doc """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """ doc doc doc """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"
