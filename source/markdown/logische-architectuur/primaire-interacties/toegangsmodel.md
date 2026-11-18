[AORTA 8.5.2](../../index.md) / [Logische architectuur](../../logische-architectuur.md) / [Primaire interacties](../primaire-interacties.md)

# Toegangsmodel

Het model van toegangsregels is het toegangsmodel. Hiervoor worden enkele aanvullende begrippen geïntroduceerd:

- opt-in van de patiënt;

- behandelrelatie;

- bevoegdheid op grond van BIG-titel van de zorgverlener;

- mandatering;

- vertegenwoordiging;

- samenwerkingsverband.

### Opt-in van de patiënt

De [AVG], [WGBO] en [WABVPZ] van de bieden het wettelijk kader voor het uitwisselen van gegevens in de zorg. Op grond van deze wetgeving geldt voor uitwisseling van medische gegevens onder dat uitdrukkelijke toestemming nodig is van de patiënt voor het beschikbaar stellen van gegevens door een gegevenshouder aan een gegevensraadpleger. Deze toestemmingen worden voor een systeem, dat zijn toestemmingen nog niet naar Mitz heeft gemigreerd, lokaal opgeslagen. Voor een systeem dat zijn toestemmingen wel heeft gemigreerd naar Mitz zijn deze toestemmingen geregistreerd in het (externe) Mitz systeem, dat door AORTA bevraagd wordt.

Hierbij zijn de volgende uitgangspunten gehanteerd:

- De opt-in-vraag is nodig voor het *beschikbaar stellen* van gegevens aan andere zorgaanbieders.

- De opt-in-vraag wordt gesteld door *elke*zorgaanbieder die patiëntgegevens beschikbaar wil stellen.

- Het vooraf vastleggen van de toestemming van de patiënt is bedoeld voor het beschikbaar stellen van patiëntgegevens door gegevenshouders voor opvragen door gegevensraadplegers; de gegevens*houder* kan hierbij namelijk geen toestemming vragen op het moment van opvragen. Bij *sturen van patiëntgegevens*kan per geval toestemming worden gevraagd en is vastlegging van toestemming vooraf niet nodig.

- De zorgaanbieder stelt gegevens van de cliënt slechts beschikbaar via een elektronisch uitwisselingssysteem, voor zover bij het raadplegen van die gegevens door een andere zorgaanbieder, de persoonlijke levenssfeer van een ander dan de cliënt niet wordt geschaad.

### Behandelrelatie

Het bestaan van een behandelrelatie tussen de zorgverlener en de patiënt is een voorwaarde voor toegang van de zorgverlener tot patiëntgegevens.

De volgende zorgaanbieders[^2] of zorgverleners hebben een behandelrelatie volgens de [WGBO]:

- degene die een behandelingsovereenkomst[^3] heeft met de patiënt;

- degene die rechtstreeks betrokken is bij de uitvoering van de behandelingsovereenkomst;

- degene die optreedt als vervanger van degene die een behandelingsovereenkomst heeft met de patiënt.

Bij het opvragen van gegevens moet de zorgverlener die de rol heeft van gegevensraadpleger een behandelrelatie hebben. Bij het verzenden van gegevens geldt dit voor de zorgverlener die de gegevens verstuurt én voor de zorgverlener of zorgaanbieder die de ontvangen gegevens raadpleegt.

### Bevoegdheid op basis van BIG-titel

Zoals vastgelegd in de definitie van het begrip zorgverlener oefent de zorgverlener een beroep uit zoals bedoeld in de wet BIG. Niet alle patiëntgegevens zijn voor iedere zorgverlener relevant. Bij het uitwisselen van patiëntgegevens kunnen daarom gegevens worden afgestemd op het beroep en specialisme[^4] van de betrokken zorgverleners. Het resultaat van deze afstemming wordt vastgelegd in een autorisatie*protocol*en in determinatietabellen.

### Mandatering

Zoals uitgelegd op pagina '[Rollen toekennen aan actoren](https://vzvz.atlassian.net/wiki/x/7oGObg)' kan een zorgverlener patiëntgegevens opvragen bij een zorgaanbieder.

In de praktijk van de zorg komt het regelmatig voor dat een medewerker van de zorgaanbieder onder verantwoordelijkheid van de zorgverlener patiëntgegevens moet opvragen of verzenden. Voorbeelden zijn vervangingssituaties, opleidingssituaties en gevallen waarin medewerkers zonder BIG-titel gegevens moeten opzoeken voor een arts. Hierbij is het mogelijk dat de zorgverlener andere zorgverleners,medewerkers of systemen van de zorgaanbieder *mandateert*om onder zijn verantwoordelijkheid gegevens op te vragen of te verzenden. De zorgverlener die verantwoordelijkheden overdraagt is de *mandaterende*, de andere zorgverleners,medewerkers of systemen zijn de *gemandateerden*. Mandaten gelden binnen de context van de zorgaanbieder waaronder de mandaten zijn verstrekt.

Bij opvragen van gegevens door een gemandateerde moet duidelijk zijn:

- wie de *gemandateerde* is en

- wie de *mandaterende* zorgverlener is onder wiens verantwoordelijkheid de gemandateerde handelt.

De controle van de autorisatie moet hierbij worden toegepast alsof de mandaterende zorgverlener *zelf* de opvraag uitvoert.

### Vertegenwoordiging

Zoals beschreven op pagina '[Rollen toekennen aan actoren](https://vzvz.atlassian.net/wiki/x/7oGObg)' kan een patiënt de eigen patiëntgegevens opvragen bij een zorgaanbieder.

Hierbij moet rekening worden gehouden met enkele uitzonderingen, waarbij:

- *In plaats van* de patiënt een vertegenwoordiger (bijvoorbeeld een ouder) namens de patiënt optreedt;

- *Naast* de patiënt ook een vertegenwoordiger namens de patiënt op*kan* treden.

Zie de tekst van de [WGBO] voor een precieze beschrijving van deze uitzonderingssituaties. Bij de bespreking van de informatiesystemen voor patiënttoegang op pagina '[Goed beheerd patiëntportaal (GBP)](https://vzvz.atlassian.net/wiki/x/5oSObg)' en '[Goed beheerd klantenloketsysteem (GBK)](https://vzvz.atlassian.net/wiki/x/_ISObg)' wordt aangegeven in hoeverre deze uitzonderingen in de architectuur een rol spelen.

### Samenwerkingsverband

Zoals uitgelegd op pagina '[Rollen toekennen aan actoren](https://vzvz.atlassian.net/wiki/x/7oGObg)' kan een zorgverlener patiëntgegevens opvragen bij een zorgaanbieder.

Hierbij moet rekening worden gehouden dat opvragingen gelimiteerd kunnen zijn tot bronsystemen waarmee het opvragende systeem een samenwerkingsverband heeft. Alle samenwerkingsverbanden zijn in het applicatieregister vastgelegd. Bij elke opvraging wordt gecontroleerd of de organisatie, behorend bij het initiërende systeem, voorkomt in een (of één van de) samenwerkingsverband(en) die aan het te bevragen bronsysteem gekoppeld is. Een zorgaanbieder kan in meerdere samenwerkingsverbanden voorkomen of er voor kiezen om zijn patiëntgegevens landelijk beschikbaar te stellen.Voor het sturen van patiëntgegevens wordt niet gekeken naar de samenwerkingsverbanden.

[1] Zie voor een uitgebreide interpretatie van de wettelijke condities de [Zienswijze CBP].

[^2]: De WGBO spreekt eigenlijk over ‘hulpverlener’; de hulpverlener is een natuurlijke of rechtspersoon die een geneeskundig beroep of bedrijf uitoefent. Omdat sprake kan zijn van een natuurlijke of rechtspersoon spelen in AORTA-terminologie zowel de zorgverlener als de zorgaanbieder een rol in de behandelingsovereenkomst. De behandelingsovereenkomst komt van rechtswege tot stand zodra medische handelingen worden verricht of hierover afspraken worden gemaakt, ook als de partijen zich hiervan niet bewust zijn.

[^3]: Zie [WGBO] (artikel 7:446 BW)

[^4]: Hiermee wordt een beroep en specialisme bedoeld uit de officiële lijst van beroepen zoals bedoeld in artikel 3 en 34 van de wet BIG. Een voorbeeld van een beroep is arts, een voorbeeld van een specialisme is huisarts.
