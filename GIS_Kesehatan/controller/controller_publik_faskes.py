from config.database import db
from controller.controller_komentar import ControllerKomentar
from model.model_faskes import ModelFaskes

class ControllerPublikFaskes:

    @staticmethod
    def get_limit_six():
        """Mengambil hanya 6 faskes teratas untuk kebutuhan landing page"""
        try:
            return list(db.faskes.find().limit(3)) # Kembalikan ke 6 sesuai rencana awal Anda
        except Exception as e:
            print(f"Error get_limit_six: {e}")
            return []

    @staticmethod
    def get_all_filtered_paginated(search="", jenis="", kecamatan="", page=1, per_page=10):
        """Mengambil data faskes dengan filter dan pagination"""
        try:
            query = {}

            if search:
                query["nama_faskes"] = {
                    "$regex": search,
                    "$options": "i"
                }

            if jenis:
                query["jenis_faskes"] = jenis

            if kecamatan:
                query["kecamatan"] = kecamatan

            # Hitung total data
            total_data = db.faskes.count_documents(query)

            # Pagination
            skip = (page - 1) * per_page

            # Ambil data faskes
            data_faskes = list(
                db.faskes.find(query)
                .skip(skip)
                .limit(per_page)
            )

            # Tambahkan rating dan total ulasan setiap faskes
            for item in data_faskes:

                statistik = ControllerKomentar.get_statistik(
                    str(item["_id"])
                )

                item["rating"] = statistik["rating"]
                item["total_ulasan"] = statistik["total"]

            # Hitung total halaman
            total_pages = (total_data + per_page - 1) // per_page

            return {
                "data": data_faskes,
                "total_data": total_data,
                "total_pages": total_pages,
                "current_page": page
            }

        except Exception as e:
            print(f"Error get_all_filtered_paginated: {e}")

            return {
                "data": [],
                "total_data": 0,
                "total_pages": 1,
                "current_page": 1
            }
        
    @staticmethod
    def get_detail(id):
        try:
            return ModelFaskes.get_by_id(id)
        except Exception as e:
            print(f"Error get_detail: {e}")
            return None