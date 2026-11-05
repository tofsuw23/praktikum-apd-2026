import os
from prettytable import PrettyTable
from data import library_game
from read import tampilkan_library

def ambil_judul_game(nomor_target):
    urutan = 0
    for judul in library_game.keys():
        urutan += 1
        if urutan == nomor_target:
            return judul
    return None

def update_game_admin():
    os.system("cls")
    print("--- UPDATE & TRACKING PLAYTIME GAME ---")
    jumlah_game = tampilkan_library()

    if jumlah_game > 0:
        try:
            pilih_nomor = int(input("Masukkan nomor urut game yang mau di-update: "))
            if pilih_nomor < 1 or pilih_nomor > jumlah_game:
                raise ValueError("\n[!] Nomor urut game tidak ditemukan di daftar!")

            judul_terpilih = ambil_judul_game(pilih_nomor)
            jam_terpilih = library_game[judul_terpilih]

            print(f"\nGame Terpilih : {judul_terpilih} ({jam_terpilih} Jam)")
            tabel_opsi = PrettyTable()
            tabel_opsi.field_names = ["Opsi", "Jenis Update"]
            tabel_opsi.align["Jenis Update"] = "l"
            tabel_opsi.add_rows([
                ["1", "Tambah Jam Bermain"],
                ["2", "Ganti Total Jam Bermain Baru"],
                ["3", "Ganti Judul Game"]
            ])
            print(tabel_opsi)
            opsi_update = input("Pilih opsi update (1/2/3): ")

            if opsi_update == "1":
                jam_main = float(input("Masukkan tambahan jam bermain (contoh 6.7): "))
                if jam_main < 0:
                    raise ValueError("\n[!] Tambahan jam tidak boleh negatif!")
                library_game[judul_terpilih] = round(library_game[judul_terpilih] + jam_main, 2)
                print(f"\n[+] Playtime berhasil di-update -> {judul_terpilih}: {library_game[judul_terpilih]} Jam")

            elif opsi_update == "2":
                total_baru = float(input("Masukkan total jam bermain yang baru (contoh 16.7): "))
                if total_baru < 0:
                    raise ValueError("\n[!] Total jam tidak boleh negatif!")
                library_game.update({judul_terpilih: round(total_baru, 2)})
                print(f"\n[+] Total playtime berhasil diubah -> {judul_terpilih}: {library_game[judul_terpilih]} Jam")

            elif opsi_update == "3":
                nama_baru = input("Masukkan judul game yang baru: ").strip()
                if nama_baru == "":
                    raise ValueError("\n[!] Judul game baru tidak boleh kosong!")
                if library_game.get(nama_baru) != None and nama_baru != judul_terpilih:
                    raise ValueError("\n[!] Judul game tersebut sudah ada di library!")
                jam_lama = library_game.pop(judul_terpilih)
                library_game[nama_baru] = jam_lama
                print(f"\n[+] Judul game berhasil diubah -> {nama_baru}: {library_game[nama_baru]} Jam")

            else:
                raise ValueError("\n[!] Waduh, opsi update tidak ada di menu!")

        except ValueError as e:
            if "invalid literal" in str(e) or "could not convert" in str(e):
                print("\n[!] Input tidak valid! Harus berupa angka yang sesuai.")
            else:
                print(e)
        finally:
            input("\nTekan Enter untuk kembali ke menu...")
    else:
        input("\nTekan Enter untuk kembali ke menu...")

def update_playtime_user():
    os.system("cls")
    print("--- TRACKING PLAYTIME GAME STEAM ---")
    jumlah_game = tampilkan_library()

    if jumlah_game > 0:
        try:
            nomor_target = int(input("Masukkan nomor game yang baru dimainkan: "))
            if nomor_target < 1 or nomor_target > jumlah_game:
                raise ValueError("\n[!] Nomor game tidak ditemukan di daftar!")

            judul_terpilih = ambil_judul_game(nomor_target)
            tambah_jam = float(input(f"Masukkan tambahan jam main untuk '{judul_terpilih}': "))
            if tambah_jam < 0:
                raise ValueError("\n[!] Tambahan jam main tidak boleh negatif!")
        except ValueError as e:
            if "invalid literal" in str(e) or "could not convert" in str(e):
                print("\n[!] Input tidak valid! Harus berupa angka.")
            else:
                print(e)
        else:
            library_game[judul_terpilih] = round(library_game[judul_terpilih] + tambah_jam, 2)
            print(f"\n[+] Mantap! Playtime sekarang -> {judul_terpilih}: {library_game[judul_terpilih]} Jam")
        finally:
            input("\nTekan Enter untuk kembali ke menu...")
    else:
        input("\nTekan Enter untuk kembali ke menu...")