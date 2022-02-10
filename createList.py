print("Příkad 6")

listSize = int(input("Zadej počet hodnot seznamu: "))
seznamPrvku = []

i=0

while i< listSize:
    zadejCislo = int(input(f"Zadej {i + 1}. číslo z {listSize}: "))
    if zadejCislo > 0:
        seznamPrvku.append(zadejCislo)
    else:
        print("Nepodporovaná hodnota, zadej znovu!")
        i-=1
    i+= 1

