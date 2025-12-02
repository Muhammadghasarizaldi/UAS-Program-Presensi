from flask import Flask, render_template, request, redirect, url_for
import csv, os
from datetime import datetime

app = Flask(__name__)
FILE = 'presensi.csv'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    nama = request.form.get('nama','').strip()
    if nama:
        with open(FILE,'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([nama, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
    return redirect(url_for('view'))

@app.route('/view')
def view():
    rows = []
    if os.path.exists(FILE):
        with open(FILE,'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
    return render_template('view.html', rows=rows)

@app.route('/clear', methods=['POST'])
def clear():
    if os.path.exists(FILE):
        open(FILE,'w', encoding='utf-8').close()
    return redirect(url_for('view'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
