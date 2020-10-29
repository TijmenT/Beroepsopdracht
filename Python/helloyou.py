import time
from datetime import date

start_over = 1

repeat = "ja"

today = date.today()

while repeat[0] not in ("nee"):
    
    print("Hello you, ik ben Tijmen")
    print("Wie ben jij?: ")
    naam = input()
    print("En je achternaam?: ")
    achternaam = input()
    print("Hello, " + naam + " " + achternaam)
    question = input("Wilt u de datum en tijd zien?: ")
    if question == "ja":
        time.sleep(1)
        print(today)
        print (time.strftime("%H:%M:%S"))
    else:
        print("Oke!")
    question = input("Wilt u een rekensom uitvoeren?: ")
    if question == "ja":
            #Info
        def add(x, y):
            return x + y
    
        def subtract(x, y):
            return x - y
    
        def multiply(x, y):
            return x * y

        def divide(x, y):
            return x / y



        print("Kies een optie: 1.optellen, 2.aftrekken, 3.vermenigvuldigen, 4.gedeelddoor")

        while True:
            keuze = input("Maak een keuze tussen die cijfers: ")

            if keuze in ('1', '2', '3', '4'):
                num1 = float(input("Eerste nummer: "))
                num2 = float(input("Tweede nummer: "))

                if keuze == '1':
                    print(num1, "+", num2, "=", add(num1, num2))
    
                elif keuze == '2':
                    print(num1, "-", num2, "=", subtract(num1, num2))

                elif keuze == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))
    
                elif keuze == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))
                break
            else:
                print("Geen nummer")
              
    time.sleep(1)
    print("Wilt u het programma opnieuw uitvoeren?: ")
    repeat = input()
print("oke dan niet")
time.sleep(3)
raise SystemExit
