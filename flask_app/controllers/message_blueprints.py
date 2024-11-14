from flask import Blueprint, request, jsonify

from flask_app.producer import produce_to_kafka

message_bp = Blueprint('message_bp', __name__, url_prefix='/api')


@message_bp.route('/email', methods=['POST'])
def email():
    data = request.get_json()
    produce_to_kafka(data)
    return jsonify({'message': 'ok'}), 200




