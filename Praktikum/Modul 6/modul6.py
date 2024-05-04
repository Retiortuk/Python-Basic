# def ini_fungsi():
#     print("Hello ini Fungsi")

# ini_fungsi() 

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# print("Luas Persegi:%d" %luas_persegi(5))

# def salam(ucapan):
#     print(ucapan)
# salam("Halo, Selamat Pagi")   

# def luas_segitiga(alas, tinggi):
#     luas = alas * tinggi / 2 
#     print("Luas Segitiga: %f" %luas)
# luas_segitiga(5,7)

# def keliling_persegi(sisi): 
#     return 4*sisi
 
# def luas_persegi(sisi): 
#     return sisi*sisi 

# panjang = 8 
# print("Masukan panjang sisi: %f" %panjang) 
# print("kelilingnya adalah: %f" %keliling_persegi(panjang)) 
# print("Luasnya adalah: %f" %luas_persegi(panjang)) 

# def keliling_luas_persegi(sisi): 
#     keliling = 4*sisi     
#     luas = sisi*sisi 
#     print("Keliling: %f" %keliling)     
#     print("Luas: %f" %luas) 
     
# panjang = int(input("Masukan panjang sisi:")) 
# keliling_luas_persegi(panjang) 

# def banding(nilai1, nilai2):     
#     if(nilai1>nilai2):         
#         print(nilai1)     
#     elif(nilai1==nilai2):         
#         print("Tidak ada")     
#     else: 
#         print(nilai2) 
 
# bil1 = int(input("Masukan bilangan 1: ")) 
# bil2 = int(input("Masukan bilangan 2: ")) 
# print("bilangan yang lebih besar adalah ") 
# banding(bil1,bil2) 

import math

def hitung_lingkaran(jarijari):
 
  luas = math.pi * jarijari ** 2
  keliling = 2 * math.pi * jarijari

  print(f"Luas lingkaran: {luas:.2f}")
  print(f"Keliling lingkaran: {keliling:.2f}")

# Meminta input jari-jari dari pengguna
jarijari = float(input("Masukkan jari-jari lingkaran: "))

# Menghitung dan menampilkan luas dan keliling
hitung_lingkaran(jarijari)



