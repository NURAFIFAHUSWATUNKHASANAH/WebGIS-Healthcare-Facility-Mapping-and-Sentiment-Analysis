from model.model_kecamatan import ModelKecamatan


class ControllerKecamatan:

    @staticmethod
    def index():

        # AUTO SYNC DATA KECAMATAN DARI GEOJSON
        ModelKecamatan.sync_from_geojson()
        layer = ModelKecamatan.get_geojson_layer()
        if not layer:
            return []
        geojson = layer.get("geojson", {})
        features = geojson.get("features", [])
        kecamatan_db = ModelKecamatan.get_all_colors()

        # Mapping berdasarkan nama kecamatan
        kecamatan_map = {
            item["nama"]: item
            for item in kecamatan_db
        }
        result = []
        for f in features:
            props = f.get("properties", {})
            nama = (
                props.get("NAME_3")
                or props.get("nama")
                or props.get("kecamatan")
            )

            if not nama:
                continue

            # Ambil data dari koleksi kecamatan
            db_data = kecamatan_map.get(nama, {})

            result.append({
                "nama": nama,
                "warna": db_data.get("warna", "#00f2fe"),
                "keterangan": db_data.get("keterangan"),
                "geometry": f.get("geometry")
            })

        return result

    # =========================
    # UPDATE WARNA
    # =========================
    @staticmethod
    def update_warna(nama, warna, keterangan=None):
        return ModelKecamatan.update_color(nama, warna, keterangan)

    @staticmethod
    def get_by_name(nama):
        return ModelKecamatan.get_by_name(nama)

    @staticmethod
    def get_dropdown():
        return ModelKecamatan.get_dropdown()