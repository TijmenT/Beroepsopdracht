import time
from datetime import date

start_over = 1

repeat = "Y", "y"
repeat2 = "Y", "y"
repeat3 = "Y", "y"

import time

today = date.today()

while repeat[0] not in ("N"):
    
    print("Hello you, ik ben Tijmen")
    print("Wie ben jij?: ")
    naam = input()
    print("En je achternaam?: ")
    achternaam = input()
    print("Hello, " + naam + " " + achternaam)
    print(" ")
    print(" ")
    print("Ik ben een nieuwkomer op het Mediacollege Amsterdam.")
    print(" ")
    print("Er komen wat vragen over mij zodat je mij beter kan leren kennen veel succes!")
    print(" ")
    print("Ik ga je hier een kleine hint geven! mijn reistijd is 1,5 uur en ik woon in een dorp")
    print("Het dorp waar ik woon heet: ")
    print(" A: Opperdoes")
    print(" B: Berkhout")
    print(" C: Limmen")
    question = input("Ik woon in (Vul hier A, B of C in):  ")
    if question == "A":
        print("Correct!")
        print("Op naar de volgende ronde!")
    if question == "a":
        print("Correct!")
        print("Op naar de volgende ronde!")
        start_over -= 1
    if question == "B":
        print("Fout!")
        print("Probeer het nog een keer")
        print("wilt u het programma opnieuw uitvoeren?: ")
        repeat = input()
    if question == "b":
        print("Fout!")
        print("Probeer het nog een keer")
        print("wilt u het programma opnieuw uitvoeren?: ")
        repeat = input()
    if question == "C":
        print("Fout!")
        print("Dit dorpje ligt in Australie lol")
        print("wilt u het programma opnieuw uitvoeren?: ")
        repeat = input()
    if question == "c":
        print("Fout!")
        print("Dit dorpje ligt in Australie lol")
        print("Probeer het later opnieuw.")
        repeat = input()
        
    print("Tweede vraag!")
    time.sleep(1)
    print(" ")
    while repeat2[0] not in ("N"):
        print("Hoe oud ben ik?")
        print("Keuzes: A: 16, B: 15, C: 17")
        question2 = input("Hoe oud ben ik?: ")
        if question2 == "A":
            print("Goedzo!")
            print(" ")
            print("Vraag 3")
            break
        else:
            print("Fout!")
            repeat2 = input("Wilt u het nog eens proberen? (Y/N): ")
    
    print("Wat is mijn favourite eten?")
    print("Keuzes: A: Pizza, B: Patat, C: Friet")
    while repeat3[0] not in ("N"):
        question3 = input("Antwoord: ")
        if question3 == "A":
            print("Fout!")
            repeat3 = input("Wilt u het opnieuw proberen(Y/N)?: ")
        if question3 == "B":
            print("Goedzo!")
            print()
            break
        if question3 == "C":
            print("Fout!")
            print("Het is patat.")
            repeat3 = input("Wilt u het opnieuw proberen(Y/N)?: ")

    print(" ")
    print("Dit waren de vragen!")
    
    print("wilt u het programma opnieuw uitvoeren?: ")
    repeat = input()
print("oke dan niet")
time.sleep(3)
raise SystemExit
