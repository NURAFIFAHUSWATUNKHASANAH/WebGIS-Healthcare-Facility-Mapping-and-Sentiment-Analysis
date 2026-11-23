from flask import Blueprint, render_template, request, redirect, url_for, flash
from controller.controller_kecamatan import ControllerKecamatan

kecamatan_bp = Blueprint("kecamatan", __name__, url_prefix="/admin/kecamatan")


@kecamatan_bp.route("/")
def index():
    data = ControllerKecamatan.index()
    return render_template("admin/data_kecamatan/index.html", page_active='kecamatan', data=data)


@kecamatan_bp.route("/update", methods=["POST"])
def update():
    nama = request.form.get("nama")
    warna = request.form.get("warna")
    keterangan = request.form.get("keterangan")

    ControllerKecamatan.update_warna(nama, warna, keterangan)

    flash("Data kecamatan berhasil diupdate!", "success")
    return redirect(url_for("kecamatan.index"))

@kecamatan_bp.route("/edit/<nama>")
def edit(nama):

    print("NAMA DARI URL:", nama)

    data = ControllerKecamatan.get_by_name(nama)

    print("DATA DARI DB:", data)

    if not data:
        flash("Data kecamatan tidak ditemukan!", "danger")
        return redirect(url_for("kecamatan.index"))

    return render_template("admin/data_kecamatan/edit.html", item=data)