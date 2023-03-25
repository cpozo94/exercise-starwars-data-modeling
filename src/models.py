import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id= Column(String(250), primary_key=True)
    username = Column(String(250),nullable=False)
    password = Column(String(250), nullable=False)
    firstname=Column(String(250), nullable=False)
    lastname=Column(String(250), nullable=False)
    registername=Column(String(250), nullable=False)
    email=Column(String(250), nullable=False)

class Persona(Base):
    __tablename__ = 'persona'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_name = Column(String(250))
    description = Column(String(250))
    eye_color = Column(String(250), nullable=False)
    hair_color = Column(Integer)
    height = Column(Integer)
    
    
   

#unique=True

class Planeta(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    
    

class Vehiculo(Base):
    __tablename__ = 'vehiculo'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    color = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    


class Favourite(Base):
    __tablename__ = 'favourite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer,ForeignKey("persona.id"))
    persona = relationship(Persona)
    planet_id = Column(Integer,ForeignKey("planeta.id"))
    planeta = relationship(Planeta)
    car_id = Column(Integer,ForeignKey("vehiculo.id"))
    car = relationship(Vehiculo)
    user_id = Column(Integer, ForeignKey("user.id"))
    user= relationship(User)
    

    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
