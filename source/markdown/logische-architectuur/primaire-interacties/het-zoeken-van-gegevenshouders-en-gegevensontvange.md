[AORTA 8.5.2](../../index.md) / [Logische architectuur](../../logische-architectuur.md) / [Primaire interacties](../primaire-interacties.md)

# Het zoeken van gegevenshouders en gegevensontvangers

Bij het opvragen van patiëntgegevens door een gegevensraadpleger kan er sprake zijn van meerdere gegevenshouders en hoeven de gegevenshouders in de praktijk niet bekend te zijn bij de gegevensraadpleger.

AORTA adresseert dit probleem door het introduceren van een intermediair, het Landelijk Schakelpunt (LSP).

Het Landelijk Schakelpunt is een intermediaire organisatie die diensten verleend aan zorgaanbieders die zorginformatie willen uitwisselen en waarbij de gegevenshouders de beschikbaarheid van gegevens over patiënten kunnen aanmelden.

Door het aanmelden worden deze locatie gegevens opgenomen in een Verwijsindex.

De Verwijsindex (VWI) is een register waarin vastligt welke gegevenshouders over patiëntgegevens van specifieke patiënten beschikken.

Vervolgens kunnen gegevensraadplegers via de intermediair de beschikbare gegevens opvragen, zonder dat de gegevensraadpleger elke gegevenshouder afzonderlijk hoeft te benaderen.

Overigens is voor het aanmelden van gegevens bij de verwijsindex het verkrijgen van toestemming vooraf van de patiënt (opt-in) vereist.

De gegevensraadplegers en de gegevenshouders maken bij dit mechanisme één set van afspraken met de intermediair over uitwisselingsformaten, beveiligingsaspecten en dergelijke.

De voordelen van deze oplossing zijn:

- Gegevenshouders en gegevensraadplegers hoeven elkaar niet te kennen; het bijhouden van gegevenslocaties en het verzamelen van gegevens afkomstig van verschillende locaties wordt door de intermediair voor de gegevensraadpleger opgelost;

- Alleen gegevenshouders die over informatie beschikken worden om informatie gevraagd;

- Gegevenshouders en gegevensraadplegers hoeven slechts één set van afspraken te maken over de randvoorwaarden van gegevensuitwisseling.

Indien een gegevensraadpleger een specifieke gegevenshouder(s) wil bevragen, dan wordt de VWI niet geraadpleegd. Als dit systeem gemigreerd is naar Mitz, wordt Mitz wel bevraagd met een **gesloten** vraag [[MITZ-IHOG](../../referenties.md#IHOG)] om te kijken of er toestemming gegeven is voor het bevragen van dit systeem.

Om te kunnen bepalen aan welke gegevensbronnen toestemming is verleend door de patiënt voor opvraging, wordt er eerst een **open** vraag uitgezet bij Mitz. Hiermee worden alle systemen gevonden die de patiënttoestemmingen gemigreerd hebben naar Mitz. De systemen die nog niet gemigreerd zijn worden gevonden door de VWI te bevragen.

Bij het versturen van gegevens is het minder waarschijnlijk dat de gegevenszender de gegevensontvanger niet kent, maar er doen zich wel soortgelijke vraagstukken voor:

- De manier waarop verschillende gegevensontvangers kunnen worden geadresseerd kan verschillen.

- Er moeten ook in dit geval afspraken worden gemaakt over diverse technische aspecten van de uitwisseling.

Door ook bij het verzenden van gegevens gebruik te maken van het LSP als intermediair, kunnen de wijze van adressering en de technische aspecten van gegevensuitwisseling worden gestandaardiseerd.

Daarnaast biedt een adresboek een mogelijkheid om identificerende zorgaanbieder- en zorgverlener gegevens op te zoeken met de bijbehorende (technische) adressering. Hiervoor is aangesloten op ZORG-AB, is een database waarin diverse zorgaanbiedersgegevens en zorgverlenersgegevens zijn opgeslagen en raadpleegbaar worden gemaakt voor derden.

Bij de bespreking van de informatiesysteem aspecten van de architectuur (vanaf hoofdstuk 6) worden de concepten van gegevensuitwisseling via een intermediair en verwijsindex verder uitgewerkt.
