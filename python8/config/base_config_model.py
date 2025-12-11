from pydantic import BaseModel


class BaseConfigModel(BaseModel):
    def as_dict(self) -> dict:
        raise NotImplementedError
