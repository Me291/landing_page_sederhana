# Landing Page Sederhana dengan Django

Proyek ini adalah landing page sederhana yang dibuat menggunakan **Django**, framework web berbasis Python. Proyek ini memungkinkan navigasi antara beberapa halaman seperti **Home** dan **About**.

## 🚀 Fitur
- Menampilkan halaman utama (Home)
- Menampilkan halaman About
- Struktur proyek yang rapi dan modular
- Menggunakan **Django Templates** untuk render halaman
- Konfigurasi URL routing untuk navigasi antar halaman

## 🛠️ Instalasi & Setup
### 1. Clone Repository
```sh
git clone https://github.com/Me291/landing_page_sederhana.git
cd landing_page_sederhana
```

### 2. Buat Virtual Environment
```sh
python -m venv env
source env/bin/activate  # Untuk macOS/Linux
env\Scripts\activate    # Untuk Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Migrasi Database
```sh
python manage.py migrate
```

### 5. Jalankan Server Django
```sh
python manage.py runserver
```
Kemudian buka **http://127.0.0.1:8000/home/** di browser.

---

## 📂 Struktur Proyek
```
landing_page_sederhana/
│-- web/                 # Folder utama proyek Django
│   │-- settings.py       # Konfigurasi Django
│   │-- urls.py           # Routing utama
│-- landing/             # Aplikasi utama
│   │-- templates/
│   │   │-- landing/
│   │   │   │-- home.html   # Template halaman Home
│   │   │   │-- about.html  # Template halaman About
│   │-- views.py         # Logika tampilan halaman
│   │-- urls.py          # Routing aplikasi landing
│-- manage.py           # File manajemen Django
│-- db.sqlite3          # Database default Django
```

---

## 🔗 URL Endpoints
| URL         | Halaman  |
|------------|----------|
| `/home/`   | Home     |
| `/about/`  | About    |

---

## 📌 Deployment
Untuk melakukan deploy ke **Heroku**, **Railway**, atau **Render**, pastikan:
- **Gunakan PostgreSQL** untuk database produksi.
- **Tambahkan `gunicorn`** sebagai WSGI server.
- **Buat file `Procfile`** untuk menjalankan Django di production.

---

## 🤝 Kontribusi
Jika ingin berkontribusi, silakan fork repository ini dan buat pull request.

1. Fork repo ini.
2. Buat branch baru (`git checkout -b feature-branch`).
3. Commit perubahan (`git commit -m "Menambahkan fitur baru"`).
4. Push ke branch (`git push origin feature-branch`).
5. Buat pull request!

---

## 📞 Kontak
Jika ada pertanyaan, hubungi saya di [GitHub](https://github.com/Me291) atau email saya di **your-email@example.com**.

---

**Django Landing Page Sederhana** - 2025

