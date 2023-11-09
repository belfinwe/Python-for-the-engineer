# Python for ingeniøren

__2023-11-08__

## Dag 1
Kursleder: `kbotnen` på GitHub.
Ein må ikkje ha fire spaces/tab, gjeng med to space også! omg!1!one!eleven!

### Etter lunsj

Litt meir Python og git.

Tester å endre på nett.

### Siste delen av første dagen

Det som kjem no er ein forsmak på det som kjem i morga, NumPy og Pandas.

`import plotly.express as px # pip install plotly or conda install -c conda-forge plotly` for grafing av dataframe.

Oppgave nederst på sida: https://www.kaggle.com/code/joakimnilsen/notebooke6cf216982/edit
Sikkert ei grei anledning til å teste meir på Notebooks.

__Endex__

## Dag 2

Begynner klokka 09:00 (2023-11-09).

Pandas har moglegheit for å lese Excel-filer. Får då ein dict, der key er namnet på eit sheet i Excel-arket. Typen på valuen til disse dictane er ein Pandas dataframe.

Kan legge til eigne kolonner på dataframen med berekninger, tekst eller kva ein vil.


### Bildebehandlding

Ein pixel har ein verdi frå 0 (svart) til 255 (kvitt).
Skal burde eit bibliotek som heiter OpenCV. Skal være så effektivt at ein kan kunne bruke det til realtime, som video.
Begynte i 1999. OpenSource. Koden skrevet i C++. Fungera på dei fleste OS.

Oss skal prøve å finne eit ansikt i eit bilete. OpenCV har innebygde algortimer for å kjenne igjen ansikter.

__Brukernamnet til foreleseren på Kaggle.com: `adrock2nd`.__

Kan finne kanter, kommer som ei liste med lister med koordinater for kva den har funnet. Antall lister viser antall kanter, eller ansikter, som er funnet.


__Lunsj__

Kan bruke det her direkte på eit kamera. Lurer på om det var ~~Pandas~~ OpenCV som koblast direkte på kameraet?
Må nok testes lokalt på maskina, sidan scriptet trenger tilgong til kameraet.

Sliter ein del med å få den webcamera-tingen til å fungere, mest med å få innstallert ting på venv på Windows. Naboen (-->) fekk det til.

Pakker Python-filane med `pyinstaller <filnavn>.py`. Filane det blir lagt i ligger i `.gitignore`.
