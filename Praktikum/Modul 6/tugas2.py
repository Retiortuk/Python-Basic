# AULIA AHMAD GHAUS ADZAM
# 2311104028

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