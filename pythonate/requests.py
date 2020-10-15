from urllib.parse import urlencode
from typing import Union, List, Tuple

import requests
import pythonate.logs as logging


# HTTP Requests #
def http_get(url: str,
             params: dict = None,
             headers: dict = None,
             timeout: int = 2,
             log_level: str = None) -> Union[requests.Response, None]:
    if params:
        url += f"?{urlencode(params)}"
    try:
        res = requests.get(url=url, headers=headers, timeout=timeout)
        if log_level:
            logging.log(message=f"GET {url}", level=log_level)
            logging.log(message=f"Response: {res}", level=("error" if not res else log_level))
        return res
    except requests.exceptions.Timeout:
        return None


def http_post(url: str,
              params: dict = None,
              headers: dict = None,
              data: dict = None,
              timeout: int = 2,
              log_level: str = None) -> Union[requests.Response, None]:
    if params:
        url += f"?{urlencode(params)}"
    try:
        res = requests.post(url=url, json=data, headers=headers, timeout=timeout)
        if log_level:
            logging.log(message=f"POST {url}, Body: {data}", level=log_level)
            logging.log(message=f"Response: {res}", level=("error" if not res else log_level))
        return res
        # use json= rather than data= to convert single-quoted dict to double-quoted JSON
    except requests.exceptions.Timeout:
        return None


def http_put(url: str,
             params: dict = None,
             headers: dict = None,
             data: dict = None,
             timeout: int = 2,
             log_level: str = None) -> Union[requests.Response, None]:
    if params:
        url += f"?{urlencode(params)}"
    try:
        res = requests.put(url=url, json=data, headers=headers, timeout=timeout)
        if log_level:
            logging.log(message=f"PUT {url}, Body: {data}", level=log_level)
            logging.log(message=f"Response: {res}", level=("error" if not res else log_level))
        return res
        # use json= rather than data= to convert single-quoted dict to double-quoted JSON
    except requests.exceptions.Timeout:
        return None


def http_delete(url: str,
                params: dict = None,
                headers: dict = None,
                data: dict = None,
                timeout: int = 2,
                log_level: str = None) -> Union[requests.Response, None]:
    if params:
        url += f"?{urlencode(params)}"
    try:
        res = requests.delete(url=url, json=data, headers=headers, timeout=timeout)
        if log_level:
            logging.log(message=f"DELETE {url}, Body: {data}", level=log_level)
            logging.log(message=f"Response: {res}", level=("error" if not res else log_level))
        return res
        # use json= rather than data= to convert single-quoted dict to double-quoted JSON
    except requests.exceptions.Timeout:
        return None
