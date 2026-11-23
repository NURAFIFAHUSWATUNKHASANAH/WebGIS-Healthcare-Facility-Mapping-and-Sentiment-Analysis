from flask import Blueprint, render_template, jsonify
from controller.controller_map import ControllerMap

map_bp = Blueprint("map", __name__, url_prefix="/map")


@map_bp.route("/")
def index():
    return render_template("publik/map/index.html")


@map_bp.route("/geojson")
def geojson():
    data = ControllerMap.get_geojson_colored()
    return jsonify(data)