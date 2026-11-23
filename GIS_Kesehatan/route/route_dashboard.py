from flask import Blueprint, render_template
from controller.controller_faskes import ControllerFaskes
from controller.controller_map import ControllerMap

dashboard_bp = Blueprint(
    'dashboard_bp',
    __name__
)

@dashboard_bp.route('/dashboard')
def dashboard():

    geojson = ControllerMap.get_geojson_colored()

    statistik = ControllerFaskes.get_dashboard_statistik()

    return render_template(
        'admin/dashboard/index.html',
        geojson=geojson,
        statistik=statistik,
        page_active='dashboard'
    )