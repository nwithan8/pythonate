from flask import (
    Blueprint,
    jsonify,
)

from python8.rest_api.constants import (
    FLASK_GET,
    FLASK_POST
)
from python8.rest_api.controllers.authentication import (
    require_authentication,
    AuthenticationType
)

health = Blueprint("health", __name__, url_prefix="/health")


@health.route("/ok", methods=[FLASK_GET])
def health_ok():
    return jsonify({"status": "ok"})


@health.route("/boom", methods=[FLASK_POST])
@require_authentication(AuthenticationType.ADMIN)
def health_boom():
    raise Exception("boom, failed.")
