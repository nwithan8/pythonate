from typing import Union

import requests
from objectrest.request_handler import get, post, put, patch, delete, options, head, get_json, post_json, put_json, \
    patch_json, delete_json, get_object, post_object, put_object, patch_object, delete_object, get_proxy_dict

import pythonate.logs as logs


def _log_call(http_type: str, url: str, level: logs.LogLevel = None) -> None:
    if level:
        logs.log(message=f"{http_type} {url}", level=level)


def _log_response(res: requests.Response, default_log_level: logs.LogLevel = None) -> None:
    if not res:
        logs.log(message=f"Response: {res}", level=logs.LogLevel.ERROR)
    else:
        logs.log(message=f"Response: {res}", level=default_log_level)


def get_and_log(url: str,
                params: dict = None,
                headers: dict = None,
                timeout: int = 2,
                log_level: logs.LogLevel = None) -> Union[requests.Response, None]:
    try:
        res = get(url=url, params=params, headers=headers, timeout=timeout)
        _log_call("GET", url, log_level)
        _log_response(res, log_level)
        return res
    except requests.exceptions.Timeout:
        return None


def post_and_log(url: str,
                 params: dict = None,
                 headers: dict = None,
                 data: dict = None,
                 timeout: int = 2,
                 log_level: logs.LogLevel = None) -> Union[requests.Response, None]:
    try:
        res = post(url=url, params=params, headers=headers, data=data, timeout=timeout)
        _log_call("POST", url, log_level)
        _log_response(res, log_level)
        return res
    except requests.exceptions.Timeout:
        return None


def put_and_log(url: str,
                params: dict = None,
                headers: dict = None,
                data: dict = None,
                timeout: int = 2,
                log_level: logs.LogLevel = None) -> Union[requests.Response, None]:
    try:
        res = put(url=url, params=params, headers=headers, data=data, timeout=timeout)
        _log_call("PUT", url, log_level)
        _log_response(res, log_level)
        return res
    except requests.exceptions.Timeout:
        return None


def patch_and_log(url: str,
                  params: dict = None,
                  headers: dict = None,
                  data: dict = None,
                  timeout: int = 2,
                  log_level: logs.LogLevel = None) -> Union[requests.Response, None]:
    try:
        res = patch(url=url, params=params, headers=headers, data=data, timeout=timeout)
        _log_call("PATCH", url, log_level)
        _log_response(res, log_level)
        return res
    except requests.exceptions.Timeout:
        return None


def delete_and_log(url: str,
                   params: dict = None,
                   headers: dict = None,
                   data: dict = None,
                   timeout: int = 2,
                   log_level: logs.LogLevel = None) -> Union[requests.Response, None]:
    try:
        res = delete(url=url, params=params, headers=headers, data=data, timeout=timeout)
        _log_call("DELETE", url, log_level)
        _log_response(res, log_level)
        return res
    except requests.exceptions.Timeout:
        return None
