# ATM Mesin Sederhana

def ATM_Machine():
    print("\n----- Welcome To ATM Machine -----")

    # INPUT PIN And Balance Information
    pin = int(input("\nInsert Your Pin: "))
    Early_Balance = float(input("Insert Your Balance: Rp."))

    print(f"\nHere's Your Balance Rp.{Early_Balance:,.2f}")

    print("\n------------------------------------")

    # INPUT For Withdraw Cash & Procces
    withdraw = int(input("\nHow Much You Want to Draw: Rp."))
    if withdraw > Early_Balance:
        print("Your Balance it's Not Enough")
        return
    
    last_balance = Early_Balance - withdraw

    # Output
    print("\n----- Your Transaction Has Succeed -----")
    print(f"\nYour Balance: Rp.{Early_Balance:,.2f}")
    print(f"Your Draw: Rp.{withdraw:,.2f}")
    print(f"Your Current Balance: Rp.{last_balance:,.2f}")
    print("\n------------ Thank You -----------------")

ATM_Machine()
