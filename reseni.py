#1
print("\nPříkad 1")
def multiplication(x):
    for i in range(1, 11):
            print(i*x)

print("Násobek 2")
multiplication(2)

print("Násobek 10")
multiplication(10)

#2
print("\nPříkad 2")
def row(u):
    for i in range(0, u+1):
        print(i, end=" ")

    for n in range(u-1, -1, -1):
        print(n, end=" ")

row(10)

#3
print("\n\nPříkad 3")

def reverse(seznam):
    delka = len(seznam)
    for i in range(delka, 0, -1):
        print(seznam[i-1])

seznamPrvku = [10, 20, 30, 40, 50, 60, 70, 80, 90]
reverse(seznamPrvku)

#4
print("\nPříkad 4")

def reverseList(seznam):
    delka = len(seznam)
    obracenySeznam = []

    for i in range(delka, 0, -1):
        obracenySeznam.append(seznam[i-1])

    return obracenySeznam

seznamPrvku2 = [100, 200, 300, 400, 500, 600, 700, 800, 900]
print(reverseList(seznamPrvku2))


#5
print("\nPříkad 5")

def removeFromList(seznam, hodnota):
    for i in range (0, len(seznam)-1 ):
        print(i)
        if seznam[i] == hodnota:
            print(seznam[i])
            del seznam[i]
    return seznam

print( removeFromList(seznamPrvku2, 300) )