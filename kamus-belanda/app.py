from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Mengizinkan cross-origin requests

# Route untuk URL root '/'
@app.route('/')
def home():
    return "Hello, this is the homepage!"

# Menghubungkan ke database SQLite
def connect_db():
    conn = sqlite3.connect('kamus_belanda.db')
    return conn

# Membuat tabel jika belum ada
def create_table():
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS kamus (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kalimat_belanda TEXT NOT NULL,
            terjemahan_indonesia TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Route untuk menambah kalimat baru
@app.route('/tambah', methods=['POST'])
def tambah_kalimat():
    data = request.json
    kalimat_belanda = data.get('kalimat_belanda')
    terjemahan_indonesia = data.get('terjemahan_indonesia')

    if not kalimat_belanda or not terjemahan_indonesia:
        return jsonify({'error': 'Kalimat atau terjemahan tidak boleh kosong.'}), 400

    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO kamus (kalimat_belanda, terjemahan_indonesia) VALUES (?, ?)", 
              (kalimat_belanda, terjemahan_indonesia))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Kalimat berhasil ditambahkan!'})

# Route untuk mencari terjemahan
@app.route('/cari', methods=['GET'])
def cari_kalimat():
    kalimat_belanda = request.args.get('kalimat_belanda')
    
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT terjemahan_indonesia FROM kamus WHERE kalimat_belanda = ?", (kalimat_belanda,))
    result = c.fetchone()
    conn.close()

    if result:
        return jsonify({'kalimat_belanda': kalimat_belanda, 'terjemahan_indonesia': result[0]})
    else:
        return jsonify({'error': 'Kalimat tidak ditemukan'}), 404

# Route untuk mendapatkan kuis acak
@app.route('/quiz', methods=['GET'])
def quiz():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT kalimat_belanda, terjemahan_indonesia FROM kamus ORDER BY RANDOM() LIMIT 1")
    result = c.fetchone()
    conn.close()

    if result:
        return jsonify({'kalimat_belanda': result[0], 'terjemahan_indonesia': result[1]})
    else:
        return jsonify({'error': 'Tidak ada kalimat dalam database'}), 404

if __name__ == "__main__":
    create_table()  # Membuat tabel jika belum ada
    app.run(debug=True)
