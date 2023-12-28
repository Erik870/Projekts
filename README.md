# Projekts par Tulkošanu automātizāciju dažadas valodas
### Uzdevuma apraksts
1. **Uzdevumu apraksts**
   Angļu valodas kursā mums bija uzdevums izveidot un papildnāt vārdnīcu visa semestrā garumā, kurā jābūt tulkojumi vairākās valodās (vismaz 2). Tāpēc mans uzdevums ir automātizēt šo procesu. Man ir dots Execel fails "Words", kur lapā "Sheet1" atrodas vārdi angļu valodā. Mans uzdevums ir tājā pašā failā, bet lapā "result" izveidot vārdnīcu, kurā būs trīs kolonnas ar pārtulkotiem vārdiem un ar trīs vīrsrakstiem "English", "Latvian", "Russian". Angļu vārdi būs sakārtoti alfabēta secībā.
2.  **Python bibliotēkas**
    * **pandas** - tiek izmantots, lai nolasītu datus no Excel faila un saglabātu tos sarakstā.
    * **openpyxl** - izmanto, lai ielasītu un pēc tam saglabātu datus Excel failos. Ar to tiek izveidots darba loks un tā saglabāšana.
    * **Font un Alignment** - tiek izmantoti, lai piešķirtu formatējumu teksta rindām un kolonnām Excel failā.
    * **webdriver** - ļauj automatizēt tīmekļa pārlūka darbības un kontrolēt tīmekļa pārlūka procesu no Python koda.
    * **By** - nodrošina konstantes un metodes, lai identificētu HTML elementus pēc dažādiem atribūtiem vai kritērijiem
    * **WebDriverWait** - tiek izmantota, lai veiktu gaidīšanu (waiting) tīmekļa lapā, līdz tiek izpildīti noteikti nosacījumi vai notikumi
    * **EC** -  tiek izmantots projekta izstrādes laikā, lai piekļūtu "gaidāmām situācijām" (expected conditions)
    * **Service** - Šī bibliotēka piedāvā iespēju norādīt specifiskas iestatījumus un konfigurācijas, kas attiecas uz Chrome pārlūku
    * **Time** - tiek izmantota, lai iegūtu kontroli pār laiku un veiktu aizkaves (delays) Python kodā
 
3. **Programmatūras izmantošanas metodes.** Dots Excel fails ar lapām: "result" un "Sheet1". "Sheet1" atrodas vārdi angļu valodā, nejaušā sēcībā, palaižot programmu: **"result.py"** notiek šādi procesi:
   1. Programma nolasa visus vārdus no lapas: "Sheet1", ievieto un sakārto alfabēta secībā angļu valodas vārdus masīvā: **"words"**
   2. Izmantojot "for ciklus", tiek veidots algoritms, kurš paņem katru vārdu no masīva: **"words"**, pārtulko tos un ievieto tos jaunos māsīvos: **"Translations","Translations_2"**
   3. Excel failā, jau izvedota no sakumā lapā: "result", programma veido un formātē  trīs virsrakstus: "English", "Latvian", "Russian"
   4. Izmantojot "for ciklus", lapā "result" tiek ievietoti vārdi no masīviem: **"words", "Translations", "Translations_2"**
      
## P.S.
Lai iedarbinātu programmu, ir nepieciešāms lējupielādēt repozitorīju, un palaist kompilātorā. Programma kopumā apstrādā un tulko datus 15 min. Tiek izmantots "Yandex" tulkotājs, jo ar citiem tulkošānas rīkiem, kā "Deepl.com" un "GoogleTranslate.com" bija vairākas problēmas, tādas kā: automatīskā HTML "id" elementu nejauša mainība tīmeklī, ka arī dažādas problēmas ar sertifikātu valīdāciju, kas neļava ņemt pārtulkotus vārdus un saglabāt masīvā. Arī šo iemēslu dēļ netiek realizēta vārdu definīcijas idēja. Darbu izpildīja **Ēriks Baumanis 231RDC032**  
