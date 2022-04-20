import os
from datetime import datetime
from tkinter import ttk

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


BASE_DIR=os.path.dirname(os.path.realpath(__file__))
connection_string="sqlite:///"+os.path.join(BASE_DIR,'DataBase.db')

Base = declarative_base()
engine=create_engine(connection_string, echo=True)
session = sessionmaker()


"""
    Class User
    id int
    user_name str
    email str
    created_at datetime
"""

class User(Base):
    """Classe de usuario"""
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    user_name = Column(String(25), nullable=False, unique=True)
    email = Column(String(120), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"<User username={self.user_name} email={self.email}>"

new_user = User(id=1, user_name="Jamilson", email="jamilson@email.com")
print(new_user)

print(BASE_DIR)
     

