from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary dictionary to store words (akan diganti dengan Google Sheets nanti)
dictionary = {}

@app.route('/')
def index():
    return render_template('index.html', words=dictionary)

@app.route('/add', methods=['POST'])
def add_word():
    word = request.form['word']
    definition = request.form['definition']
    dictionary[word] = definition
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)