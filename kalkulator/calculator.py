# Excersise

# Busta Calculator

print(30*"=")
print("Welcome To Busta Calculator")
print(30*"=")

number_1 = float(input("Insert First Number: "))
operator = input("Insert Operator (+,-,x,/): ")
number_2 = float(input("Insert Second Number: "))

if operator =="+":
    value = number_1 + number_2
    print(f"Result Is {value}")
elif operator =="-":
    value = number_1 - number_2
    print(f"Result Is {value}")
elif operator =="x" or operator =="*":
    value = number_1 * number_2
    print(f"Result Is {value}")
elif operator =="/" or operator ==":" or operator=='~':
    value = number_1 / number_2
    print(f"Result Is {value}")

else:
    print("Error Can't Calculate!!")
    print("Make Sure To Use the right Operator As it Shown!!")


print(30*"=")





