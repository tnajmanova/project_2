"""
projekt_2.py: Bulls and Cows -> druhý projekt do Engeto Online Python Akademie -> VERZE 2

author: Tereza Najmanová
email: najmanova.tereza@gmail.com
"""

import random

ODDELOVAC = '-' * 47

def pozdrav_uzivatele() -> str:
    '''
    Funkce pozdraví uživatele a informuje o začátku hry.
    '''
    print(f'Hi there!\n{ODDELOVAC}\nI\'ve generated a random 4 digit number for you.\nLet\'s play a bulls and cows game.')
    
def vygenerovani_cisla() -> int:
    '''
    Funkce s pomocí knihovny random (funkce .randint()) generuje a vrací náhodné čtyrmístné číslo v rozsahu mezi 1000 a 9999 
    ve formátu int.
    Dále pomocí while cyklu po úpravě čísla na set (za účelem spojení duplicit) zkontroluje délku čísla.
    '''
    while True:
        random_cislo = str(random.randint(1000, 9999))

        if len(set(random_cislo)) == len(random_cislo):
            return random_cislo

def zadani_cisla() -> str:
    '''
    Vyzve uživatele k zadání 4 místného čísla. 

    Při zadání nepodporovaného formátu čísla (začínající 0, nečtyřmístné, nečíselné nebo duplictiní) upozorní na tuto chybu 
    a vyzve znovu uživatele k zadání.

    Při správném zadání, funkce zobrazí vložené 4 místné číslo jako str.
    '''
    print(ODDELOVAC)
    prepinac = True

    while prepinac:
        zadane_cislo = input('Enter a number: ')

        if len(zadane_cislo) != 4:
            print('Please enter number with 4 digits!')
        elif zadane_cislo[0] == '0':
            print('Number must not begin with 0!')
        elif not zadane_cislo.isdigit():
            print('Please enter only numbers!')
        elif len(set(zadane_cislo)) != len(zadane_cislo):
            print('Number must not contain same numbers')
        else:
            print(ODDELOVAC, f'>>> {zadane_cislo}', sep='\n')
            prepinac = False
            return zadane_cislo
            
def vyhodnoceni_cisla(zadane_cislo: str, random_cislo: str) -> int:
    '''
    Funkce vyhodnotí uživatelem zadané čtyřmístné číslo a náhodně vygenerované číslo pomocí hry 'cows and bulls'.
    
    Pracuje s parametry zadané číslo uživatelem a náhodně vygenerované číslo.

    Pokud se jedno či více čísel objeví ve vygenerovaném čísle, přičte se správný odhad do proměnné cows.
    Pokud se pozice zadaného čísla shoduje s pozicí ve vygenerovaném čísle, přičte se správný odhad do proměnné bulls.
    Dále ošetří počet cows aby se neduplikovali s počtem bulls.

    Funkce vrací dvě proměnné cows a bulls ve formátu int.
    '''
    cows = 0
    bulls = 0

    for index in range(len(zadane_cislo)): 
        if zadane_cislo[index] in random_cislo:
            cows += 1
        if zadane_cislo[index] == random_cislo[index]:
            bulls += 1
    
    cows -= bulls
    return cows, bulls
   
def spust_hru() -> str:
    '''
    Pomocí spuštění nadefinovaných funkcí pozdraví uživatele a vytvoří dvě proměnné: uživatelem zadané číslo a náhodně 
    vygenerované číslo.
    
    Vyhodnotí shodu čísel, informuje uživatele o rozsahu shody pomocí hry 'cows and bulls', započítá počet pokusů a opakuje 
    proces do té doby, než se čísla shodují. Poté pogratuluje uživateli, zobrazí počet pokusů a ukončí hru.
    '''
    pozdrav_uzivatele()
    random_cislo, zadane_cislo = vygenerovani_cisla(), zadani_cisla()
    hra_bezi = True
    pokusy = 1

    while hra_bezi:
        if zadane_cislo == random_cislo:
            print('Correct, you\'ve guessed the right number', f'in {pokusy} guesses!', sep='\n')
            hra_bezi = False 
        else:
            cows, bulls = vyhodnoceni_cisla(zadane_cislo, random_cislo)
            
            strcow = 'cow' if cows <= 1 else 'cows'
            strbull = 'bull' if bulls <= 1 else 'bulls'
                
            print(f'{bulls} {strbull}, {cows} {strcow}')
            zadane_cislo = zadani_cisla()
            pokusy += 1
    else:
        print('That\'s amazing!')   

spust_hru()


