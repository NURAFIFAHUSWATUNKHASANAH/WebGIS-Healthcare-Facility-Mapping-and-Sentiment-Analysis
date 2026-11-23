document.addEventListener("DOMContentLoaded", function () {

    const btnLogout = document.getElementById("btnLogout");

    if (btnLogout) {

        btnLogout.addEventListener("click", function (e) {

            e.preventDefault();

            const url = this.getAttribute("href");

            // Deteksi tema aktif
            const isLayoutLight =
                document.documentElement.getAttribute("data-theme") === "light" ||
                document.body.getAttribute("data-theme") === "light";

            // Warna adaptif
            const bgModal = isLayoutLight ? "#ffffff" : "#111827";
            const titleColor = isLayoutLight ? "#0f172a" : "#f8fafc";

            Swal.fire({
                title: "Keluar Sistem?",
                text: "Anda akan keluar dari sistem.",
                icon: "warning",
                showCancelButton: true,

                background: bgModal,
                color: titleColor,

                confirmButtonColor: "#ef4444",
                cancelButtonColor: isLayoutLight ? "#64748b" : "#334155",

                confirmButtonText: "Ya, Keluar",
                cancelButtonText: "Batal",
                reverseButtons: true,

                customClass: {
                    popup: "premium-swal-popup",
                    title: "premium-swal-title",
                    htmlContainer: "premium-swal-text"
                }

            }).then((result) => {

                if (result.isConfirmed) {

                    Swal.fire({
                        title: "Proses...",
                        text: "Mohon tunggu sebentar",
                        background: bgModal,
                        color: titleColor,
                        allowOutsideClick: false,
                        showConfirmButton: false,
                        didOpen: () => {
                            Swal.showLoading();
                        }
                    });

                    setTimeout(() => {
                        window.location.href = url;
                    }, 500);

                }

            });

        });

    }

});