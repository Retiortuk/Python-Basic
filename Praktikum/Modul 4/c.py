
# TUGAS C AULIA AHMAD GHAUS ADZAM 2311104028 
# Input dua bilangan bulat
bilangan1 = int(input("Masukkan bilangan bulat pertama: "))
bilangan2 = int(input("Masukkan bilangan bulat kedua: "))

def cari_kpk(a, b):
    max_num = max(a, b)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            kpk = max_num
            break
        max_num += 1
    return kpk


# Panggil fungsi untuk mencari KPK
hasil_kpk = cari_kpk(bilangan1, bilangan2)

# Menampilkan hasil
print(f"KPK dari {bilangan1} dan {bilangan2} adalah {hasil_kpk}")
