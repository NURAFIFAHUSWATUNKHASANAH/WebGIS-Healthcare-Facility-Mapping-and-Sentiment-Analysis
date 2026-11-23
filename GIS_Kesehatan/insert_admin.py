from pymongo import MongoClient
from werkzeug.security import generate_password_hash

client = MongoClient(
    "mongodb+srv://afifahhffi_db_user:a0IXA5ODF0XcRgaK@cluster0.g52wpk6.mongodb.net/?appName=Cluster0"
)

db = client["gis_kesehatan"]

admin = {
    "nama": "Administrator",
    "email": "admin@healthgis.id",
    "password": generate_password_hash("admin123"),
    "status": True
}

# Cek apakah email sudah ada
if db.admin.find_one({"email": admin["email"]}):
    print("Admin sudah ada.")
else:
    db.admin.insert_one(admin)
    print("Admin berhasil ditambahkan.")