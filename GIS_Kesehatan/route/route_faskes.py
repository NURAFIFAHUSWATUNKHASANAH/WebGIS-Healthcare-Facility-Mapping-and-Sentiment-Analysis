import os
from werkzeug.utils import secure_filename
from flask import Blueprint, flash, redirect, render_template, request, url_for
from controller.controller_faskes import ControllerFaskes
from controller.controller_kecamatan import ControllerKecamatan

faskes_bp = Blueprint(
    'faskes',
    __name__,
    url_prefix='/admin/faskes'
)


@faskes_bp.route('/')
def index():

    data = ControllerFaskes.index()

    kecamatan_list = ControllerKecamatan.get_dropdown()

    return render_template(
        'admin/data_faskes/index.html',
        page_active='faskes',
        data=data,
        kecamatan_list=kecamatan_list
    )


@faskes_bp.route('/create', methods=['GET', 'POST'])
def create():

    if request.method == 'POST':

        foto = request.files.get("foto")
        nama_file = None

        if foto and foto.filename:

            nama_file = secure_filename(foto.filename)

            upload_folder = os.path.join(
                "static",
                "image",
                "faskes"
            )

            os.makedirs(upload_folder, exist_ok=True)

            foto.save(
                os.path.join(upload_folder, nama_file)
            )

        data = {
            "nama_faskes": request.form.get("nama_faskes"),
            "jenis_faskes": request.form.get("jenis_faskes"),
            "alamat": request.form.get("alamat"),
            "kecamatan": request.form.get("kecamatan"),
            "kelurahan": request.form.get("kelurahan"),
            "latitude": request.form.get("latitude"),
            "longitude": request.form.get("longitude"),
            "telepon": request.form.get("telepon"),
            "website": request.form.get("website"),
            "status_operasional": request.form.get("status_operasional"),
            "foto": nama_file
        }

        ControllerFaskes.store(data)

        flash(
            "Data fasilitas kesehatan berhasil disimpan.",
            "success"
        )

        return redirect(
            url_for('faskes.index')
        )

    kecamatan_list = ControllerFaskes.get_kecamatan_dropdown()

    return render_template(
        'admin/data_faskes/create.html',
        kecamatan_list=kecamatan_list
    )

@faskes_bp.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):

    item = ControllerFaskes.get_by_id(id)

    if request.method == 'POST':

        foto = request.files.get("foto")

        nama_file = item.get("foto")

        if foto and foto.filename:

            nama_file = secure_filename(foto.filename)

            upload_folder = os.path.join(
                "static",
                "image",
                "faskes"
            )

            os.makedirs(upload_folder, exist_ok=True)

            foto.save(
                os.path.join(upload_folder, nama_file)
            )

        data = {
            "nama_faskes": request.form.get("nama_faskes"),
            "jenis_faskes": request.form.get("jenis_faskes"),
            "alamat": request.form.get("alamat"),
            "kecamatan": request.form.get("kecamatan"),
            "kelurahan": request.form.get("kelurahan"),
            "latitude": request.form.get("latitude"),
            "longitude": request.form.get("longitude"),
            "telepon": request.form.get("telepon"),
            "website": request.form.get("website"),
            "status_operasional": request.form.get("status_operasional"),
            "foto": nama_file
        }

        ControllerFaskes.update(id, data)

        flash(
            "Data fasilitas kesehatan berhasil diperbarui.",
            "success"
        )

        return redirect(
            url_for('faskes.index')
        )

    kecamatan_list = ControllerFaskes.get_kecamatan_dropdown()

    return render_template(
        'admin/data_faskes/edit.html',
        item=item,
        kecamatan_list=kecamatan_list
    )

@faskes_bp.route('/delete/<id>')
def delete(id):

    ControllerFaskes.delete(id)

    flash(
        "Data fasilitas kesehatan berhasil dihapus.",
        "success"
    )

    return redirect(
        url_for('faskes.index')
    )