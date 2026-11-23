from model.model_faskes import ModelFaskes


class ControllerFaskes:

    # ==========================
    # DATA KECAMATAN DROPDOWN
    # ==========================
    @staticmethod
    def get_kecamatan_dropdown():
        return ModelFaskes.get_all_kecamatan()

    # ==========================
    # LIST FASKES
    # ==========================
    @staticmethod
    def index():
        return ModelFaskes.get_all()

    # ==========================
    # DETAIL
    # ==========================
    @staticmethod
    def get_by_id(id):
        return ModelFaskes.get_by_id(id)

    # ==========================
    # SIMPAN
    # ==========================
    @staticmethod
    def store(data):
        return ModelFaskes.insert(data)

    # ==========================
    # UPDATE
    # ==========================
    @staticmethod
    def update(id, data):
        return ModelFaskes.update(id, data)

    # ==========================
    # DELETE
    # ==========================
    @staticmethod
    def delete(id):
        return ModelFaskes.delete(id)
    
    # ==========================
    # DASHBOARD STATISTIK
    # ==========================
    @staticmethod
    def get_dashboard_statistik():
        return ModelFaskes.get_dashboard_statistik()
    
    @staticmethod
    def get_charts_data():
        # Data untuk grafik per kecamatan
        per_kecamatan = ModelFaskes.get_stats_by_kecamatan()
        
        # Data untuk grafik jenis faskes (sudah ada di get_dashboard_statistik)
        stats = ModelFaskes.get_dashboard_statistik()
        
        return {
            "kecamatan": {
                "labels": [item["_id"] for item in per_kecamatan],
                "values": [item["total"] for item in per_kecamatan]
            },
            "jenis": {
                "labels": ["RS", "Puskesmas", "Klinik", "Apotek"],
                "values": [stats["rumah_sakit"], stats["puskesmas"], stats["klinik"], stats["apotek"]]
            }
        }