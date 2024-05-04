# AULIA AHMAD GHAUS ADZAM
# 2311104028

def bilangan_genap(bilangan):

  if bilangan % 2 == 0:
    return "Genap"
  else:
    return "Ganjil"


bilangan_input = int(input("Masukkan bilangan bulat: "))
hasil = bilangan_genap(bilangan_input)
print(f"Bilangan {bilangan_input} adalah {hasil}")
