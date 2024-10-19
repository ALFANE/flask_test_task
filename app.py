import os
from flask import Flask
from extensions import db
from routes.api import api_blueprint
from routes.admin_client import admin_blueprint


def create_app():
    app = Flask(__name__)
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f'sqlite:///{os.path.join(BASE_DIR, "database.db")}'
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "your_secret_key"

    db.init_app(app)

    app.register_blueprint(api_blueprint, url_prefix="/api")
    app.register_blueprint(admin_blueprint, url_prefix="/admin")

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
