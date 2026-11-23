from config.database import db

kecamatan_collection = db["kecamatan"]
geojson_layers = db["geojson_layers"]


class ModelKecamatan:

    # =========================
    # AMBIL GEOJSON UTAMA
    # =========================
    @staticmethod
    def get_geojson_layer():
        return geojson_layers.find_one({})

    @staticmethod
    def sync_from_geojson():
        layer = geojson_layers.find_one({})

        if not layer:
            return

        geojson = layer.get("geojson", {})
        features = geojson.get("features", [])

        for f in features:
            props = f.get("properties", {})

            nama = (
                props.get("NAME_3") or
                props.get("nama") or
                props.get("kecamatan")
            )

            if not nama:
                continue

            kecamatan_collection.update_one(
                {"nama": nama},
                {
                    "$setOnInsert": {
                        "nama": nama,
                        "warna": "#00f2fe",
                        "keterangan": None
                    }
                },
                upsert=True
            )
            
    # =========================
    # AMBIL WARNA KECAMATAN
    # =========================
    @staticmethod
    def get_all_colors():
        return list(kecamatan_collection.find({}))

    # =========================
    # UPSERT WARNA
    # =========================
    @staticmethod
    def update_color(nama, warna, keterangan=None):
        update_data = {
            "nama": nama,
            "warna": warna
        }

        if keterangan is not None:
            update_data["keterangan"] = keterangan

        return kecamatan_collection.update_one(
            {"nama": nama},
            {"$set": update_data},
            upsert=True
        )
    
    @staticmethod
    def get_by_name(nama):
        return kecamatan_collection.find_one({"nama": nama})
    
# model/model_kecamatan.py

    @staticmethod
    def get_dropdown():
        return list(
            kecamatan_collection.find(
                {},
                {"nama": 1}
            ).sort("nama", 1)
        )