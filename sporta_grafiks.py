import pandas as pd

class Trenins:
    def __init__(self, datums, diena, laiks, vieta):
        self.datums = datums
        self.diena = diena
        self.laiks = laiks
        self.vieta = vieta

class TreninuGrafiks:
    def __init__(self, fails):
        df = pd.read_excel(fails)
        self.trenini = [
            Trenins(r["Datums"], r["Diena"], r["Laiks"], r["Vieta"])
            for _, r in df.iterrows()
        ]

    def meklēt_pēc_datuma(self, datums_str):
        found = [t for t in self.trenini if t.datums == datums_str]
        if not found:
            print("Šajā datumā nav treniņš")
        else:
            for t in found:
                print(f"{t.datums} | {t.diena} | {t.laiks} | {t.vieta}")

    def filtrēt_un_saglabāt(self, cell, vērtība):
        vērtība = vērtība.lower()
        found = [
            t for t in self.trenini if getattr(t, cell).lower() == vērtība
        ]
        if not found:
            print(f"Nav atrasts neviens treniņš ar: {cell} = {vērtība}")
        else:
            df = pd.DataFrame([vars(t) for t in found])
            fails = f"Treniņu_grafiks_filtrēts_{vērtība}.xlsx".replace(" ", "_")
            df.to_excel(fails, index=False)
            print(f"Rezultāts saglabāts failā: {fails}")

grafiks = TreninuGrafiks("Treninu_grafiks2025.xlsx")

while True:
    print("\n---- Treniņu grafika meklēšana tabulā ----")
    print("Spiest 1, lai meklētu treniņu pēc datuma (DD.MM.YYYY)")
    print("Spiest 2, lai filtrētu treniņus pēc nedēļas dienas")
    print("Spiest 3, lai filtrētu treniņus pēc vietas")
    print("Spiest 4, lai filtrētu treniņus pēc laika")
    print("Spiest 0, lai izietu")
    izvēle = input("Tava izvēle: ")

    if izvēle == "1":
        datums = input("Ievadi datumu (DD.MM.YYYY): ")
        grafiks.meklēt_pēc_datuma(datums)
    elif izvēle == "2":
        diena = input("Ievadi dienu (piemēram, Ceturtdiena): ")
        grafiks.filtrēt_un_saglabāt("diena", diena)
    elif izvēle == "3":
        vieta = input("Ievadi vietu (piemēram, Halle): ")
        grafiks.filtrēt_un_saglabāt("vieta", vieta)
    elif izvēle == "4":
        laiks = input("Ievadi laiku (piemēram, 17:00): ")
        grafiks.filtrēt_un_saglabāt("laiks", laiks)
    elif izvēle == "0":
        print("Programmas beigas. Visu labu!")
        break
    else:
        print("Nepareiza komanda")