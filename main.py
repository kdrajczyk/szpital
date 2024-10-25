import json
import pygal

with open("pacjenci.json", encoding='utf-8') as pacjenci_json:
    baza_pacjentow = json.load(pacjenci_json)

    print(baza_pacjentow["1234567890"])

ODDZIAŁY_SZPITALNE = ['alergologia','kardiologia','nefrologia','neurologia']


# def dodawaniePacjenta(numer_pesel_pacjenta, imie_pacjenta, nazwisko_pacjenta,
#                       wiek_pacjenta, oddział_szpitalny, diagnoza_pacjenta):
#

imie_pacjenta = "Katarzyna"

for element in baza_pacjentow:
    pacjent = baza_pacjentow[element]
    for parametr in pacjent.values():
        if parametr == imie_pacjenta:
            print(f"Znalazłem pacjenta, jego pesel to: {element}")


pacjenci_per_oddział = {"alergologia":0,"kardiologia":0,"nefrologia":0,"neurologia":0}
print(f"Liczba przed liczeniem: {pacjenci_per_oddział}")
oddzialy = [oddzial for oddzial in pacjenci_per_oddział.keys()]
for pacjent in baza_pacjentow:
    pacjent = baza_pacjentow[pacjent]
    for szczegoly in pacjent.values():
        if szczegoly  == oddzialy[0]:
            pacjenci_per_oddział["alergologia"] += 1
        elif szczegoly == oddzialy[1]:
            pacjenci_per_oddział["kardiologia"] += 1
        elif szczegoly == oddzialy[2]:
            pacjenci_per_oddział["nefrologia"] += 1
        elif szczegoly == oddzialy[3]:
            pacjenci_per_oddział["neurologia"] += 1

print(pacjenci_per_oddział)

def usuwaniePacjentaZBazy():
    with open("pacjenci.json", encoding='utf-8') as pacjenci_json:
        baza_pacjentow = json.load(pacjenci_json)
        print(f"baza przed usunieciem: {baza_pacjentow}")
        pesel_do_usuniecia = input("wpisz swoj pesel ")
        baza_pacjentow.pop(pesel_do_usuniecia)
        print(f"baza po usunieciu: {baza_pacjentow}")



usuwaniePacjentaZBazy()
