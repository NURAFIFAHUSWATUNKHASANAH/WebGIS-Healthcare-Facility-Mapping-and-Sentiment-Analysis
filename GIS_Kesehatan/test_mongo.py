from pymongo import MongoClient
import certifi

uri = "mongodb+srv://afifahhffi_db_user:a0IXA5ODF0XcRgaK@cluster0.g52wpk6.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(
        uri,
        tls=True,
        tlsCAFile=certifi.where()
    )

    print(client.admin.command("ping"))
    print("Koneksi berhasil")
except Exception as e:
    print("ERROR:")
    print(e)