# Game Tebak Angka

Game Tebak Angka adalah aplikasi web sederhana yang dibuat menggunakan **Python** dan **Flask**. Pemain mencoba menebak angka rahasia berdasarkan tingkat kesulitan yang dipilih.

## Fitur

- Tiga tingkat kesulitan: Mudah, Sedang, dan Sulit.
- Rentang angka menyesuaikan tingkat kesulitan:
  - Mudah: 1–10
  - Sedang: 1–50
  - Sulit: 1–100
- Petunjuk apakah tebakan terlalu tinggi atau terlalu rendah.
- Jumlah kesempatan terbatas.
- Pesan ketika pemain menang atau kehabisan kesempatan.
- Pilihan untuk memulai permainan baru.
- Tampilan responsif.

## Tech Stack

- Python
- Flask
- HTML
- CSS

## 📁 Struktur Proyek

```text
game-tebak-angka/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── .env.example
├── .gitignore
└── README.md
```

> File `.env` berisi konfigurasi rahasia untuk penggunaan lokal. Jangan unggah file `.env` ke GitHub. Gunakan `.env.example` sebagai contoh konfigurasi tanpa nilai rahasia.

## Cara Menjalankan

### 1. Clone repositori

Ganti URL berikut dengan URL repositori GitHub milikmu.

```bash
git clone https://github.com/YeremiPurba/game-tebak-angka.git
cd game-tebak-angka
```

### 2. Buat dan aktifkan virtual environment

Di Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Jika PowerShell menolak menjalankan skrip aktivasi, kamu bisa menggunakan Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### 3. Instal dependensi

```bash
python -m pip install Flask python-dotenv
```

### 4. Siapkan variabel lingkungan

Buat file bernama `.env` di folder utama proyek, lalu isi dengan:

```env
SECRET_KEY=ganti-dengan-kunci-acak-yang-panjang
```

Gunakan nilai rahasia yang acak dan jangan membagikannya. Pastikan `.env` tercantum di `.gitignore`.

### 5. Jalankan aplikasi

```bash
python app.py
```

Buka alamat berikut di browser:

```text
http://127.0.0.1:5000
```

## Cara Bermain

1. Pilih tingkat kesulitan.
2. Masukkan tebakan angka sesuai rentang yang ditampilkan.
3. Baca petunjuk apakah angka rahasia lebih tinggi atau lebih rendah.
4. Terus menebak sampai berhasil atau kesempatan habis.
5. Pilih **Main Lagi** untuk memulai permainan baru.