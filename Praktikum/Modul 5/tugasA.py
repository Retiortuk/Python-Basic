# AULIA AHMAD GHAUS ADZAM
# 2311104028

# o	100 > Nilai >= 90 	
# Predikat = A o 90 > 
# Nilai >= 70 	Predikat = B o 70 > 
# Nilai >= 50 	Predikat = C o 50 > 
# Nilai >= 30 	Predikat = D o 30 > 
# Nilai >= 0 	Predikat = E 

print(45*"=")
print("Telkom University")
print("Insert Your Name Then Rate !")
print(45*"=")

#INPUT
name = input("What's Your Name: ")
nilai_1 = int(input("Insert Your Rate For 1st Subject: "))
nilai_2 = int(input("Insert Your Rate For 2nd Subject: "))
nilai_3 = int(input("Insert Your Rate For 3rd Subject: "))
nilai_4 = int(input("Insert Your Rate For 4th Subject: "))
nilai_5 = int(input("Insert Your Rate For 5th Subject: "))

#NILAI
nilai = ['A', 'B', 'C', 'D', 'E']

print(45*"=")
print("Your Grade Is !")
print(45*"=")

#MATKUL 1
if nilai_1 > 89 < 100:
    print(f"Your Rate is {nilai[0]} For the 1st Subject")
elif nilai_1 > 69:
    print(f"Your Rate is {nilai[1]} For the 1st Subject")       
elif nilai_1 > 49:                                       #Array started from 0 Not 1 That's Why is A is 0
    print(f"Your Rate is {nilai[2]} For the 1st Subject")
elif nilai_1 > 29:
    print(f"Your Rate is {nilai[3]} For the 1st Subject")
elif nilai_1 > 0 :
    print(f"Your Rate is {nilai[4]} For the 1st Subject")
else:
    print("Value It's Not Vaild")

#MATKUL 2
if nilai_2 > 89 < 100:
    print(f"Your Rate is {nilai[0]} For the 2nd Subject")
elif nilai_2 > 69:
    print(f"Your Rate is {nilai[1]} For the 2nd Subject")
elif nilai_2 > 49:
    print(f"Your Rate is {nilai[2]} For the 2nd Subject")
elif nilai_2 > 29:                                      #Array started from 0 Not 1 That's Why is A is 0
    print(f"Your Rate is {nilai[3]} For the 2nd Subject")
elif nilai_2 > 0 :
    print(f"Your Rate is {nilai[4]} For the 2nd Subject")
else:
    print("Value It's Not Vaild")

#MATKUL 3
if nilai_3 > 89 < 100:
    print(f"Your Rate is {nilai[0]} For the 3rd Subject")
elif nilai_3 > 69:
    print(f"Your Rate is {nilai[1]} For the 3rd Subject")
elif nilai_3 > 49:
    print(f"Your Rate is {nilai[2]} For the 3rd Subject")   #Array started from 0 Not 1 That's Why is A is 0
elif nilai_3 > 29:
    print(f"Your Rate is {nilai[3]} For the 3rd Subject")
elif nilai_3 > 0 :
    print(f"Your Rate is {nilai[4]} For the 3rd Subject")
else:
    print("Value It's Not Vaild")

#MATKUL 4
if nilai_4 > 89 < 100:
    print(f"Your Rate is {nilai[0]} For the 4th Subject")
elif nilai_4 > 69:
    print(f"Your Rate is {nilai[1]} For the 4th Subject")
elif nilai_4 > 49:
    print(f"Your Rate is {nilai[2]} For the 4th Subject")   #Array started from 0 Not 1 That's Why is A is 0
elif nilai_4 > 29:
    print(f"Your Rate is {nilai[3]} For the 4th Subject")
elif nilai_4 > 0 :
    print(f"Your Rate is {nilai[4]} For the 4th Subject")
else:
    print("Value It's Not Vaild")

#MATKUL 5
if nilai_5 > 89 < 100:
    print(f"Your Rate is {nilai[0]} For the 5h Subject")
elif nilai_5 > 69:
    print(f"Your Rate is {nilai[1]} For the 5th Subject")
elif nilai_5 > 49:
    print(f"Your Rate is {nilai[2]} For the 5th Subject")   #Array started from 0 Not 1 That's Why is A is 0
elif nilai_5 > 29:
    print(f"Your Rate is {nilai[3]} For the 5th Subject")
elif nilai_5 > 0 :
    print(f"Your Rate is {nilai[4]} For the 5th Subject")
else:
    print("Value It's Not Vaild")



















