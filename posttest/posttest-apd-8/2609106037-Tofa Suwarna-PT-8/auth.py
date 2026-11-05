import os
import random
from datetime import datetime
from prettytable import PrettyTable
from data import role_akun, akun_pengguna

def cek_login(nama_input, sandi_input):
    for user_key, data_val in akun_pengguna.items():
        if user_key == nama_input and data_val["sandi"] == sandi_input:
            return data_val["role"]
    return None

def sapa_pengguna(nama_user, status_role):
    os.system("cls")
    kumpulan_angka = "0123456789"
    pin_sesi = ""
    for i in range(4):
        pin_sesi += random.choice(kumpulan_angka)
    waktu_login = datetime.now().strftime("%d/%m/%Y %H:%M")

    print("Yeayy! Login Berhasil Cuy, selamat datang " + nama_user)
    tabel_sesi = PrettyTable()
    tabel_sesi.field_names = ["Informasi Sesi", "Detail"]
    tabel_sesi.align["Informasi Sesi"] = "l"
    tabel_sesi.align["Detail"] = "l"
    tabel_sesi.add_rows([
        ["Nama Pengguna", nama_user],
        ["Status Role", status_role],
        ["Kode Sesi Acak", pin_sesi],
        ["Waktu Login", waktu_login]
    ])
    print(tabel_sesi)
    input("\nTekan Enter untuk masuk ke menu utama...")

def register_akun():
    os.system("cls")
    print("----- ^-^ REGISTER AKUN BARU ^-^ -----")
    try:
        user_baru = input("Buat Username Baru : ").strip()
        pass_baru = input("Buat Password Baru : ").strip()

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
        tabel_reg = PrettyTable()
        tabel_reg.field_names = ["Username Baru", "Role Akun", "Status"]
        tabel_reg.add_row([user_baru, role_akun[1], "Berhasil Terdaftar"])
        print("\n[+] Yeayy! Akun baru berhasil dibuat:")
        print(tabel_reg)
    finally:
        input("\nTekan Enter untuk kembali ke menu awal...")