from flask import Blueprint

from controller.controller_pengaturan import PengaturanController

pengaturan_bp = Blueprint(
    "pengaturan",
    __name__,
    url_prefix="/admin/pengaturan"
)

pengaturan_bp.route("/")(
    PengaturanController.index
)

pengaturan_bp.route("/create")(
    PengaturanController.create
)

pengaturan_bp.route(
    "/store",
    methods=["POST"]
)(
    PengaturanController.store
)

pengaturan_bp.route(
    "/delete/<id>"
)(
    PengaturanController.delete
)