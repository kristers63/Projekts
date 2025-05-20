import pandas as pd

df = pd.read_excel("Treninu_grafiks_2025_latviski.xlsx")

def meklēt_pēc_datuma(datums_str):
    try:
        df_filtrs = df[df["Datums"] == datums_str]
        if df_filtrs.empty:
            print("Šajā datumā treniņš nav ieplānots.")
        else:
            print(df_filtrs.to_string(index=False))
    except Exception as e:
        print("Kļūda:", e)

def filtrēt_un_saglabāt(kolone, vērtība):
    df_filtrs = df[df[kolone].str.lower() == vērtība.lower()]
    if df_filtrs.empty:
        print(f"Nav atrasts neviens treniņš ar: {kolone} = {vērtība}")
    else:
        fails = f"Treniņi_filtrēti_{kolone}_{vērtība}.xlsx".replace(" ", "_")
        df_filtrs.to_excel(fails, index=False)
        print(f"Rezultāts saglabāts: {fails}")

while True:
    print("\n--- Treniņu grafika meklēšana ---")
    print("Spiest 1, lai meklētu treniņu pēc datuma (DD.MM.YYYY)")
    print("Spiest 2, lai filtrētu treniņus pēc nedēļas dienas")
    print("Spiest 3, lai filtrētu treniņus pēc vietas")
    print("Spiest 4, lai filtrētu treniņus pēc laika")
    print("Spiest 0, lai izietu no programmas")
    izvēle = input("Tava izvēle: ")

    if izvēle == "1":
        datums = input("Ievadi datumu (DD.MM.YYYY): ")
        meklēt_pēc_datuma(datums)
    elif izvēle == "2":
        diena = input("Ievadi dienu (piemēram, Pirmdiena): ")
        filtrēt_un_saglabāt("Diena", diena)
    elif izvēle == "3":
        vieta = input("Ievadi vietu (piemēram, Zāle): ")
        filtrēt_un_saglabāt("Vieta", vieta)
    elif izvēle == "4":
        laiks = input("Ievadi laiku (piemēram, 18:00): ")
        filtrēt_un_saglabāt("Laiks", laiks)
    elif izvēle == "0":
        print("Programma beidzas. Visu labu!")
        break
    else:
        print("Nederīga izvēle.")        
