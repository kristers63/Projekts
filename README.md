
# Projekts "Treniņu grafika automatizācijas sistēma"

**Projekta autors:** Kristers Ģērmanis 14.grupa

**Apliecības nr.:** 241RDB156

---

## 📌 Projekta tēmas izvēle un tās pamatojums

Šis projekts tika izstrādāts, lai vieglāk noskaidrotu treniņa laikus un pārvietotos treniņu grafikā. Sistēma ļauj viegli meklēt un filtrēt treniņus pēc dažādiem parametriem, kā  datuma, dienas, vietas un laika. Es trenējos pludmales volejbolā, un senāk bija tabulā apkopots nodarbību grafiks, kur bija teikti datumi un vietas, kur notiks treniņi, tapēc es iespaidojos no savas personīgās pieredzes, un uzstaisīju sistēmu, kas spēj tikt galā ar dažādiem meklēšanas un filtrēšanas uzdevumiem, kas ļauj lietotājam orientēties tabulā, un vieglāk noskaidrot, kādās dienās paredzēts treniņš, kādā laikā, kurā vietā un kādā datumā. Šī programma arī palīdzēs lietotājiem ātri atrast un saglabāt filtrētos rezultātus Excel tabulā, kuru pēc tam var izmanot ikdienā. 

---

## 📚 Izmantotās Python bibliotēkas

Projektā tiek izmantotas šādas Python bibliotēkas:

| Bibliotēka    | Izmantošana, un pamatojums |
|---------------|----------------------------|
| `pandas`      | Tiek izmantota datu apstrādei un analīzei, īpaši Excel failu lasīšanai un rakstīšanai. Šī bibliotēka palīdz viegli strādāt ar datu tabulām un veikt dažādas filtrēšanas funckijas ērti un viegli. Pandas iekšēji izmanto openpyxl, kuru atsevišķi kā bibliotēku nenorādīšu.|

Lai instalētu nepieciešamo bibliotēku, terminālī jāieraksta: 'pip install pandas'

---

## 🧠 Izmantotās datu struktūras

Es izmantoju paši definētu datu struktūru – klasi ```Trenins``` un ```TreninuGrafiks``` . Šīs klases strukturē datus par treniņu

Katram treniņam tiek saglabāti četri lauki:
+ datums – treniņa norises datums;
+ diena – nedēļas diena; 
+ laiks – treniņa sākuma laiks; 
+ vieta – treniņa norises vieta. 


---
## 🕜 Koda efektivitāte(Laika sarežģītība)


Noskaidrosim galvano funckiju laika sarežģītību:

### Meklēšana pēc datuma
```python
[t for t in self.trenini if t.datums == datums_str]
```
– šeit tiek veikta pilna saraksta pārbaude, tāpēc laika sarežģītība ir **O(n)**.

### Filtrēšana dienas, vietas, laika
```python
[t for t in self.trenini if getattr(t, cell).lower() == vērtība]
```
– šeit notiek pilna saraksta pārbaude arī, tapēc ir **O(n)** laika sarežģītība.

### Excel faila saglabāšana
```python
df.to_excel(fails, index=False)
```
– rakstīšana excel failā aizņem **O(n)** laiku.

Visas funkcijas darbojas ātri un efektīvi, un kodā lielākā laika sarežģītiba ir **O(n)**. 

---

## 💻 Programmatūras izmantošana

Lietotājs ar šo programmu darbību uzsāk, ievadot atbilstošo numuru.Pēc tam atbilstoši pēc izvēlētā numura, tiek palaista atbilstošā funckija. Tālāk ievadot prasīto informāciju, tiek izveidota .xlsx tabula, kura satur filtrētus datus par treniņiem, atkarībā no tā, kādus datus lietotājs bija ievadījis.

### 1. 📅 Meklēšana pēc datuma

>Lietotājs ievada datumu: '15.05.2025'

meklet_pec_datuma('15.05.2025')


### 2. 📆 Filtrēšana pēc nedēļas dienas


> Lietotājs ievada dienu: 'Trešdiena'

filtrets_pec_dienas('Trešdiena')

### 3. 📍 Filtrēšana pēc vietas


> Lietotājs ievada vietu: 'Zāle'

filtrets_pec_vietas('Zāle')


### 4. ⏰ Filtrēšana pēc laika

> Lietotājs ievada laiku: '18:30'

filtrets_pec_laika('18:30')

---

##  Nobeigums

Šo projektu izstrādāju, lai uzlabotu treniņu grafika pārskatāmību un lietošanas ērtumu, īpaši priekš sportistiem, kuri regulāri plāno savus treniņus. Mana sistēma ļauj atrast nepieciešamo informāciju par treniņiem ļoti ātri, kā arī saglabāt informaciju par treniņiem atbilstoši prasībām, lai laikus varētu sagatavoties, un man kā sportistam šis liekas ļoti noderīgi, un manuprāt šī sistēma būtu ļoti noderīga profesionāliem sportistiem, kuriem ir spēļu grafiki, un nedēļā vairākas reizēs ir mači un treniņi, tapēc šī sistēma viņiem būtu ideāla.
