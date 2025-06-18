from python8.rest_api.database.generic_secrets_model import Secret

from python8.database import SQLAlchemyDatabase


class BaseDatabase(SQLAlchemyDatabase):
    def __init__(self,
                 sqlite_file: str):
        super().__init__(sqlite_file=sqlite_file)
        Secret.__table__.create(bind=self.engine, checkfirst=True)

    # region Secrets

    def add_secret(self, name: str, value: str) -> None | Secret:
        """
        Add a secret to the database
        :param name:
        :param value:
        :return:
        """
        try:
            return self._create_entry_fail_if_exists(table_schema=Secret, fields_to_check=["name"],  # type: ignore
                                                     name=name,
                                                     value=value)
        except Exception as e:
            raise Exception("Failed to add secret to database")

    def get_secret_by_name(self, name: str) -> None | str:
        """
        Get a secret by name
        :param name:
        :return:
        """
        try:
            return self._get_attribute_from_first_entry(table_schema=Secret, field_name="value",
                                                        name=name)
        except Exception as e:
            raise Exception("Failed to get secret from database")

    # endregion
