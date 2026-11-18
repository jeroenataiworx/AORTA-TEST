[AORTA 8.5.2](../../index.md) / [Logische architectuur](../../logische-architectuur.md) / [Inleiding en context](../inleiding-en-context.md)

# Achtergrond

Zorgverleners in Nederland zijn op grond van de [[WGBO](https://vzvz.atlassian.net/wiki/x/pICObg)] verplicht tot het inrichten van een dossier waarin alle gegevens omtrent de behandeling en de gezondheid van de patiënt worden opgenomen. Zorgverleners maken hiertoe niet alleen gebruik van papieren dossiers, maar ook van verschillende gespecialiseerde informatiesystemen zoals huisartsinformatiesystemen (HIS) en ziekenhuisinformatiesystemen (ZIS).

Vaak worden gegevens over dezelfde patiënt opgenomen in meerdere informatiesystemen, doordat de patiënt behandeld wordt door meerdere zorgverleners, bijvoorbeeld de huisarts, de vervangende huisarts, de apotheker en de medisch specialist. De verschillende behandelaars hebben hierbij niet altijd direct inzicht in elkaars gegevens. Dit kan ertoe leiden dat behandelaars niet beschikken over voor hen relevante informatie over eerdere of gelijktijdige behandelingen of medicatie.

Uitwisseling van patiëntgegevens tussen zorgverleners is in het belang van zowel patiënt als behandelaar. In veel situaties is voor de behandelaar belangrijke informatie namelijk al bij andere zorgverleners aanwezig; inzicht in de actuele medicatiestatus bij huisartswaarneming of in spoedgevallen is een klassiek voorbeeld. Indien deze uitwisseling elektronisch kan plaatsvinden kan dit de snelheid, doelmatigheid en betrouwbaarheid van gegevensuitwisseling bevorderen. Elektronische uitwisseling van gegevens is echter complex om een aantal redenen:

- Er is een grote diversiteit aan bronsystemen waarin patiëntgegevens zijn opgeslagen; om desondanks efficiënt informatie te kunnen uitwisselen is standaardisatie nodig van de wijze waarop gegevensuitwisseling plaatsvindt.

- Zorgverleners weten niet in alle gevallen in welke informatiesystemen van andere zorgverleners gegevens over hun patiënten zijn opgeslagen. Er is dus een mechanisme nodig om relevante bronsystemen te achterhalen.

- Patiënten en zorgverleners moeten erop kunnen vertrouwen dat patiëntgegevens slechts worden geraadpleegd door personen die daartoe bevoegd zijn. Dit stelt speciale eisen aan de informatie-uitwisseling.

Elk initiatief tot informatie-uitwisseling in de zorg wordt geconfronteerd met deze aspecten. Vanuit het oogpunt van doelmatigheid is het zinvol om te komen tot een gezamenlijke aanpak tussen meerdere zorgpartijen, waaronder zorgverleners, koepelorganisaties, patiëntenorganisaties en leveranciers van ICT-systemen, waarbij gedeelde en toekomstvaste oplossingen worden gezocht. AORTA, de infrastructuur voor berichtenuitwisseling in de zorg, is tot stand gekomen in samenwerking met vertegenwoordigers van elk van deze partijen in het zorgveld.

AORTA adresseert de bovengenoemde uitdagingen door een aantal belangrijke uitgangspunten te kiezen ten aanzien van de architectuur:

- De berichtenuitwisseling binnen AORTA maakt gebruik van internationaal en/of nationaal geaccepteerde standaarden, zowel op technisch als medisch inhoudelijk niveau.

- AORTA bevat een verwijsindex waardoor kan worden bijgehouden in welke zorginformatiesystemen patiëntgegevens aanwezig zijn. Een verzoek om gegevens kan hierdoor efficiënt worden gerouteerd, terwijl de gegevens bij de bron blijven, niet onnodig worden gedupliceerd en actueel zijn op het moment van opvragen.

- AORTA is gebaseerd op het [Vertrouwensmodel] waarbinnen gebruikers eenduidig worden geïdentificeerd, geauthenticeerd en geautoriseerd voor gegevensuitwisselingen. Alle uitwisselingen vinden plaats over beveiligde verbindingen tussen geïdentificeerde systemen en worden gelogd. De patiënt kan volledig inzicht krijgen tussen wie en welke gegevens uitgewisseld worden.

- AORTA stelt eisen aan alle bij de informatie-uitwisseling betrokken organisaties en informatiesystemen, zowel op het gebied van techniek als op het gebied van beveiliging en beheer.
