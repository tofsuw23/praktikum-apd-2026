import os
import random
from datetime import datetime
from prettytable import PrettyTable
from data import library_game

def hitung_koleksi():
    jumlah = len(library_game)
    return jumlah

def tampilkan_library():
    print("--- DAFTAR LIBRARY GAME ---")
    nomor = 0
    if len(library_game) == 0:
        print("Belum ada game di dalam library.")
        return 0

    tabel_game = PrettyTable()
    tabel_game.field_names = ["No", "Judul Game", "Playtime"]
    tabel_game.align["Judul Game"] = "l"
    tabel_game.align["Playtime"] = "r"

    for judul, jam in library_game.items():
        nomor += 1
        tabel_game.add_row([nomor, judul, f"{round(jam, 2)} Jam"])

    print(tabel_game)
    return nomor

def ambil_judul_game(nomor_target):
    urutan = 0
    for judul in library_game.keys():
        urutan += 1
        if urutan == nomor_target:
            return judul
    return None

def hitung_total_jam_rekursif(daftar_jam, indeks):
    if indeks == len(daftar_jam):
        return 0.0
    else:
        return daftar_jam[indeks] + hitung_total_jam_rekursif(daftar_jam, indeks + 1)

def lihat_library_lengkap():
    os.system("cls")
    jumlah_game = tampilkan_library()
    if jumlah_game > 0:
        list_jam = list(library_game.values())
        total_jam = round(hitung_total_jam_rekursif(list_jam, 0), 2)
        rekomendasi_acak = random.choice(list(library_game.keys()))
        tanggal_cek = datetime.now().strftime("%d/%m/%Y")

        tabel_info = PrettyTable()
        tabel_info.field_names = ["Ringkasan Library", "Keterangan"]
        tabel_info.align["Ringkasan Library"] = "l"
        tabel_info.align["Keterangan"] = "l"
        tabel_info.add_rows([
            ["Total Koleksi Game", f"{hitung_koleksi()} Game"],
            ["Total Jam Bermain", f"{total_jam} Jam"],
            ["Rekomendasi Game Acak", rekomendasi_acak],
            ["Tanggal Pengecekan", tanggal_cek]
        ])
        print(tabel_info)
    input("\nTekan Enter untuk kembali ke menu...")