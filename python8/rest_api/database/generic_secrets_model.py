from python8.database.base import BaseDatabaseModel


class Secret(BaseDatabaseModel):
    from sqlalchemy import (
        Column,
        String,
    )

    __tablename__ = 'secrets'
    name = Column("name", String(255), primary_key=True, nullable=False)
    value = Column("value", String(255), nullable=False)

    def __init__(self, name: str, value: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name or kwargs.get('name', None)  # Field is non-nullable, will raise exception if not provided
        self.value = value or kwargs.get('value', None)  # Field is non-nullable, will raise exception if not provided
