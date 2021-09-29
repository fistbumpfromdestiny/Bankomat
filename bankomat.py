from datetime import datetime
import account_administration as aa

logged_in = False
show_menu = True
date = datetime.today().strftime('%Y-%m-%d')
bankAccounts = aa.get_bankaccounts()

def print_main_menu():
    """Shows a menu while not logged on."""

    print(15 * "*" , "Menu" , 15 * "*")
    print("\n\t1) Skapa konto")
    print("\t2) Administrera konto")
    print("\t3) Avsluta\n")
    print(36 * "*", "\n")


def print_account_menu():
    """Shows another menu while logged on."""

    print(12 * "*" , "Kontomeny" , 12 * "*")
    print("\n\t1) Ta ut pengar")
    print("\t2) Sätt in pengar")
    print("\t3) Visa saldo")
    print("\t4) Lista transaktioner")
    print("\t5) Logga ut\n")
    print(35 * "*", "\n")

while show_menu == True:

    if logged_in == False:
        print_main_menu()
    else:
        print_account_menu()
    
    menu_choice = input("Ange menyval: ")

    try:
        int(menu_choice)
    except ValueError:
        continue
    while int(menu_choice) < 1 and int(menu_choice) > 3:
         print("Felaktig inmatning, försök igen.")
         menu_choice = input("Ange menyval: ")

    if menu_choice == '1':
        aa.create_account(bankAccounts)

    elif menu_choice == '2':        
        acctNr = aa.administer_account(bankAccounts, logged_in)
        logged_in = True

    elif menu_choice == '3':
        print("Programmet avslutas.")
        show_menu = False        

    while logged_in == True:
        
        print_account_menu()
        menu_choice = input("Ange menyval: ")

        try:
            int(menu_choice)
        except ValueError:
            continue
        while int(menu_choice) < 1 and int(menu_choice) > 5:
            
            print("Felaktig inmatning, försök igen.")
            menu_choice = input("Ange menyval: ")

        if menu_choice == '1':
            aa.account_withdrawal(date, bankAccounts, acctNr)

        elif menu_choice == '2':
            aa.account_deposit(date, bankAccounts, acctNr)

        elif menu_choice == '3':
            print(f"Tillgängligt saldo är: {aa.check_balance(bankAccounts, acctNr)} kronor.\n")
        
        elif menu_choice == '4':
            aa.list_transactions(bankAccounts, acctNr)

        elif menu_choice == '5':
            print(f"Loggar ut konto {acctNr}.")
            logged_in = False
            
        