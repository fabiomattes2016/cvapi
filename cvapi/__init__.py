from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow

def create_app():
    app = Flask(__name__)
    ma = Marshmallow(app)

    @app.route('/validate-json', methods=['POST'])
    def validate_json():
        if request.json:
            return jsonify({'ok': 'dados válidos'}), 200

        return jsonify({}), 200

    return app