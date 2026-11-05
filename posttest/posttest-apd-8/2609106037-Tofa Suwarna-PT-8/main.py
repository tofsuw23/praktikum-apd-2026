import os
from menu import header_aplikasi, tampil_menu_admin, tampil_menu_user
from auth import cek_login, sapa_pengguna, register_akun
from create import tambah_game
from read import tampilkan_library, lihat_library_lengkap
from update import update_game_admin, update_playtime_user
from delete import hapus_game

while True:
    header_aplikasi()
    pilih_awal = input("Pilih Menu (1/2/3): ")

    if pilih_awal == "1":
        os.system("cls")
        print("----- ^-^ HALAMAN LOGIN STEAM ^-^ -----")
        nama = input("Masukkan Username Anda : ")
        sandi = input("Masukkan Password Anda : ")

        role_aktif = cek_login(nama, sandi)

        if role_aktif is not None:
            user_aktif = nama
            sapa_pengguna(user_aktif, role_aktif)

            while True:
                if role_aktif == "admin":
                    tampil_menu_admin(user_aktif)
                    pilihan = input("PILIH MENU ATMINT (1/2/3/4/5): ")

                    if pilihan == "1":
                        tambah_game()
                    elif pilihan == "2":
                        lihat_library_lengkap()
                    elif pilihan == "3":
                        update_game_admin()
                    elif pilihan == "4":
                        hapus_game()
                    elif pilihan == "5":
                        print("\nBerhasil logout dari akun Atmint.")
                        input("Tekan Enter untuk kembali ke halaman awal...")
                        break
                    else:
                        print("\nWaduh, nggak ada pilihannya di menu wak!")
                        input("Tekan Enter untuk mencoba lagi...")

                else:
                    tampil_menu_user(user_aktif)
                    pilihan_user = input("PILIH MENU PENGGUNA (1/2/3): ")

                    if pilihan_user == "1":
                        os.system("cls")
                        tampilkan_library()
                        input("\nTekan Enter untuk kembali ke menu...")
                    elif pilihan_user == "2":
                        update_playtime_user()
                    elif pilihan_user == "3":
                        print("\nBerhasil logout dari akun Pengguna.")
                        input("Tekan Enter untuk kembali ke halaman awal...")
                        break
                    else:
                        print("\nWaduh, nggak ada pilihannya di menu wak!")
                        input("Tekan Enter untuk mencoba lagi...")

        else:
            print("\n---- T-T Yaaah.. login gagal. Username atau Password ada yang salah tuh. T-T ----")
            input("Tekan Enter untuk kembali...")

    elif pilih_awal == "2":
        register_akun()

    elif pilih_awal == "3":
        os.system("cls")
        print("=====================================================")
        print("  Terima kasih sudah menggunakan Steam Tracker Cik!  ")
        print("=====================================================")
        break

    else:
        print("\nWaduh, nggak ada pilihannya di menu wak!")
        input("Tekan Enter untuk mencoba lagi...")