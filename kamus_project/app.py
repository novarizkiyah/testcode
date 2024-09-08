from flask import Flask, render_template, request, redirect, url_for
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

app = Flask(__name__)

# Setup Google Sheets connection
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join('adept-ethos-272307-a3582e24ba23.json'), scope)
client = gspread.authorize(creds)

# Ganti 'YOUR_SPREADSHEET_ID' dengan ID spreadsheet Anda
SPREADSHEET_ID = 'Kamus Project'
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

@app.route('/')
def index():
    # Mengambil semua data dan mengubahnya menjadi list of dictionaries
    words = sheet.get_all_records()
    return render_template('index.html', words=words)

@app.route('/add', methods=['POST'])
def add_word():
    word = request.form['word']
    definition = request.form['definition']
    sheet.append_row([word, definition])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)