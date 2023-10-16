import time
import os

def menu():
    os.system("clear")
    print(
        """
        ______________________________________________________________
                              WITAJ W GRZE W HUJA

                             Nadus 1 aby se zaczonc
        ______________________________________________________________
        """
    )
    try:
        choice = int(input("Wybieram: "))
        return choice
    except:
        print("")
        print("Wybierz jedna z dostepnych opcji!")
        time.sleep(2)
        menu()

def main():
    menu()


main()
