import json
from idlelib.iomenu import encoding
import pygal
import datetime

ODDZIAŁY_SZPITALNE = ['alergologia','kardiologia','nefrologia','neurologia']

def HistoriaWizytPacjenta():
    with open("histroria_wizyt.json", encoding="utf-8", mode="a") as historia_wizyt_json:
        nowa_wizyta= {"1234567890": {
            "imie": "Katarzyna",
            "nazwisko": "Drajczyk",
            "numer pesel": "1234567890",
            "oddzial": "alergologia",
            "diagnoza": "AZS",
            "data": "30.10.2024"
        }
        }
        json.dump(nowa_wizyta,historia_wizyt_json)


def dodawaniePacjenta():
    while True:
        imie_nowego_pacjenta = str(input("Podaj imie: "))
        for letter in imie_nowego_pacjenta:
            print(ord(letter))
            if ord(letter) in [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]:
                print("to jest liczba")
        print(imie_nowego_pacjenta)
        nazwisko_nowego_pacjenta = input("Podaj nazwisko: ")
        print(nazwisko_nowego_pacjenta)
        numer_pesel_nowego_pacjenta = input("Podaj numer pesel pacjenta: ")
        print(numer_pesel_nowego_pacjenta)
        wiek_nowego_pacjenta = input("Podaj wiek: ")
        print(wiek_nowego_pacjenta)

        for oddzial, numer_z_listy_oddzialow in zip(ODDZIAŁY_SZPITALNE, range(1, len(ODDZIAŁY_SZPITALNE)+1)):
            print(numer_z_listy_oddzialow, oddzial)
        oddzial_nowego_pacjenta = int(input("Wybierz oddzial z listy: "))

        oddzial_nowego_pacjenta_wybrany_z_listy = ODDZIAŁY_SZPITALNE[oddzial_nowego_pacjenta-1]
        print(oddzial_nowego_pacjenta_wybrany_z_listy)

        diagnoza_nowego_pacjenta = input("Podaj diagnoze: ")
        print(diagnoza_nowego_pacjenta)

        profil_nowego_pacjenta= {
            numer_pesel_nowego_pacjenta: {
                "imie": imie_nowego_pacjenta,
                "nazwisko": nazwisko_nowego_pacjenta,
                "numer pesel": numer_pesel_nowego_pacjenta,
                "oddzial": oddzial_nowego_pacjenta_wybrany_z_listy,
                "diagnoza": diagnoza_nowego_pacjenta,
                }
            }

        with open("pacjenci.json", encoding="utf-8", mode="a") as baza_pacjentow_json:
            json.dumps(obj=profil_nowego_pacjenta, fp=baza_pacjentow_json, separators=(',', ':'))
            return False





def SzukaniePacjentaWBazie():
    for element in baza_pacjentow:
        pacjent = baza_pacjentow[element]
        for parametr in pacjent.values():
            if parametr == imie_pacjenta:
                print(f"Znalazłem pacjenta, jego pesel to: {element}")

def LiczbaPacjentowNaOddziale():
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


def main():
    imie_pacjenta = "Katarzyna"
    print(f"Time and date: {datetime.datetime.now().strftime("%d.%m.%Y")}")


    print("MENU")
    print("1. dodawanie pacjenta")
    print("2.edytowanie danych pacjenta")
    print("3.usuwanie danych pacjenta")
    print("4.wyswietlanie danych pacjenta z oddzialow")
    print("5.historia wizyt pacjentow")
    print("6..wyszukaj pacjenta po numer PESEL")
    print("7.statystyka - liczba pacjentow na oddzialach")
    print("8. Wyłacz program")

    while True:
        try:
            wybor_z_menu = int(input("Wybierz numer z listy: "))
            if wybor_z_menu == 1:
                dodawaniePacjenta()
            elif wybor_z_menu == 2:
                pass
            elif wybor_z_menu == 3:
                usuwaniePacjentaZBazy()

            elif wybor_z_menu == 4:
                pass

            elif wybor_z_menu == 5:
                HistoriaWizytPacjenta()

            elif wybor_z_menu == 6:
                SzukaniePacjentaWBazie()

            elif wybor_z_menu == 7:
                LiczbaPacjentowNaOddziale()

            elif wybor_z_menu == 8:
                return False

            else:
                print("wybrales zly numer")
        except ValueError:
            print("To co pdałes nie jest liczba!!! PODAJ LICZBE")



if __name__ == "__main__":
    main()
