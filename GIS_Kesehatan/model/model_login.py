from config.database import db

class ModelLogin:

    collection = db["admin"]

    @staticmethod
    def get_admin_by_email(email):

        return ModelLogin.collection.find_one({

            "email": email,
            "status": True
        })