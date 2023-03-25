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
    username = Column(String(250))
    password = Column(String(250))
    firstname=Column(String(250))
    lastname=Column(String(250))
    registername=Column(String(250))
    email=Column(String(250))

class Persona(Base):
    __tablename__ = 'persona'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_name = Column(String(250))
    description = Column(String(250))
    eye_color = Column(String(250))
    hair_color = Column(Integer)
    height = Column(Integer)
    
    
   

#unique=True

class Planeta(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    color = Column(String(250))
    clima = Column(String(250))
    longitude = Column(Integer)
    
    

class Vehiculo(Base):
    __tablename__ = 'vehiculo'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    color = Column(String(250))
    matricula = Column(Integer)
    altura = Column(Integer)
    


class Favourite(Base):
    __tablename__ = 'favourite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    persona_id = Column(Integer,ForeignKey("persona.id"))
    persona = relationship(Persona)
    planeta_id = Column(Integer,ForeignKey("planeta.id"))
    planeta = relationship(Planeta)
    vehiculo_id = Column(Integer,ForeignKey("vehiculo.id"))
    vehiculo = relationship(Vehiculo)
    user_id = Column(Integer, ForeignKey("user.id"))
    user= relationship(User)
    

    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
