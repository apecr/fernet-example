import json
import logging
import uuid

import flask
from cryptography.fernet import Fernet

user_bp = flask.Blueprint("users", __name__, url_prefix="/users")
logger = logging.getLogger()


def create_user(token):
    return {"id": uuid.uuid4(), "token": token}


@user_bp.route("/", methods=["GET"])
def get_users():
    key = Fernet.generate_key()
    f = Fernet(key)
    tokens = (
        f.encrypt(b"A really secret message. Not for prying eyes."),
        f.encrypt(b"A really secret message. Not for prying eyes. Version 2"),
    )
    logger.info(tokens[0])
    logger.info(f.decrypt(tokens[0]))
    users = [create_user(token) for token in tokens]
    response = flask.make_response(json.dumps(users, default=str), 200)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response
