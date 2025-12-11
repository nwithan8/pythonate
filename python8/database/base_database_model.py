from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseDatabaseModel(Base):
    """
    Base class for all database models.
    Inherits from SQLAlchemy's Base class.
    """

    __abstract__ = True  # This class should not be instantiated directly
