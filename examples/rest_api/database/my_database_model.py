from python8.database.base import BaseDatabaseModel


class MyDatabaseModel(BaseDatabaseModel):
    from sqlalchemy import Column, Integer

    __tablename__ = 'my_database_table'
    id = Column("id", Integer, primary_key=True, autoincrement=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
