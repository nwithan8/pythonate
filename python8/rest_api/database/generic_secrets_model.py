from python8.database.base_database_model import BaseDatabaseModel
import python8.database.imports as sqlalchemy_imports


class Secret(BaseDatabaseModel):
    __tablename__ = 'secrets'
    name = sqlalchemy_imports.Column("name", sqlalchemy_imports.String(255), primary_key=True, nullable=False)
    value = sqlalchemy_imports.Column("value", sqlalchemy_imports.String(255), nullable=False)

    def __init__(self, name: str, value: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name or kwargs.get('name', None)  # Field is non-nullable, will raise exception if not provided
        self.value = value or kwargs.get('value', None)  # Field is non-nullable, will raise exception if not provided
