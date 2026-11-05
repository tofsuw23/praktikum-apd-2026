import os
from prettytable import PrettyTable

def header_aplikasi():
    os.system("cls")
    print("=====================================================")
    print("----- ^-^ SELAMAT DATANG DI STEAM TRACKER ^-^ -----")
    print("   Sistem Pencatatan & Tracking Playtime Game Steam  ")
    print("=====================================================")
    tabel_awal = PrettyTable()
    tabel_awal.field_names = ["No", "Menu Awal Steam Tracker"]
    tabel_awal.align["Menu Awal Steam Tracker"] = "l"
    tabel_awal.add_rows([
        ["1", "Login Akun"],
        ["2", "Register Akun Baru"],
        ["3", "Keluar Program"]
    ])
    print(tabel_awal)

def tampil_menu_admin(user_aktif):
    os.system("cls")
    print("=====================================================")
    print("  STEAM PLAYTIME TRACKER  Pengguna: " + user_aktif)
    print("=====================================================")
    tabel_admin = PrettyTable()
    tabel_admin.field_names = ["No", "Menu Admin (Atmint)"]
    tabel_admin.align["Menu Admin (Atmint)"] = "l"
    tabel_admin.add_rows([
        ["1", "Tambah Game Baru"],
        ["2", "Lihat Daftar Library Game"],
        ["3", "Update / Tracking Playtime Game"],
        ["4", "Hapus Game dari Library"],
        ["5", "Logout"]
    ])
    print(tabel_admin)

def tampil_menu_user(user_aktif):
    os.system("cls")
    print("=====================================================")
    print("  STEAM PLAYTIME TRACKER  Pengguna: " + user_aktif)
    print("=====================================================")
    tabel_user = PrettyTable()
    tabel_user.field_names = ["No", "Menu Pengguna"]
    tabel_user.align["Menu Pengguna"] = "l"
    tabel_user.add_rows([
        ["1", "Lihat Daftar Library Game"],
        ["2", "Update Playtime"],
        ["3", "Logout"]
    ])
    print(tabel_user)