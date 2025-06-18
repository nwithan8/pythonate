from python8 import BaseDatabaseModel


class MyDatabaseModel(BaseDatabaseModel):
    def __init__(self, kwargs):
        """
        Initialize the database model
        """
        super().__init__(**kwargs)
