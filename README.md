# NGAWASIN.AI - Student Monitoring System

<div align="center">

![Python Version](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-squared&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat-squared&logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=flat-squared&logo=opencv&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFA6?style=flat-squared&logo=yolo&logoColor=black)
![Playsound](https://img.shields.io/badge/Playsound-Audio-FF6F61?style=flat-squared&logo=google-play&logoColor=white)

**Sistem Pemantauan Siswa Berbasis AI untuk Mendeteksi Penggunaan Handphone secara Real-Time.**

</div>

---

## 🏫 Proyek UAS - Kecerdasan Buatan

Proyek ini dikembangkan sebagai tugas akhir **UAS (Ujian Akhir Semester) mata kuliah Kecerdasan Buatan**. Sistem ini dirancang untuk memantau tingkat fokus siswa selama kegiatan belajar-mengajar atau ujian berlangsung dengan mendeteksi distraksi berupa penggunaan Handphone (HP) secara otomatis.

### 👥 Anggota Kelompok

| Nama Anggota | NPM |
| :--- | :---: |
| **Dwiyandra Raysha Putra Syawal** | `2410631170069` |
| **Ananda Fahrizal Assidiq** | `2410631170007` |

---

## 🛠️ Tech Stack & Modul Utama

Berikut adalah teknologi dan pustaka utama yang digunakan dalam pengembangan **NGAWASIN.AI**:

*   **[Python](https://www.python.org/)** `v3.8+` — Bahasa pemrograman utama proyek.
*   **[PyTorch](https://pytorch.org/)** — Engine utama untuk memuat dan menjalankan model neural network.
*   **[Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)** — Framework object detection state-of-the-art yang digunakan untuk mendeteksi handphone secara instan.
*   **[OpenCV](https://opencv.org/)** — Library pemrosesan gambar untuk akses webcam komputer dan penggambaran overlay grafis.
*   **[Playsound](https://pypi.org/project/playsound/)** — Modul Python untuk memainkan alarm peringatan audio secara otomatis.

---

## 🚀 Fitur Utama

1.  **Deteksi HP Real-Time (AI Engine)**: Menggunakan model YOLOv8 kustom (`dataTRAINING.pt`) yang dioptimalkan untuk mendeteksi perangkat handphone dalam berbagai sudut secara cepat.
2.  **Alarm Suara Peringatan**: Memainkan berkas audio peringatan (`jokowi-kaget.mp3`) secara otomatis ketika HP terdeteksi. Proses pemutaran suara berjalan di thread terpisah (*multithreading*) agar frame rate pemantauan kamera tetap lancar tanpa *lag*.
3.  **Cyber HUD Live Overlay**: Menampilkan kotak pembatas (*bounding box*) deteksi YOLO beserta indikator visual status distraksi langsung di layar kamera.
4.  **Dashboard Terminal Dinamis**: Antarmuka berbasis teks minimalis di terminal yang menampilkan status fokus siswa secara dinamis serta menghitung akumulasi total frekuensi pelanggaran.

---

## 📁 Struktur Proyek

```text
ngawasin-ai/
├── dataTRAINING.pt           # Model YOLOv8 kustom untuk deteksi HP
├── jokowi-kaget.mp3          # Berkas audio alarm peringatan
├── requirements.txt          # Daftar dependensi modul Python
├── README.md                 # Dokumentasi panduan sistem ini
└── src/
    ├── __init__.py           # File inisialisasi paket Python
    ├── __main__.py           # Entry point eksekusi paket
    ├── main.py               # Pemroses argument CLI (start / status)
    └── detector.py           # Logika utama deteksi & dashboard HUD
```

---

## 💻 Panduan Instalasi & Cara Mencoba (Step-by-Step)

Ikuti langkah-langkah di bawah ini untuk menjalankan sistem **NGAWASIN.AI** di komputer Anda:

### 1. Prasyarat Sistem
*   Pastikan Anda sudah menginstal **Python (versi 3.8 atau yang lebih baru)**. Anda dapat memverifikasinya melalui terminal:
    ```bash
    python --version
    ```
*   Pastikan komputer Anda memiliki perangkat **Webcam/Kamera bawaan** atau eksternal yang berfungsi dengan baik.

### 2. Kloning Repositori
Unduh kode sumber proyek dari GitHub dan masuk ke direktori proyek:
```bash
git clone https://github.com/dwiyandra-raysha/ngawasin-ai.git
cd ngawasin-ai
```
*(Catatan: Sesuaikan URL repositori di atas dengan URL repositori Anda jika berbeda)*

### 3. Setup Virtual Environment (Direkomendasikan)
Gunakan Virtual Environment agar library proyek ini terisolasi dan tidak bertabrakan dengan library Python lain di komputer Anda:

*   **Membuat Virtual Environment:**
    ```bash
    python -m venv venv
    ```
*   **Mengaktifkan Virtual Environment:**
    *   **Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```
    *   **Windows (CMD / Command Prompt):**
        ```cmd
        .\venv\Scripts\activate.bat
        ```
    *   **Linux / macOS:**
        ```bash
        source venv/bin/activate
        ```

### 4. Instalasi Dependensi
Instal modul-modul yang dibutuhkan dengan perintah berikut:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> [!NOTE]
> Proses instalasi `torch` (PyTorch) dan `ultralytics` mungkin memerlukan waktu beberapa menit tergantung pada kecepatan koneksi internet Anda.

### 5. Memulai Pemantauan
Setelah instalasi selesai, jalankan perintah berikut untuk mengaktifkan sistem:
```bash
python -m src start
```

*   **Cara kerja**: Jendela kamera webcam akan muncul dan terminal Anda akan berubah menjadi dashboard pemantauan real-time. Jika Anda memegang Handphone di depan kamera, sistem akan mendeteksinya, memutar alarm suara `jokowi-kaget.mp3`, dan menambahkan statistik pelanggaran di terminal.
*   **Menghentikan sistem**: Arahkan fokus ke jendela kamera lalu tekan tombol **[Q]** pada keyboard Anda, atau tekan **[Ctrl + C]** pada jendela terminal.

### 6. Memeriksa Status Mesin AI
Untuk melihat informasi ringkas status sistem dan engine yang terkonfigurasi, jalankan perintah:
```bash
python -m src status
```

---

## 💡 Troubleshooting (Pemecahan Masalah)

*   **Webcam Tidak Terdeteksi / Error OpenCV**:
    Jika program berhenti dengan error kamera, pastikan webcam Anda tidak sedang digunakan oleh aplikasi lain (seperti Zoom, Google Meet, dll). Jika Anda memiliki beberapa kamera (misal webcam eksternal), coba ubah indeks kamera pada baris `cap = cv2.VideoCapture(0)` di berkas [detector.py](file:///c:/Users/wixx/Downloads/ngawasin-ai/ngawasin-ai/src/detector.py#L64) menjadi `1` atau `2`.
*   **Suara Alarm Tidak Terdengar**:
    Pastikan berkas `jokowi-kaget.mp3` berada di direktori root yang sama dengan folder `src`. Pastikan juga volume audio komputer Anda aktif dan driver audio Anda sudah terinstal.

---

## 🤝 Kontribusi

Proyek ini dibuat untuk keperluan akademis mata kuliah Kecerdasan Buatan. Namun, masukan, saran perbaikan bug, atau penambahan fitur baru sangat kami apresiasi!

Langkah untuk berkontribusi:
1. **Fork** repositori ini.
2. Buat branch baru untuk fitur Anda (`git checkout -b fitur/FiturBaru`).
3. Commit perubahan Anda (`git commit -m 'Menambahkan Fitur Baru'`).
4. Push ke branch tersebut (`git push origin fitur/FiturBaru`).
5. Buat **Pull Request**.

