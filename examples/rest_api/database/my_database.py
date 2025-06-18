from examples.rest_api.database.my_database_model import MyDatabaseModel
from python8.rest_api.database.base_database import BaseDatabase


class MyDatabase(BaseDatabase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_data(self, **kwargs):
        # Implement your data retrieval logic here
        return self._get_first_entry(
            table_schema=MyDatabaseModel,
            **kwargs
        )
