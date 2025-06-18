from python8.rest_api.repositories.base_repository_model import BaseRepositoryModel


class MyRepositoryModel(BaseRepositoryModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
