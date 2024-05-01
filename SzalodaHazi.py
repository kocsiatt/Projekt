import datetime


class Szoba:
    """Az alap atrributumokat tartalmazza a szobáról: ár, szobaszám."""

    ar = 0

    szobaszam = 0


class EgyagyasSzoba(Szoba):
    """Egyágyas szoba, mely a szoba osztály leszármazottja."""

    tengerreNezo = False

    def __init__(self, szobaszamEgyagyas, tengerreNezo):

        """A szoba számot és az extra igényt kéri, és így határozza meg az árat."""

        self.szobaszam = szobaszamEgyagyas

        self.tengerreNezo = tengerreNezo

        if tengerreNezo == True:

            self.ar = 6000

        else:

            self.ar = 5000


class KetagyasSzoba(Szoba):
    """Kétágyas szoba, mely a szoba osztály leszármazottja."""

    lakosztaly = False

    def __init__(self, szobaszamKetagyas, lakosztaly):

        """A szoba számot és az extra igényt kéri, és így határozza meg az árat."""

        self.szobaszam = szobaszamKetagyas

        self.lakosztaly = lakosztaly

        if lakosztaly == True:

            self.ar = 10000

        else:

            self.ar = 8000


class Szaloda():
    """A szobákat és a foglalásokat tárolja"""

    nev = ""

    szobak = []

    foglalasok = []

    def __init__(self, nev):
        """A száloda nevét kéri"""

        self.nev = nev


class Foglalas:
    """Elmenti a létrehozás dátumát, és foglalásokat rögzít."""

    foglalsEv = datetime.datetime.now().year

    foglalasHonap = datetime.datetime.now().month

    foglalasNap = datetime.datetime.now().day

    def __init__(self, ev, honap, nap, szoba, extra):
        """Be kéri az évet, hónapot, napot, szobaszámot és elmenti"""

        self.lefoglaltEv = ev

        self.lefoglaltHonap = honap

        self.lefoglaltNap = nap

        self.szoba = szoba

        self.extra = extra


def szobaFoglalas(ev, honap, nap, szobaszam, extra, szaloda):
    """A szobák foglalását végzi el és visszatér az árával."""

    tempExtra = False

    if extra == 1:
        tempExtra = True

    foglalas = Foglalas(ev, honap, nap, szobaszam, tempExtra)

    szaloda.foglalasok.append(foglalas)

    for i in szaloda.szobak:

        if i.szobaszam == szobaszam:


            if type(i) == EgyagyasSzoba:
                print(f"\nA foglalás megtörtént! Az ár: {EgyagyasSzoba(szobaszam, tempExtra).ar} Ft")

            if type(i) == KetagyasSzoba:
                print(f"\nA foglalás megtörtént! Az ár: {KetagyasSzoba(szobaszam, tempExtra).ar} Ft")


def foglalasLemondas(ev, honap, nap, szobaszam, szaloda):
    """A beírt szobaszámot a megadott dátumban törli a foglalás listából!"""

    for i in range(len(szaloda.foglalasok)):

        if szaloda.foglalasok[i].szoba == szobaszam:

            if szaloda.foglalasok[i].lefoglaltEv == ev and szaloda.foglalasok[i].lefoglaltHonap == honap and szaloda.foglalasok[i].lefoglaltNap == nap:

                del szaloda.foglalasok[i]

                return 1



    return 0




def foglalasokListazasa(szaloda):
    """Kilistázza a foglalásokat."""

    print(f"A {szaloda.nev} szálodában a következő foglalások vannak:\n")

    for i in szaloda.foglalasok:
        print(
            f"Szoba: {i.szoba}, extrák: {i.extra}, Foglalás dátuma: {i.lefoglaltEv}.{i.lefoglaltHonap}.{i.lefoglaltNap}, Létrehozás dátuma: {i.foglalsEv}.{i.foglalasHonap}.{i.foglalasNap}")


def lehetosegekFoglalas(szaloda):
    """A felhasználó foglalását vezeti végig. Figyeli, hogy létezik e olyan szoba, amit le akar foglalni."""

    print("\nKérem adja meg a foglalás dátumát! Először az évet, utána a hónapot és végül a napot szám formátumban!\n")

    evFoglalas = 0
    honapFoglalas = 0
    napFoglalas = 0
    szobaszamFoglalas = 0

    tempWhile = True

    while tempWhile:

        napJoDatum = False

        try:

            evFoglalas = int(input("Kérem adja meg az évet! pl: 2024: "))
            honapFoglalas = int(input("Kérem adja meg a hónapot! pl: 7: "))
            napFoglalas = int(input("Kérem adja meg a napot! pl: 9: "))

            tempIdo = datetime.datetime.now()

            if honapFoglalas == 1:

                if napFoglalas > 31:

                    print("A január csak 31 napos!")

                else:

                    napJoDatum = True

            elif honapFoglalas == 2:

                if napFoglalas > 28:

                    print("A február csak 28 napos!")

                else:

                    napJoDatum = True

            elif honapFoglalas == 3:

                if napFoglalas > 31:
                    print("A március csak 31 napos!")

                else:

                    napJoDatum = True

            elif honapFoglalas == 4:

                if napFoglalas > 30:
                    print("Az április csak 30 napos!")

                else:

                    napJoDatum = True

            elif honapFoglalas == 5:

                if napFoglalas > 31:
                    print("A május csak 31 napos!")

                else:

                    napJoDatum = True

            elif honapFoglalas == 6:

                if napFoglalas > 30:
                    print("A június csak 30 napos!")

                else:

                    napJoDatum = True

            elif honapFoglalas == 7:

                if napFoglalas > 31:
                    print("A július csak 31 napos!")

                else:

                    napJoDatum = True

            elif honapFoglalas == 8:

                if napFoglalas > 31:
                    print("Az augusztus csak 31 napos!")

                else:

                    napJoDatum = True

            elif honapFoglalas == 9:

                if napFoglalas > 30:
                    print("A szeptember csak 30 napos!")

                else:

                    napJoDatum = True

            elif honapFoglalas == 10:

                if napFoglalas > 31:
                    print("A február csak 31 napos!")

                else:

                    napJoDatum = True

            elif honapFoglalas == 11:

                if napFoglalas > 30:
                    print("A november csak 30 napos!")

                else:

                    napJoDatum = True

            elif honapFoglalas == 12:

                if napFoglalas > 31:
                    print("A december csak 31 napos!")

                else:

                    napJoDatum = True

            if napJoDatum == True and honapFoglalas <= 12:

                if evFoglalas > tempIdo.year:

                    tempWhile = False


                elif evFoglalas == tempIdo.year:

                    if honapFoglalas > tempIdo.month:

                        tempWhile = False


                    elif honapFoglalas == tempIdo.month:

                        if napFoglalas > tempIdo.day:
                            tempWhile = False

                        else:

                            print("\nCsak a holnapi naptól lehet foglalni!\n")

                    else:

                        print("\nCsak a holnapi naptól lehet foglalni!\n")



            else:

                print("\nCsak a holnapi naptól lehet foglalni!\n")





        except:

            print("Kérem csak egész számokat írjon be!")

    tempWhile = True

    while tempWhile:

        try:
            szobaszamFoglalas = int(input(f"\nKérem adja meg a szoba számát {100 + len(szaloda.szobak) - (len(szaloda.szobak) - 1)} - {100 + len(szaloda.szobak)} : "))

            tempSzobaszam = False

            for i in szaloda.szobak:

                if szobaszamFoglalas == i.szobaszam:
                    tempSzobaszam = True

            if tempSzobaszam:

                tempWhile = False

            else:

                print("\nCsak a megadott szobák közül választhat!\n")



        except:

            print("\nKérem csak a szoba számát írja be!\n")

    tempWhile = True

    while tempWhile:

        try:

            extraFoglalas = int(input("\nKérem, ha kér extrát, akkor egy '1'-est írjon, ha nem, akkor '0'-át: "))

            if extraFoglalas == 1 or extraFoglalas == 0:

                tempWhile = False

                szobaFoglalas(evFoglalas, honapFoglalas, napFoglalas, szobaszamFoglalas, extraFoglalas, szaloda)


            else:

                print("\nKérem csak '1'-et, vagy '0-át írjon be!\n")


        except:
            print("ohh")
            print("\nKérem csak '1'-et, vagy '0-át írjon be!\n")


def lehetosegekLemondas(szaloda):
    """A felhasználó lemondását vezeti végig. Figyeli, hogy van e olyan foglalás, amit le akar mondani."""

    print("\nKérem adja meg a lemondás dátumát! Először az évet, utána a hónapot és végül a napot szám formátumban!\n")

    tempWhile = True

    evLemondas = 0
    honapLemondas = 0
    napLemondas = 0

    while tempWhile:

        try:

            evLemondas = int(input("Kérem adja meg az évet! pl: 2024: "))
            honapLemondas = int(input("Kérem adja meg a hónapot! pl: 7: "))
            napLemondas = int(input("Kérem adja meg a napot! pl: 9: "))

            tempWhile = False

        except:

            print("Kérem csak egész számokat írjon be!")

    tempWhile = True

    while tempWhile:

        try:
            szobaszamLemondas = int(input(
                f"\nKérem adja meg a szoba számát {100 + len(szaloda.szobak) - (len(szaloda.szobak) - 1)} - {100 + len(szaloda.szobak)} : "))

            tempSzobaszam = False

            for i in szaloda.szobak:

                if szobaszamLemondas == i.szobaszam:
                    tempSzobaszam = True

            if tempSzobaszam:

                tempWhile = False

                if foglalasLemondas(evLemondas, honapLemondas, napLemondas, szobaszamLemondas, szaloda) == 1:

                    print("\n A lemondást rögzítettük")

                else:

                    print("Nem volt szoba foglalva a megadott paraméterekre. Kérem próbálja meg újra!")

            else:

                print("\nCsak a megadott szobák közül választhat!\n")



        except:

            print("\nKérem csak a szoba számát írja be!\n")


# Száloda feltöltése!

szaloda = Szaloda("Hilton")

szoba = EgyagyasSzoba(101, False)

szaloda.szobak.append(szoba)

szoba = EgyagyasSzoba(102, True)

szaloda.szobak.append(szoba)

szoba = KetagyasSzoba(103, False)

szaloda.szobak.append(szoba)

foglalas = Foglalas(2024, 10, 18, 101, False)

szaloda.foglalasok.append(foglalas)

foglalas = Foglalas(2024, 11, 14, 102, True)

szaloda.foglalasok.append(foglalas)

foglalas = Foglalas(2024, 12, 21, 103, False)

szaloda.foglalasok.append(foglalas)

foglalas = Foglalas(2024, 6, 11, 101, True)

szaloda.foglalasok.append(foglalas)

foglalas = Foglalas(2024, 12, 30, 102, False)

szaloda.foglalasok.append(foglalas)

folyamat = True

print(f"Üdvözöljük a {szaloda.nev} szálodában!\n")

while folyamat:

    print("\nAz alábbi lehetődégek közül választhat:\n"
          "Foglalás = 'F'\n"
          "Lemondás = 'N'\n"
          "Listázás = 'I'\n"
          "Kilépés = 'K'\n")

    lehetoseg = input("Kérem írja be a kívánt lehetőséghez tartozó betűt, és nyomjon entert!: ")

    if lehetoseg == "k" or lehetoseg == "K":

        folyamat = False

    elif lehetoseg == "f" or lehetoseg == "F":

        lehetosegekFoglalas(szaloda)


    elif lehetoseg == "n" or lehetoseg == "N":

        lehetosegekLemondas(szaloda)

    elif lehetoseg == "i" or lehetoseg == "I":

        foglalasokListazasa(szaloda)
