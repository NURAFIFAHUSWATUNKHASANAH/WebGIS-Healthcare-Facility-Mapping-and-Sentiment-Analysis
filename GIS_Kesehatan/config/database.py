from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://afifahhffi_db_user:a0IXA5ODF0XcRgaK@cluster0.g52wpk6.mongodb.net/?appName=Cluster0"
)

db = client["gis_kesehatan"]