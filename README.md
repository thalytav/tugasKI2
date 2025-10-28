## TUGAS 2 KEAMANAN INFORMASI Kelas C

| Nama | NRP |
|-------------|---------|
| Thalyta Vius Pramesti | 5025231055 |
| Aqila Zahira Naia Puteri Arifin | 5025231138 |

### Two-Way DES Encrypted Communication (Client–Server)
Implementasi sistem komunikasi dua arah menggunakan Data Encryption Standard (DES) sederhana berbasis Python socket.
Program ini memungkinkan dua perangkat (client dan server) bertukar pesan teks secara terenkripsi.

### Cara Menjalankan
**1. Jalankan Server:**
`python des_server.py`
- Masukkan key (8 karakter) untuk enkripsi.
- Server akan menunggu koneksi client di port default (5555).
- Server akan menampilkan IP yang bisa dihubungi (misal 192.168.x.x).
  
**2. Jalankan Client:**
`python des_client.py`
- Masukkan IP server (contoh: 192.168.1.10)
→ Gunakan IP perangkat yang menjalankan des_server.py
- Masukkan key yang sama dengan server.
- Ketik pesan untuk dikirim.
- Server akan menerima ciphertext, mendekripsi, dan dapat membalas.
  
**3. Keluar dari Program:**
Ketik `exit` di client untuk mengakhiri sesi
