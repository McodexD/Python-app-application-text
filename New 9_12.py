

def visa_meny():
    print("\nMeny:")
    print("1. Skapa konto")
    print("2. Ta bort konto")
    print("3. Lista alla kontonummer")
    print("4. Lista totalsaldo")
    print("5. Lista alla kontonummer och saldo")
    print("0. Avsluta")

def skapa_konto(bank):
    kontonummer = input("Ange ett nytt kontonummer: ")
    if kontonummer in bank:
        print("Kontot finns redan.")
    else:
        saldo = float(input("Ange startsaldo: "))
        bank[kontonummer] = saldo
        print(f"Konto {kontonummer} skapat med saldo {saldo}.")

def ta_bort_konto(bank):
    kontonummer = input("Ange kontonumret som ska tas bort: ")
    if kontonummer in bank:
        del bank[kontonummer]
        print(f"Konto {kontonummer} har tagits bort.")
    else:
        print("Kontot existerar inte.")

def lista_kontonummer(bank):
    if bank:
        print("Alla kontonummer:")
        for kontonummer in bank:
            print(kontonummer)
    else:
        print("Inga konton att visa.")

def lista_totalsaldo(bank):
    totalsaldo = sum(bank.values())
    print(f"Totalt saldo i banken: {totalsaldo}")

def lista_konton_och_saldo(bank):
    if bank:
        print("Kontonummer och saldo:")
        for kontonummer, saldo in bank.items():
            print(f"Kontonummer: {kontonummer}, Saldo: {saldo}")
    else:
        print("Inga konton att visa.")

def bank_applikation():
    bank = {}  

    while True:
        visa_meny()
        val = input("Välj ett alternativ: ")

        if val == '1':
            skapa_konto(bank)
        elif val == '2':
            ta_bort_konto(bank)
        elif val == '3':
            lista_kontonummer(bank)
        elif val == '4':
            lista_totalsaldo(bank)
        elif val == '5':
            lista_konton_och_saldo(bank)
        elif val == '0':
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val. Försök igen.")


bank_applikation()

