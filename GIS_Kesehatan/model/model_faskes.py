from config.database import db

faskes_collection = db["faskes"]
kecamatan_collection = db["kecamatan"]


class ModelFaskes:

    # ==========================
    # GET ALL KECAMATAN
    # ==========================
    @staticmethod
    def get_all_kecamatan():
        return list(
            kecamatan_collection.find(
                {},
                {"_id": 0}
            ).sort("nama", 1)
        )

    # ==========================
    # GET ALL FASKES
    # ==========================
    @staticmethod
    def get_all():
        return list(faskes_collection.find())

    # ==========================
    # GET BY ID
    # ==========================
    @staticmethod
    def get_by_id(id):
        from bson import ObjectId

        return faskes_collection.find_one({
            "_id": ObjectId(id)
        })

    # ==========================
    # INSERT
    # ==========================
    @staticmethod
    def insert(data):
        return faskes_collection.insert_one(data)

    # ==========================
    # UPDATE
    # ==========================
    @staticmethod
    def update(id, data):
        from bson import ObjectId

        return faskes_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": data}
        )

    # ==========================
    # DELETE
    # ==========================
    @staticmethod
    def delete(id):
        from bson import ObjectId

        return faskes_collection.delete_one({
            "_id": ObjectId(id)
        })
    

    # ==========================
    # DASHBOARD STATISTIK
    # ==========================
    @staticmethod

    def get_dashboard_statistik():

        total_rs = faskes_collection.count_documents({
            "jenis_faskes": "Rumah Sakit"
        })

        total_puskesmas = faskes_collection.count_documents({
            "jenis_faskes": "Puskesmas"
        })

        total_klinik = faskes_collection.count_documents({
            "jenis_faskes": "Klinik"
        })

        total_apotek = faskes_collection.count_documents({
            "jenis_faskes": "Apotek"
        })

        total_kecamatan = kecamatan_collection.count_documents({})

        return {
            "rumah_sakit": total_rs,
            "puskesmas": total_puskesmas,
            "klinik": total_klinik,
            "apotek": total_apotek,
            "kecamatan": total_kecamatan
        }
    
    @staticmethod
    def get_stats_by_kecamatan():
        # Agregasi untuk menghitung jumlah faskes per kecamatan
        pipeline = [
            {"$group": {"_id": "$kecamatan", "total": {"$sum": 1}}},
            {"$sort": {"total": -1}}
        ]
        return list(faskes_collection.aggregate(pipeline))