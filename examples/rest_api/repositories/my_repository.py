from examples.rest_api.database.my_database import MyDatabase
from examples.rest_api.database.my_database_model import MyDatabaseModel
from examples.rest_api.repositories.my_repository_model import MyRepositoryModel
from python8.rest_api.repositories import BaseRepository


class MyRepository(BaseRepository):
    def __init__(self, **kwargs):
        super().__init__()

    def get_data(self, **kwargs):
        # Implement your data retrieval logic here
        database_model: MyDatabaseModel = MyDatabase().get_data(**kwargs)

        return MyRepositoryModel()
