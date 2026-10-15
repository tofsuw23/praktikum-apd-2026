import os

role_akun = ("admin", "user")

akun_pengguna = [
    ["Tofa Suwarna", "037", role_akun[0]],
    ["member", "member123", role_akun[1]]
]

library_game = [
    ["Dark Souls Remastered", 0.0],
    ["Dark Souls II", 0.0],
    ["Dark Souls III", 0.0],
    ["Elden Ring", 0.0],
    ["Nightreign", 0.0],
    ["RE4 Remake", 0.0],
    ["RE Requiem", 0.0],
    ["Persona 3", 0.0],
    ["Persona 5 Royal", 0.0]
]

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

        for akun in akun_pengguna:
            if akun[0] == nama and akun[1] == sandi:
                login_berhasil = True
                user_aktif = akun[0]
                role_aktif = akun[2]
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
                            sudah_ada = False
                            for game in library_game:
                                if game[0] == judul_baru:
                                    sudah_ada = True
                                    break

                            if sudah_ada == True:
                                print("\n[!] Game ini sudah ada di dalam library wak!")
                            else:
                                input_jam = input("Masukkan Playtime Awal (Jam, contoh 0 atau 6.7): ")

                                cek_jam = input_jam.replace(".", "", 1)
                                if cek_jam.isdigit() and input_jam != "":
                                    jam_awal = float(input_jam)
                                    library_game.append([judul_baru, jam_awal])
                                    print(f"\n[+] Mantap! Berhasil menambahkan -> {judul_baru}: {jam_awal} Jam")
                                else:
                                    print("\n[!] Input jam bermain tidak valid! Harus berupa angka.")

                        input("\nTekan Enter untuk kembali ke menu...")

                    elif pilihan == "2":
                        os.system("cls")
                        print("--- DAFTAR LIBRARY GAME ---")
                        
                        nomor = 0
                        total_jam = 0.0
                        for game in library_game:
                            nomor += 1
                            print(f"{nomor}. {game[0]}: {game[1]} Jam")
                            total_jam += game[1]

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
                        for game in library_game:
                            jumlah_game += 1
                            print(f"{jumlah_game}. {game[0]}: {game[1]} Jam")

                        if jumlah_game == 0:
                            print("Belum ada game yang bisa di-update.")
                        else:
                            print("---------------------------")
                            pilih_nomor = input("Masukkan nomor urut game yang mau di-update: ")

                            if pilih_nomor.isdigit():
                                indeks = int(pilih_nomor) - 1
                                if indeks >= 0 and indeks < jumlah_game:
                                    print(f"\nGame Terpilih : {library_game[indeks][0]}: {library_game[indeks][1]} Jam")
                                    print("1. Tambah Jam Bermain")
                                    print("2. Ganti Total Jam Bermain Baru")
                                    print("3. Ganti Judul Game")
                                    opsi_update = input("Pilih opsi update (1/2/3): ")

                                    if opsi_update == "1":
                                        jam_main = input("Masukkan tambahan jam bermain (contoh 6.7): ")
                                        if jam_main.replace(".", "", 1).isdigit() and jam_main != "":
                                            library_game[indeks][1] += float(jam_main)
                                            print(f"\n[+] Playtime berhasil di-update -> {library_game[indeks][0]}: {library_game[indeks][1]} Jam")
                                        else:
                                            print("\n[!] Input jam tidak valid! Harus berupa angka.")

                                    elif opsi_update == "2":
                                        total_baru = input("Masukkan total jam bermain yang baru (contoh 16.7): ")
                                        if total_baru.replace(".", "", 1).isdigit() and total_baru != "":
                                            library_game[indeks][1] = float(total_baru)
                                            print(f"\n[+] Total playtime berhasil diubah -> {library_game[indeks][0]}: {library_game[indeks][1]} Jam")
                                        else:
                                            print("\n[!] Input jam tidak valid! Harus berupa angka.")

                                    elif opsi_update == "3":
                                        nama_baru = input("Masukkan judul game yang baru: ")
                                        if nama_baru == "":
                                            print("\n[!] Judul game baru tidak boleh kosong!")
                                        else:
                                            library_game[indeks][0] = nama_baru
                                            print(f"\n[+] Judul game berhasil diubah -> {library_game[indeks][0]}: {library_game[indeks][1]} Jam")
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
                        for game in library_game:
                            jumlah_game += 1
                            print(f"{jumlah_game}. {game[0]}: {game[1]} Jam")

                        if jumlah_game == 0:
                            print("Belum ada game untuk dihapus.")
                        else:
                            print("---------------------------")
                            nomor_hapus = input("Masukkan nomor urut game yang ingin dihapus: ")

                            if nomor_hapus.isdigit():
                                indeks_hapus = int(nomor_hapus) - 1
                                if indeks_hapus >= 0 and indeks_hapus < jumlah_game:
                                    judul_terhapus = library_game[indeks_hapus][0]
                                    yakin = input(f"Yakin mau menghapus '{judul_terhapus}'? (y/n): ")
                                    if yakin == "y" or yakin == "Y":
                                        del library_game[indeks_hapus]
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
                        for game in library_game:
                            nomor += 1
                            print(f"{nomor}. {game[0]}: {game[1]} Jam")

                        if nomor == 0:
                            print("Belum ada game di dalam library.")

                        input("\nTekan Enter untuk kembali ke menu...")

                    elif pilihan_user == "2":
                        os.system("cls")
                        print("--- TRACKING PLAYTIME GAME STEAM ---")
                        print("--- DAFTAR LIBRARY GAME ---")
                        jumlah_game = 0
                        for game in library_game:
                            jumlah_game += 1
                            print(f"{jumlah_game}. {game[0]}: {game[1]} Jam")

                        if jumlah_game == 0:
                            print("Belum ada game di dalam library.")
                        else:
                            print("---------------------------")
                            pilih_nomor = input("Masukkan nomor game yang baru dimainkan: ")
                            if pilih_nomor.isdigit():
                                indeks = int(pilih_nomor) - 1
                                if indeks >= 0 and indeks < jumlah_game:
                                    tambah_jam = input(f"Masukkan tambahan jam main untuk '{library_game[indeks][0]}': ")
                                    if tambah_jam.replace(".", "", 1).isdigit() and tambah_jam != "":
                                        library_game[indeks][1] += float(tambah_jam)
                                        print(f"\n[+] Mantap! Playtime sekarang -> {library_game[indeks][0]}: {library_game[indeks][1]} Jam")
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
            terdaftar = False
            for akun in akun_pengguna:
                if akun[0] == user_baru:
                    terdaftar = True
                    break

            if terdaftar == True:
                print("\n[!] Waduh, Username tersebut sudah terdaftar! Coba nama lain.")
            else:
                akun_pengguna.append([user_baru, pass_baru, role_akun[1]])
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