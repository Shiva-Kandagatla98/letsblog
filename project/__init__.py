from flask import Flask, session
from project.routes import admin, student


def create_app():
    application = Flask(__name__)
    application.secret_key = "qazwsxedcrfvtgb"
    application.register_blueprint(student)
    application.register_blueprint(admin)

    return application
