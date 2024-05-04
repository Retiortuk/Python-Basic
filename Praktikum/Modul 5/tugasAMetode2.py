
def hitung_rerata_dan_predikat(nilai_array):
  """
  Menghitung nilai rerata dan predikat dari array nilai.

  Args:
    nilai_array: Array yang berisi nilai-nilai.

  Returns:
    Tuple yang berisi nilai rerata dan predikat.
  """
  # Menghitung nilai total.
  total_nilai = sum(nilai_array)

  # Menghitung nilai rerata.
  rerata = total_nilai / len(nilai_array)

  # Menentukan predikat.
  predikat = None
  if rerata >= 90:
    predikat = "A"
  elif rerata >= 80:
    predikat = "B"
  elif rerata >= 70:
    predikat = "C"
  elif rerata >= 50:
    predikat = "D"
  elif rerata >= 0:
    predikat = "E"
  else:
    predikat = "Nilai Tidak Valid"

  return rerata, predikat

# Contoh penggunaan.
nilai_array = [85, 90, 75, 80, 65]
rerata, predikat = hitung_rerata_dan_predikat(nilai_array)

print(f"Nilai rerata: {rerata}")
print(f"Predikat: {predikat}")
