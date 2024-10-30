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
    imie_nowego_pacjenta = input("Podaj imie: ")
    print(imie_nowego_pacjenta)
    nwzwisko_nowego_pacjenta = input("Podaj nazwisko: ")
    print(nwzwisko_nowego_pacjenta)
    numer_pesel_nowego_pacjenta = input("Podaj numer pesel pacjenta: ")
    print(numer_pesel_nowego_pacjenta)
    wiek_nowego_pacjenta = input("Podaj wiek: ")
    print(wiek_nowego_pacjenta)
    oddzial_nowego_pacjenta = input("Podaj oddzial: ")
    print(oddzial_nowego_pacjenta)
    diagnoza_nowego_pacjenta = input("Podaj diagnoze: ")
    print(diagnoza_nowego_pacjenta)




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

    else:
        print("wybrales zly numer")





if __name__ == "__main__":
    main()
