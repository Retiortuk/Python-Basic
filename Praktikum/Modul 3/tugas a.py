# HURUF VOKAL DAN KONSONAN 

print(35*"=")
print("Huruf Konsonan Atau Huruf Vokal")
print(35*"=")

#Huruf Konsonan : C, R, M, H.
#Huruf Vokal : E, A, 

perintah = input("Masukan Huruf (C/E/R/A/M/A/H) Pilih Satu: ")

if perintah =="C" or perintah =="R" or perintah =="M" or perintah =="H" :
    print(perintah, "Adalah Huruf Konsonan")
elif perintah =="E" or perintah =="A" :
    print(perintah, "Adalah Huruf Vokal")
else :
    print("Tolong Masukan Huruf Yang Ada")
