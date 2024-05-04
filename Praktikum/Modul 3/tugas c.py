# Identifikasi Biaya operasi penyakit

# Operasi Mata: Katarak : Rp.7.500.000 | Plus/Minus : Rp.5.000.000 |
# Silinder : Rp. 4.000.000

# Operasi Jantung : Jantung Koroner : Rp. 500.000.000 |
# Katup Jantung : Rp. 350.000.000 | Otot Jantung : Rp. 450.000.000 |


print(35*"=")
print("Hitung Biaya operasi penyakit")
print(35*"=")

print("1. Biaya Operasi Mata ")
print("2. Biaya Operasi Jantung ")

milih = input("Masukkan Pilihan: ")

if milih =='1':
    print("JENIS PENYAKIT MATA")
    print("1. Katarak")
    print("2. Plus/Minus")
    print("3. Silinder")
mata = input("Masukkan Pilihan: ")
if mata =='1':
    print("Rp. 7.500.000") 
elif mata =='2':
    print("Rp. 5.000.000")
elif mata =='3':
    print("Rp. 4.000.000")
else: 
    print("Mohon Masukkann Yang Tertera")


if milih =='2':
    print("JENIS PENYAKIT JANTUNG")
    print("1. Koroner")
    print("2. Katup Jantung")
    print("3. Otot Jantung")
jantung = input("Masukkan Pilihan: ")
if jantung =='1':
    print("Rp. 500.000.000") 
elif jantung =='2':
    print("Rp. 350.000.000")
elif jantung =='3':
    print("Rp. 450.000.000")
else: 
    print("Mohon Masukkann Yang Tertera")
    



            

