#TUGAS B AULIA AHMAD GHAUS ADZAM 2311104028

bilangan = int(input("Masukan Bilangan: "))

pangkat = int(input("Masukan Pangkat: "))

hasil = bilangan

for i in range(pangkat - 1):
    hasil *= bilangan
print(hasil)