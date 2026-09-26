print("----- ^-^ SELAMAT DATANG DI ANGKASA ^-^ -----")

nama=input("Masukkan Nama Anda: ")
nim=input("Masukkan NIM Anda: ")

if nama == "Tofa Suwarna" and nim == ("37"): 
    print(" Yeayy! Login Berhasil Cuy, selamat datang " + nama)

    biaya_langganan = 1500000

    print("\n---- PILIHAN PAKET ANGKASA ---- ")
    print("1. Paket Orbit (Admin 1%) - Akses dasar lagu populer")
    print("2. Paket Nebula (Admin 3%) - Akses premium & playlist")
    print("3. Paket Galaxy (Admin 5%) - Akses premium, playlist & offline")
    print("4. Paket Supernova (Admin 7%) - Semua fitur & konten eksklusif")
    print("■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")

    pilihan=input("PILIH PAKET ANGKASA (1/2/3/4): ")

    if pilihan == "1":
        paket = "Orbit"
        admin = 0.01
        fitur = "Akses dasar ke lagu-lagu populer"
    elif pilihan == "2":
        paket = "Nebula"
        admin = 0.03
        fitur = "Akses lagu premium dan playlist kustom"
    elif pilihan == "3":
        paket = "Galaxy"
        admin = 0.05
        fitur = "Akses lagu premium, playlist kustom, dan mode offline"
    elif pilihan == "4":
        paket = "Supernova"
        admin = 0.07
        fitur = "Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis"
    else:
        print("Waduh, nggak ada pilihannya di menu!")
   
        
    biaya_admin = int(biaya_langganan * admin)
    total_bayar = int(biaya_langganan) + int(biaya_langganan * admin)

    print("\n==========================================")
    print("          STRUK LANGGANAN ANGKASA         ")
    print("==========================================")
    print(f"Nama Pengguna    : {nama}")
    print(f"NIM              : {nim}")
    print(f"Paket Pilihan    : Paket {paket}")
    print(f"Harga Langganan  : Rp {biaya_langganan}")
    print(f"Biaya Admin      : Rp {biaya_admin}")
    print("------------------------------------------+")
    print(f"TOTAL BAYAR      : Rp {total_bayar}")
    print("=====================================================================================================")
    print(f"Fitur yang Didapat    : {fitur}")
    print("=====================================================================================================")

else:
    print("\n ---- T-T Yaaah.. login gagal. Nama atau NIM ada yang salah tuh. T-T ----")