from python8 import BaseDatabaseModel
from python8.database import imports


class MyDatabaseModel(BaseDatabaseModel):
    __tablename__ = 'my_database_table'
    id = imports.Column("id", imports.Integer, primary_key=True, autoincrement=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
