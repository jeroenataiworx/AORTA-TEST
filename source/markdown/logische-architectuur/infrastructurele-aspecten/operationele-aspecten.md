[AORTA 8.5.2](../../index.md) / [Logische architectuur](../../logische-architectuur.md) / [Infrastructurele aspecten](../infrastructurele-aspecten.md)

# Operationele aspecten

### 14.2.1 Beschikbaarheid

Zorgverleners kunnen idealiter 7 dagen per week en 24 uur per dag patiënt­gegevens opvragen en versturen. Dit geldt ook voor patiënttoegang via een GBP. Dit stelt hoge eisen aan verschillende platformen in de basis­infrastructuur, waaronder de aangesloten GBZ’en en DCN’en. Immers, als één GBZ patiëntgegevens opvraagt die verspreid liggen bij andere GBZ’en, moeten deze ook beschikbaar en bereikbaar zijn.

Beschikbaarheid wordt in het algemeen uitgedrukt in percentages van de totale mogelijke beschikbaarheid, waarbij geplande niet-beschikbaarheid wegens onderhoud niet wordt meegerekend. Voor onderhoud worden in het algemeen vaste tijdsintervallen ingesteld. In een keten van systemen is de totale beschikbaarheid het product van de beschikbaarheidspercentages van de individuele componenten.

In het geval van AORTA hangt de samenstelling van de keten af van het gebruiksscenario, maar bestaat meestal uit:

- Het initiërend systeem dat een bericht stuurt naar de ZIM;

- het DCN tussen GBx en ZIM;

- de ZIM;

- het DCN tussen ZIM en reagerend systeem of reagerende systemen;

- het reagerend GBZ of register.

Ten aanzien van de individuele componenten in de keten worden eisen gesteld in programma’s van eisen.

Enkele belangrijke maatregelen binnen AORTA ten aanzien van beschikbaarheid zijn:

- het stellen van eisen aan infrastructuur en beheer van aangesloten systemen, netwerken en de centrale infrastructuur en het uitvoeren van controles op de naleving van deze eisen;

- het vastleggen en naleven van afspraken tussen de verschillende systeembeheerpartijen in het kader van de inrichting van operationeel beheer (zie ook [AORTA DAP]);

- het dubbel uitvoeren van de ZIM en het spreiden van de ZIM over twee locaties;

- het verzorgen van een redundante aansluiting tussen DCN en ZIM;

- de aanwezigheid van test- en acceptatieomgevingen van de ZIM, waardoor de aansluiting van nieuwe GBx’en en het installeren van nieuwe software-releases kan worden getest voordat de productieomgeving wordt aangepast.

Voor GBx’en zijn twee statussen gedefinieerd die gerelateerd zijn aan de beschikbaarheid:

- opengesteld;

- geblokkeerd.

Voor de individuele applicaties die zijn geregistreerd onder een GBx zijn vier statussen gedefinieerd die gerelateerd zijn aan de beschikbaarheid. Deze zijn:

- gereed: de applicatie is na een periode van onbeschikbaarheid (toestand ‘onderhoud’ of ‘storing’) gereed om weer actief te worden;

- actief: de applicatie is in staat tot berichtuitwisseling;

- storing: de applicatie is ongepland niet beschikbaar;

- onderhoud: de applicatie is gepland niet beschikbaar.

De actuele beschikbaarheidstoestand van elk GBx en applicatie onder een GBx wordt centraal in het applicatieregister van de ZIM geregistreerd. De beheerder van het GBx dient de beheerder van de ZIM te informeren over de actuele status. De ZIM kent dezelfde vier statussen als een applicatie: gereed, actief, storing en onderhoud. De beheerder van de ZIM informeert de beheerders van informatiesystemen over de actuele status.

### 14.2.2 Capaciteit en schaalbaarheid

Om te komen tot een schatting van de vereiste capaciteit voor de AORTA infrastructuur is een schatting gemaakt van de aantallen te verwachten gebruikersinteracties voor de zorgtoepassingen ‘medicatieproces’ en ‘huisartswaarneemgegevens’. Dergelijke schattingen zijn vertaald naar ‘service level agreements’ met de leverancier van de ZIM.

Aan de leverancier van de ZIM en beheerders van aangesloten DCN’en en GBx’en worden eisen gesteld ten aanzien van de schaalbaarheid van de systemen. De schaalbaarheid van een systeem is de mate waarin het systeem is voorbereid op toename van het gebruik zonder merkbare verslechtering van het functioneren van het systeem.

### 14.2.3 Responstijden

Net als bij het onderwerp beschikbaarheid geldt dat de snelheid van AORTA als geheel afhangt van de snelheid van de componenten in de keten. Ten aanzien van de gemiddelde responstijden van AORTA zijn gebruikerswensen geïnventariseerd en zijn streefgetallen vastgesteld. Gewenste responstijden worden vastgelegd in programma’s van eisen.
