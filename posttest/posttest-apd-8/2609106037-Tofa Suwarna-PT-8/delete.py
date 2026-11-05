import os
from prettytable import PrettyTable
from data import library_game
from read import tampilkan_library, ambil_judul_game

def hapus_game():
    os.system("cls")
    print("--- HAPUS GAME DARI LIBRARY ---")
    jumlah_game = tampilkan_library()

    if jumlah_game > 0:
        try:
            nomor_hapus = int(input("Masukkan nomor urut game yang ingin dihapus: "))
            if nomor_hapus < 1 or nomor_hapus > jumlah_game:
                raise ValueError("\n[!] Nomor urut game tidak ada di dalam daftar!")
        except ValueError as e:
            if "invalid literal" in str(e):
                print("\n[!] Input harus berupa angka nomor urut!")
            else:
                print(e)
        else:
            judul_terhapus = ambil_judul_game(nomor_hapus)
            yakin = input(f"Yakin mau menghapus '{judul_terhapus}'? (y/n): ").strip().lower()
            if yakin == "y":
                jam_terhapus = library_game.pop(judul_terhapus)
                tabel_hapus = PrettyTable()
                tabel_hapus.field_names = ["Judul Game Dihapus", "Playtime Terakhir", "Status"]
                tabel_hapus.add_row([judul_terhapus, f"{round(jam_terhapus, 2)} Jam", "Terhapus dari Library"])
                print(f"\n[-] Game '{judul_terhapus}' berhasil dihapus dari library!")
                print(tabel_hapus)
            else:
                print("\n[i] Penghapusan game dibatalkan.")
        finally:
            input("\nTekan Enter untuk kembali ke menu...")
    else:
        input("\nTekan Enter untuk kembali ke menu...")