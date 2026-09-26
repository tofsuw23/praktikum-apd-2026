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
nim = 37
bolean = nim != rata_rata

idr_ke_euro = total_bayar / 20400

print("biaya aplikasi: Rp" + str(biaya_aplikasi))
print("total Bayar (IDR): Rp" + str(total_bayar))
print("total Bayar (Euro): €" + str(idr_ke_euro))
print("nim: " + str(nim))
print("rata-rata: Rp" + str(rata_rata))
print("bolean: " + str(bolean))
print("harga makanan: " + str(harga_makanan[-6:]))