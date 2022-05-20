from flask import request, jsonify, Blueprint
from flask_expects_json import expects_json

from schema import ROUTING
from services.vroom import get_solution

api_v1 = Blueprint("api/v1", __name__, url_prefix='/api/v1/')


@api_v1.route("/calculate-route", methods=["POST"])
@expects_json(ROUTING)
def calculate_routes():
    data = request.get_json()

    solution = get_solution(data)

    return jsonify(solution)
