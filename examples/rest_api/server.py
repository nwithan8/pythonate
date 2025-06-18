from examples.rest_api.constants import SQLITE_FILE
from examples.rest_api.database.my_database import MyDatabase
from python8.rest_api import (
    FlaskApp
)
from python8.rest_api.controllers import (
    setup_authentication,
    health_blueprint,
)
from python8.rest_api.constants import (
    FLASK_DATABASE_PATH
)

from examples.rest_api.controllers.my_controller import my_controller

# Initialize Flask application
application = FlaskApp("MY-SERVICE")

# Link the database path to the Flask app config
application.config[FLASK_DATABASE_PATH] = SQLITE_FILE

# Register Flask blueprints
application.register_blueprint(health_blueprint)
application.register_blueprint(my_controller)

# Set up authentication
database = MyDatabase(sqlite_file=SQLITE_FILE)
admin_api_key, was_set_up = setup_authentication(database=database)
if not was_set_up:
    print("System already established. Not echoing admin API key for security reasons.")
else:
    print(f"System set up successfully\nAdmin API key: {admin_api_key}")

# Run the Flask application
application.run(host="0.0.0.0", port=8080)  # Adjust host and port as needed
