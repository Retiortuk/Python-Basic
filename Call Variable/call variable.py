#fungsi Def Memanggil Data Mahasiswa Pada Python

def data_student_info():
    name = "Henry Hill"
    Student_ID = "901110405"      #variabel = Input
    class_ = "GN-01A"
    from_= "New York"

    print("Name:", name)
    print("ID:", Student_ID)      #proses
    print("Class:", class_)
    print("From", from_)

data_student_info() #Manggil Harus Diluar = Output

def data_parent_family():
    name = "Jonah Hill"
    parent_born = "Boston"      #variabel = Input
    from_= "New York"

    print("Henry's Parent Info")
    print("Dad:", name)
    print("Born:", parent_born)      #proses
    print("From:", from_)

data_parent_family() #Manggil Harus Diluar = Output

def data_salary_info():
    name = "Henry Hill"
    salary = "$500.000.000"

    person_2 = "Jonah Hill"
    money = "$250.000.000.00"

    print("Sallary Info")
    print("Name:", name)
    print("Sallary:", salary)

    print("Name:", person_2)
    print("Sallary:", money)

data_salary_info()

#Totally Of Sallary

Henry = 500.000
Jonah = 250.000
made = Henry+Jonah

print("Sallary Total:", made)

