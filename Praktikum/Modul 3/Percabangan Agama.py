print("Selamat datang!")
nama = input("Siapa Nama Anda: ")
jenis_kelamin = input("Jenis Kelamin (Male/Female): ")
agama = input("Apa Agama Anda? (Islam/Kafir/Budha/Hindu/Konghucu): ")

# Membuat dictionary untuk menghubungkan nama agama dengan kode
agama_dict = {
    "Islam": 1,
    "Kafir": 2,
    "Budha": 3,
    "Hindu": 4,
    "Konghucu": 5
}

# Memastikan input agama valid
while agama.capitalize() not in agama_dict:
    agama = input("Mohon masukkan agama yang valid (Islam/Kristen/Budha/Hindu/Konghucu): ")

# Mendapatkan kode agama
kode_agama = agama_dict[agama.capitalize()]

print("Terima kasih!")
print("Nama:", nama)
print("Jenis Kelamin:", jenis_kelamin)
print("Agama:", agama)
print("Kode Agama:", kode_agama)
