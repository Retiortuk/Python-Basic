# def nama_fungsi():
#     print("Ini Adalah Methode Fungsi")

# nama_fungsi()

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# print("Luas Persegi: %d" % luas_persegi(10))

# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print("Luas Persegi Panjang: %d" %luas)

# luas_persegi_panjang(10, 7)

def hitung_luas_segitiga(alas, tinggi):
    luas = 0,5 * alas * tinggi
    return luas

def main():
    alas = float(input("Masukkan Panjang Alas Segitiga: "))
    tinggi = float(input("Masukkan Tinggi Segitiga: "))
    luas = hitung_luas_segitiga(alas, tinggi)
    print("Luas Segitiga Adalah: ", luas)

main()
