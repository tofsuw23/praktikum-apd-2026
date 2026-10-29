import os

role_akun = ("admin", "user")

akun_pengguna = {
    "Tofa Suwarna": {
        "sandi": "037",
        "role": role_akun[0]
    },
    "member": {
        "sandi": "member123",
        "role": role_akun[1]
    }
}

library_game = {
    "Dark Souls Remastered": 0.0,
    "Dark Souls II": 0.0,
    "Dark Souls III": 0.0,
    "Elden Ring": 0.0,
    "Nightreign": 0.0,
    "RE4 Remake": 0.0,
    "RE Requiem": 0.0,
    "Persona 3": 0.0,
    "Persona 5 Royal": 0.0
}

jalan = "ya"
menu_login = "ya"

def header_aplikasi():
    os.system("cls")
    print("=====================================================")
    print("----- ^-^ SELAMAT DATANG DI STEAM TRACKER ^-^ -----")
    print("   Sistem Pencatatan & Tracking Playtime Game Steam  ")
    print("=====================================================")

def sapa_pengguna(nama_user, status_role):
    os.system("cls")
    print("Yeayy! Login Berhasil Cuy, selamat datang " + nama_user)
    print("Status Role Anda : " + status_role)
    input("\nTekan Enter untuk masuk ke menu utama...")

def hitung_koleksi():
    jumlah = len(library_game)
    return jumlah

def tampilkan_library():
    print("--- DAFTAR LIBRARY GAME ---")
    nomor = 0
    for judul, jam in library_game.items():
        nomor += 1
        print(f"{nomor}. {judul}: {jam} Jam")

    if nomor == 0:
        print("Belum ada game di dalam library.")
    return nomor

def cek_login(nama_input, sandi_input):
    for user_key, data_val in akun_pengguna.items():
        if user_key == nama_input and data_val["sandi"] == sandi_input:
            return data_val["role"]
    return None

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

def register_akun():
    os.system("cls")
    print("----- ^-^ REGISTER AKUN BARU ^-^ -----")
    try:
        user_baru = input("Buat Username Baru : ")
        pass_baru = input("Buat Password Baru : ")

        if user_baru == "" or pass_baru == "":
            raise ValueError("\n[!] Username dan Password tidak boleh kosong!")
        if akun_pengguna.get(user_baru) != None:
            raise ValueError("\n[!] Waduh, Username tersebut sudah terdaftar! Coba nama lain.")
    except ValueError as e:
        print(e)
    else:
        akun_pengguna[user_baru] = {
            "sandi": pass_baru,
            "role": role_akun[1]
        }
        print(f"\n[+] Yeayy! Akun '{user_baru}' berhasil didaftarkan sebagai Pengguna Biasa!")
    finally:
        input("\nTekan Enter untuk kembali ke menu awal...")

def tambah_game():
    os.system("cls")
    print("--- TAMBAH GAME BARU KE LIBRARY ---")
    try:
        judul_baru = input("Masukkan Judul Game : ")
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
        library_game[judul_baru] = jam_awal
        print(f"\n[+] Mantap! Berhasil menambahkan -> {judul_baru}: {jam_awal} Jam")
    finally:
        input("\nTekan Enter untuk kembali ke menu...")

def lihat_library_lengkap():
    os.system("cls")
    jumlah_game = tampilkan_library()
    if jumlah_game > 0:
        list_jam = list(library_game.values())
        total_jam = hitung_total_jam_rekursif(list_jam, 0)
        print("---------------------------")
        print(f"Total Koleksi Game : {hitung_koleksi()} Game")
        print(f"Total Jam Bermain  : {total_jam} Jam")
    input("\nTekan Enter untuk kembali ke menu...")

def update_game_admin():
    os.system("cls")
    print("--- UPDATE & TRACKING PLAYTIME GAME ---")
    jumlah_game = tampilkan_library()

    if jumlah_game > 0:
        print("---------------------------")
        try:
            pilih_nomor = int(input("Masukkan nomor urut game yang mau di-update: "))
            if pilih_nomor < 1 or pilih_nomor > jumlah_game:
                raise ValueError("\n[!] Nomor urut game tidak ditemukan di daftar!")

            judul_terpilih = ambil_judul_game(pilih_nomor)
            jam_terpilih = library_game[judul_terpilih]

            print(f"\nGame Terpilih : {judul_terpilih}: {jam_terpilih} Jam")
            print("1. Tambah Jam Bermain")
            print("2. Ganti Total Jam Bermain Baru")
            print("3. Ganti Judul Game")
            opsi_update = input("Pilih opsi update (1/2/3): ")

            if opsi_update == "1":
                jam_main = float(input("Masukkan tambahan jam bermain (contoh 6.7): "))
                if jam_main < 0:
                    raise ValueError("\n[!] Tambahan jam tidak boleh negatif!")
                library_game[judul_terpilih] += jam_main
                print(f"\n[+] Playtime berhasil di-update -> {judul_terpilih}: {library_game[judul_terpilih]} Jam")

            elif opsi_update == "2":
                total_baru = float(input("Masukkan total jam bermain yang baru (contoh 16.7): "))
                if total_baru < 0:
                    raise ValueError("\n[!] Total jam tidak boleh negatif!")
                library_game.update({judul_terpilih: total_baru})
                print(f"\n[+] Total playtime berhasil diubah -> {judul_terpilih}: {library_game[judul_terpilih]} Jam")

            elif opsi_update == "3":
                nama_baru = input("Masukkan judul game yang baru: ")
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

def hapus_game():
    os.system("cls")
    print("--- HAPUS GAME DARI LIBRARY ---")
    jumlah_game = tampilkan_library()

    if jumlah_game > 0:
        print("---------------------------")
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
            yakin = input(f"Yakin mau menghapus '{judul_terhapus}'? (y/n): ")
            if yakin == "y" or yakin == "Y":
                del library_game[judul_terhapus]
                print(f"\n[-] Game '{judul_terhapus}' berhasil dihapus dari library!")
            else:
                print("\n[i] Penghapusan game dibatalkan.")
        finally:
            input("\nTekan Enter untuk kembali ke menu...")
    else:
        input("\nTekan Enter untuk kembali ke menu...")

def update_playtime_user():
    os.system("cls")
    print("--- TRACKING PLAYTIME GAME STEAM ---")
    jumlah_game = tampilkan_library()

    if jumlah_game > 0:
        print("---------------------------")
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
            library_game[judul_terpilih] += tambah_jam
            print(f"\n[+] Mantap! Playtime sekarang -> {judul_terpilih}: {library_game[judul_terpilih]} Jam")
        finally:
            input("\nTekan Enter untuk kembali ke menu...")
    else:
        input("\nTekan Enter untuk kembali ke menu...")

while jalan == "ya":
    header_aplikasi()
    print("1. Login Akun")
    print("2. Register Akun Baru")
    print("3. Keluar Program")
    print("=====================================================")

    pilih_awal = input("Pilih Menu (1/2/3): ")

    if pilih_awal == "1":
        os.system("cls")
        print("----- ^-^ HALAMAN LOGIN STEAM ^-^ -----")
        nama = input("Masukkan Username Anda : ")
        sandi = input("Masukkan Password Anda : ")

        role_aktif = cek_login(nama, sandi)

        if role_aktif != None:
            user_aktif = nama
            sapa_pengguna(user_aktif, role_aktif)

            menu_login = "ya"
            while menu_login == "ya":
                os.system("cls")
                print("=====================================================")
                print("  STEAM PLAYTIME TRACKER  Pengguna: " + user_aktif)
                print("=====================================================")

                if role_aktif == "admin":
                    print("1. Tambah Game Baru")
                    print("2. Lihat Daftar Library Game")
                    print("3. Update / Tracking Playtime Game")
                    print("4. Hapus Game dari Library")
                    print("5. Logout")
                    print("=====================================================")
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
                        menu_login = "tidak"
                        print("\nBerhasil logout dari akun Atmint.")
                        input("Tekan Enter untuk kembali ke halaman awal...")
                    else:
                        print("\nWaduh, nggak ada pilihannya di menu wak!")
                        input("Tekan Enter untuk mencoba lagi...")

                else:
                    print("1. Lihat Daftar Library Game ")
                    print("2. Update Playtime")
                    print("3. Logout")
                    print("=====================================================")
                    pilihan_user = input("PILIH MENU PENGGUNA (1/2/3): ")

                    if pilihan_user == "1":
                        os.system("cls")
                        tampilkan_library()
                        input("\nTekan Enter untuk kembali ke menu...")
                    elif pilihan_user == "2":
                        update_playtime_user()
                    elif pilihan_user == "3":
                        menu_login = "tidak"
                        print("\nBerhasil logout dari akun Pengguna.")
                        input("Tekan Enter untuk kembali ke halaman awal...")
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
        jalan = "tidak"

    else:
        print("\nWaduh, nggak ada pilihannya di menu wak!")
        input("Tekan Enter untuk mencoba lagi...")
        