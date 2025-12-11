from typing import Optional, Dict, Any

from pydantic import BaseModel
from werkzeug.datastructures.file_storage import FileStorage


class BaseControllerModel(BaseModel):
    headers: Optional[Dict[str, Any]]
    method: str
    url: str
    path_params: Optional[Dict[str, Any]]
    query_params: Optional[Dict[str, Any]]
    raw_data: Optional[bytes] = None
    json_data: Optional[Dict[str, Any]] = None
    files: Optional[dict[str, list[FileStorage]]] = None

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def from_flask_request(cls, request: 'flask.Request') -> 'IncomingRequest':
        return BaseControllerModel(
            headers=dict(request.headers),
            method=request.method,
            url=request.url,
            path_params=dict(request.view_args),
            query_params=dict(request.args),
            raw_data=request.data,
            json_data=request.get_json(silent=True),
            files=request.files,  # type: ignore
        )

    def _get_value_from_json_data(self, *path) -> Optional[Any]:
        """
        Get a value from the JSON data using a path.
        :param path: Path to the value in the JSON data.
        :return: Value from the JSON data.
        """
        if self.json_data is None:
            return None

        value = self.json_data
        for key in path:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return None
        return value

    def _get_value_from_query_params(self, key: str) -> Optional[Any]:
        """
        Get a value from the query parameters
        :param key: Key to get the value for.
        :return: Value from the query parameters.
        """
        if self.query_params is None:
            return None

        return self.query_params.get(key, None)

    def _get_value_from_path_params(self, key: str) -> Optional[Any]:
        """
        Get a value from the path parameters
        :param key: Key to get the value for.
        :return: Value from the path parameters.
        """
        if self.path_params is None:
            return None

        return self.path_params.get(key, None)
