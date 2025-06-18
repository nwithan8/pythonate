from flask import (
    Blueprint,
)

from python8.rest_api.constants import (
    FLASK_GET,
    FLASK_POST
)
from python8.rest_api.controllers.authentication import (
    require_authentication,
    AuthenticationType
)

admin = Blueprint("admin", __name__, url_prefix="/admin")
