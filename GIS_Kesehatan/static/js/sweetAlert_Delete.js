document.addEventListener("DOMContentLoaded", function () {

    const deleteButtons = document.querySelectorAll(".btn-delete-layer");

    deleteButtons.forEach(button => {

        button.addEventListener("click", function () {

            const url = this.dataset.url;
            
            // 1. DETEKSI TEMA AKTIF (Mengecek atribut data-theme di html/body)
            // Sesuai dengan CSS kamu: [data-theme="light"]
            const isLayoutLight = document.documentElement.getAttribute('data-theme') === 'light' || 
                                  document.body.getAttribute('data-theme') === 'light';

            // 2. ATUR WARNA ADAPTIF UNTUK SWEETALERT
            const bgModal = isLayoutLight ? '#ffffff' : '#111827'; // Putih atau Navy Gelap Premium
            const titleColor = isLayoutLight ? '#0f172a' : '#f8fafc';
            const textColor = isLayoutLight ? '#475569' : '#94a3b8';

            Swal.fire({
                title: 'Hapus Data?',
                text: 'Data yang dihapus tidak dapat dikembalikan.',
                icon: 'warning',
                showCancelButton: true,
                
                // Kustomisasi Warna Berdasarkan Tema Aktif
                background: bgModal,
                color: titleColor,
                confirmButtonColor: '#ef4444', // Merah modern (Tailwind red-500)
                cancelButtonColor: isLayoutLight ? '#64748b' : '#334155', // Slate gray adaptif
                
                confirmButtonText: 'Ya, Hapus',
                cancelButtonText: 'Batal',
                reverseButtons: true,
                
                // Tambahan custom class untuk kontrol teks jika dibutuhkan lewat CSS
                customClass: {
                    popup: 'premium-swal-popup',
                    title: 'premium-swal-title',
                    htmlContainer: 'premium-swal-text'
                }
            }).then((result) => {

                if (result.isConfirmed) {

                    Swal.fire({
                        title: 'Menghapus...',
                        text: 'Mohon tunggu sebentar',
                        background: bgModal,
                        color: titleColor,
                        allowOutsideClick: false,
                        didOpen: () => {
                            Swal.showLoading();
                        }
                    });

                    window.location.href = url;
                }

            });

        });

    });

});