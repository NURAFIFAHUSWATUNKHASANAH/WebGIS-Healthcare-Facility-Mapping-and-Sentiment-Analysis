from bson import ObjectId

from config.database import db

komentar_collection = db["komentar_faskes"]

class ModelKomentar:

    @staticmethod
    def insert(data):
        return komentar_collection.insert_one(data)

    @staticmethod
    def get_by_faskes(id_faskes):
        return list(
            komentar_collection.find(
                {"id_faskes": id_faskes}
            ).sort("created_at", -1)
        )
    from bson import ObjectId

    @staticmethod
    def get_all():

        pipeline = [

            {
                "$addFields": {
                    "id_faskes_obj": {
                        "$toObjectId": "$id_faskes"
                    }
                }
            },

            {
                "$lookup": {
                    "from": "faskes",
                    "localField": "id_faskes_obj",
                    "foreignField": "_id",
                    "as": "faskes"
                }
            },

            {
                "$unwind": {
                    "path": "$faskes",
                    "preserveNullAndEmptyArrays": True
                }
            },

            {
                "$sort": {
                    "created_at": -1
                }
            }

        ]

        return list(
            komentar_collection.aggregate(pipeline)
        )

    @staticmethod
    def delete(id):

        komentar_collection.delete_one({
            "_id":ObjectId(id)
        })

    @staticmethod
    def get_statistik(id_faskes):

        pipeline = [
            {
                "$match": {
                    "id_faskes": str(id_faskes)
                }
            },
            {
                "$group": {
                    "_id": "$sentimen",
                    "jumlah": {
                        "$sum": 1
                    }
                }
            }
        ]

        hasil = list(komentar_collection.aggregate(pipeline))

        positif = 0
        negatif = 0

        for item in hasil:
            if item["_id"] == "positif":
                positif = item["jumlah"]
            elif item["_id"] == "negatif":
                negatif = item["jumlah"]

        total = positif + negatif

        if total == 0:
            rating = 0
        else:
            rating = round(1 + ((positif / total) * 4), 1)

        return {
            "positif": positif,
            "negatif": negatif,
            "total": total,
            "rating": rating
        }