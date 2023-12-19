from flask import Flask

from core.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Flask extension

    # Flask blueprint
    from apps.auth.routes import auth_route
    app.register_blueprint(auth_route, url_prefix='/auth')

    # Flask custom exeption

    return app


app = create_app()
