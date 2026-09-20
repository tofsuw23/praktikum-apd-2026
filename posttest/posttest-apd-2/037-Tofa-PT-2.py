harga_makanan = [15000, 16000, 19000, 20000, 21000, 22000]
biaya_aplikasi = 5000

total_harga_makanan = (
    harga_makanan[0]
    + harga_makanan[1]
    + harga_makanan[2]
    + harga_makanan[3]
    + harga_makanan[4]
    + harga_makanan[5]
)

total_bayar = total_harga_makanan + biaya_aplikasi
rata_rata = total_bayar / len(harga_makanan)
nim = 32
boolean = nim != rata_rata

idr_ke_euro = total_bayar / 17000

print("Biaya aplikasi: Rp." + str(biaya_aplikasi))
print("Total Bayar (IDR): Rp." + str(total_bayar))
print("Total Bayar (Euro): €" + str(idr_ke_euro))
print("Nim: " + str(nim))
print("Rata-rata: Rp." + str(rata_rata))
print("Boolean: " + str(boolean))
print("Harga makanan: " + str(harga_makanan[-6:]))