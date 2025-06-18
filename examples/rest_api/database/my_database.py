from examples.rest_api.database.my_database_model import MyDatabaseModel
from python8.rest_api.database.base_database import BaseDatabase


class MyDatabase(BaseDatabase):
    def __init__(self,
                 sqlite_file: str):
        super().__init__(sqlite_file=sqlite_file)
        # IMPORTANT: Remember to add each database model to the database to register the table
        MyDatabaseModel.__table__.create(bind=self.engine, checkfirst=True)

    def get_data(self, **kwargs):
        # Implement your data retrieval logic here
        return self._get_first_entry(
            table_schema=MyDatabaseModel,
            **kwargs
        )
