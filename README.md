# Projekts par Tulkošanu automātizāciju dažadas valodas
### Uzdevumu apraksts
1. Angļu valoda kursā, mums bija uzdevums izveidot un papildnāt  vārdnīcu visa semestrā laikā, kurā jābūt tilkojūmi vairākas valodas (vismaz 2). Tāpēc mans uzdevums ir automātizēt šo processu. Man ir dots Execel fails "Words", kur sheetā "Sheet1" atrodas angļu valodā vārdi. Mans uzdevums ir tājā pašā faila, bet sheetā "result" izveidot vārdnīcu, kurā būs tris koloni ar pārtulkotiem vārdiem un ar tris vīrsrakstiem "English", "Latvian", "Russian". Angļu vārdi būs sakārtoti alfabēta secība
2.  Python bibliotēkas
    * **pandas** - tiek izmantots, lai nolasītu datus no Excel faila un saglabātu tos sarakstā.
    * **openpyxl** - izmanto, lai ielasītu un pēc tam saglabātu datus Excel failos. Ar to tiek izveidots darba loks un tā saglabāšana.
    * **Font un Alignment** - tiek izmantoti, lai piešķirtu formatējumu teksta rindām un kolonnām Excel failā.
    * **webdriver** - ļauj automatizēt tīmekļa pārlūka darbības un kontrolēt tīmekļa pārlūka procesu no Python koda.
    * **By** - nodrošina konstantes un metodes, lai identificētu HTML elementus pēc dažādiem atribūtiem vai kritērijiem
    * **WebDriverWait** - tiek izmantota, lai veiktu gaidīšanu (waiting) tīmekļa lapā, līdz tiek izpildīti noteikti nosacījumi vai notikumi
    * **EC** -  tiek izmantots projekta izstrādes laikā, lai piekļūtu "gaidāmām situācijām" (expected conditions)
    * **Service** - Šī bibliotēka piedāvā iespēju norādīt specifiskas iestatījumus un konfigurācijas, kas attiecas uz Chrome pārlūku
    * **Time** - tiek izmantota, lai iegūtu kontroli pār laiku un veiktu aizkaves (delays) Python kodā
 
3.  
  
