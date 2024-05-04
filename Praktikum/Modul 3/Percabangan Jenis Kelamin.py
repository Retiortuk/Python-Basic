
#Challenge
jenis_kelamin = input("Masukkan jenis kelamin (L/P): ")
status_pernikahan = input("Apakah sudah menikah? (Y/T): ")

if jenis_kelamin == 'L':
    if status_pernikahan == 'Y':
        print("Halo, Pak.")
    else:
        print("Halo, Mas.")
elif jenis_kelamin == 'P':
    if status_pernikahan == 'Y':
        print("Halo, Ibu.")
    else:
        print("Halo, Mbak.")
else:
    print("Masukkan jenis kelamin dan status pernikahan dengan benar.")


        
