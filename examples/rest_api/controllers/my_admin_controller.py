from flask import request

from examples.rest_api.constants import SQLITE_FILE
from examples.rest_api.controllers.my_controller_model import MyControllerModel
from examples.rest_api.database.my_database import MyDatabase
from examples.rest_api.repositories.my_repository import MyRepository
from examples.rest_api.repositories.my_repository_model import MyRepositoryModel
from python8.rest_api.controllers import require_authentication, AuthenticationType
from python8.rest_api.controllers.admin import admin_blueprint as admin_controller
from python8.rest_api.utils import build_api_response

my_database = MyDatabase(sqlite_file=SQLITE_FILE)


@admin_controller.route("/example", methods=["GET"])
@require_authentication(database=my_database, auth_type=AuthenticationType.ADMIN)
def example_admin_route():
    """
    Example route for the admin_controller blueprint.
    This route can be accessed via GET request.
    """
    incoming_data = MyControllerModel.from_flask_request(request=request)

    resulting_data: MyRepositoryModel = MyRepository().get_data()

    response_data = {
        "message": "This is a response from the example route",
        "incoming_data": incoming_data.to_dict(),
        "resulting_data": resulting_data
    }

    return build_api_response(status_code=200, data=response_data)
