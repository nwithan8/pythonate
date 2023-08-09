from typing import Union

import objectrest

import pythonate.logs as logs


def _log_call(http_type: str, url: str, level: logs.LogLevel = None) -> None:
    if level:
        logs.log(message=f"{http_type} {url}", level=level)


def _log_response(res: objectrest.Response, default_log_level: logs.LogLevel = None) -> None:
    if not res:
        logs.log(message=f"Response: {res}", level=logs.LogLevel.ERROR)
    else:
        logs.log(message=f"Response: {res}", level=default_log_level)


def get_and_log(url: str,
                params: dict = None,
                headers: dict = None,
                timeout: int = 2,
                log_level: logs.LogLevel = None) -> Union[objectrest.Response, None]:
    """
    Make a GET request to the given URL and log the request and response.
    :param url: The URL to make the request to.
    :type url: str
    :param params: The parameters to send with the request.
    :type params: dict
    :param headers: The headers to send with the request.
    :type headers: dict
    :param timeout: The timeout to use for the request.
    :type timeout: int
    :param log_level: The log level to use for logging.
    :type log_level: LogLevel
    :return: The response from the request.
    :rtype: Union[objectrest.Response, None]
    """
    try:
        res = objectrest.get(url=url, params=params, headers=headers, timeout=timeout)
        _log_call("GET", url, log_level)
        _log_response(res, log_level)
        return res
    except objectrest.exceptions.Timeout:
        return None


def post_and_log(url: str,
                 params: dict = None,
                 headers: dict = None,
                 data: dict = None,
                 timeout: int = 2,
                 log_level: logs.LogLevel = None) -> Union[objectrest.Response, None]:
    """
    Make a POST request to the given URL and log the request and response.
    :param url: The URL to make the request to.
    :param params: The parameters to send with the request.
    :param headers: The headers to send with the request.
    :param data: The data to send with the request.
    :param timeout: The timeout to use for the request.
    :param log_level: The log level to use for logging.
    :return: The response from the request.
    :rtype: Union[objectrest.Response, None]
    """
    try:
        res = objectrest.post(url=url, params=params, headers=headers, data=data, timeout=timeout)
        _log_call("POST", url, log_level)
        _log_response(res, log_level)
        return res
    except objectrest.exceptions.Timeout:
        return None


def put_and_log(url: str,
                params: dict = None,
                headers: dict = None,
                data: dict = None,
                timeout: int = 2,
                log_level: logs.LogLevel = None) -> Union[objectrest.Response, None]:
    """
    Make a PUT request to the given URL and log the request and response.
    :param url: The URL to make the request to.
    :type url: str
    :param params: The parameters to send with the request.
    :type params: dict
    :param headers: The headers to send with the request.
    :type headers: dict
    :param data: The data to send with the request.
    :type data: dict
    :param timeout: The timeout to use for the request.
    :type timeout: int
    :param log_level: The log level to use for logging.
    :type log_level: LogLevel
    :return: The response from the request.
    :rtype: Union[objectrest.Response, None]
    """
    try:
        res = objectrest.put(url=url, params=params, headers=headers, data=data, timeout=timeout)
        _log_call("PUT", url, log_level)
        _log_response(res, log_level)
        return res
    except objectrest.exceptions.Timeout:
        return None


def patch_and_log(url: str,
                  params: dict = None,
                  headers: dict = None,
                  data: dict = None,
                  timeout: int = 2,
                  log_level: logs.LogLevel = None) -> Union[objectrest.Response, None]:
    """
    Make a PATCH request to the given URL and log the request and response.
    :param url: The URL to make the request to.
    :type url: str
    :param params: The parameters to send with the request.
    :type params: dict
    :param headers: The headers to send with the request.
    :type headers: dict
    :param data: The data to send with the request.
    :type data: dict
    :param timeout: The timeout to use for the request.
    :type timeout: int
    :param log_level: The log level to use for logging.
    :type log_level: logs.LogLevel
    :return: The response from the request.
    :rtype: Union[objectrest.Response, None]
    """
    try:
        res = objectrest.patch(url=url, params=params, headers=headers, data=data, timeout=timeout)
        _log_call("PATCH", url, log_level)
        _log_response(res, log_level)
        return res
    except objectrest.exceptions.Timeout:
        return None


def delete_and_log(url: str,
                   params: dict = None,
                   headers: dict = None,
                   data: dict = None,
                   timeout: int = 2,
                   log_level: logs.LogLevel = None) -> Union[objectrest.Response, None]:
    """
    Make a DELETE request to the given URL and log the request and response.
    :param url: The URL to make the request to.
    :type url: str
    :param params: The parameters to send with the request.
    :type params: dict
    :param headers: The headers to send with the request.
    :type headers: dict
    :param data: The data to send with the request.
    :type data: dict
    :param timeout: The timeout to use for the request.
    :type timeout: int
    :param log_level: The log level to use for logging.
    :type log_level: logs.LogLevel
    :return: The response from the request.
    :rtype: Union[objectrest.Response, None]
    """
    try:
        res = objectrest.delete(url=url, params=params, headers=headers, data=data, timeout=timeout)
        _log_call("DELETE", url, log_level)
        _log_response(res, log_level)
        return res
    except objectrest.exceptions.Timeout:
        return None
