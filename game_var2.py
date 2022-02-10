import random #nahrání knihovny

#funkce pro generování náhodného čísla, argument od, do
rozsahOd = 10
rozsahDo = 20
nahodnecislo = random.randint(rozsahOd,rozsahDo)

while True:
    hledane = int(input("Zadejte číslo: "))


    if hledane == -1: # konec hry
        break

    elif hledane > nahodnecislo:
        print("Hledané číslo je menší.")

    elif hledane < nahodnecislo:
        print("Hledané číslo je větší")

    else: #cisla se rovnaji - vyhra
        print("Bingo. Našel jsi číslo!")
        break

print(f"Konec hry. Hledané číslo bylo: {nahodnecislo}.")