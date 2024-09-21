import sqlite3
import random

# Membuat/menghubungkan database SQLite
conn = sqlite3.connect('kamus_belanda.db')
c = conn.cursor()

# Membuat tabel jika belum ada
c.execute('''
    CREATE TABLE IF NOT EXISTS kamus (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kalimat_belanda TEXT NOT NULL,
        terjemahan_indonesia TEXT NOT NULL
    )
''')

# Fungsi untuk menambah kalimat baru ke kamus
def tambah_kalimat(kalimat_belanda, terjemahan_indonesia):
    c.execute("INSERT INTO kamus (kalimat_belanda, terjemahan_indonesia) VALUES (?, ?)", 
              (kalimat_belanda, terjemahan_indonesia))
    conn.commit()
    print(f'Kalimat "{kalimat_belanda}" berhasil ditambahkan.')

# Fungsi untuk mencari terjemahan kalimat
def cari_kalimat(kalimat_belanda):
    c.execute("SELECT terjemahan_indonesia FROM kamus WHERE kalimat_belanda = ?", (kalimat_belanda,))
    result = c.fetchone()
    if result:
        print(f'Terjemahan: {result[0]}')
    else:
        print(f'Kalimat "{kalimat_belanda}" tidak ditemukan.')

# Fungsi untuk melakukan quiz acak
def quiz():
    c.execute("SELECT kalimat_belanda, terjemahan_indonesia FROM kamus ORDER BY RANDOM() LIMIT 1")
    result = c.fetchone()
    if result:
        jawaban = input(f'Apa arti dari "{result[0]}"? ')
        if jawaban.lower() == result[1].lower():
            print("Benar!")
        else:
            print(f'Salah. Jawaban yang benar adalah "{result[1]}".')

# Fungsi menu utama
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Kalimat")
        print("2. Cari Kalimat")
        print("3. Kuis Acak")
        print("4. Keluar")
        pilihan = input("Pilih opsi: ")
        
        if pilihan == '1':
            kalimat_belanda = input("Masukkan kalimat bahasa Belanda: ")
            terjemahan_indonesia = input("Masukkan terjemahannya dalam bahasa Indonesia: ")
            tambah_kalimat(kalimat_belanda, terjemahan_indonesia)
        
        elif pilihan == '2':
            kalimat_belanda = input("Masukkan kalimat bahasa Belanda yang ingin dicari: ")
            cari_kalimat(kalimat_belanda)
        
        elif pilihan == '3':
            quiz()
        
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main_menu()

# Menutup koneksi database saat aplikasi selesai
conn.close()
