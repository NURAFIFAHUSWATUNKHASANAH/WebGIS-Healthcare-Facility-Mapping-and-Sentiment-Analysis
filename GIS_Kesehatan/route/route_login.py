from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from controller.controller_login import ControllerLogin

login_bp = Blueprint(
    "login_bp",
    __name__
)

@login_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        admin = ControllerLogin.login(
            email,
            password
        )

        if admin:

            session["admin_id"] = str(admin["_id"])
            session["admin_nama"] = admin["nama"]
            session["admin_email"] = admin["email"]

            return redirect(url_for("dashboard_bp.dashboard"))

        flash(
            "Email atau password salah!",
            "danger"
        )

    return render_template("admin/login.html")


@login_bp.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login_bp.login"))