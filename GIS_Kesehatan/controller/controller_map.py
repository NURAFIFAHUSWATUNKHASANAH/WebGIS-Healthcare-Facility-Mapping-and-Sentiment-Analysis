from model.model_kecamatan import ModelKecamatan
from model.model_faskes import ModelFaskes

class ControllerMap:

    @staticmethod
    def get_geojson_colored():
        layer = ModelKecamatan.get_geojson_layer()

        if not layer:
            return {
                "type": "FeatureCollection",
                "features": []
            }

        geojson = layer.get("geojson", {})
        features = geojson.get("features", [])

        # 1. Hitung statistik faskes per kecamatan
        all_faskes = ModelFaskes.get_all() or []
        faskes_stat = {}
        for faskes in all_faskes:
            kec = faskes.get("kecamatan")
            jenis = faskes.get("jenis_faskes")
            if kec:
                if kec not in faskes_stat:
                    faskes_stat[kec] = {
                        "Rumah Sakit": 0,
                        "Puskesmas": 0,
                        "Klinik": 0,
                        "Laboratorium": 0,
                        "Apotek": 0,
                        "Total": 0
                    }
                if jenis in faskes_stat[kec]:
                    faskes_stat[kec][jenis] += 1
                faskes_stat[kec]["Total"] += 1

        # 2. Ambil data kecamatan (warna & keterangan) dari MongoDB
        kecamatan_db = ModelKecamatan.get_all_colors() or []
        kecamatan_map = {item["nama"]: item for item in kecamatan_db}

        result_features = []

        for f in features:
            props = f.get("properties", {})

            nama = (
                props.get("NAME_3")
                or props.get("nama")
                or props.get("NAMA")
                or props.get("kecamatan")
            )

            if not nama:
                continue

            db_data = kecamatan_map.get(nama, {})
            stat_kec = faskes_stat.get(nama, {
                "Rumah Sakit": 0,
                "Puskesmas": 0,
                "Klinik": 0,
                "Laboratorium": 0,
                "Apotek": 0,
                "Total": 0
            })

            # Kembalikan properti warna ke GeoJSON
            props["nama"] = nama
            props["warna"] = db_data.get("warna", "#00f2fe")  # <-- Dikembalikan
            props["keterangan"] = db_data.get("keterangan", "")
            
            # Properti statistik faskes
            props["jumlah_rs"] = stat_kec["Rumah Sakit"]
            props["jumlah_pusk"] = stat_kec["Puskesmas"]
            props["jumlah_klinik"] = stat_kec["Klinik"]
            props["jumlah_lab"] = stat_kec["Laboratorium"]
            props["jumlah_apotek"] = stat_kec["Apotek"]
            props["jumlah_total"] = stat_kec["Total"]

            result_features.append(f)

        return {
            "type": "FeatureCollection",
            "features": result_features
        }