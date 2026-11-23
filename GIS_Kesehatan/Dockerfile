# Menggunakan image resmi Python
FROM python:3.10-slim

# Menentukan direktori kerja di dalam container
WORKDIR /app

# Menyalin file requirements.txt terlebih dahulu agar bisa dicache oleh Docker
COPY requirements.txt .

# Menginstal semua dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin seluruh file proyek ke dalam container
COPY . .

# Menentukan port dan perintah untuk menjalankan aplikasi menggunakan Gunicorn
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]