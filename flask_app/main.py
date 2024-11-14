from flask import Flask
from flask_app.controllers.message_blueprints import message_bp

app = Flask(__name__)



app.register_blueprint(message_bp)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000,
        host='0.0.0.0'
    )
