def is_prime(n):
    '''
    Verifica primalitatea unui numar
    :param n: nr. natural
    :return: True daca n este prim, altfel False
    '''
    if int(n) < 2: return False
    for i in range(2, int(n)//2 + 1):
        if int(n)%int(i)==0: return False
    return True

assert is_prime(3) == True
assert is_prime(5) == True
assert is_prime(6) == False

def get_min(a, b, c):
    '''
    Determina cel mai mic numar dintre a, b si c
    :param a: nr. natural
    :param b: nr. natural
    :param c: nr. natural
    :return: minimul dintre a, b si c
    '''
    if a<=b and a<=c: return a
    if b<=a and b<=c: return b
    return c

assert get_min(5, 7, 3) == 3
assert get_min(16, 4, 64) == 4
assert get_min(1, 2, 3) == 1

def get_reflected(n):
    '''
    Calculeaza oglinditul lui n
    :param n: nr. natural
    :return: Oglinditul lui n
    '''
    result = int(0)
    while n:
        result = result*10 + int(n)%10
        n = int(n) // 10
    return result

def main():
    while True:
        print("Ce algoritm doriti sa rulati?")
        print("Optiunea 1: Minimul a trei numere citite de la tastatura")
        print("Optiunea 2: Verificati daca un numar citit de la tastatura este prim")
        print("Optiunea 3: Verificati daca n numere citite de la tastatura sunt prime")
        print("Optiunea 4: Afisarea unui numar citit de la tastatura cu cifrele in ordine inversa ( oglindit )")
        print("Optiunea 5: Terminati programul")
        option = input("\nScrieti numarul unei optiuni: ")
        print()

        if option == "1":
            print("Dati cele trei numere:", end = " ")
            a, b, c = input().split()
            print("Minimul este:", end = " ")
            print(get_min(a, b, c))

        if option == "2":
            n = input("Dati numarul: ")
            print("Primalitatea lui " + n + " este:", end = " ")
            print(is_prime(n))

        if option == "3":
            n = input("Dati numarul de numere: ")
            print()
            for i in range(0, int(n)):
                print("Dati numarul", end = " ")
                print(i+1, end = ": ")
                nr= input()
                print("Primalitatea lui " + nr + " este:", end=" ")
                print(is_prime(nr))

        if option == "4":
            n = input("Dati numarul: ")
            print("Numarul " + n + " afisat cu cifrele in ordine inversa este:", end = " ")
            print(get_reflected(n))

        if option == "5":
            break
        print()

if __name__ == '__main__':
    main()