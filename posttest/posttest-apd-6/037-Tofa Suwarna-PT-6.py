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

while jalan == "ya":
    os.system("cls")
    print("=====================================================")
    print("----- ^-^ SELAMAT DATANG DI STEAM TRACKER ^-^ -----")
    print("   Sistem Pencatatan & Tracking Playtime Game Steam  ")
    print("=====================================================")
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

        login_berhasil = False
        user_aktif = ""
        role_aktif = ""

        for user_key, data_val in akun_pengguna.items():
            if user_key == nama and data_val["sandi"] == sandi:
                login_berhasil = True
                user_aktif = user_key
                role_aktif = data_val["role"]
                break

        if login_berhasil == True:
            os.system("cls")
            print("Yeayy! Login Berhasil Cuy, selamat datang " + user_aktif)
            print("Status Role Anda : " + role_aktif)
            input("\nTekan Enter untuk masuk ke menu utama...")

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
                        os.system("cls")
                        print("--- TAMBAH GAME BARU KE LIBRARY ---")
                        judul_baru = input("Masukkan Judul Game : ")

                        if judul_baru == "":
                            print("\n[!] Waduh, judul game nggak boleh kosong wak!")
                        else:
                            if library_game.get(judul_baru) != None:
                                print("\n[!] Game ini sudah ada di dalam library wak!")
                            else:
                                input_jam = input("Masukkan Playtime Awal (Jam, contoh 0 atau 6.7): ")

                                cek_jam = input_jam.replace(".", "", 1)
                                if cek_jam.isdigit() and input_jam != "":
                                    jam_awal = float(input_jam)
                                    library_game[judul_baru] = jam_awal
                                    print(f"\n[+] Mantap! Berhasil menambahkan -> {judul_baru}: {jam_awal} Jam")
                                else:
                                    print("\n[!] Input jam bermain tidak valid! Harus berupa angka.")

                        input("\nTekan Enter untuk kembali ke menu...")

                    elif pilihan == "2":
                        os.system("cls")
                        print("--- DAFTAR LIBRARY GAME ---")
                        
                        nomor = 0
                        total_jam = 0.0
                        for judul, jam in library_game.items():
                            nomor += 1
                            print(f"{nomor}. {judul}: {jam} Jam")
                            total_jam += jam

                        if nomor == 0:
                            print("Belum ada game di dalam library.")
                        else:
                            print("---------------------------")
                            print(f"Total Koleksi Game : {nomor} Game")
                            print(f"Total Jam Bermain  : {total_jam} Jam")

                        input("\nTekan Enter untuk kembali ke menu...")

                    elif pilihan == "3":
                        os.system("cls")
                        print("--- UPDATE & TRACKING PLAYTIME GAME ---")
                        print("--- DAFTAR LIBRARY GAME ---")
                        
                        jumlah_game = 0
                        for judul, jam in library_game.items():
                            jumlah_game += 1
                            print(f"{jumlah_game}. {judul}: {jam} Jam")

                        if jumlah_game == 0:
                            print("Belum ada game yang bisa di-update.")
                        else:
                            print("---------------------------")
                            pilih_nomor = input("Masukkan nomor urut game yang mau di-update: ")

                            if pilih_nomor.isdigit():
                                nomor_target = int(pilih_nomor)
                                if nomor_target >= 1 and nomor_target <= jumlah_game:
                                    urutan = 0
                                    judul_terpilih = ""
                                    jam_terpilih = 0.0
                                    for judul, jam in library_game.items():
                                        urutan += 1
                                        if urutan == nomor_target:
                                            judul_terpilih = judul
                                            jam_terpilih = jam
                                            break

                                    print(f"\nGame Terpilih : {judul_terpilih}: {jam_terpilih} Jam")
                                    print("1. Tambah Jam Bermain")
                                    print("2. Ganti Total Jam Bermain Baru")
                                    print("3. Ganti Judul Game")
                                    opsi_update = input("Pilih opsi update (1/2/3): ")

                                    if opsi_update == "1":
                                        jam_main = input("Masukkan tambahan jam bermain (contoh 6.7): ")
                                        if jam_main.replace(".", "", 1).isdigit() and jam_main != "":
                                            library_game[judul_terpilih] += float(jam_main)
                                            print(f"\n[+] Playtime berhasil di-update -> {judul_terpilih}: {library_game[judul_terpilih]} Jam")
                                        else:
                                            print("\n[!] Input jam tidak valid! Harus berupa angka.")

                                    elif opsi_update == "2":
                                        total_baru = input("Masukkan total jam bermain yang baru (contoh 16.7): ")
                                        if total_baru.replace(".", "", 1).isdigit() and total_baru != "":
                                            library_game.update({judul_terpilih: float(total_baru)})
                                            print(f"\n[+] Total playtime berhasil diubah -> {judul_terpilih}: {library_game[judul_terpilih]} Jam")
                                        else:
                                            print("\n[!] Input jam tidak valid! Harus berupa angka.")

                                    elif opsi_update == "3":
                                        nama_baru = input("Masukkan judul game yang baru: ")
                                        if nama_baru == "":
                                            print("\n[!] Judul game baru tidak boleh kosong!")
                                        elif library_game.get(nama_baru) != None and nama_baru != judul_terpilih:
                                            print("\n[!] Judul game tersebut sudah ada di library!")
                                        else:
                                            jam_lama = library_game.pop(judul_terpilih)
                                            library_game[nama_baru] = jam_lama
                                            print(f"\n[+] Judul game berhasil diubah -> {nama_baru}: {library_game[nama_baru]} Jam")
                                    else:
                                        print("\n[!] Waduh, opsi update tidak ada di menu!")
                                else:
                                    print("\n[!] Nomor urut game tidak ditemukan di daftar!")
                            else:
                                print("\n[!] Input harus berupa angka nomor urut!")

                        input("\nTekan Enter untuk kembali ke menu...")

                    elif pilihan == "4":
                        os.system("cls")
                        print("--- HAPUS GAME DARI LIBRARY ---")
                        print("--- DAFTAR LIBRARY GAME ---")
                        
                        jumlah_game = 0
                        for judul, jam in library_game.items():
                            jumlah_game += 1
                            print(f"{jumlah_game}. {judul}: {jam} Jam")

                        if jumlah_game == 0:
                            print("Belum ada game untuk dihapus.")
                        else:
                            print("---------------------------")
                            nomor_hapus = input("Masukkan nomor urut game yang ingin dihapus: ")

                            if nomor_hapus.isdigit():
                                target_hapus = int(nomor_hapus)
                                if target_hapus >= 1 and target_hapus <= jumlah_game:
                                    urutan = 0
                                    judul_terhapus = ""
                                    for judul in library_game.keys():
                                        urutan += 1
                                        if urutan == target_hapus:
                                            judul_terhapus = judul
                                            break

                                    yakin = input(f"Yakin mau menghapus '{judul_terhapus}'? (y/n): ")
                                    if yakin == "y" or yakin == "Y":
                                        del library_game[judul_terhapus]
                                        print(f"\n[-] Game '{judul_terhapus}' berhasil dihapus dari library!")
                                    else:
                                        print("\n[i] Penghapusan game dibatalkan.")
                                else:
                                    print("\n[!] Nomor urut game tidak ada di dalam daftar!")
                            else:
                                print("\n[!] Input harus berupa angka nomor urut!")

                        input("\nTekan Enter untuk kembali ke menu...")

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
                        print("--- DAFTAR LIBRARY GAME ---")
                        nomor = 0
                        for judul, jam in library_game.items():
                            nomor += 1
                            print(f"{nomor}. {judul}: {jam} Jam")

                        if nomor == 0:
                            print("Belum ada game di dalam library.")

                        input("\nTekan Enter untuk kembali ke menu...")

                    elif pilihan_user == "2":
                        os.system("cls")
                        print("--- TRACKING PLAYTIME GAME STEAM ---")
                        print("--- DAFTAR LIBRARY GAME ---")
                        jumlah_game = 0
                        for judul, jam in library_game.items():
                            jumlah_game += 1
                            print(f"{jumlah_game}. {judul}: {jam} Jam")

                        if jumlah_game == 0:
                            print("Belum ada game di dalam library.")
                        else:
                            print("---------------------------")
                            pilih_nomor = input("Masukkan nomor game yang baru dimainkan: ")
                            if pilih_nomor.isdigit():
                                nomor_target = int(pilih_nomor)
                                if nomor_target >= 1 and nomor_target <= jumlah_game:
                                    urutan = 0
                                    judul_terpilih = ""
                                    for judul in library_game.keys():
                                        urutan += 1
                                        if urutan == nomor_target:
                                            judul_terpilih = judul
                                            break

                                    tambah_jam = input(f"Masukkan tambahan jam main untuk '{judul_terpilih}': ")
                                    if tambah_jam.replace(".", "", 1).isdigit() and tambah_jam != "":
                                        library_game[judul_terpilih] += float(tambah_jam)
                                        print(f"\n[+] Mantap! Playtime sekarang -> {judul_terpilih}: {library_game[judul_terpilih]} Jam")
                                    else:
                                        print("\n[!] Input jam tidak valid! Harus berupa angka.")
                                else:
                                    print("\n[!] Nomor game tidak ditemukan di daftar!")
                            else:
                                print("\n[!] Input harus berupa angka nomor urut!")

                        input("\nTekan Enter untuk kembali ke menu...")

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
        os.system("cls")
        print("----- ^-^ REGISTER AKUN BARU ^-^ -----")
        user_baru = input("Buat Username Baru : ")
        pass_baru = input("Buat Password Baru : ")

        if user_baru == "" or pass_baru == "":
            print("\n[!] Username dan Password tidak boleh kosong!")
        else:
            if akun_pengguna.get(user_baru) != None:
                print("\n[!] Waduh, Username tersebut sudah terdaftar! Coba nama lain.")
            else:
                akun_pengguna[user_baru] = {
                    "sandi": pass_baru,
                    "role": role_akun[1]
                }
                print(f"\n[+] Yeayy! Akun '{user_baru}' berhasil didaftarkan sebagai Pengguna Biasa!")

        input("\nTekan Enter untuk kembali ke menu awal...")

    elif pilih_awal == "3":
        os.system("cls")
        print("=====================================================")
        print("  Terima kasih sudah menggunakan Steam Tracker Cik!  ")
        print("=====================================================")
        jalan = "tidak"

    else:
        print("\nWaduh, nggak ada pilihannya di menu wak!")
        input("Tekan Enter untuk mencoba lagi...")