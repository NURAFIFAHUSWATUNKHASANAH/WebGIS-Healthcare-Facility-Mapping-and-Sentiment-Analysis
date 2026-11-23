import json
from datetime import datetime

from flask import render_template, request, redirect, url_for, flash

from model.model_pengaturan import PengaturanModel


class PengaturanController:

    @staticmethod
    def index():

        layers = PengaturanModel.get_all()

        return render_template(
            "admin/pengaturan/index.html",
            page_active='upload_geojson',
            layers=layers
        )

    @staticmethod
    def create():
        return render_template(
            "admin/pengaturan/create.html"
        )

    @staticmethod
    def store():

        file = request.files.get("geojson")

        if not file:
            flash("File GeoJSON wajib dipilih")
            return redirect(
                url_for("pengaturan.create")
            )

        geojson_data = json.load(file)

        data = {
            "nama_layer": request.form["nama_layer"],
            "jenis_layer": request.form["jenis_layer"],
            "filename": file.filename,
            "geojson": geojson_data,
            "created_at": datetime.now()
        }

        PengaturanModel.insert(data)

        flash("GeoJSON berhasil diupload")

        return redirect(
            url_for("pengaturan.index")
        )

    @staticmethod
    def delete(id):

        PengaturanModel.delete(id)

        flash("Layer berhasil dihapus")

        return redirect(
            url_for("pengaturan.index")
        )