[AORTA 8.5.2](../../index.md) / [Logische architectuur](../../logische-architectuur.md) / [Ondersteunende interacties](../ondersteunende-interacties.md)

# Actoren en rollen

De actoren ‘zorgverlener’ en ‘patiënt’ zijn geïntroduceerd op pagina '[Actoren](https://vzvz.atlassian.net/wiki/x/2YGObg)'. Aanvullende actoren worden hier besproken.

### SBV-Z

De Sectorale Berichtenvoorziening in de Zorg (SBV-Z) is een onderdeel van het agentschap CIBG, uitvoeringsorganisatie van het ministerie van VWS. De SBV-Z vormt voor de zorgsector de toegangspoort tot de Beheervoorziening BSN (BVBSN), de organisatie die primair verantwoordelijk is voor de uitgifte en het beheer van het Burgerservicenummer (BSN). Bij deze instantie kunnen Burgerservicenummers van patiënten opgevraagd en geverifieerd worden. Ook biedt de SBV-Z een dienst om de omloopstatus van een wettelijk identificatiedocument (WID) te controleren.

#### Landelijk schakelpunt

Het Landelijk Schakelpunt (LSP) (geïntroduceerd op pagina '[Het zoeken van gegevenshouders en gegevensontvangers](https://vzvz.atlassian.net/wiki/x/QYKObg)') is een intermediaire organisatie die diensten verleend aan zorgaanbieders die zorginformatie willen uitwisselen en waarbij de gegevenshouders de beschikbaarheid van gegevens over patiënten kunnen aanmelden. Het LSP treedt op als intermediair tussen gegevensraadplegers en gegevenshouders, en tussen gegevenszender en gegevensontvanger.

#### Klantenloket en Medewerker klantenloket

Een uitgangspunt van AORTA is dat de patiënt volledig inzicht moet kunnen krijgen in de uitwisseling van de eigen patiëntgegevens. Er is voorzien dat patiënten, die zelf geen toegang hebben tot de daarvoor benodigde technische voorzieningen, toch een aanspreekpunt hebben dat dit inzicht kan verschaffen; dit aanspreekpunt is het klantenloket. Een medewerker van het klantenloket kan de patiënt van informatie voorzien over de uitwisseling van zijn patiëntgegevens via AORTA, overigens zonder dat de klantenloketmedewerker de uitgewisselde patiëntgegevens zelf kan inzien (de klantenloketmedewerker heeft uitsluitend toegang tot verwijsindexgegevens en toegangsloggegevens, zie pagina '[Raadplegen verwijsindex](https://vzvz.atlassian.net/wiki/x/UoOObg)' en '[Raadplegen toegangslog](https://vzvz.atlassian.net/wiki/x/JIOObg)' ). Klantenloketmedewerkers worden geïdentificeerd aan de hand van een PKIoverheidscertificaat (zie pagina '[PKIO](../informatiesystemen/basisregistraties-en-vertrouwensmiddelen.md#pkio)').

#### Mitz

Mitz is een landelijk voorziening waarin de toestemmingen van burgers worden opgeslagen. Mitz is een onafhankelijk uitwisselingssysteem en kan worden gebruikt als een locatieservice (waar staan er gegevens van deze burger en waar heeft de patiënt toestemming gegeven voor gegevensuitwisseling) en als toestemmingsregister (is er wel toestemming om deze opvraging bij deze zorgaanbieder te doen).

#### Autorisatiecommissie

De autorisatiecommissie is een commissie met diverse vertegenwoordigers uit het zorgveld die per beroep en specialisatie van zorgverleners vaststelt wie welke gegevens mag raadplegen, versturen en/of ontvangen via AORTA. Deze commissie stelt dus het autorisatieprotocol en de determinatietabellen vast die zijn beschreven op pagina '[Bevoegdheid op basis van BIG-titel](../primaire-interacties/toegangsmodel.md#bevoegdheid-op-basis-van-big-titel)'. De autorisatiemanager is een rol van de voorzitter van de autorisatiecommissie. De autorisatiemanager zorgt ervoor dat de afgesproken autorisatieprotocollen worden vastgelegd bij het landelijk schakelpunt.

#### Toezichthouder

De toezichthouder op het correct gebruik van AORTA:

- behandelt klachten over mogelijk onterechte toegang tot patiëntgegevens;

- kan zorgverleners om verantwoording vragen ten aanzien van het geconstateerd gebruik van AORTA;

- kan gepaste maatregelen nemen in geval van geconstateerd misbruik.

De rol van toezichthouder wordt vervuld door het College Bescherming Persoonsgegevens (CBP) en de Inspectie voor de Gezondheidszorg (IGZ).

#### Rollen

In het overzichtsdiagram AORTA.ALG.d1030.5 worden diverse rollen geïntroduceerd, zoals ‘bewerker verwijsindex’ en ‘raadpleger verwijsindex’. Deze rollen worden geïntroduceerd om modeltechnische redenen (om het telkens herhalen van alle betrokken actoren te voorkomen) en impliceren niet dat voor iedere actor die een bepaalde rol vervult exact dezelfde autorisatie-eisen gelden; voor de rol van ‘raadpleger verwijsindex’ geldt bijvoorbeeld dat een zorgverlener toegang krijgt tot andere indexgegevens dan een patiënt.

#### Mandatering

De mogelijkheid van mandatering die is geïntroduceerd op pagina '[Mandatering](../primaire-interacties/toegangsmodel.md#mandatering)' voor de interacties ‘opvragen van patiëntgegevens’ en ‘sturen van patiëntgegevens’ strekt zich ook uit tot de ondersteunende interacties die een zorgverlener mag uitvoeren. Waar sprake is van ‘zorgverlener’ kan dit, tenzij anders vermeld, dus worden geïnterpreteerd als ‘zorgverlener’ of een door de zorgverlener gemandateerde zorgverlener, medewerker of systeem.
