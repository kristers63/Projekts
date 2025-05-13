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