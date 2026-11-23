from config.database import db
from bson import ObjectId

collection = db["geojson_layers"]

class PengaturanModel:

    @staticmethod
    def get_all():
        return list(collection.find())

    @staticmethod
    def get_by_id(id):
        return collection.find_one({"_id": ObjectId(id)})

    @staticmethod
    def insert(data):
        return collection.insert_one(data)

    @staticmethod
    def delete(id):
        return collection.delete_one({
            "_id": ObjectId(id)
        })