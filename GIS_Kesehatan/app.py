from flask import Flask, render_template
from controller.controller_faskes import ControllerFaskes
from controller.controller_kecamatan import ControllerKecamatan
from controller.controller_publik_faskes import ControllerPublikFaskes
from route.route_login import login_bp
from route.route_dashboard import dashboard_bp
from route.route_faskes import faskes_bp
from route.route_pengaturan import pengaturan_bp
from route.route_kecamatan import kecamatan_bp
from route.route_map import map_bp
from route.route_publik_faskes import faskes_publik_bp
from route.route_komentar import komentar_bp

app = Flask(__name__)

app.register_blueprint(login_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(faskes_bp)
app.register_blueprint(pengaturan_bp)
app.register_blueprint(kecamatan_bp)
app.register_blueprint(map_bp)
app.register_blueprint(faskes_publik_bp)
app.register_blueprint(komentar_bp)

app.config['SECRET_KEY'] = 'gis_kesehatan_2026'

@app.route('/')
def home():

    # STATISTIK
    stat = ControllerFaskes.get_dashboard_statistik()

    # LIST FASKES (UNTUK DIREKTORI)
    data_limit = ControllerPublikFaskes.get_limit_six()

    # DROPDOWN KECAMATAN
    kecamatan_list = ControllerKecamatan.get_dropdown()
    chart_data = ControllerFaskes.get_charts_data()

    return render_template(
        'landingpage.html',

        # STATISTIK
        total_kecamatan=stat["kecamatan"],
        total_rs=stat["rumah_sakit"],
        total_puskesmas=stat["puskesmas"] + stat["klinik"],
        total_apotek=stat["apotek"],

        # DIREKTORI DATA
        data=data_limit,
        kecamatan_list=kecamatan_list,
        chart_data=chart_data
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)