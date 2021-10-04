import connexion
from connexion.apps.flask_app import FlaskJSONEncoder

def create_app():
    app = connexion.FlaskApp(
        __name__,
        specification_dir='openapi',
        options = {
            "swagger_ui": True,
            "serve_spec": True
        }
    )
    app.add_api("spec.yml", strict_validation = True)
    flask_app = app.app
    flask_app.json_encoder = FlaskJSONEncoder

    return flask_app
