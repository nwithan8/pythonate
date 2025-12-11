def build_api_response(status_code: int = 200, data: dict = None) -> tuple['flask.Response', int]:
    """
    Build an API response with a status code and optional data.
    :param status_code: Status code to return (200 by default).
    :param data: Data to include in the response (None by default).
    :return: Tuple containing the status code and data.
    """
    from flask import jsonify
    if data is None:
        data = {}

    response = jsonify(data)

    headers = {
        "Content-Type": "application/json",
        'Cache-Control': "no-cache, no-store, must-revalidate, max-age=0",
        'Pragma': 'no-cache',
        'Expires': '0',
        "Access-Control-Allow-Origin": "*",
        # "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization",
    }
    for key, value in headers.items():
        response.headers[key] = value

    return response, status_code
