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
        