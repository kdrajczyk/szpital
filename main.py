import json

with open("pacjenci.json", encoding='utf-8') as pacjenci_json:
    pacjenci_slownik = json.load(pacjenci_json)

    print(pacjenci_slownik["1234567890"])

# def dodawaniePacjenta(numer_pesel_pacjenta, imie_pacjenta, nazwisko_pacjenta,
#                       wiek_pacjenta, oddział_szpitalny, diagnoza_pacjenta):
#

for element in pacjenci_slownik:
    pacjent = pacjenci_slownik[element]
    for parametr in pacjent.values():
        if parametr == "alergologia":
            print(element)


# szpital["1234567890","diagnoza"]= atopia
