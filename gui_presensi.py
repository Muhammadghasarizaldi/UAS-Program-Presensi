import csv
import os
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox

FILE = 'presensi.csv'

def tambah_presensi(nama):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama, waktu])

def baca_presensi():
    rows = []
    if os.path.exists(FILE):
        with open(FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
    return rows

class PresensiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Aplikasi Presensi (GUI)')
        self.geometry('500x400')
        self.build_ui()

    def build_ui(self):
        frm = ttk.Frame(self, padding=10)
        frm.pack(fill='both', expand=True)

        ttk.Label(frm, text='Nama:').grid(column=0, row=0, sticky='w')
        self.nama_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.nama_var, width=40).grid(column=1, row=0, sticky='w')

        ttk.Button(frm, text='Presensi', command=self.on_presensi).grid(column=2, row=0, padx=5)

        self.tree = ttk.Treeview(frm, columns=('Nama','Waktu'), show='headings', height=15)
        self.tree.heading('Nama', text='Nama')
        self.tree.heading('Waktu', text='Waktu')
        self.tree.grid(column=0, row=1, columnspan=3, pady=10, sticky='nsew')

        frm.rowconfigure(1, weight=1)
        frm.columnconfigure(1, weight=1)

        ttk.Button(frm, text='Refresh', command=self.refresh).grid(column=0, row=2, pady=5, sticky='w')
        ttk.Button(frm, text='Clear CSV', command=self.clear_csv).grid(column=2, row=2, pady=5, sticky='e')

        self.refresh()

    def on_presensi(self):
        nama = self.nama_var.get().strip()
        if not nama:
            messagebox.showwarning('Peringatan','Nama tidak boleh kosong')
            return
        tambah_presensi(nama)
        self.nama_var.set('')
        self.refresh()

    def refresh(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for row in baca_presensi():
            self.tree.insert('', 'end', values=(row[0], row[1]))

    def clear_csv(self):
        if messagebox.askyesno('Konfirmasi','Hapus semua data presensi?'):
            open(FILE,'w').close()
            self.refresh()

if __name__ == '__main__':
    app = PresensiApp()
    app.mainloop()
