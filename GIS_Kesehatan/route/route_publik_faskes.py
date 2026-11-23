from flask import Blueprint, redirect, render_template, request
from controller.controller_komentar import ControllerKomentar
from controller.controller_publik_faskes import ControllerPublikFaskes
from controller.controller_kecamatan import ControllerKecamatan

faskes_publik_bp = Blueprint('faskes_publik', __name__)

@faskes_publik_bp.route('/faskes-direktori')
def index_publik():
    search_query = request.args.get('search', '')
    jenis_query = request.args.get('jenis', '')
    kecamatan_query = request.args.get('kecamatan', '')
    
    page = request.args.get('page', 1, type=int)
    per_page = 10

    result = ControllerPublikFaskes.get_all_filtered_paginated(
        search=search_query, 
        jenis=jenis_query, 
        kecamatan=kecamatan_query, 
        page=page, 
        per_page=per_page
    )

    # 🔥 INI YANG KURANG
    kecamatan_list = ControllerKecamatan.get_dropdown()

    return render_template(
        'publik/faskes/index.html',
        data=result["data"],
        total_data=result["total_data"],
        total_pages=result["total_pages"],
        current_page=result["current_page"],
        search_query=search_query,
        jenis_query=jenis_query,
        kecamatan_query=kecamatan_query,
        kecamatan_list=kecamatan_list  # 🔥 WAJIB DITAMBAH
    )

@faskes_publik_bp.route('/faskes/detail/<id>')
def detail_faskes(id):

    data = ControllerPublikFaskes.get_detail(id)

    print(data)  # DEBUG

    if not data:
        return "Data tidak ditemukan", 404

    return render_template(
        'publik/faskes/detail.html',
        item=data
    )

@faskes_publik_bp.route('/faskes/penilaian', methods=['POST'])
def simpan_penilaian():

    id_faskes = request.form.get('id_faskes')
    komentar = request.form.get('komentar')

    ControllerKomentar.simpan(
        id_faskes,
        komentar
    )

    return redirect('/faskes-direktori')