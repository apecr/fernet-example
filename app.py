import click
from flask import Flask

from src.blueprint.user import user_bp
from src.helper.logging_helper import configure_logger

configure_logger()
app = None


def create_app():
    global app
    if app is None:
        app = Flask(__name__)
        app.config["PROPAGATE_EXCEPTIONS"] = True
        app.register_blueprint(user_bp)
    return app


@click.command()
@click.option("--port", "-p", help="Port where the application will run", default=5000)
def main(port):
    run_app = create_app()
    run_app.logger.debug("Creating the app")
    run_app.run(port=port, debug=True)


if __name__ == "__main__":
    main()
