from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json, os

app = Flask(__name__)

FILE = "data.json"


# ------------------------
# Load & Save JSON
# ------------------------
def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# ------------------------
# ROUTES
# ------------------------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add():
    nama = request.form["nama"]
    nim = request.form["nim"]

    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = load_data()

    new_item = {
        "id": len(data) + 1,
        "nama": nama,
        "nim": nim,
        "waktu": waktu
    }

    data.append(new_item)
    save_data(data)

    return redirect(url_for("index"))


@app.route("/view")
def view():
    data = load_data()
    data = list(reversed(data))  # tampilkan terbaru paling atas
    return render_template("view.html", data=data)


@app.route("/delete")
def delete_all():
    save_data([])
    return redirect(url_for("view"))


if __name__ == "__main__":
    app.run(debug=True)
