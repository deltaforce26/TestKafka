from flask import Flask

from db.database import init_db, test_connection
from flask_app.controllers.message_blueprints import message_bp

app = Flask(__name__)



app.register_blueprint(message_bp)


with app.app_context():
    test_connection()
    init_db()


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000,
        host='0.0.0.0'
    )
