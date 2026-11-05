import os
from data import library_game

def tambah_game():
    os.system("cls")
    print("--- TAMBAH GAME BARU KE LIBRARY ---")
    try:
        judul_baru = input("Masukkan Judul Game : ").strip()
        if judul_baru == "":
            raise ValueError("\n[!] Waduh, judul game nggak boleh kosong wak!")
        if library_game.get(judul_baru) != None:
            raise ValueError("\n[!] Game ini sudah ada di dalam library wak!")

        input_jam = input("Masukkan Playtime Awal (Jam, contoh 0 atau 6.7): ")
        jam_awal = float(input_jam)
        if jam_awal < 0:
            raise ValueError("\n[!] Jam bermain tidak boleh bernilai negatif wak!")
    except ValueError as e:
        if "could not convert" in str(e):
            print("\n[!] Input jam bermain tidak valid! Harus berupa angka.")
        else:
            print(e)
    else:
        library_game[judul_baru] = round(jam_awal, 2)
        print(f"\n[+] Mantap! Berhasil menambahkan -> {judul_baru}: {library_game[judul_baru]} Jam")
    finally:
        input("\nTekan Enter untuk kembali ke menu...")