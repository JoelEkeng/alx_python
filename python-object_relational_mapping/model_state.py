"""
    Using the sqlaclchemy libary
"""
from sqlalchemy import column, integer, string
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    """
    Maps to the 'states' table.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.

    Args:
        Base (DeclarativeMeta): The base class.
    """
    
    __tablename__ = 'states'

    id = column(integer, primary_key=True, autoincrement=True, nullable=False)
    name = column(String(128), nullable=False)