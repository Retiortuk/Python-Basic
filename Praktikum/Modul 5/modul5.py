# Pengunaan Array Di Python
# Angka = [1,2,3,4,5]
# Text = ["Satu", "Dua", "Tiga", "Empat", "Lima"]

# print(Angka,Text)


# #Urutan makanan Sebelum Diganti
# Menu = ['Nasi Goreng', 'Mie Goreng', 'Ayam Goreng']
# print(Menu)

# #Diganti
# Menu[1] = "Bebek Goreng"

# #Setelah DIganti
# print(Menu)

# Menu = ["Nasi Goreng", "Mie Goreng", "Ayam Goreng", "Bebek Goreng"]

# Menu.pop(1) 
# Menu.remove("Nasi Goreng") #Ini Harus String Tidak Seperti .pop()

# print(Menu)

# Menu = [["Nasi Goreng", "Mie Goreng", "Ayam Goreng", "Bebek Goreng"],
#         ["Mie Ayam", "Ayam Bakar", "Bakso", "Steak Sapi"]]

# for i in range (len(Menu)):
#     for x in range (len(Menu[i])):
#         print(Menu[i][x])

# angka = [0,1,2,3,4,5,6,7,8,9,10]
# for i in angka:
#     if i %2==0:
#         print(i)

# bilangan = int(input("Masukan jumlah kata: ")) 
# kata = [] 

# for x in range(bilangan): 
#     kata.append(input("masukan kata: "))     
#     if x == bilangan - 1: 
#         print("") 
#         cari = input("Masukan kata yang ingin dicari: ")         
#         for h in kata: 

#             if(h == cari): 
#                 print(cari,"ditemukan pada indeks ke-",kata.index(h))             
                
#             else: 
#                 print("Data tidak ditemukan !") 

