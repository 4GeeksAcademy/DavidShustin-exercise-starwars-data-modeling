import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    favorites = relationship("Favorite", backref="user")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        
        }
    
class Favorite(Base):
    __tablename__= 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    character_id = Column(Integer, ForeignKey("character.id", ondelete="CASCADE"), nullable=True)
    planet_id = Column(Integer, ForeignKey("planet.id", ondelete="CASCADE"), nullable=True)

class Character(Base):
    __tablename__= 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=True)
    eye_color = Column(String(50), nullable=True)
    character_img = Column(String(512), nullable=True)
    favorites= relationship("Favorite", backref="character")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(Integer, nullable=True)
    climate = Column(String(50), nullable=True)
    population = Column(String(50), nullable=True)
    favorites= relationship("Favorite", backref="planet")


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
