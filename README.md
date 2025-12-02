# Presensi 

Folder ini berisi aplikasi Presensi dan Counting dalam tiga varian:
- CLI (command-line)
- GUI (Tkinter)
- Web (Flask)

## Struktur
presensi_app/
  - main_presensi.py  (CLI)
  - gui_presensi.py   (Tkinter GUI)
  - web_presensi.py   (Flask web app)

counting_app/
  - main_counting.py  (CLI)
  - gui_counting.py   (Tkinter GUI)
  - web_counting.py   (Flask web app)

## Menjalankan
- CLI: `python main_presensi.py` atau `python main_counting.py`
- GUI: `python gui_presensi.py` atau `python gui_counting.py`
- Web: `python web_presensi.py` (port 5000) atau `python web_counting.py` (port 5001)

## Requirements
- Python 3.8+
- Flask (jika menjalankan server web)

Install dependencies:
```bash
pip install -r requirements.txt
```
