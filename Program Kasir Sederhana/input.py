# Program Kasir Warung Makan Gesa

def cashier_system_gesa_resto():
    # Initialitation
    total_purchase = 0
    purchase = 0
    change_money = 0

    # Food List
    menu_list = {
        'Ayam Geprek': 10,
        'Ayam Bakar': 10,
        'Ayam Rica-Rica': 10,
        'Ayam Gulai': 10,
        'Ayam Goreng': 9,
        'Rendang Beef': 11,
        'White Rice': 3,
        'Nasi Goreng': 7,
        'Tempe Orek': 5,
        'Cah Kangkung': 5,
        'Sayur Asem': 5,
        'Indomie Goreng': 3,
    }

    print('\n-------- Welcome To Indo Resto NYC By Gesa ---------')
    print("\nOur Menu:")
    print("- Ayam Geprek $10")
    print("- Ayam Bakar $10")
    print("- Ayam Rica-Rica $10")
    print("- Ayam Goreng $9")
    print("- Ayam Gulai $10")
    print("- Rendang Beef $11")
    print("- Nasi Goreng $7")
    print("- Tempe Orek $5")
    print("- Cah Kangkung $5")
    print("- Sayur Asem $5")
    print("- Indomie Goreng $3")
    print("- White Rice $2")

    # Input & Price Calculation
    how_many = int(input("\nHow Much Items You Want To Proceed: "))

    for i in range(how_many):
        items_name = input(f"\nInsert Your {i + 1} Items: ")
        if items_name not in menu_list:
            print(f"Sorry, We Don't Have {items_name}")
            continue
        
        how_much = int(input(f"How Many {items_name} You Want ?: "))
        if how_much < 1:
            print("Sorry, It Must at Least 1")
            continue

        food_price = menu_list[items_name] * how_much
        total_purchase += food_price

        print(f"{how_much} {items_name} Total all: ${total_purchase:,}")

    # Payment & Change
    purchase = float(input(f"\nTotal Pay: ${total_purchase}\nInsert Your Money: $"))

    if purchase > total_purchase:
        change_money = purchase - total_purchase
    else:
        print(f"Sorry It's ${total_purchase}, We Received ${purchase} It Needs More. ")
        print("You Are Broke AF Get A Job DumbAss$$")
        return
    
    # Bill
    print("\n--------- Indo Resto NYC By Gesa ---------")
    print(f"Total Pay: ${total_purchase}")
    print(f"Paid: ${purchase}")
    print(f"Change: ${change_money}")
    print("--------- Thanks Come again Soon! --------")

cashier_system_gesa_resto()
print("End")
