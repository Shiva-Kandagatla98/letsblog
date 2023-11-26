from flask import Flask, session
from project.routes import admin, student


def create_app():
    app = Flask(__name__)
    app.secret_key = "qazwsxedcrfvtgb"
    app.register_blueprint(student)
    app.register_blueprint(admin)

    return app
