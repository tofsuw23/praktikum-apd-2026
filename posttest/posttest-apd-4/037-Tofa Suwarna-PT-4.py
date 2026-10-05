total_kalimantan_gambut = 0
total_kalimantan_mineral = 0
total_sumatera_gambut = 0
total_sumatera_mineral = 0


print(" ^*^  SISTEM REKAPITULASI TITIK API BPBD bersama MANGGALA AGNI  ^*^ ")

while True:
    username = input("Masukkan Username: ").strip()
    password = input("Masukkan Password: ").strip()
    
    if username == "" or password == "":
        print("Error: Username dan Password tidak boleh kosong!\n")
        continue
        
    username = username.lower()
    
    if username == "tofa" and password == "037":
        print("\nLogin Berhasil\n")
        break
    elif username != "tofa" and password == "037":
        print("Error: Username salah, masukkan username yang benar.\n")
    elif username == "tofa" and password != "037":
        print("Error: Password salah, masukkan password yang benar.\n")
    else:
        print("Error: Username dan Password salah, silakan masukkan kembali dengan benar.\n")

while True:

    pulau = input("Masukkan Wilayah Pulau (Kalimantan/Sumatera): ").strip().upper()
    
    if pulau == "":
        print("Input pulau tidak boleh kosong!")
        continue

    if pulau == "KALIMANTAN":

        jenis_lahan = input("Masukkan Jenis Lahan (Gambut/Mineral): ").strip().upper()
        
        if jenis_lahan == "GAMBUT":
            titik_api_str = input("Jumlah Titik Api (Hotspot): ").strip()
            if not titik_api_str.isdigit(): 
                print("Error: Input jumlah titik api harus berupa angka!!")
                continue
            
            luas_terbakar = int(titik_api_str) * 5
            total_kalimantan_gambut += luas_terbakar
            print(f"Data Tersimpan: Kalimantan-Gambut bertambah {luas_terbakar} Hektare.")
            
        elif jenis_lahan == "MINERAL":
            titik_api_str = input("Jumlah Titik Api (Hotspot): ").strip()
            if not titik_api_str.isdigit():
                print("Input jumlah titik api harus berupa angka!")
                continue
                
            luas_terbakar = int(titik_api_str) * 5
            total_kalimantan_mineral += luas_terbakar
            print(f"Data Tersimpan: Kalimantan-Mineral bertambah {luas_terbakar} Hektare.")
        else:
            print("Jenis lahan tidak valid! Masukkan Gambut atau Mineral.")
            continue
            
    elif pulau == "SUMATERA":
        jenis_lahan = input("Masukkan Jenis Lahan (Gambut/Mineral): ").strip().upper()
        
        if jenis_lahan == "GAMBUT":
            titik_api_str = input("Jumlah Titik Api (Hotspot): ").strip()
            if not titik_api_str.isdigit():
                print("Input jumlah titik api harus berupa angka!")
                continue
                
            luas_terbakar = int(titik_api_str) * 5
            total_sumatera_gambut += luas_terbakar
            print(f"Data Tersimpan: Sumatera-Gambut bertambah {luas_terbakar} Hektare.")
            
        elif jenis_lahan == "MINERAL":
            titik_api_str = input("Jumlah Titik Api (Hotspot): ").strip()
            if not titik_api_str.isdigit():
                print("Input jumlah titik api harus berupa angka!")
                continue
                
            luas_terbakar = int(titik_api_str) * 5
            total_sumatera_mineral += luas_terbakar
            print(f"Data Tersimpan: Sumatera-Mineral bertambah {luas_terbakar} Hektare.")
        else:
            print("Jenis lahan tidak valid! Masukkan Gambut atau Mineral.")
            continue
    else:
        print("Wilayah pulau tidak valid! Masukkan Kalimantan atau Sumatera.")
        continue

    lanjut = input("\nApakah anda masih mau input data titik api lagi? (Y/T):").strip().upper()
    print('')
    
    if lanjut == "T":
        break 
    
print("*^* RINGKASAN TOTAL LUAS LAHAN TERBAKAR *^*")
print(f"1. Kalimantan - Gambut  : {total_kalimantan_gambut} Hektare")
print(f"2. Kalimantan - Mineral : {total_kalimantan_mineral} Hektare")
print(f"3. Sumatera - Gambut    : {total_sumatera_gambut} Hektare")
print(f"4. Sumatera - Mineral   : {total_sumatera_mineral} Hektare")