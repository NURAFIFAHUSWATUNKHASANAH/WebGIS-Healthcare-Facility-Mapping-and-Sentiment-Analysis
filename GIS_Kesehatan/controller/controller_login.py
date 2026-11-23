from model.model_login import ModelLogin
from werkzeug.security import check_password_hash

class ControllerLogin:

    @staticmethod
    def login(email, password):

        admin = ModelLogin.get_admin_by_email(email)

        if admin is None:
            return None

        if not check_password_hash(
            admin["password"],
            password
        ):
            return None

        return admin