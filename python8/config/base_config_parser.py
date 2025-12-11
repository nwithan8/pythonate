import os
from typing import Any, Callable, Optional

import python8.core.dictionaries as json
import python8.core.yaml as yaml

from python8.core.general import set_default_if_none_or_empty

from python8.config.base_config_model import BaseConfigModel


def mark_exists(value: Optional[Any]) -> str:
    if value:
        return "Present"
    return "Not Present"


class ConfigSection:
    def __init__(self, data: dict):
        self.data = data

    def get_value(self, key: str, default: Any = None) -> Any:
        value = self.data.get(key, default)

        return set_default_if_none_or_empty(value=value, default=default)

    def get_subsection_data(self, key: str, optional: bool = False) -> dict:
        try:
            data = self.data[key]
            assert isinstance(data, dict)
            return data
        except KeyError:
            if optional:
                return {}
            raise KeyError(f"Subsection '{key}' not found in section")

    def to_model(self) -> BaseConfigModel:
        """
        Converts the section data to a BaseConfigModel.
        :return: An instance of BaseConfigModel with the section data.
        """
        raise NotImplementedError


class Config:
    def __init__(self, config_path: str, logging_function: Callable = None):
        """
        Initializes the Config object by loading a YAML configuration file.
        :param config_path: Path to the YAML configuration file.
        :param logging_function: Optional logging function to log the loaded configuration. If not provided, will not log.
        :raises FileNotFoundError: If the configuration file does not exist.
        """
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")

        self.yaml_data = yaml.load_from_file(file_path=config_path)
        self.json_data = json.load_from_string(json.object_to_json_string(self.yaml_data))

        self.root_section = ConfigSection(data=self.json_data)

        if logging_function:
            logging_function(f"Config loaded. Using the following settings:\n{self.__repr__()}")

    def as_json(self) -> dict:
        """
        Converts the configuration data to a JSON-compatible dictionary.
        :return: Dictionary representation of the configuration.
        """
        return self.root_section.data

    def as_yaml(self) -> str:
        return yaml.object_to_yaml_string(self.as_json(), sort_keys=False)

    def __repr__(self) -> str:
        return json.pretty_print(self.as_json(), sort=True)
