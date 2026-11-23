from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for

from controller.controller_kecamatan import ControllerKecamatan
from controller.controller_komentar import ControllerKomentar

komentar_bp = Blueprint(
    "komentar_bp",
    __name__
)


@komentar_bp.route("/admin/komentar")
def index():

    data = ControllerKomentar.get_all()
    kecamatan_list = ControllerKecamatan.get_dropdown()

    return render_template(
        "admin/komentar/index.html",
        data=data,
        kecamatan_list=kecamatan_list,
        page_active="komentar"
    )


@komentar_bp.route("/admin/komentar/delete/<id>")
def delete(id):

    ControllerKomentar.delete(id)

    return redirect(
        url_for("komentar_bp.index")
    )