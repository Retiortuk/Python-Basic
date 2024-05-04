# AULIA AHMAD GHAUS ADZAM
# 2311104028

def kalkulator_sederhanna():
    print("\n----- KALKULATOR -----\n")

    print("1. PENJUMLAHAN (+)")
    print("2. PERKALIAN(x)")
    print("3. PEMBAGIAN (/, :)")
    print("4. PENGURANGAN (-)")
    print("5. PANGKAT (^)\n")

    bil_1 = int(input("Masukan Bilangan Pertama: "))
    operator = input("Masukan Operator Sesuai Yang Tertera Di Atas: ")
    bil_2 = int(input("Masukan Bilangan Kedua: "))

    if operator =="+":
        hasil = bil_1 + bil_2
        print(f"\nHASIL DARI {bil_1} + {bil_2} Adalah {hasil}")
    elif operator =="x" or operator =="*":
        hasil = bil_1 * bil_2
        print(f"\nHASIL DARI {bil_1} X {bil_2} Adalah {hasil}")
    elif operator =="/" or operator ==":":
        hasil = bil_1 / bil_2
        print(f"\nHASIL DARI {bil_1} / {bil_2} Adalah {hasil}")
    elif operator =="-":
        hasil = bil_1 - bil_2
        print(f"\nHASIL DARI {bil_1} - {bil_2} Adalah {hasil}")
    elif operator =="**" or operator =="^":
        hasil = bil_1 ** bil_2
        print(f"\nHASIL DARI {bil_1} ^ {bil_2} Adalah {hasil}")
    else:
        print("Tolong Masukann Operator Sesuai Diatas!")
kalkulator_sederhanna()


    