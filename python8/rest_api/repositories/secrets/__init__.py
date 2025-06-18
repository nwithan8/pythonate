from python8.rest_api.database.base_database import BaseDatabase
from python8.rest_api.repositories import BaseRepository

MASTER_KEY_NAME = "master_key"


class SecretRepository(BaseRepository):
    def __init__(self, database: BaseDatabase):
        super().__init__()
        self._database = database

    def add_admin_api_key_to_database(self, api_key: str) -> bool:
        """
        Add an admin API key to the database

        :param api_key: API key
        :return:
        """
        try:
            _ = self._database.add_secret(name=MASTER_KEY_NAME, value=api_key)
            return True
        except Exception as e:
            print(f'Error adding master secret to database: {e}')
            return False

    def get_admin_api_key_from_database(self) -> None | str:
        """
        Get the admin API key from the database

        :return:
        """
        try:
            return self._database.get_secret_by_name(name=MASTER_KEY_NAME)
        except Exception as e:
            print(f'Error getting master secret from database: {e}')
            return None
