[AORTA 8.5.2](../../index.md) / [Logische architectuur](../../logische-architectuur.md) / [Berichtafhandeling](../berichtafhandeling.md)

# Foutafhandeling

In de berichtafhandeling zoals beschreven in '[Berichtafhandeling door de ZIM](berichtafhandeling-door-de-zim.md)' is aangegeven dat op meerdere momenten in de berichtafhandeling fouten kunnen optreden. Een fout is een gebeurtenis die afwijkt van de verwachte of gewenste wijze van afhandeling van het bericht. Dergelijke fouten worden zoveel mogelijk teruggemeld aan het initiërend systeem.

Indien een bericht de ZIM bereikt (zie diagram AORTA.ZIM.d1050.2), kan een fout plaatsvinden tijdens de berichtvalidatie, de controle van het applicatieregister, de authenticatie of de autorisatie. Deze fouten gaan vooraf aan de inhoudelijke afhandeling van het bericht en leiden tot het staken van de verdere berichtafhandeling. De fout wordt opgenomen in een systeemlog en het initiërend systeem ontvangt een foutmelding, zo mogelijk op HL7v3 niveau.

Indien de ZIM overgaat tot inhoudelijke afhandeling van het bericht, zijn voor de meeste berichten interacties nodig met reagerende systemen (zie diagram AORTA.ZIM.d1060).

Interacties met meerdere reagerende systemen vinden parallel plaats. In deze gevallen ontvangt de ZIM *per reagerend systeem* een resultaat of een foutmelding. Bij fouten in reagerende systemen zet de ZIM de uitwisseling met de andere systemen voort totdat ook de communicatie met deze systemen is afgehandeld. De ZIM combineert de deelresultaten tot een samengesteld antwoord, dat dus voor een deel uit foutmeldingen kan bestaan. Het samengestelde antwoord wordt teruggemeld aan het initiërend systeem. Omdat de uitwisseling met andere systemen parallel verloopt, is in het geval van meerdere foutmeldingen in de reagerende systemen de volgorde van foutmeldingen in het samengestelde antwoord aan het initiërend systeem willekeurig.

Voor de foutafhandeling in situaties waarbij de ZIM optreedt als intermediair tussen initiërend en reagerend systeem gelden de volgende regels:

- Indien de ZIM bij de communicatie met een reagerend systeem een fout ontvangt op HL7-v3-niveau[^1] wordt deze fout opgenomen in het antwoord aan het initiërend systeem.[^2] Ook de fouten die de ZIM zelf intern detecteert worden op HL7-v3-niveau gerapporteerd aan het initiërend systeem.

- Indien de ZIM bij de communicatie met één reagerend GBZ, waarbij sprake is van het versturen van patiëntgegevens, een SOAP fout ontvangt, retourneert de ZIM deze fout eveneens als zodanig aan het initiërend systeem. Bij fouten op lager gelegen protocollen interpreteert de ZIM de fout en rapporteert de ZIM deze op HL7-v3-niveau aan het initiërend systeem.

- Indien de ZIM in overige communicatie met reagerende systemen een fout ontvangt op een lager protocolniveau dan HL7-v3 (SOAP, HTTP, TCP/IP) interpreteert de ZIM deze fout en rapporteert de ZIM deze op HL7-v3-niveau aan het initiërend systeem. Hierbij is de ZIM niet verplicht om de details van de oorspronkelijke foutmelding van het reagerend systeem in het bericht op te nemen, tenzij anders aangegeven in de [Foutentabel]. Dit kan namelijk vanuit beveiligingsoogpunt ongewenst zijn.

De [Foutentabel] geeft een lijst van mogelijke foutcondities per berichttype. De [Foutentabel] geeft per foutconditie:

- het type fout;

- de gewenste reactie bij detectie van de fout;

- meldingscode;

- verplichte op te nemen details;

- voorgestelde meldingstekst;

- mogelijke herstelacties.

[^1]: Er is een lijst van HL7-v3 meldingscodes gedefinieerd die is opgenomen in de foutentabel.

[^2]: Het initiërend systeem is vrij om de ontvangen meldcode te verrijken met een zelfgekozen tekst voor presentatie aan de eindgebruiker.
