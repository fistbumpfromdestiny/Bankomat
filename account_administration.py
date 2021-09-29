import json
filename = 'accounts.json'

def get_bankaccounts():
    """Imports account info to calling functions."""
    
    with open(filename) as f:

        bankAccounts = json.load(f)
        return bankAccounts


def write_to_file(bankAccounts):
    """Lets calling functions write account info changes to file."""

    with open(filename, 'w') as f:
        json.dump(bankAccounts, f)


def create_account(bankAccounts):
    """Creates an account if not already taken and writes it to file."""

    while True:
        accExists = False
        acctNr = input("Ange kontonummer: ")
        if acctNr == '':
            return
        try:
            int(acctNr)
            if int(acctNr) <= 0:
                raise ValueError

        except ValueError:
            print("Felaktigt kontonummer.")
            continue

        for account in bankAccounts: 
            for key, value in account.items():
                if value == acctNr:
                    print("Kontonumret är upptaget.\n")
                    accExists = True
                    continue

        if accExists == False:            
            accountDetails = {
                'Kontonummer': acctNr,  
                'Saldo': 0, 
                'Transaktioner': []
                }
            bankAccounts.append(accountDetails)

            print(f"Konto {acctNr} skapat.\n")
            write_to_file(bankAccounts)
            break


def administer_account(bankAccounts, logged_in):
    """Logs on to an account, enabling the print_account_menu-function."""
   
    while logged_in == False:
        acctNr = input("Ange kontonummer: ")
        try:
            int(acctNr)
            for account in bankAccounts: 
                for key, value in account.items():
                    if value == acctNr:
                        print(f"Loggar in på kontonummer {acctNr}.\n")  
                        logged_in = True

            if logged_in == False:
                print("Kontonumret existerar inte.\n")  

        except ValueError:
            print("Felaktigt kontonummer.\n")
    
    return acctNr


def account_withdrawal(date, bankAccounts, acctNr):
    """Withdraws money from account as long as balance is high enough."""

    withdraw = True
    while withdraw == True:
        amount_to_withdraw = input(f"Ange belopp att ta ut från konto {acctNr}: ")

        try:
            int(amount_to_withdraw)
            amount_to_withdraw = int(amount_to_withdraw)
            if amount_to_withdraw > 0:
                for account in bankAccounts: 
                    for key, value in account.items():
                        if value == acctNr:
                            if account['Saldo'] - amount_to_withdraw >= 0:
                                account['Saldo'] -= amount_to_withdraw
                                print(f"Uttag av: {amount_to_withdraw} kronor.")
                                print(f"Tillgängligt saldo: {account['Saldo']}")
                                account['Transaktioner'].append(
                                    {
                                    'Transaktionsdatum': date, 
                                    'Belopp': -amount_to_withdraw
                                    }
                                )   
                                withdraw = False
                            else:
                                print(f"För lågt saldo för att ta ut {amount_to_withdraw} kronor.")
                                print(f"Tillgängligt saldo är: {account['Saldo']}\n")

            elif amount_to_withdraw < 0:
                print("Kan inte göra uttag på ett negativt belopp.\n")

        except ValueError:
            print("Felaktigt belopp.\n")

    write_to_file(bankAccounts)


def account_deposit(date, bankAccounts, acctNr):
    """Deposits money as long as amount is bigger than 0."""

    deposit = True
    while deposit == True:
        amount_to_deposit = input(f"Ange belopp att sätta in på konto {acctNr}: ")

        try:
            int(amount_to_deposit)
            amount_to_deposit = int(amount_to_deposit)
            if amount_to_deposit > 0:
                for account in bankAccounts: 
                    for key, value in account.items():
                        if value == acctNr:
                            account['Saldo'] += amount_to_deposit
                            print(f"Insättning av: {amount_to_deposit} kronor.")
                            print(f"Tillgängligt saldo: {account['Saldo']} kronor.\n")
                            account['Transaktioner'].append(
                                {
                                    'Transaktionsdatum': date, 
                                    'Belopp': amount_to_deposit
                                    }
                            )  
                            deposit = False
            else:
                print("Beloppet måste vara större än 0.\n")

        except ValueError:
            print("Felaktigt belopp.\n")
           
    write_to_file(bankAccounts)


def check_balance(bankAccounts, acctNr):
    """Returns account balance to calling function."""

    for account in bankAccounts: 
            for key, value in account.items():
                if value == acctNr:
                    return account['Saldo']


def list_transactions(bankAccounts, acctNr):
    """Lists functions for logged on account."""

    for account in bankAccounts: 
        for key, value in account.items():
            if value == acctNr:
                if account['Transaktioner'] == []:
                    print("Inga transaktioner att visa.\n")
                else:
                    print(str(account['Transaktioner'])
                    .replace("[{", "")
                    .replace("'", "")
                    .replace("}]", "")
                    .replace("}, {","\n"))
