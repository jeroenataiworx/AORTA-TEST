[AORTA 8.5.2](index.md)

# Principes

**Wat zijn principes (Bron ZIRA)**

Er zijn vele theoretische definities en interpretaties van architectuurprincipes. De rode draad is dat het regels zijn, afgeleid van organisatiedoelstellingen, -missie en -visie, die richting en structuur geven aan het ontwerp van organisatie, proces, informatie, applicatie en techniek, en daarmee dus restricties aan de ontwerpvrijheid vormen.

Architectuurprincipes zijn:

- Richtinggevende afspraken binnen een organisatie, gebaseerd op overtuigingen hoe de ambities van de organisatie te realiseren.Richtinggevende uitspraken over de inrichting en realisatie van de informatievoorziening, geven structuur aan de inrichting van proces, informatie, applicatie en techniek;Richtinggevende uitspraken die gebruikt kunnen worden als leidraad en toetsinstrument bij veranderingen;

Architectuurprincipes zijn een kernonderdeel van enterprise-architectuur; ze richten zich op de essentie en bieden een stabiel handvat voor veranderingen in organisaties.

**Proces (conform Handboek Architectuur)**

Wanneer projecten of toepassingen willen afwijken van bestaande principes kan dit grote gevolgen hebben voor o.a.

- Afspraken en technieken die gebruikt worden in bestaande uitwisselingen

- Herbruikbaarheid

- Herstelwerkzaamheden (architectuurschuld, technologieschuld)

- Relatie met andere ontwikkelingen

- Volgordelijkheid van implementaties

- Doorlooptijd

- Conformance aan wet- en regelgeving

Principes worden toegepast conform pas-toe-of-leg-uit. Afwijkingen op de principes worden gesignaleerd, opgenomen in het architectuurlogboek en ter besluitvorming voorgedragen.

Met AORTA 8.3 zijn ook de AORTA principes herzien. Generieke (stelseloverstijgende) principes zijn geïntroduceerd met daarbij een (associatieve) referentie naar de DIZRA en de principes en uitgangspunten genoemd in de Visie op samenhang in zorginfrastructuren.

Uiteraard volgen we de vigerende wetgeving, regelgeving en normering in de zorg. Hiervoor zijn geen aparte principes opgenomen en zijn een paar oude AORTA principes vervallen omdat de implicaties inmiddels zijn opgenomen in de wet- en regelgeving.

- AORTA.ALG.p1020: voor toegang tot patiëntgegevens moeten zorgverleners persoonlijk worden geïdentificeerd en geauthentiseerd

- AORTA.ALG.p1030: de mate van toegang van zorgverleners tot patiëntgegevens wordt bepaald door de rol van de zorgverlener.

- AORTA.ALG.p1040.1: gegevens worden slechts beschikbaar gesteld door zorgaanbieders via AORTA na toestemming van de patiënt;

## Generieke Architectuurprincipes / Stelseloverstijgende principes

Generieke architectuurprincipes zijn stelseloverstijgend.

| **ID** ; | **VZVZ.GEN.P100** ; |
| --- | --- |
| Toepassingsgebied ; | Generiek ; |
| Stelling ; | <span id="latestPrincipes-Leverenvanmeerwaardevoordepersoon"></span>Leveren van meerwaarde voor de persoon |
| Beschrijving ; | De systemen en voorzieningen die geleverd worden moeten een meerwaarde leveren ten aanzien van informatievoorziening aan de persoon (zorgverlener en cliënt/patiënt). Eisen die worden gesteld ondersteunen dat doel. Bij het maken van (architectuur)keuzes dient het [VZVZ manifest](manifest-vzvz.md) als morele leidraad. ; |
| Rationale ; | Voor het leveren van meerwaarde t.b.v. het verlenen van goede zorg is het nodig dat: ;  Er wordt voorzien in de informatiebehoefte van de zorgverlener omdat de zorgverlener hierdoor in staat wordt gesteld om betere beslissingen te nemen in het behandeltraject van de patiënt. ;  Het tijdig mogelijk maken van nieuwe gegevensuitwisselingen ter ondersteuning van die informatiebehoefte biedt een belangrijke meerwaarde voor zowel client/patiënt als zorgverlener. ; |
| Implicaties ; | Het leveren van meerwaarde vergt architectuurdenken dat nieuwe gegevensuitwisselingen tussen verschillende infrastructuren mogelijk maakt. ;  Het koppelen van verschillende vertrouwensdomeinen moet mogelijk gemaakt worden. Nieuwe gegevensuitwisselingen tussen systemen die al met elkaar communiceren binnen een bestaand vertrouwensdomein zijn vaak sneller te realiseren dan gegevensuitwisselingen die moeten worden opgezet tussen verschillende vertrouwensdomeinen. ;  Meerwaarde tijdig leveren vergt architectuurdenken in korte en lange termijn doelstellingen. ; |
| *Mappingen* ; | *Onder de mappingen wordt een relatie gelegd met het VZVZ Manifest, de DIZRA en de visie op samenhang. Een mapping is een (associatieve) relatie.* ; |
| Mapping VZVZ Manifest ; | 1 Persoon op één ;  2 Zorg-centrisch ;  3 Waarde gedreven ; |
| [Mapping DIZRA](https://dizra.gitbook.io/dizra/manifest) ; | In het informatiestelsel hebben burgers regie op hun eigen gezondheidsdata en kunnen deze data meenemen en delen in hun reis door het zorglandschap en in het netwerk van zorgverleners en ondersteuners dat zich rondom hen vormt. ;  BP1 Mensgericht: “bij het verstrekken van gegevens over mij, aan mij, houden dienstverleners rekening met mijn wensen en kunnen.”. ;  AP1 Vanuit een gebruiksdoel: “onze bouwstenen zijn ontwikkeld vanuit de eindgebruikers van het informatiestelsel en zijn of haar gebruiksdoelen”. ; |
| [Mapping Visie samenhang](https://public.vzvz.nl/pages/worddav/preview.action?fileName=Visie+op+samenhang+in+zorginfrastructuren+3.0+schoon+.pdf&pageId=24545583) ; | N.A. ; |
| Mapping AORTA oud ; | N.A. ; |
|  |  |

| **ID** ; | **VZVZ.GEN.P110** ; |
| --- | --- |
| Toepassingsgebied ; | Generiek ; |
| Stelling ; | <span id="latestPrincipes-Eenstelselofvoorzieningbevateenvertrouwensmodel"></span>Een stelsel of voorziening bevat een vertrouwensmodel |
| Beschrijving ; | Een stelsel of voorziening beschrijft hoe het vertrouwen tussen de deelnemers is geregeld met betrekking tot de aspecten: ;  Identificatie ;  Authenticatie ;  Toestemming ;  Logging ;  Transparantie ;  Beheer ;  Beveiliging ;  Beschikbaarheid ; |
| Rationale ; | Het vertrouwensmodel is het geheel van technische, organisatorische en juridische waarborgen voor het vertrouwen in de landelijke elektronische uitwisseling van medische gegevens. Het vertrouwensmodel ziet toe op het onderlinge vertrouwen tussen zorgaanbieders, zorgverleners en patiënten en borgt daarmee de vertrouwelijkheid van het medische dossier. ; |
| Implicaties ; |  |
|  |  |
| Mapping VZVZ Manifest ; | 10. Veilig ; |
| Mapping DIZRA ; | In het informatiestelsel wordt federatief samengewerkt aan afspraken voor data en voor diensten. Iedereen implementeert deze afspraken en is aanspreekbaar op het nakomen van de afspraken en de kwaliteit van de implementatie. ; |
| Mapping Visie samenhang ; | Dankzij afspraken, waaronder een gezamenlijk vertrouwensmodel, ontstaat een basis voor interoperabiliteit tussen de verschillende zorginfrastructuren; ; |
| Mapping AORTA oud ; |  |
|  |  |

| **ID** ; | **VZVZ.GEN.P120** ; |
| --- | --- |
| Toepassingsgebied ; | Generiek ; |
| Stelling ; | <span id="latestPrincipes-Hetkoppelenvanverschillendevertrouwensdomeinenvergteenovereengekomengroeipad"></span>Het koppelen van verschillende vertrouwensdomeinen vergt een overeengekomen groeipad |
| Beschrijving ; | Het koppelen van verschillende vertrouwensdomeinen vergt maatwerk doordat er in ieder domein andere afspraken zijn gemaakt over de omgang met de waarborgen uit het vertrouwensmodel. Een transitie gericht op het tijdig leveren van meerwaarde is waardevoller dan afwachten tot het moment waarop iedereen aan dezelfde eisen kan voldoen maar vergt wel een groeipad met duidelijke afspraken waarbinnen de vertrouwensdomeinen naar elkaar kunnen toegroeien. ; |
| Rationale ; | Voor het tijdig realiseren van gegevensuitwisselingen tussen verschillende vertrouwensdomeinen is het nodig dat: ;  De verschillen in afspraken over de te leveren waarborgen worden overbrugt. Deze verschillen in afspraken zijn vaak dermate groot dat de zoektocht naar een uniforme set aan eisen, waaraan ieder domein moet voldoen voordat er gekoppeld kan worden, het tijdig leveren van meerwaarde in de weg staat, ;  Het leveren van meerwaarde in de situatie waarin verschillende vertrouwensdomeinen aan elkaar worden gekoppeld moet daarom niet wachten tot zo’n beoogde toekomstige situatie volledig gerealiseerd is. ;  Een transitie gericht op het tijdig leveren van meerwaarde is waardevoller maar vergt een groeipad met duidelijke afspraken waarbinnen de vertrouwensdomeinen naar elkaar kunnen toegroeien. ; |
| Implicaties ; | Gegevensuitwisselingen worden gerealiseerd onder behoeve van afspraken die worden gemaakt tussen (vertegenwoordigers van) de raadplegende en dossier houdende zorgaanbieders waarbij de raadplegende dossierhouder, conform wetgeving, gezien wordt als verantwoordelijke voor het al dan niet beschikbaar stellen van medische gegevens. De dossierhouder is derhalve verantwoordelijk voor de autorisatie en de daarbij horende identificatie, authenticatie en accounting. ; |
|  |  |
| Mapping VZVZ Manifest ; | 4 In balans ; |
| Mapping DIZRA ; | Het informatiestelsel is duurzaam doordat het relevant is en blijft. Het omarmt voor nu en in de toekomst de complexiteit van meerdere standaarden in een stelsel waarin verandering en innovatie welkom is. ;  AP3 Een gemodereerd ecosysteem: “we voldoen aan de gemeenschappelijke afspraken om mee te doen aan het informatiestelsel”. ; |
| Mapping Visie samenhang ; | Gebruikers (of hun vertegenwoordigers) zijn middels de governance medeverantwoordelijk voor de doorontwikkeling van de voorzieningen ; ; |
| Mapping AORTA oud ; | N.A. ; |
|  |  |

| **ID** ; | **VZVZ.GEN.P130** ; |
| --- | --- |
| Toepassingsgebied ; | Generiek ; |
| Stelling ; | <span id="latestPrincipes-Gegevenswordenbijdebronopgevraagd"></span>Gegevens worden bij de bron opgevraagd |
| Beschrijving ; | Voor zover gegevens worden opgeslagen dient dit uitsluitend om: ;  de gegevensbronnen op efficiënte wijze te kunnen ontsluiten; ;  te kunnen voldoen aan wettelijke verplichtingen t.a.v. dataminimalisatie (AVG, WGBO); ;  vast te kunnen stellen wie welke gegevens mag uitwisselen; ;  vast te kunnen stellen wie op welk moment gegevens heeft uitgewisseld. ; |
| Rationale ; | Er zijn diverse argumenten om patiëntgegevens bij het bronsysteem op te vragen: ;  Omdat er steeds uitgegaan wordt van de oorspronkelijke gegevens en niet van gekopieerde gegevens, blijft de actualiteit van gegevens gewaarborgd. Eerder ontvangen gegevens (push en pull) verliezen voor een raadpleger snel hun waarde vanwege het verloop in actualiteit van deze gegevens. Door gegevens telkens bij de bron op te vragen wordt de datakwaliteit, en daarmee de patiëntveiligheid, beter doordat (foutieve)gegevens alleen bij de bron kunnen worden gecorrigeerd en dus alleen bij de bron recent blijven. ;  De dossier houdende zorgaanbieder, als eigenaar van het bronsysteem, houdt de controle over de gegevens. Deze eigenaar is conform wetgeving (m.n. AVG, WGBO, WABVPZ) verantwoordelijk voor de geheimhouding van deze gegevens en daarom verantwoordelijk voor de toegangsverlening tot die gegevens. ;  Er is minder kans op gebruik van de gegevens voor andere doeleinden dan de oorspronkelijke. De dossierhouder is verantwoordelijk voor de verwerkingen die op de gegevens mogen worden uitgevoerd doordat de dossierhouder de patiënt heeft moeten informeren over deze verwerkingen. Verwerkingen die buiten de scope van deze doelbinding vallen zijn primair niet toegestaan (AVG). ; |
| Implicaties ; |  |
|  |  |
| Mapping VZVZ Manifest ; | N.A. ; |
| Mapping DIZRA ; | De data blijft bij de bron, onder de verantwoordelijkheid van de bronhouder, voor een veilig en vertrouwd informatiestelsel waarin het voor burgers transparant is welke bronhouders welke gezondheidsgegevens registreren en wie ze raadpleegt. ; |
| Mapping Visie samenhang ; | De verantwoordelijkheid voor de (inhoudelijke) kwaliteit van gegevens ligt bij de (oorspronkelijke) bron; ; |
| Mapping AORTA oud ; | AORTA.ALG.p1000: Patiëntgegevens worden steeds bij het bronsysteem opgevraagd. ; |
|  |  |

| **ID** ; | **VZVZ.GEN.P140** ; |
| --- | --- |
| Toepassingsgebied ; | Generiek ; |
| Stelling ; | <span id="latestPrincipes-WehanterendeFAIRdatauitgangspuntenbinnenwettelijkekaders"></span>We hanteren de FAIR data uitgangspunten binnen wettelijke kaders |
| Beschrijving ; | **The FAIR Guiding Principles** ;  To be Findable: ;  F1. (meta)data are assigned a globally unique and persistent identifier ;  F2. data are described with rich metadata (defined by R1 below) ;  F3. metadata clearly and explicitly include the identifier of the data it describes ;  F4. (meta)data are registered or indexed in a searchable resource ;  Uiteraard rekening houdend met AVG, wet en regelgeving (conform toestemming e.d.) ;  To be Accessible: ;  A1. (meta)data are retrievable by their identifier using a standardized communications protocol ;  A1.1 the protocol is open, free, and universally implementable ;  A1.2 2 the protocol allows for an authentication and authorization procedure, where necessary ;  A2. metadata are accessible, even when the data are no longer available ;  Uiteraard rekening houdend met WGBO het recht vergeten te worden. ;  To be Interoperable: ;  I1. (meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation. ;  I2. (meta)data use vocabularies that follow FAIR principles ;  I3. (meta)data include qualified references to other (meta)data ;  To be Reusable: ;  R1. meta(data) are richly described with a plurality of accurate and relevant attributes ;  R1.1. (meta)data are released with a clear and accessible data usage license ;  R1.2. (meta)data are associated with detailed provenance ;  R1.3. (meta)data meet domain-relevant community standards ;  Bron: [The FAIR Guiding Principles for scientific data management and stewardship](https://openaccess.leidenuniv.nl/bitstream/handle/1887/46904/ScientificData3\(2016\)160018.pdf?sequence=1) ; |
| Rationale ; |  |
| Implicaties ; |  |
|  |  |
| Mapping VZVZ Manifest ; | 9 Transparant ; |
| Mapping DIZRA ; | Data wordt enkelvoudig geregistreerd bij de bron en vervolgens beschikbaar gesteld voor meervoudig gebruik in verschillende toepassingen. Hiervoor hanteert het informatiestelsel de FAIR-data principes. ;  BP6 Vindbaar en toegankelijk: “mijn gegevens zijn eenvoudig te vinden en te hergebruiken.” ; |
| Mapping Visie samenhang ; | Informatie (zorginhoudelijk, administratief, kwaliteit en proces) is binnen wettelijke kaders beschikbaar voor alle betrokkenen en wordt daarmee zorgbreed (her)gebruikt; ; |
| Mapping AORTA oud ; |  |
|  |  |

| **ID** ; | **VZVZ.GEN.P150** ; |
| --- | --- |
| Toepassingsgebied ; | Generiek ; |
| Stelling ; | <span id="latestPrincipes-Privacybydesign&amp;ZeroTrust(nevertrust,alwaysverify)"></span>Privacy by design & Zero Trust (never trust, always verify) |
| Beschrijving ; |  |
| Rationale ; | Er wordt gewerkt conform de gebruikelijke principes van privacy en security by design. O.a: ;  **Privacy** ;  Proactive not reactive – hier gaat om maatregelen om te voorkomen dat de privacy van mensen wordt geschonden. ;  Privacy as the default setting – individuen hoeven geen actie te ondernemen om hun privacy te beschermen, privacy is ingebouwd in de software. ;  Privacy embedded into design – privacy wordt een essentieel deel van de kernfunctionaliteiten. ;  Full functionality – valse tegenstelling zoals security vs. privacy of functionaliteit vs privacy vermijden. ;  Transparantie & recht op informatie – De applicaties waar een organisatie gebruik van maakt moet conform zijn aan het niveau van privacy en security dat door de organisatie wordt gehanteerd. ;  Respect for User Privacy – de privacy van het individu is overal in het ontwerp van de software op de voorgrond aanwezig. ;  End-to-end encryption ;  Autorisaties tot gegevensverzamelingen worden nauwlettend volgens de geldende privacy normen ingesteld. ;  **Beveiligingsprincipes** ;  Minimaliseer het aanvalsoppervlak ;  Stel veilige standaardwaarden vast ;  Principe van het minste voorrecht ;  Verdedigingsprincipe ;  Veilig falen ;  Vertrouw geen services Scheiding van taken ;  Vermijd beveiliging door onduidelijkheid ;  Houd beveiliging eenvoudig ;  Beveiligingsproblemen correct oplossen ;  **Zero Trust** ;  Devices mogen standaard niet worden vertrouwd, zelfs als ze zijn verbonden met een geautoriseerd netwerk zoals een bedrijfs-LAN en zelfs als ze eerder zijn geverifieerd ;  Continue verificatie. Controleer altijd de toegang tot alle bronnen. ;  Minimaliseer de impact als er een externe of interne inbreuk plaatsvindt. ;  Automatiseer het verzamelen en reageren van context. Neem gedragsgegevens op en haal context uit de hele IT-stack (identiteit, eindpunt, werklast, enz.) voor de meest nauwkeurige reactie ; |
| Implicaties ; |  |
|  |  |
| Mapping VZVZ Manifest ; | 10. Veilig ; |
| Mapping DIZRA ; | BP4 Vertrouwen: “ik kan er op vertrouwen dat mijn gegevens de juiste zorg krijgen”. ;  AP7 Verantwoord gebruik: “we dragen zorg voor de bescherming van persoonsgegevens”. ; |
| Mapping Visie samenhang ; | Er wordt gewerkt conform de principes van privacy en security by design, autorisaties tot gegevensverzamelingen worden nauwlettend volgens de geldende privacy normen ingesteld. ; |
| Mapping AORTA oud ; |  |
|  |  |

| **ID** ; | **VZVZ.GEN.P160** ; |
| --- | --- |
| Toepassingsgebied ; | Generiek ; |
| Stelling ; | <span id="latestPrincipes-Stelselenvoorzieningenleggenalleeneisenopdienoodzakelijkzijnvoorveiligeuitwisselingvangegevensopbasisvangezamenlijkvastgesteldeopenstandaarden,"></span>Stelsel en voorzieningen leggen alleen eisen op die noodzakelijk zijn voor veilige uitwisseling van gegevens op basis van gezamenlijk vastgestelde open standaarden, |
| Beschrijving ; |  |
| Rationale ; | Zorgverleners werken met diverse zorginformatiesystemen die zij afnemen van verschillende marktpartijen. Stelsels zijn bedoeld om de uitwisseling van patiëntgegevens tussen deze systemen te faciliteren met behoud van marktwerking. Daarom moeten eisen aan de systemen waartussen gegevens worden uitgewisseld zoveel mogelijk worden beperkt tot het strikt noodzakelijke en gebaseerd op internationale standaarden om te komen tot: ;  gestandaardiseerde uitwisseling van gegevens; ;  adequate beveiliging van de uitwisselingsinfrastructuur als geheel; ;  functioneren van de uitwisselingsinfrastructuur als geheel, bijvoorbeeld wat betreft beschikbaarheid. ; |
| Implicaties ; | We gebruiken zoveel mogelijk internationale standaarden, deze prefereren boven nationale standaarden maar erkennen dat nationale uitbreidingen of beperkingen soms nodig en nuttig kunnen zijn ; |
|  |  |
| Mapping VZVZ Manifest ; | 7 Op alle lagen ; |
| Mapping DIZRA ; | Het informatiestelsel hanteert een gelijk speelveld voor alle leveranciers. Afspraken worden gemaakt over het gebruik van standaarden, niet over het gebruik van een product of dienst. Iedere organisatie kiest haar eigen leveranciers voor het implementeren van de standaarden. ;  Semantische en technische interoperabiliteit wordt in het informatiestelsel gerealiseerd door te kiezen voor open internationale standaarden. Iedere deelnemer aan het stelsel moet voldoen aan de standaarden die zijn afgesproken. ;  AP21 Internationale standaarden: “we maken gebruik van open standaarden, internationaal boven nationaal”. ; |
| Mapping Visie samenhang ; | De (zorg)informatiesystemen kunnen eenvoudig aansluiten op basis van gezamenlijk vastgestelde open standaarden en koppelvlakken. Er worden (nationale extensies van) internationale standaarden gebruikt. Data wordt onafhankelijk van applicaties opgeslagen en beheerd, met procesondersteuning gebaseerd op bij voorkeur (wettelijk) verplicht gestelde open standaarden. ;  In een gelijkwaardig speelveld met open interfaces (eventueel op basis van open source) kunnen verschillende ICT-leveranciers en data-organisaties (versneld) diensten ontwikkelen, waardoor de belangen van betrokken partijen goed tot hun recht komen. Voor aangesloten partijen zijn alle mogelijkheden aanwezig om zelfstandig te innoveren en beschikbare kennis, expertise en technologieën te benutten. De markt kan haar werk doen; ;  Er wordt gebruik gemaakt van (nationale extensies van) internationale standaarden; ; |
| Mapping AORTA oud ; | AORTA.ALG.p1010: aan aangesloten zorgsystemen worden uitsluitend eisen gesteld die noodzakelijk zijn voor veilige gestandaardiseerde uitwisseling van gegevens. ; |
|  |  |

| **ID** ; | **VZVZ.GEN.P170** ; |
| --- | --- |
| Toepassingsgebied ; | Generiek ; |
| Stelling ; | <span id="latestPrincipes-Gebruikers(ofhunvertegenwoordigers)zijnmiddelsdegovernancemedeverantwoordelijkvoorhetbeheerendedoorontwikkelingvandevoorzieningen"></span>Gebruikers (of hun vertegenwoordigers) zijn middels de governance medeverantwoordelijk voor het beheer en de doorontwikkeling van de voorzieningen |
| Beschrijving ; |  |
| Rationale ; | om besluiten te nemen voor ontwikkeling en beheer ; |
| Implicaties ; | Beheerspartijen en leveranciers van de in de gegevensuitwisseling betrokken informatiesystemen werken proactief samen om beheersproblemen te voorkomen en lossen de problemen primair onderling op maar kunnen problemen escaleren naar een regie-voerende partij. ;  Beheerpartijen van de in de gegevensuitwisseling betrokken informatiesystemen maken afspraken over de beschikbaarheid. ; |
|  |  |
| Mapping VZVZ Manifest ; | 5 Samen ; |
| Mapping DIZRA ; | In het informatiestelsel wordt federatief samengewerkt aan afspraken voor data en voor diensten. Iedereen implementeert deze afspraken en is aanspreekbaar op het nakomen van de afspraken en de kwaliteit van de implementatie. ;  AP4 Federatief: “we ontwikkelen en beheren het informatiestelsel gezamenlijk”. ; |
| Mapping Visie samenhang ; | Gebruikers (of hun vertegenwoordigers) zijn middels de governance medeverantwoordelijk voor de doorontwikkeling van de voorzieningen ; ; |
| Mapping AORTA oud ; | N.A. ; |
|  |  |

| **ID** ; | **VZVZ.GEN.P180** ; |
| --- | --- |
| Toepassingsgebied ; | Generiek ; |
| Stelling ; | <span id="latestPrincipes-Openspeelveldenkeuzevrijheid"></span> Open speelveld en keuzevrijheid |
| Beschrijving ; | Afspraken worden gemaakt over het gebruik van standaarden, niet over het gebruik van een product of dienst. Iedere organisatie kiest haar eigen leveranciers voor het implementeren van de standaarden. ; |
| Rationale ; |  |
| Implicaties ; |  |
|  |  |
| Mapping VZVZ Manifest ; | 8 Keuzevrijheid ; |
| Mapping DIZRA ; | Het informatiestelsel hanteert een gelijk speelveld voor alle leveranciers. Afspraken worden gemaakt over het gebruik van standaarden, niet over het gebruik van een product of dienst. Iedere organisatie kiest haar eigen leveranciers voor het implementeren van de standaarden ; |
| Mapping Visie samenhang ; | In een gelijkwaardig speelveld met open interfaces (eventueel op basis van open source) kunnen verschillende ICT-leveranciers en data-organisaties (versneld) diensten ontwikkelen, waardoor de belangen van betrokken partijen goed tot hun recht komen. ;  Voor aangesloten partijen zijn alle mogelijkheden aanwezig om zelfstandig te innoveren en beschikbare kennis, expertise en technologieën te benutten. De markt kan haar werk doen; ; |
| Mapping AORTA oud ; | N.A. ; |
|  |  |

| **ID** ; | **VZVZ.GEN.P190** ; |
| --- | --- |
| Toepassingsgebied ; | Generiek ; |
| Stelling ; | <span id="latestPrincipes-SemantischevertalingenvallenonderdeMDR(MedicalDeviceRegulation)verordening,technischetransformatiesniet.VZVZvoertdaaromgeensemantischevertalingenuit."></span>Semantische vertalingen vallen onder de MDR (Medical Device Regulation) verordening, technische transformaties niet. VZVZ voert daarom geen semantische vertalingen uit. |
| Beschrijving ; | Technische transformaties zijn iets anders dan semantische transformatie. Er kan pas worden gesproken van semantische transformatie als de betekenis van de gegevens bij het interpreteren door een gebruiker (zorgverlener) anders is geworden door een uitgevoerde transformatie. Technische transformaties dienen het doel om gegevensuitwisseling mogelijk te maken tussen systemen die verschillende (versies van) standaarden hanteren. Bij een technische transformatie wordt de semantiek van de informatie niet geraakt. ;  Er moet dus anders worden omgegaan met semantische transformaties dan met technische transformaties. Dit volgt uit o.a. Europese richtlijnen. ;  Uit Qualification and classification of software - Regulation (EU) 2017/745 and Regulation (EU) 2017/746 m.b.t. de MDR volgt dat: ;  De software medische informatie moet creëren of modificeren met een medisch doel anders dan de representatie van data aanpassen voor compatibiliteitsdoeleinden om de MDR van toepassing te kunnen verklaren. ;  Software voor zoeken (dossier ophalen via match op metadata) en/of het ophalen/vragen van informatie niet onder de MDR verordening valt. ;  Zie ook de NEN-7503-2022 m.b.t. MDR ; |
| Rationale ; | Semantische transformaties kunnen de betekenis bij interpretatie door de gebruiker van de opgevraagde gegevens veranderen. Bij technische transformatie verandert de betekenis van de opgevraagde gegevens niet. ; |
| Implicaties ; | Technische transformaties om de gegevensuitwisseling tot stand te brengen kennen een ander kader dan semantische transformaties, dat heeft gevolgen voor de technische omgang met die gegevens. ;  Er is een tussenvorm waarin er door een technische vertaling informatie wegvalt doordat de standaard waar naar omgezet wordt geen ruimte biedt waarin die gegevens (al dan niet één-op-één) kunnen worden overgenomen. Daar moeten we zorgvuldig mee omgaan. ; |
|  |  |
| Mapping VZVZ Manifest ; | N.A. ; |
| Mapping DIZRA ; | Semantische en technische interoperabiliteit wordt in het informatiestelsel gerealiseerd door te kiezen voor open internationale standaarden. Iedere deelnemer aan het stelsel moet voldoen aan de standaarden die zijn afgesproken ;  AP14 Een gemeenschappelijk vocabulaire: “onze gegevens zijn uitwisselbaar met een gemeenschappelijk vocabulaire zodat we elkaar kunnen begrijpen”. ;  AP20 Taal los van transport: “we maken onderscheid tussen taal en transport en koppelen dat los van elkaar”. ; |
| Mapping Visie samenhang ; | N.A. ; |
| Mapping AORTA oud ; | N.A. ; |
|  |  |

## AORTA Principes

| **ID** ; | **VZVZ.AORTA.P1000** ; |
| --- | --- |
| Toepassingsgebied ; | AORTA ; |
| Stelling ; | <span id="latestPrincipes-Hetisvoordeburgertransparantwelkegegevenstussenwelkezorgaanbiedersisuitgewisseld"></span>Het is voor de burger transparant welke gegevens tussen welke zorgaanbieders is uitgewisseld |
| Beschrijving ; | Burgers hebben achteraf inzicht in welke gegevens zijn uitgewisseld. Daarbij wordt inzichtelijk tussen welke zorgaanbieders de gegevens zijn uitgewisseld. Er wordt expliciet niet transparant welke zorgverlener(s) betrokken was (waren) bij de uitwisseling. Het is de verantwoordelijkheid van de zorgaanbieder om een patiënt inzage te geven in de loggegevens van de betrokken zorgverleners. ; |
| Rationale ; |  |
| Implicaties ; |  |
|  |  |
| Mapping VZVZ Manifest ; | 9 Transparant ; |
| Mapping DIZRA ; | In het informatiestelsel hebben burgers regie op hun eigen gezondheidsdata en kunnen deze data meenemen en delen in hun reis door het zorglandschap en in het netwerk van zorgverleners en ondersteuners dat zich rondom hen vormt. ;  AP12 Regie over gegevens: “we stellen patiënten, cliënten en burgers in staat om controle en regie te nemen over hun gegevens” ; |
| Mapping Visie samenhang ; | Informatie (zorginhoudelijk, administratief, kwaliteit en proces) is binnen wettelijke kaders beschikbaar voor alle betrokkenen en wordt daarmee zorgbreed (her)gebruikt; ; |
| Mapping AORTA oud ; | AORTA.ALG.p1050: patiënten hebben via AORTA toegang tot hun eigen gegevens. ;  AORTA.ALG.p1060: toegang tot patiëntgegevens wordt vastgelegd en is hierdoor traceerbaar. ; |
|  |  |

| **ID** ; | **VZVZ.AORTA.P1100** ; |
| --- | --- |
| Toepassingsgebied ; | AORTA ; |
| Stelling ; | <span id="latestPrincipes-AORTAkenteenmodulairearchitectuur"></span>AORTA kent een modulaire architectuur |
| Beschrijving ; | Gebruik van voor-gedefinieerde, herbruikbare bouwstenen ; |
| Rationale ; | Gebruik van voor-gedefinieerde, herbruikbare bouwstenen vereenvoudigt het ontwerpen van uitwisselingen voor nieuwe zorgtoepassingen. Het bespaart (ontwikkel-) inspanning en –kosten en verkort de doorlooptijd van nieuwe toepassingen. De complexiteit voor XIS-leveranciers die meerdere zorgtoepassingen implementeren in hun software wordt hiermee gereduceerd. ; |
| Implicaties ; |  |
|  |  |
| Mapping VZVZ Manifest ; |  |
| Mapping DIZRA ; | Het informatiestelsel is duurzaam doordat het relevant is en blijft. Het omarmt voor nu en in de toekomst de complexiteit van meerdere standaarden in een stelsel waarin verandering en innovatie welkom is. ; |
| Mapping Visie samenhang ; | Het stelsel van zorginfrastructuren omvat (ook) voorzieningen en gegevensdiensten, welke voor algemeen gebruik beschikbaar zijn en op basis van keuzevrijheid kunnen worden gebruikt. ; |
| Mapping AORTA oud ; | AORTA.ALG.p1070: De AORTA architectuur ondersteunt informatie-uitwisseling via berichten met informatie opgenomen in voorgedefinieerde, herbruikbare bouwstenen ; |
