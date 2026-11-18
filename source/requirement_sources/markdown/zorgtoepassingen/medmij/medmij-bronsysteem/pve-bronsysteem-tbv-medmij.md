[AORTA 8.5.2](../../../index.md) / [Zorgtoepassingen](../../../zorgtoepassingen.md) / [MedMij](../../medmij.md) / [MedMij Bronsysteem](../medmij-bronsysteem.md)

# PvE Bronsysteem tbv MedMij

| Datum: 15 juni 2022 ; |
| --- |
| Status: Definitief ; |
| Versie: ; |
| Classificatie: Openbaar ; |
| Revisie: 1.0 ; |

### Documenthistorie

*Documentversies*

| **Datum** ; | **Status** ; | **Versie** ; | **Omschrijving** ; |
| --- | --- | --- | --- |
| 15 juni 2022 ; | Definitief ; |  | Eerste opzet PvE Bronsysteem tbv MedMij ; |
|  |  |  |  |

Inhoudsopgave   
[Documenthistorie](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731210)  
[1 Inleiding](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731211)  
[1.1 Doelgroep voor dit document](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731212)  
[**1.2** Doel en scope](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731213)  
[2 Diagrammen Kwaliteitseisen](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731214)  
[2.1 AORTA Eisen Kwaliteit aangesloten systemen](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731215)  
[2.1.1 Tijdige verwerking van berichten](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731216)  
[2.1.2 Genereren time-out](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731217)  
[2.1.3 Borgen van minimale verwerkingssnelheid](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731218)  
[2.1.4 Borgen van de beschikbaarheid van een GBx](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731219)  
[2.1.5 Minimaliseren van de impact van gepland onderhoud](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731220)  
[2.1.6 Borgen van de betrouwbaarheid bij kleine storingen](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731221)  
[2.1.7 Borgen van de betrouwbaarheid bij grote storingen](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731222)  
[2.1.8 Beveiliging van patiëntgegevens in het GBx](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731223)  
[2.1.9 Borgen van plicht tot uitwisselen van patiëntgegevens](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731224)  
[2.1.10 Een GBx beschikt over een geldig UZI/PKIO-servercertificaat](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731225)  
[2.1.11 Beveiligde opslag](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731226)  
[2.1.12 Communicatie met het LSP via een GZN](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731227)  
[2.1.13 Gebruik van IP en DNS](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731228)  
[2.1.14 Tijdsynchronisatie GBx en ZIM](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731229)  
[2.1.15 Aansluiting op productie-omgeving LSP](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731230)  
[2.2 AORTA Eisen Kwaliteit applicatie](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731231)  
[2.2.1 Afbreken van een gebruikerssessie](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731232)  
[2.2.2 Opzetten beveiligde verbinding met de ZIM](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731233)  
[2.2.3 Instellen configuratieparameters t.b.v. communicatie en authenticatie van de ZIM](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731234)  
[2.2.4 Opzetten en gebruiken van TLS-sessies](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731235)  
[2.2.5 Opzetten beveiligde verbinding vanuit de ZIM met een GBx](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731236)  
[2.2.6 Hardening](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731237)  
[2.2.7 Toegangslog bijhouden (FHIR)](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731238)  
[2.2.8 Onderscheiden van fictieve gegevens](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731239)  
[2.2.9 Ondersteunen servercertificaten en ondertekeningalgoritmen](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731240)  
[2.2.10 Kenbaar maken Certificate Authorities](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731241)  
[2.2.11 Afhandelen transactietoken](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731242)  
[2.2.12 Protocolstack voor gegevensuitwisseling o.b.v. FHIR](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731243)  
[2.3 Eisen aan de beheerorganisatie van een GBX](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731244)  
[2.3.1 Ondersteuning van gebruikers bij problemen met de landelijke uitwisseling van informatie](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731245)  
[2.3.2 Instrueren systeemgebruikers over beveiligingsbeleid](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731246)  
[2.3.3 Toekennen functiescheiding tussen systeemgebruikers](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731247)  
[2.3.4 Beheren van en toegang verschaffen tot de toegangslog](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731248)  
[2.3.5 Systeembeheer van een GBx](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731249)  
[2.3.6 Actueel houden van het applicatieregister](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731250)  
[2.3.7 Beperking inzage door beheerder](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731251)  
[2.3.8 Bijhouden van een beheerlog](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731252)  
[2.3.9 Kennisvergaring m.b.t. GBX-beheer](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731253)  
[2.3.10 Een GBx valt onder Nederlandse wet- en regelgeving](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731254)  
[2.3.11 Vernietigen materialen volgens standaarden](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731255)  
[2.3.12 Voldoen aan wet- en regelgeving](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731256)  
[2.3.13 Loggen toegangsregeling](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731257)  
[2.3.14 Bewaartermijn loggegevens](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731258)  
[2.3.15 Loggen inzage logging](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731259)  
[2.3.16 Uitschakelen logging](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731260)  
[2.3.17 Vernietigen loggegevens](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731261)  
[2.3.18 Wijzigen logging](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731262)  
[2.3.19 Toegangsbeheer tot logging](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731263)  
[2.4 Eisen Infrastructurele Systeemrollen](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731264)  
[2.4.1 Afschermen patiëntgegevens voor bevraging patiënt](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731265)  
[2.4.2 Compatibiliteit bieden met de diverse (zorg)toepassingen](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731266)  
[2.4.3 Leeftijdscontrole patiënt](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731267)  
[2.4.4 Opnemen BSN in opleverbericht](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731268)  
[2.4.5 Wijzigen TKID applicatie o.b.v. FHIR](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731269)  
[2.4.6 Bevestigen applicatiekoppeling o.b.v. FHIR](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731270)  
[2.4.7 Verwerken geboortedatums waarin nullen zijn opgenomen](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731271)  
[2.4.8 Voorlopig koppelen van patiëntgegevens aan een BSN](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731272)  
[2.4.9 Definitief koppelen van patiëntgegevens aan een BSN](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731273)  
[2.4.10 Controleren geldigheid van een WID](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731274)  
[2.4.11 Opzoeken en tonen patiëntgegevens](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731275)  
[2.4.12 Gebruik van geverifieerde BSN's](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731276)  
[2.5 Eisen XIS-leverancier](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731277)  
[2.5.1 Beschikbaarheid XIS-servicedesk](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731278)  
[2.5.2 Inrichten XIS-servicedesk](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731279)  
[2.5.3 Gebruik Supportal](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731280)  
[2.6 Eisen specifieke gegevensdienst](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731281)  
[2.6.1 Implementeren gegevensdienst Verzamelen Huisartsgegevens 2.0](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731282)  
[2.6.2 Implementeren gegevensdienst Verzamelen Medicatiegegevens 9.0](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731283)  
[2.6.3 Implementeren gegevensdienst Verzamelen Medicatiegerelateerde Overgevoeligheden 2.A](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731284)  
[2.6.4 Implementeren gegevensdienst Verzamelen Basisgegevens GGZ 2.0](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731285)  
[2.6.5 Implementeren gegevensdienst Verzamelen Basisgegevens zorg 3.0](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731286)  
[2.6.6 Implementeren gegevensdienst Delen antwoorden op vragenlijsten 2.0](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731287)  
[2.6.7 Implementeren Ontvankelijkheidstoets](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731288)  
[2.6.8 Controleren behandelrelatie](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731289)  
[2.6.9 Bijhouden behandelrelatie](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731290)  
[2.6.10 Implementeren gegevensdienst Delen Meetwaarden vitale functies 2.0](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731291)  
[2.6.11 Implementeren gegevensdienst Verzamelen Afspraken 2.0](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731292)  
[2.6.12 Implementeren gegevensdienst Verzamelen Documenten 3.0](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731293)  
[2.6.13 Implementeren gegevensdienst Meetwaarden vitale functies 2.0](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731294)  
[2.6.14 Implementeren gegevensdienst Verzamelen verwijzingen naar vragenlijsten 2.0](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-_Toc88731295)

## Inleiding

Dit programma van eisen gaat over de toepassing bronsysteem t.b.v. MedMij. Het PvE Bronsysteem t.b.v. MedMij betreft een document waarin eisen zijn opgenomen waaraan een GBZ moet voldoen om aangesloten te worden op de AORTA-infrastructuur.

### Doelgroep voor dit document

De doelgroep voor dit document bestaat uit diverse rollen aan de kant van de XIS-leverancier en de GBx beheerorganisatie. Het gaat hierbij om o.a. architecten, software ontwikkelaars, productmanagers, testers en systeembeheerders. Tevens is dit document bedoeld voor diverse rollen binnen VZVZ. Het gaat hierbij o.a. om architecten, productmanagers, testers, demandmanagers en ketenregie.

### Doel en scope

Het doel van dit document is om de eisen te beschrijven waaraan moet worden voldaan om een GBZ als bronsysteem t.b.v. MedMij aan te sluiten op de AORTA-infrastructuur. De hierin opgenomen hoofdstukken gelden voor alle bronsystemen ongeacht de gegevensdienst waarvoor zij gegevens beschikbaar stellen. Paragraaf 1.6 bevat per gegevensdienst de specifieke eisen voor die gegevensdienst. Deze zijn alleen van toepassing indien de betreffende XIS ook daadwerkelijk gegevens beschikbaar wil stellen t.b.v. die gegevensdienst.   
<span id="latestPvEBronsysteemtbvMedMij-INSERT_Section1"></span><span id="INSERT_Section1"></span>Section: Section1

## Diagrammen Kwaliteitseisen

### AORTA Eisen Kwaliteit aangesloten systemen

![Diagram](../../../../assets/15cfb97455191b1b4884da95bab2da7617d50da1d2e314457581bd26b013dd50.png)  
*Figure 1 : AORTA Eisen Kwaliteit aangesloten systemen - Prestatie-efficiëntie*

#### Tijdige verwerking van berichten

**Alias**: GBX.PST.e4015

| Details ; |
| --- |
| **Eis:** ; Een GBx dient voor gebruikersinteracties, na het commando van een gebruiker of een daaropvolgende ontvangst van een bericht van de ZIM, binnen 0,3 seconden het aangegeven resultaat te hebben bereikt. ; **Toelichting bij eis:** ; Deze eis is nodig om te voorkomen dat een zorgaanbieder bij zijn GZN of het LSP gaat klagen over te lange responstijden terwijl de oorzaak misschien ligt bij bijv. een eigen computer die in beslag wordt genomen door andere toepassingen of een lokaal netwerk met onvoldoende bandbreedte. ; Deze eis betekent voor de zorgaanbieder dat hij zijn XIS-applicatie moet installeren op ICT-voorzieningen met voldoende prestaties. Zonodig moeten bijv. de computers worden ingeregeld op de behoefte van deze XIS-applicatie, bijv. als ze ook worden gebruikt voor andere toepassingen. Wellicht kan zijn XIS-leverancier helpen bij het selecteren en inregelen van ICT-voorzieningen. Indien de zorgaanbieder een ASP-leverancier heeft geselecteerd voor zijn XIS, kan hij dit voor de centrale ICT-voorzieningen wellicht overlaten aan die ASP-leverancier, maar moeten de lokale werkplekken niet vergeten worden. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Genereren time-out

**Alias**: GBX.PST.e4020

| Details ; |
| --- |
| **Eis:** ; Het bronsysteem moet binnen 60 seconden na ontvangst van een opvraagbericht een antwoord gegeven. Indien het bronsysteem constateert dat het niet binnen 60 seconden kan antwoorden, dan dient het bronsysteem een foutmelding te genereren. ; **Toelichting bij eis:** ; Om te voorkomen dat TLS-verbindingen onnodig lang tussen het LSP en GBx-en blijven bestaan, worden de TLS-verbindingen automatisch door het LSP verbroken. Het LSP zal na 60 seconden de verbinding met een bronsysteem verbreken en een foutmelding (time-out) terugsturen naar het initiërende systeem. ; Indien het bronsysteem zelf kan vaststellen dat er niet binnen de in de eis opgegeven tijd een antwoord verstuurd kan worden, dan dient het bronsysteem een foutmelding (timeout) te versturen. Op deze manier kan voorkomen worden, dat een initiërend systeem onnodig lang hoeft te wachten. ; De waarde voor de time-out is gebaseerd op voorgaande AORTA-versies. Hierbij is nog geen rekening gehouden met aansluiting op MedMij, die vereist dat een DVZA binnen 60 seconden een antwoord moet geven aan een PGO. Vooralsnog blijft de waarde zoals opgenomen in deze eis gehandhaaft. Het DVZA zal in dat geval na 60 seconden een time-out versturen naar het PGO. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Borgen van minimale verwerkingssnelheid

**Alias**: GBX.PST.e4010.1

| Details ; |
| --- |
| **Eis:** ; Een GBx dient minimaal de hieronder genoemde snelheden te halen voor de hieronder genoemde interactiemechanismen. ; **Interactiemechanisme Minimale verwerkingssnelheid** ; Sturen van gegevens <GBx-verwerkingssnelheid-sturen> ; Opvragen van gegevens <GBx-verwerkingssnelheid-opvragen> ; Een GBx dient een zodanige capaciteit te hebben voor het beantwoorden en ontvangen van berichten van de ZIM dat het kan voldoen aan de gestelde verwerkingssnelheden. Indien dat als gevolg van een onverwacht hoge piekbelasting tijdelijk niet mogelijk is, dan prevaleren de eisen inzake beschikbaarheid boven de eisen inzake verwerkingssnelheid. ; **Toelichting bij eis:** ; Deze eis is nodig opdat een XIS-applicatie tijdig berichten van de ZIM kan verwerken/beantwoorden ten behoeve van andere zorgaanbieders, ook als de belasting zodanig hoog is, dat de volgende berichten binnenkomen terwijl de vorige nog niet verwerkt/beantwoord zijn. ; Deze eis betekent voor de organisatie dat de applicatie is geïnstalleerd op ICT-voorzieningen met voldoende capaciteit om een variabele belasting van berichten vanwege de ZIM te kunnen verwerken. Omdat de exacte belasting per GBx flink kan verschillen moet iedere organisatie zelf een inschatting maken van de benodigde capaciteit en ervoor zorgen dat het GBx die belasting aankan. ; De waarden <GBx-verwerkingssnelheid-sturen> en <GBx-verwerkingssnelheid-opvragen> kunnen verschillen per gebruikte technologie. Voor de HL7v3-berichten gelden de waarden zoals opgenomen in de het configuratieinstellingendocument. Met betrekking tot FHIR dienen deze waarden nog afgestemd te worden met de diverse leveranciers. Deze waarden dienen vastgesteld te worden na afloop van de PoC. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/993a78a4fcd200ec1ceb781a8b0ccb564956d3192942e0caa91d3cc3d948802c.png)  
*Figure 2 : AORTA Eisen Kwaliteit aangesloten systemen - Betrouwbaarheid*  
ISO 25010 definieert Betrouwbaarheid als: De mate waarin een systeem, product of component gespecificeerde functies uitvoert onder gespecificeerde condities gedurende een gespecificeerde hoeveelheid tijd.

#### Borgen van de beschikbaarheid van een GBx

**Alias**: GBX.BES.e4010

| Details ; |
| --- |
| **Eis:** ; Met uitzondering van gepland onderhoud dient een GBx-applicatie te allen tijde beschikbaar te zijn voor het afhandelen van berichten. ; {GBZ} {GBP} De totale beschikbaarheid is minimaal 99,5%. ; {GBK} De totale beschikbaarheid is minimaal 90,0%. ; {GBO} De beschikbaarheid van het systeem is afhankelijk van procedurele afspraken tussen de uitwisselende partijen. ; **Toelichting bij eis:** ; Deze eis is nodig om te voorkomen dat een organisatie, die patiëntgegevens beschikbaar stelt of bereikbaar moet zijn om patiëntgegevens te ontvangen, de voor deze zaken benodigde systemen aan het eind van de werkdag uitschakelt. Deze eis betekent dat deze ICT-voorzieningen nagenoeg continu operationeel moeten zijn. De beschikbaarheid wordt als een voortschrijdend gemiddelde berekend. Omdat het GBK signaleringen kan ontvangen, is de eis verplicht voor GBK. ; **Implicaties:** ; Deze eis betekent dat deze ICT-voorzieningen nagenoeg continu operationeel moeten zijn. De beschikbaarheid wordt als een voortschrijdend gemiddelde berekend. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Minimaliseren van de impact van gepland onderhoud

**Alias**: GBX.BES.e4020

| Details ; |
| --- |
| **Eis:** ; Gepland onderhoud van een GBX-applicatie mag niet meer dan twaalf keer per jaar voorkomen en dient niet langer dan een uur te duren. Gepland onderhoud wordt bij voorkeur uitgevoerd binnen aangetoonde daluren. ; De beheerders van de ZIM moeten twee weken van te voren worden ingelicht door de systeembeheerder. ; **Toelichting bij eis:** ; Deze eis is nodig om te voorkomen dat een GBZ wegens onderhoud onnodig lang onbereikbaar is, ze betekent voor de organisatie dat onderhoud van de ICT-voorzieningen zoveel mogelijk wordt gepland en zodanig voorbereid dat het GBZ slechts kort onbeschikbaar hoeft te zijn. Omdat het GBK signaleringen kan ontvangen, is de eis verplicht voor GBK. ; **Implicaties:** ; Deze eis betekent voor de organisatie dat onderhoud van de ICT-voorzieningen zoveel mogelijk wordt gepland en zodanig voorbereid dat het GBX slechts kort onbeschikbaar hoeft te zijn. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Borgen van de betrouwbaarheid bij kleine storingen

**Alias**: GBX.BET.e4010.1

|  | Details ; |
| --- | --- |
| **Eis:** ; Kleine storingen in een GBx mogen niet meer dan gemiddeld keer per maand voorkomen en dienen dan binnen te zijn opgelost. ; **Toelichting bij eis:** ; De term 'kleine storing' is niet SMART gedefinieerd. Het kan vele soorten storingen betreffen. Het doel van deze eis is om te voorkomen dat een GBZ te vaak uitvalt en na een eenvoudig te verhelpen storing meteen langere tijd onbeschikbaar blijft. ; <ac:structured-macro ac:name="unmigrated-wiki-markup" ac:schema-version="1" ac:macro-id="aed2ce65-1953-4e10-9197-9db154973d09"><ac:plain-text-body><![CDATA[Deze eis betekent voor de zorgaanbieder dat zijn ICT-voorzieningen professioneel moet (laten) beheren. Dit vergt periodieke controle met eventueel preventief onderhoud. Verder moet een onverhoopte storing meteen worden gesignaleerd, zodat een GBZ-beheerder snel beschikbaar kan zijn om het probleem te verhelpen. Wellicht kan zijn XIS-leverancier hem daarbij helpen. Indien de zorgaanbieder een ASP-leverancier heeft geselecteerd voor zijn XIS, zal hij dit wellicht geheel delegeren aan die ASP-leverancier. De afspraken en procedures zoals opgenomen in de [AORTA DAP] dienen hierbij gevolgd te worden. ; ]]></ac:plain-text-body></ac:structured-macro> ; <ac:structured-macro ac:name="unmigrated-wiki-markup" ac:schema-version="1" ac:macro-id="c0af72eb-27c0-45c6-9c0c-f23bcd270c27"><ac:plain-text-body><![CDATA[Voor de waarden en moeten de waardes gehanteerd worden zoals zijn opgenomen in de [AORTA DAP]. Deze eis dient als kapstokeis. Het is mogelijk dat de tekst en variabele namen in de [AORTA DAP] afwijken van deze eis. ; | ]]></ac:plain-text-body></ac:structured-macro> ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Borgen van de betrouwbaarheid bij grote storingen

**Alias**: GBX.BET.e4020.1

| Details ; |
| --- |
| **Eis:** ; Grote storingen in een GBx mogen niet meer dan gemiddeld 2 keer per jaar voorkomen en dienen dan binnen 1 dag te zijn opgelost. ; **Toelichting bij eis:** ; De term 'grote storing' is niet SMART gedefineerd. Het kan vele soorten storingen betreffen. Het doel van deze eis is om te voorkomen dat een GBx na een ernstige storing zeer lang onbeschikbaar blijft. Onbeschikbaarheid zou bijvoorbeeld kunnen komen omdat er geen onderhoudscontract is en daardoor de hulp slechts langzaam op gang komt. ; Deze eis betekent voor de zorgaanbieder dat hij behalve professioneel beheer ook snel moet kunnen terugvallen op zijn XIS-leverancier, GZN en/of andere ICT-leveranciers. Zo moet bij ernstige storing, snel een leverancier beschikbaar zijn om het probleem te verhelpen. Wellicht kunnen zijn ICT-leveranciers hem een 24-uurs onderhoudscontract bieden. Indien de zorgaanbieder een ASP-leverancier heeft geselecteerd voor zijn XIS, zal hij dit wellicht geheel delegeren aan die ASP-leverancier. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/094f31b2c4853e27a43c6d6d453d8f3b95c042eda7f66445fdfbf59c0037a460.png)  
*Figure 3 : AORTA Eisen Kwaliteit aangesloten systemen - Beveiligbaarheid*  
ISO 25010 definieert Beveiligbaarheid als: De mate waarin een product of systeem informatie en gegevens beschermt zodat personen, andere producten of systemen de juiste mate van gegevenstoegang hebben passend bij hun soort en niveau van autorisatie.  
   
Dit schema toont de subcategorieën van Beveilgbaarheid volgens ISO 25010.

#### Beveiliging van patiëntgegevens in het GBx

**Alias**: GBX.BVL.e4060

| Details ; |
| --- |
| **Eis:** ; Voor een GBx moet zijn gedefinieerd: ;  welke landelijke toepassingen en systeemrollen worden ondersteund en gebruikt; ;  hoe de grenzen van het GBx lopen door de ICT-voorzieningen van de organisatie; ;  hoe en wanneer patiëntgegevens die grenzen kunnen passeren; ;  hoe wordt gewaarborgd dat patiëntgegevens in de dossiers en postbussen niet kunnen lekken naar onbetrouwbare bestemmingen; ;  hoe wordt gewaarborgd dat patiëntgegevens uit onbetrouwbare bronnen niet kunnen terechtkomen in de dossiers en postbussen of de ZIM; ;  hoe wordt gewaarborgd dat anderen dan bevoegde gebruikers geen fysieke toegang tot (delen van) het GBx kunnen krijgen. ; **Toelichting bij eis:** ; Deze eis is nodig om te voorkomen dat patiëntgegevens, bijvoorbeeld via een andere applicatie, door willekeurige medewerkers kunnen worden benaderd terwijl de organisatie zijn GBx heeft beveiligd met firewalls, authenticatie- en vertrouwensmiddelen. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Documentverificatie  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Borgen van plicht tot uitwisselen van patiëntgegevens

**Alias**: GBX.BVL.e4070

| Details ; |
| --- |
| **Eis:** ; Als een GBx voor een systeemrol is aangesloten op de ZIM, moet dat GBx patiëntgegevens in het kader van die systeemrol ook daadwerkelijk uitwisselen onder de regie van de ZIM. ; **Toelichting bij eis:** ; Alle aan AORTA deelnemende partijen zijn gebaat bij een zo volledig mogelijk beeld van relevante patiëntgegevens, daarom is het van belang dat aangesloten partijen hun gegevens ook daadwerkelijk beschikbaar maken via AORTA. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Een GBx beschikt over een geldig UZI/PKIO-servercertificaat

**Alias**: GBX.BVL.e4080 (voorheen GBX.BVL.e4080.1)

| Details ; |
| --- |
| **Eis:** ; Een GBx dient een {GBx}UZI- of {GBK}{GBP}{GBO} PKIO-servercertificaat te hebben dat op naam staat van de opdrachtgever en is gecertificeerd door een Certificate Authority (CA) onder de root van de Staat der Nederlanden. ; **Toelichting bij eis:** ; Deze eis is nodig opdat de authenticiteit van het GBx en de exclusiviteit van getransporteerde gegevens door een Trusted Third Party (TTP) kan worden gewaarborgd. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Aansluittoets  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Beveiligde opslag

**Alias**: SYS.BVL.e4010

| Details ; |
| --- |
| **Eis:** ; Data die persoonsgegevens bevatten dienen versleuteld en beveiligd te worden opgeslagen. Het gaat hierbij om alle opgeslagen data (bv. logging en backups). ; **Toelichting bij eis:** ; In principe moet alle data met persoonsgegevens worden geëncrypted. Dit betreft o.a. gegevens die worden opgeslagen ten behoeve van een autorisatiesessie. Mocht hiervan met het oog op systeemprestaties van afgeweken worden, dan dient dit overlegt te worden met de DVZA-opdrachtgever. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Audit  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/75448c0d298dbf9ac29fd4e35eba49135602db468df984e154a1b131875aea0e.png)  
*Figure 4 : AORTA Eisen Kwaliteit aangesloten systemen - Uitwisselbaarheid*  
ISO 25010 definieert Uitwisselbaarheid als: De mate waarin een product, systeem of component informatie uit kan wisselen met andere producten, systemen of componenten, en/of het de gewenste functies kan uitvoeren terwijl het dezelfde hard- of software-omgeving deelt.  
Dit diagram toont de subcategorieën zoals gedefinieerd door ISO 25010.

#### Communicatie met het LSP via een GZN

**Alias**: GBX.CON.e4010, GBX.CON.e4010.1

| Details ; |
| --- |
| **Eis:** ; Een GBx dient via een DCN van een gekwalificeerde GZN te communiceren met het LSP. ; **Toelichting bij eis:** ; Organisaties kunnen bij VZVZ verifiëren of een netwerkaanbieder over een GZN-kwalificatie beschikt. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Aansluittoets  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Gebruik van IP en DNS

**Alias**: GBX.CON.e4020, GBX.CON.e4020.1, GBX.CON.e4020.2

| Details ; |
| --- |
| **Eis:** ; Een GBx moet bereikbaar zijn voor de ZIM: ;  {GBx}{GBO} via het IP-adres dat is toegekend aan het GBx en dat is verkregen door DNS-vertaling van de hostnaam van dat GBx; ;  {GBK} via het IP-adres dat door het LSP is toegekend aan het GBK en dat is verkregen door DNS-vertaling van de hostnaam van dat GBK; ;  {GBP} via het IP-adres en de fully qualified domain name (FQDN) die door het LSP zijn toegekend aan het GBP en waarvoor het LSP de DNS-vertaling biedt. ; De ZIM moet bereikbaar zijn vanuit een GBx via het IP-adres van de operationele ZIM, dat is verkregen door DNS-vertaling van de hostnaam van de ZIM. ; Voor de DNS-vertaling geldt dat: ;  de hostnaam een maximale time-to-live (TTL) heeft voor verversing van de cache; ;  het IP-adres van de ZIM zich binnen een vooraf overeengekomen range bevindt die altijd gerouteerd moet worden naar de GZN; ;  een systeem vanuit de applicatie alleen benaderd mag worden op de FQDN. Vertaling naar IP-adres wordt door de DNS uitgevoerd. ; Een GBx mag de volgende IP-adressen niet intern gebruiken: ;  het IP-adres dat door het LSP is uitgegeven voor het GBx als geheel, ;  de IP-adressen die zijn gereserveerd voor de ZIM, ;  de IP-adressen uit het landelijke IP-nummerplan van het LSP. ; **Toelichting bij eis:** ; Deze eis is nodig om ervoor te zorgen dat FQDN en IP-adressen op een juiste wijze worden ingesteld. ; Deze eis is ook nodig voor het gebruik van een ZIM op twee operationele locaties en om IP-netwerkconflicten te voorkomen. ; Deze eis betekent voor de organisatie dat die voor zijn GBx/GBO een FQDN moet krijgen van zijn GZN en deze laten registreren bij het LSP of bij SIDN. De GZN zal daaraan een IP-adres toekennen. De organisatie moet het toegekende IP-adres tenslotte (laten) configureren in zijn netwerkapparatuur binnen zijn GBx. Deze eis betekent dat een applicatie een ZIM expliciet op naam benadert en dat systemen geconfigureerd moeten worden voor het gebruik van DNS. Door middel van DNS-resolving kan voor het GBx transparant gebruik gemaakt worden van de operationele ZIM op locatie 1 of locatie 2. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Aansluittoets  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Tijdsynchronisatie GBx en ZIM

**Alias**: GBX.CON.e4030, GBX.CON.e4030.1

| Details ; |
| --- |
| **Eis:** ; Een GBx dient NTP te gebruiken voor tijdsynchronisatie met de ZIM. De tijdklok van een GBx mag niet meer dan een halve seconde afwijken van de tijdklok van de ZIM. ; **Toelichting bij eis:** ; Deze eis is nodig om te voorkomen dat de tijdklok van het GBx gaat afwijken van de tijdklok van de ZIM. Voor eenzelfde interactie tussen een GBx en de ZIM moeten beide systemen immers dezelfde tijdstempels loggen. Dit is belangrijk wanneer de toezichthouder of patiënt een geval van vermeend onrechtmatige uitwisseling van patiëntgegevens wil onderzoeken en daartoe zowel de lokale toegangslog van het GBx als de centrale toegangslog van het LSP wil raadplegen. ; Deze eis betekent voor de organisatie dat er binnen het GBx een NTP-client is geïnstalleerd en dat deze is afgestemd op de NTP-server van de ZIM. Ook is het mogelijk dat de GZN een gezamenlijke NTP-client beheert voor alle aangesloten zorgaanbieders en op een andere wijze klaarspeelt dat de tijdklok van hun GBx'en gelijk lopen met die van de ZIM. Deze eis betekent voor de organisatie dat het GBx periodiek moet synchroniseren met de ZIM. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Aansluiting op productie-omgeving LSP

**Alias**: GBX.CON.e4120

| Details ; |
| --- |
| **Eis:** ; GBZ-beheerder moet er namens de eigenaar van het GBZ op toezien dat uitsluitend productiesystemen gekoppeld worden aan de productie-omgeving van het LSP. Overtredingen van deze eis zullen gemeld worden aan de eigenaar van het GBZ. ; **Toelichting bij eis:** ; Vanwege mogelijke beveiligingsrisico's en kwaliteitgaranties in de keten mogen er alleen GBZ-en met een geaccepteerde XIS-applicatie aansluiten op de productie-omgeving van het LSP . ; Bij het niet naleven van bovenstaande eis behoudt VZVZ zich het recht voor op aanvullende sancties. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

### AORTA Eisen Kwaliteit applicatie

![Diagram](../../../../assets/5f965dfcf16e3091324176683daaf64f73452ac1242eef5fa1b664cefb158024.png)  
*Figure 5 : AORTA Eisen Kwaliteit applicatie - Beveiligbaarheid*  
ISO 25010 definitieert Beveiligbaarheid als: De mate waarin een product of systeem informatie en gegevens beschermt zodat personen, andere producten of systemen de juiste mate van gegevenstoegang hebben passend bij hun soort en niveau van autorisatie.

#### Afbreken van een gebruikerssessie

**Alias**: GBX.IDA.e4090

| Details ; |
| --- |
| **Eis:** ; Het systeem moet een gebruikerssessie voor het landelijk uitwisselen van patiëntgegevens op vertrouwensniveau laag of midden afsluiten: ;  op commando van de gebruiker (zoals een muisklik of toetsencombinatie); ;  door uitnemen van het vertrouwensmiddel door de zorgverlener/medewerker; ;  wanneer de applicatie gedurende gebruiker-max-applicatie-onbruik niet is gebruikt; ;  wanneer de se*ssie gedurende* open staat. ;  IP-adres van gebruiker gedurende een sessie wijzigt. ; De parameter gebruiker-max-applicatie-onbruik is binnen de applicatie instelbaar, naar redelijkheid en risico, en heeft een maximale waarde van 60 minuten. ; **Toelichting bij eis:** ; Dit is nodig opdat een gebruiker zelf zijn gebruikerssessie kan uitloggen met de zekerheid dat niemand anders zijn sessie kan voortzetten en vervolgens zijn bevoegdheden kan misbruiken. Daarnaast is deze eis nodig om te tegen te gaan dat een in onbruik geraakte sessie door een onbevoegde kan worden misbruikt. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Opzetten beveiligde verbinding met de ZIM

**Alias**: GBX.CON.e4080.4

| Details ; |
| --- |
| **Eis:** ; Het GBx dient voor het landelijk uitwisselen van patiëntgegevens een TLS-sessie met de ZIM met de volgende kenmerken op te zetten: ;  tweezijdige authenticatie met behulp van het servercertificaat van de ZIM en ;  (indien tokenauthenticatie) het servercertificaat van het GBx voor vertrouwensniveau midden ;  het servercertificaat van het GBx voor vertrouwensniveau laag {GBK} en midden ;  tijdelijke sleutels die elke applicatie-max-sleutel-duur ververst worden door middel van TLS Secure Renegotiation; ;  gebruikmakend van Cipher Suites die door het NCSC minimaal worden gekenmerkt als voldoende; ;  gebruikmakend van de sterkste cipher suite die gedeeld wordt met de ZIM; ;  gebruikmakend van de hoogste toegestane TLS-versie die door beide partijen wordt ondersteunt; ;  een ten hoogste ongebruikte TLS-sessie van applicatie-max-sessie-onbruik. ; **Toelichting bij eis:** ; Dit is nodig opdat een GBx een voldoende hoog beveiligingsniveau kan afdwingen bij het opzetten van een TLS-sessie met de ZIM. ; Dit betekent voor de organisatie dat hij of zijn XIS-leverancier de bovenstaande parameters moet instellen in de TLS-library in de betrokken applicatie(s) en/of de eventuele communicatieserver. Het GBx is niet in staat te controleren of de ZIM daadwerkelijk het (server)certificaat van de GBx opvraagt, maar mag er impliciet van uitgaan dat dit gebeurt en dat de ZIM het certificaat ook controleert. Hiermee wordt tweezijdige authenticatie bewerkstelligd. ; |

**Vzvz_Moscow**: Conditioneel.  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Instellen configuratieparameters t.b.v. communicatie en authenticatie van de ZIM

**Alias**: GBX.FBH.e4050.2

| Details ; |
| --- |
| **Eis:** ; De GBx-beheerder moet de volgende configuratieparameters in het GBx kunnen instellen: ;  URI en hostnaam van de ZIM, ;  applicatie-id, ;  applicatie-id van het operationele schakelpunt waarop kan worden aangesloten. ; **Toelichting bij eis:** ; Dit is nodig opdat een GBx deze parameters kan gebruiken bij de HTTP-communicatie met en authenticatie van de ZIM. ; De in het GBx ingestelde waarden komen overeen met de in het applicatieregister van de ZIM geregistreerde gegevens. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Opzetten en gebruiken van TLS-sessies

**Alias**: GBX.CON.e4070.2

| Details ; |
| --- |
| **Eis:** ; Het GBx moet na het beschikbaar worden voor de ZIM: ;  verzoeken van de ZIM voor het opzetten van nieuwe TLS-sessies honoreren ten behoeve van berichtuitwisseling voor andere zorgaanbieders, ;  {GBx}{GBK}{GBO} voor gebruikers die landelijk patiëntgegevens willen uitwisselen, een of meer TLS-sessies met de ZIM (her)gebruiken voor berichtuitwisseling als gevolg van gebruikersfuncties. ; **Toelichting bij eis:** ; Deze eis is nodig opdat een GBx beveiligd kan communiceren met de ZIM volgens bewezen technologie op eigen initiatief en op initiatief van de ZIM. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Opzetten beveiligde verbinding vanuit de ZIM met een GBx

**Alias**: GBX.CON.e4090.2

| Details ; |
| --- |
| **Eis:** ; Het GBx dient voor het landelijk uitwisselen van patiëntgegevens een TLS-sessie met de ZIM met de volgende kenmerken te accepteren: ;  tweezijdige authenticatie met behulp van het UZI-servercertificaat van het GBZ en het servercertificaat van de ZIM, ;  tijdelijke sleutels die elke systeem-max-sleutel-duur ververst worden, ;  gebruikmakend van Cipher Suites die door het NCSC minimaal worden gekenmerkt als voldoende(goed dus altijd ook) en tevens worden ondersteund door de ZIM.Voor encryptie moet altijd de sterkste vorm als eerste worden geprobeerd, ;  een maximale sessieduur van systeem-max-sessie-duur, ;  een ten hoogste ongebruikte TLS-sessie van systeem-max-sessie-onbruik. ; **Toelichting bij eis:** ; Dit is nodig opdat de ZIM een voldoende hoog beveiligingsniveau kan afdwingen bij het opzetten van een TLS-sessie met een GBx. ; Dit betekent voor de zorgaanbieder dat hij of zijn XIS-leverancier de bovenstaande parameters moet instellen in de TLS-library in de betrokken XIS-applicatie(s) en/of de eventuele communicatieserver. ; |

**Vzvz_Moscow**: Conditioneel.  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Hardening

**Alias**: SYS.BVL.e4065

| Details ; |
| --- |
| **Eis:** ; Er dient hardening op de diverse systeemlagen te worden toegepast. Het gaat hierbij om hardening op het niveau van operating system, middleware en database. ; Alle systeemparameters dienen zodanig te zijn ingesteld dat met behoud van de gewenste functionaliteit een zo hoog mogelijk niveau van beveiliging bestaat. ; **Toelichting bij eis:** ; De intentie van deze eis is dat datgene wordt gedaan dat in de markt onder de gangbare maatregelen wordt gerekend op het gebied van hardening. Hierbij moet er uiteraard een afweging worden gemaakt tussen gebruiksvriendelijkheid en veiligheid. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Audit  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Toegangslog bijhouden (FHIR)

**Alias**: GBX.LOG.e4016

| Details ; |
| --- |
| **Eis:** ; Het systeem moet alle binnenkomende en uitgaande berichten loggen in de toegangslog. Hierbij dienen onderstaande gegevens gelogd te worden, indien aanwezig in het bericht: ;  de identiteit van de patiënt/cliënt/burger (BSN) waar het bericht betrekking op heeft; ;  de identiteit van de organisatie waar het bericht vandaan komt of naar toe wordt gestuurd; ;  de functie en identiteit van de zorgverlener, medewerker of patiënt zoals opgenomen in het verstuurde en/of ontvangen bericht. De functie is de aorta-rolcode zoals opgenomen in het claim-element van het transactietoken. ;  de gebruikersinteractieID. Dit is een combinatie van HTTP-operatie, de URL inclusief de ontvangen zoekparameters en de contentVersion uit de AORTA-Version header; ;  het tijdstip en tijdzone (ten opzichte van UTC) van het moment dat het bericht ontvangen/verstuurd is; ;  de bericht-id van het ontvangen/verstuurde bericht. Dit is het messageID in de HTTP header; ;  het initiële bericht-id van het ontvangen/verstuurde bericht. Dit is het initialMessageID in de HTTP header; ;  de aan het bericht gekoppelde gegevensdienst. Dit is de waarde zoals opgenomen in de scope van het transactietoken; ;  een indicatie van eventueel opgetreden foutsituaties met betrekking tot het ontvangen en verzenden van de berichten. Hierbij dient de HTTP-foutcode, alle informatie in de eventueel aanwezige operationOutcome en de enventuele WWW-Authenticate HTTP response header gelogd te worden. ; **Toelichting bij eis:** ; Het doel van de logging is het inzichtelijk kunnen maken van de datastroom door de gehele keten. Het inzichtelijk maken van de loggegevens kan van belang zijn voor auditredenen of beheerwerkzaamheden zoals het oplossen van fouten in de keten. Deze eis is conform de vereisten zoals beschreven in de NEN7513. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/3af6a7a9acae6be85136e363594a0bbb8c9c0d96b28646bf89bea29cc29094da.png)  
*Figure 6 : Generieke eisen*

#### Onderscheiden van fictieve gegevens

**Alias**: GBX.BVL.e4090

| Details ; |
| --- |
| **Eis:** ; Het systeem moet fictieve gegevens opvallend onderscheidend presenteren aan gebruikers. ; **Toelichting bij eis:** ; Deze eis dient om onjuist gebruik van fictieve gegevens te voorkomen. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: n/a  
   
![Diagram](../../../../assets/cd58a85d00aee14371c094917bdc3481e76425b9cd3c1c289ffab28319969f80.png)  
*Figure 7 : AORTA Eisen Kwaliteit applicatie - Uitwisselbaarheid*  
ISO 25010 definieert Uitwisselbaarheid als: De mate waarin een product, systeem of component informatie uit kan wisselen met andere producten, systemen of componenten, en/of het de gewenste functies kan uitvoeren terwijl het dezelfde hard- of software-omgeving deelt.

#### Ondersteunen servercertificaten en ondertekeningalgoritmen

**Alias**: GBX.CON.e4110.2

| Details ; |
| --- |
| **Eis:** ; Het GBx dient UZI/PKIo-servercertificaten van de (verschillende) generatie(s) te ondersteunen zoals beschikbaar wordt gesteld door het UZI-Register. ; Er moet gebruik worden gemaakt van het SHA-256 ondertekeningsalgoritme. ; **Toelichting bij eis:** ; Het UZI-register geeft UZI-servercertificaten uit onder één of meerdere certificaatbomen. In het geval er onder diverse certificaatbomen UZI-servercertificaten wordt uitgegeven, is het zaak om alle servercertificaten uitgegeven onder de diverse certificaatbomen te kunnen ondersteunen. ; Een GBX-communicatieserver dient te zijn ingericht op het ondertekeningalgoritme SHA-256. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Kenbaar maken Certificate Authorities

**Alias**: GBX.CON.e4100

| Details ; |
| --- |
| **Eis:** ; Het GBx dient alleen de keten van Certificate Authorities (CA's) van het GBX-certificaat kenbaar te maken aan de ZIM in het "certificate request" bericht van de TLS-handshake, waaronder ook het stamcertificaat (Root CA) van de keten. ; **Toelichting bij eis:** ; Dit is nodig opdat een GBx beperkt kenbaar maakt welke CA's het vertrouwt. ; Dit betekent voor de zorgaanbieder dat hij of zijn XIS-leverancier selectief om moeten gaan met het aantal CA's waarmee de betrokken XIS-applicatie(s) en/of de eventuele communicatieserver worden opgezet. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Aansluittoets  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Afhandelen transactietoken

**Alias**: GBX.CON.e4140.2

| Details ; |
| --- |
| **Eis:** ; Het XIS moet een ontvangen transactietoken correct kunnen verwerken. Hiervoor dienen door het ontvangende systeem de controles uitgevoerd te worden zoals beschreven in de Implementatiehandleiding Transactietoken JWT (( ;  [https://vzvz.atlassian.net/wiki/display/UBEBVLEL/Implementatiehandleiding+Reagerend+GBZ](https://vzvz.atlassian.net/wiki/display/UBEBVLEL/Implementatiehandleiding+Reagerend+GBZ) ;  ). ; Indien een FHIR-search niet wordt begeleid door een transactietoken, dan dient de bevraging beantwoord te worden met een foutmelding. ; **Toelichting bij eis:** ; In combinatie met bepaalde berichten is het mogelijk dat er transactietokens worden toegevoegd. De specificatie en de juiste technische verwerking van het transactietoken staan beschreven in de IH Transactietoken JWT ( ;  [https://vzvz.atlassian.net/wiki/display/UBEBVLEL/Implementatiehandleiding+Reagerend+GBZ](https://vzvz.atlassian.net/wiki/display/UBEBVLEL/Implementatiehandleiding+Reagerend+GBZ) ;  ). ; Het doel van het transactietoken is tweeledig: ;  Ten eerste is het bedoeld als gegevensdrager. Er worden een aantal gegevenselementen opgenomen, die niet in het bericht zitten. Deze gegevenselementen dienen uit het token gehaald te worden en te worden gebruikt in de verdere verwerking van het bericht. Hierbij dienen de controles plaats te vinden zoals beschreven in de IH Transactietoken. ;  Ten tweede kan het transactietoken gebruikt worden t.b.v. authenticatie of als bewijs van autorisatie. Het is mogelijk om op basis van de certificaatreferenties te controleren of het token van de juiste afzender afkomstig is en dat de opvrager geautoriseerd is voor bevraging van specifieke patiëntgegevens. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Protocolstack voor gegevensuitwisseling o.b.v. FHIR

**Alias**: GBX.CON.e4130.1

| Details ; |
| --- |
| **Eis:** ; Het GBx dient voor berichtuitwisseling met de ZIM de volgende protocolstack te gebruiken: ;  HL7 FHIR ;  JWT ;  HTTP v1.1/HTTP v2.0 ;  TLS-verbindingen met NCSC beveiligingsniveau “goed” ;  TCP ;  IPv4 ; **Toelichting bij eis:** ; Het is niet toegestaan om een lagere protocolversie te hanteren dan die in deze protocolstack vermeld is. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

### Eisen aan de beheerorganisatie van een GBX

![Diagram](../../../../assets/c49aa7aa38415d2cc82af889916bfb62a1594d7a089b976cedc6824a0a8be628.png)  
*Figure 8 : Eisen aan de beheerorganisatie van een GBX*

#### Ondersteuning van gebruikers bij problemen met de landelijke uitwisseling van informatie

**Alias**: GBX.FBH.e4010

| Details ; |
| --- |
| **Eis:** ; De GBx-servicedesk dient gebruikers te ondersteunen bij GBx-, GZN- en LSP-gerelateerde problemen. De GBx-servicedesk dient: ;  Gebruikers een inschatting te geven van de verwachte oplostermijn; ;  Gebruikers regelmatig te informeren over de voortgang van de oplossing; ;  Tijdens kantooruren telefonisch bereikbaar te zijn voor gebruikers, GZN-leveranciers en het LSP-beheer; ;  Voor noodgevallen telefonisch bereikbaar te zijn voor gebruikers, de GZN en het LSP; ;  Incidenten en problemen te registreren en beheren; ;  een procedure geïmplementeerd te hebben voor het melden en afhandelen van incidenten en wijzigingsverzoeken conform het Dossier Afspraken en Procedures ([AORTA DAP](https://www.vzvz.nl/uploaded/FILES/htmlcontent/AORTA_DAP_20140130_v2.3.pdf)); ;  Nederlandstalig te zijn. ; **Toelichting bij eis:** ; Het doel van deze eis is om de landelijke elektronisch uitwisseling van gegevens door gebruikers te bevorderen, de diensten van AORTA te verbeteren en verstoringen te signaleren, voorkomen en verhelpen. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Aansluittoets  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Instrueren systeemgebruikers over beveiligingsbeleid

**Alias**: GBX.FBH.e4015

| Details ; |
| --- |
| **Eis:** ; Systeemgebruikers binnen een GBZ dienen op de hoogte te zijn van het beveiligingsbeleid en dienen het beveiligingsbeleid na te leven. In het beveiligingsbeleid dient in ieder geval aandacht te zijn voor: ;  Het gebruik van de systemen en de toegang daartoe; ;  Het gebruik van de UZI-pas (indien door het XIS gebruikt); Hierbij dient in ieder geval de verantwoordelijkheden met betrekking tot het bezit en het gebruik van de UZI-pas benoemd worden. ;  Het concept van mandatering (indien door het XIS gebruikt); Hierbij dient in ieder geval aandacht besteed te worden aan de juiste fijnmazigheid waarop gemandateerd mag worden. De verantwoordelijkheid die wordt weergegeven in een mandaattoken moet bij de reële organisatiestructuur en werkwijze horen. ; Het concept van inschrijftoken (indien door het XIS gebruikt). ; **Toelichting:** ; Een GBZ moet concreet beleid maken om het bewustzijn van het beveiligingsbeleid onder de medewerkers en zorgverleners te bevorderen en iedereen te wijzen op zijn verantwoordelijkheden. ; Beleid om bewustzijn onder personeel te bewerkstelligen horen al standaard onderdeel te zijn van beveiligingsmaatregelen binnen een GBZ. Dit is voorgeschreven in NEN 7510, 7.2.2. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Toekennen functiescheiding tussen systeemgebruikers

**Alias**: GBX.FBH.e4025

| Details ; |
| --- |
| **Eis:** ; Het autorisatiebeleid binnen een organisatie moet rekening houden met het onderscheid tussen systeemgebruikers die gebruik mogen maken van LSP-functionaliteiten en systeemgebruikers die geen toegang tot deze functionaliteiten mogen hebben. De verantwoordelijke voor het toekennen van autorisaties binnen de organisatie dient in het systeem de juiste autorisaties toe te kennen aan de systeemgebruikers. ; **Toelichting:** ; GBZ-en zouden een additionele toegangscontrole moeten implementeren voor het initiëren van interacties met het LSP. Een medewerker met toegang tot het systeem van een GBZ zou niet automatisch ook toegang moeten hebben tot de functies om het LSP te bevragen. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Beheren van en toegang verschaffen tot de toegangslog

**Alias**: GBX.SBH.e4010

| Details ; |
| --- |
| **Eis:** ; De organisatie moet een toegangslogbeheerder benoemen. De toegangslogbeheerder moet verzoeken van de toezichthouder om de lokale toegangslog te raadplegen inwilligen. ; **Toelichting bij eis:** ; Deze eis is nodig omdat de toezichthouder op AORTA voor het uitvoeren van haar bevoegdheden informatie nodig kan hebben over de gebeurtenissen waarbij het GBx met het LSP informatie heeft uitgewisseld. ; {GBx} Deze toegangslogbeheerder kan door alle zorgverleners worden gemandateerd om de toegangslog te raadplegen, om zo te voorkomen dat hij voor een verzoek tot raadplegen van de lokale toegangslog inzake een bepaalde patiënt/cliënt steeds de behandelende zorgverleners moet inschakelen. ; {GBK} Deze toegangslogbeheerder kan worden gemandateerd om de toegangslog te raadplegen door de GBK-verantwoordelijke. ; {GBP} Deze Logbeheerder dient vóór de aansluiting aan het LSP te worden doorgegeven aan VZVZ. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Audit  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Systeembeheer van een GBx

**Alias**: GBX.SBH.e4020 (voorheen GBX.SBH.e4020.2)

| Details ; |
| --- |
| **Eis:** ; De rol van systeembeheerder moet door de organisatie expliciet benoemd en belegd zijn. ; De systeembeheerder en diens vervanger(s) dienen met actuele telefoonnummers bekend te zijn bij de LSP-beheerder en de centrale AORTA servicedesk. Tenminste één beheerder dient altijd bereikbaar te zijn en in staat om de nodige beheertaken uit te voeren. ; De systeembeheerder dient verzoeken van het LSP met betrekking tot het configureren van het GBx en het activeren/deactiveren van op het LSP aangesloten systeem in te willigen. ; **Toelichting bij eis:** ; Deze eis zorgt ervoor dat een systeembeheerder altijd kan worden gewaarschuwd als er problemen zijn met een GBx, die ingrijpen van de systeembeheerder vergen. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Documentverificatie  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Actueel houden van het applicatieregister

**Alias**: GBX.SBH.e4030

| Details ; |
| --- |
| **Eis:** ; GBX-beheer moet de beheerde GBX-applicatie(s) bij LSP-beheer aanmelden zodat deze in het applicatieregister kan worden opgenomen en zodat GBX-beheer de status ervan actueel kan houden in [Supportal](https://supportal.vzvz.nl). ; **Toelichting bij eis:** ; Deze eis is nodig om te kunnen participeren in berichtuitwisselingen via AORTA. Het actueel houden van het applicatieregister is belangrijk voor een correcte afhandeling van berichten. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Documentverificatie  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Beperking inzage door beheerder

**Alias**: GBX.SBH.e4040.3

| Details ; |
| --- |
| **Eis:** ; De systeembeheerder mag de inhoud van berichten slechts inzien indien dit noodzakelijk is voor het oplossen van problemen, is ingelogd met een tweefactorauthenticatiemiddel en uitsluitend op verzoek van een: ;  {GBZ} zorgverlener/medewerker; ;  {GBP} patiënt/klant, een leidinggevende of de Toezichthouder. ; **Toelichting bij eis:** ; Vanuit zijn ondersteunende rol kan het voor een servicedeskmedewerker ({GBP}, servicemanager ({GBP}) of een beheerder nodig zijn de inhoud van berichten in te zien, bijvoorbeeld om een mogelijk verschil in twee berichten die dezelfde inhoud zouden moeten hebben te onderzoeken. Mede vanwege deze eis is het nodig dat de beheerder expliciet door de organisatieverantwoordelijke is aangewezen. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Bijhouden van een beheerlog

**Alias**: GBX.SBH.e4050

| Details ; |
| --- |
| **Eis:** ; Beheerhandelingen moeten worden vastgelegd in een beheerlog. De organisatie dient de opdrachtgever en toezichthouder inzage te geven in deze beheerlog. In het beheerlog wordt bijgehouden welke systeembeheerder de inhoud van welke berichten heeft ingezien. ; **Toelichting bij eis:** ; De beheerlog ondersteunt de controle op de juiste werking van systemen en de controle op het volgen van procedures. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Kennisvergaring m.b.t. GBX-beheer

**Alias**: GBX.SBH.e4060

| Details ; |
| --- |
| **Eis:** ; De GBX-organisatie dient voordat zij een beheerorganisatie van een op de productie-omgeving van AORTA draaiend systeem wordt, ervoor te zorgen dat de binnen de GBX-organisatie aangewezen persoon met als rol GBX-beheerder de GBX-workshop van VZVZ heeft gevolgd. ; **Toelichting bij eis:** ; Uit de praktijk blijkt dat partijen de workshop nodig hebben om zich een goed beeld te vormen van de samenwerking tussen de eigen beheerorganisatie en de andere GZN-, GBZ- en LSP-beheerorganisaties in de keten. Daarbij biedt VZVZ in de productiefase verschillende vormen van ondersteunende dienstverlening en een escalatiepad op ketenniveau. Deze ketensamenwerking vergroot de efficiency en effectiviteit van inzet van resources, en voorkomt dat verstoringen onnodig lang duren. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Aansluittoets  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Een GBx valt onder Nederlandse wet- en regelgeving

**Alias**: GBX.CON.e4050.1

| Details ; |
| --- |
| **Eis:** ; De technische infrastructuur van het GBX dient zich in de Europese Unie te bevinden. De voertaal met de zorgaanbieder en de organisatie die het GBx beheert en exploiteert is Nederlands. Met betrekking tot de contracten tussen de zorgaanbieder en bovengenoemde moet de Nederlandse wet-en regelgeving van toepassing zijn. ; De zorgaanbieder en de organisatie's die het GBX beheert en exploiteert dient in Nederland gevestigd te zijn. ; In de contracten tussen de zorgaanbieder en bovengenoemde moet de Nederlandse wet- en regelgeving van toepassing zijn. ; **Toelichting bij eis:** ; Dit is nodig om er voor te zorgen dat de infrastructuur en dienstverlening volledig onder Nederlandse wet- en regelgeving valt. De exploitant dient waarborgen actief te hebben die voorkomen dat gegevens oneigenlijk gebruikt kunnen worden en te voldoen aan de privacy wetgeving. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Aansluittoets  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Vernietigen materialen volgens standaarden

**Alias**: GBX.SBH.e4070

| Details ; |
| --- |
| **Eis:** ; Om te voorkomen dat privacygevoelige of beveiliging gerelateerde gegevens achterblijven en in ongewenste handen vallen dienen niet (meer) gebruikte websites, apps, informatie of code te worden vernietigd volgens de standaard [DoD 5220.22-M (E)](http://www.dss.mil/documents/odaa/nispom2006-5220.pdf). Te vervangen fysieke opslagmedia dienen gecontroleerd vernietigd te worden volgens DIN 32757. ; **Toelichting bij eis:** ; Er is een proces nodig dat controleert of gegevens nog noodzakelijk zijn en te verwijderen gegevens voorgoed vernietigt. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Eigenverklaring  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Business

#### Voldoen aan wet- en regelgeving

**Alias**: GBX.ALG.e4010

| Details ; |
| --- |
| **Eis:** ; Een GBX dient te voldoen aan de NEN751x normen. ; **Toelichting bij eis:** ;  In de wet gebruik BSN in de zorg Artikel 2 Lid 4a is afgedwongen dat de gegevensverwerking, zoals bedoelt in de bijbehorende wet, aantoonbaar moet voldoen aan de NEN7510. ;  In de concept AMvB aanvullende bepalingen verwerking persoonsgegevens in de zorg wordt in artikel 5 gesteld dat de netwerkverbindingen (intern netwerk en GZN) moeten voldoen aan het bepaalde in NEN 7512 en in artikel 7 wordt gesteld dat de logging van zorgaanbieders moet voldoen aan het bepaalde in NEN 7513. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Eigenverklaring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Loggen toegangsregeling

**Alias**: AGE.LOG.e4070

| Details ; |
| --- |
| **Eis:** ; Elke wijziging in de toegangsregeling dient te worden gelogd. Hierbij moet onweerlegbaar kunnen worden vastgesteld welke persoon met welke rol welke specifieke aanpassing heeft doorgevoerd. ; **Toelichting** ; Conform NEN 7513:2018 Paragraaf 6.3 ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: n/a  
**Vzvz_Req_Soort**: n/a  
**Vzvz_Req_Type**: n/a

#### Bewaartermijn loggegevens

**Alias**: AGE.LOG.e4010

| Details ; |
| --- |
| **Eis:** ; De bewaartermijn van de toegangsloggegevens is *<toegangslog_bewaartermijn>.* Voor de overige logs (technische logs) geldt een bewaartermijn van *<systeemlog_bewaartermijn>.* ; **Toelichting bij eis:** ; Voor de toegangslog (log met betrekking tot patiëntgegevens) geldt (mogelijk) een andere bewaartermijn dan voor de systeemlog. Conform NEN 7513:2018 paragraaf 8.5 kan een patiënt binnen een bepaalde tijdsperiode nog aanspraak maken op inzage in de loggegevens. Deze tijdsperiode kan voor de technische log echter onnodig lang zijn en daarmee onnodig veel opslagcapaciteit verbruiken. ; De waarden *<toegangslog_bewaartermijn>* en *<systeemlog_bewaartermijn>* kunnen per afsprakenstelsel/architectuur afgesproken worden. Indien deze waarden niet expliciet ingevuld worden door het afsprakenstelsel/architectuur, dan geldt voor beide de waarde 5 jaar. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Business

#### Loggen inzage logging

**Alias**: AGE.LOG.e4020

| Details ; |
| --- |
| **Eis:** ; Elke inzage van de toegangslog dient gelogd te worden. Hierbij moet onweerlegbaar kunnen worden vastgesteld welke persoon met welke rol inzage heeft gehad in welke specifieke gegevens. ; **Toelichting** ; Deze eis is conform NEN 7513:2018. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Audit  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Uitschakelen logging

**Alias**: AGE.LOG.e4030

| Details ; |
| --- |
| **Eis:** ; Het loggen van de berichtuitwisseling in de toegangslog en het loggen van acties op de toegangslog mogen niet uitgeschakeld kunnen worden. ; **Toelichting bij eis:** ; Conform NEN 7513:2018 Paragraaf 6.4.2 ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: n/a  
**Vzvz_Req_Soort**: n/a  
**Vzvz_Req_Type**: n/a

#### Vernietigen loggegevens

**Alias**: AGE.LOG.e4050

| Details ; |
| --- |
| **Eis:** ; Loggegevens moeten bij het verstrijken van <*log_bewaartermijn>* automatisch worden verwijderd uit de actieve log en uit het archief. De logregels moeten op een zodanige wijze vernietigd worden dat de data niet te reconstrueren is. Dit betekent ook dat eventueel reservekopieen verwijderd/vernietigd/volledig overschreven zijn. ; **Toestemming** ; Conform NEN 7513:2018 paragraaf 8.5. ; Elke afsprakenstelsel/architectuur dient expliciet invulling te geven aan de waarde voor <*log_bewaartermijn>.* Indien deze waarde ontbreekt dan geldt de standaard waarde van 5 jaar. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: n/a  
**Vzvz_Req_Soort**: n/a  
**Vzvz_Req_Type**: n/a

#### Wijzigen logging

**Alias**: AGE.LOG.e4060

| Details ; |
| --- |
| **Eis:** ; Gegevens in de log mogen niet wijzigbaar of verwijderbaar (alleen in het kader van eis **AGE.LOG.e4050**) zijn. Het niet kunnen wijzigen/verwijderen van loggegevens moet worden afgedwongen door technische maatregelen. ; **Toelichting** ; Conform NEN 7513:2018 Paragraaf 6.4.3 ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: n/a  
**Vzvz_Req_Soort**: n/a  
**Vzvz_Req_Type**: n/a

#### Toegangsbeheer tot logging

**Alias**: AGE.LOG.e4040

| Details ; |
| --- |
| **Eis:** ; Directe toegang tot loggegevens en tot zoekvragen moet alleen mogelijk zijn op basis van twee factor authenticatie en expliciete autorisatie. Alleen de rol toegangslogbeheerder kan geautoriseerd worden voor toegang tot loggegevens waarin echte patiëntgegevens voorkomen of kunnen worden afgeleid. ; **Toelichting** ; Conform NEN 7513:2018 Paragraaf 8.4 ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: n/a  
**Vzvz_Req_Soort**: n/a  
**Vzvz_Req_Type**: n/a

### Eisen Infrastructurele Systeemrollen

![Diagram](../../../../assets/caa92ab3fc943f06e7ef6d14fb9dccb3e1bdd571389cfc4e20f2a8e8698d8d1b.png)  
*Figure 9 : Eisen Infrastructurele Systeemrollen - Primaire interacties - opleverend systeem*

#### Afschermen patiëntgegevens voor bevraging patiënt

**Alias**: GBX.OPV.e4537

| Details ; |
| --- |
| **Eis:** ; Afscherming van patiëntgegevens voor bevraging door een patiënt moet op dossierniveau kunnen worden ingesteld door de zorgverlener. ; **Toelichting bij eis:** ; Naast de aggregatieniveaus die zijn beschreven in de domeinspecificaties (zoals beschreven in eis Afschermen van patiëntgegevens ) dient het mogelijk te zijn om op verzoek van een patiënt of op inzicht van een zorgverlener het complete dossier af te schermen voor bevraging door een patiënt. ; Het afschermen van patiëntgegevens voor een patiënt is niet gebonden aan het afschermen van patiëntgegevens voor een zorgverlener (en vice versa). ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Compatibiliteit bieden met de diverse (zorg)toepassingen

**Alias**: GBX.OPV.e4550.1

| Details ; |
| --- |
| **Eis:** ; Een bronsysteem moet bevragingen van diverse actoren en vanuit diverse organisaties kunnen verwerken. ; **Toelichting bij eis:** ; De volgende actoren of groep van actoren moeten door het bronsysteem worden ondersteunt als opvrager (of opvraagverantwoordelijke): ;  Een zorgverlener op basis van UZI; ;  Een burger op basis van BSN. ; De volgende organisaties moeten door het bronsysteem worden ondersteunt als organisatie vanuit waar opgevraagd wordt: ;  ZIM; ;  Patiëntenportaal (GBP); ;  Goed beheerde organisatie (GBO). ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Leeftijdscontrole patiënt

**Alias**: GBX.OPV.e4570

| Details ; |
| --- |
| **Eis:** ; Indien de opvrager een patiënt is, dan dient het systeem te controleren of de leeftijd van de persoon van wie gegevens worden opgevraagd minimaal 16 jaar is. ; Indien de opvrager jonger is dan 16 jaar, dan dient het systeem de opvraag te beantwoorden met een foutmelding (PATLFT). ; **Toelichting bij eis:** ; Een patiënt jonger dan 16 jaar is niet gerechtigd om zijn eigen gegevens op te vragen zonder toestemming van bijvoorbeeld een ouder of voogd. Op dit moment is het voor een patiënt niet mogelijk om een opvraag te doen onder mandaat. ; De controle of de opvrager een patiënt is moet gebeuren op basis van de rolcode van de 'overseer' van het bericht. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Opnemen BSN in opleverbericht

**Alias**: GBX.OPV.e4660

| Details ; |
| --- |
| **Eis**: ; In FHIR-responses dient er altijd een BSN opgenomen te worden conform de technische specificaties. ; **Toelichting bij eis:** ; Een bronsysteem moet agnostisch zijn voor de infrastructuur ten behoeve waarvan opgeleverd wordt. Indien nodig, zal de resource broker het BSN verwijderen uit de FHIR-response. In de AORTA-communicatie tussen zorgaanbieders dient er altijd een BSN doorgestuurd te worden naar de uiteindelijke bevrager. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/d862cc4224416fd6ca12a37d128c79b163f24a6ddb618075ca625ccf082c157f.png)  
*Figure 10 : Eisen Infrastructurele Systeemrollen - Applicatiebeheer*

#### Wijzigen TKID applicatie o.b.v. FHIR

**Alias**: GBX.APR.e4070.1

| Details ; |
| --- |
| **Eis:** ; Het XIS moet op basis van het beherenTKID-bericht aangeven welke FHIR resources de bron kan opleveren en/of kan verwerken. Hiervoor dient de implementatie gevolgd te worden zoals beschreven in de implementatiehandleiding van het TKID-bericht. ; **Toelichting bij eis:** ; Momenteel wordt nog gewerkt aan de implementatiehandleiding voor de implememantie van het TKID-bericht. Deze eis dient dan ook vooralsnog als 'kapstokeis' en kan worden uitgebreid en/of aangescherpt. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Bevestigen applicatiekoppeling o.b.v. FHIR

**Alias**: GBX.APR.e4080

| Details ; |
| --- |
| **Eis:** ; Het XIS moet een applicatiekoppelingverificatie-bericht kunnen ontvangen en/of versturen. Hiervoor dient de implementatie gevolgd te worden zoals beschreven in de implementatiehandleiding van het applicatiekoppelingverificatie-bericht. ; **Toelichting bij eis:** ; Momenteel wordt nog gewerkt aan de implementatiehandleiding voor de implementatie van het applicatiekoppelingverificatie-bericht.. Deze eis dient dan ook vooralsnog als 'kapstokeis' en kan worden uitgebreid en/of aangescherpt. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/b29a9fcb9d2e4edc262e76d608da8ba0b74decddd234ec778ce8fabcc55e98ed.png)  
*Figure 11 : Eisen Infrastructurele Systeemrollen - Patiëntadministratie*

#### Verwerken geboortedatums waarin nullen zijn opgenomen

**Alias**: GBX.IDA.e4015

| Details ; |
| --- |
| **Eis:** ; Een geboortedatum die teruggegeven wordt door de SBV-Z kan nullen bevatten (jjjjmm00, jjjj0000 of 00000000). Het XIS moet in staat zijn hiermee adequaat om te gaan zonder dat de applicatie vastloopt. ; **Toelichting bij eis:** ; Deze eis leidt tot de volgende aanvullende eisen: ;  Alle XISsen moeten naast de mogelijkheid om een BSN op te vragen of te verifiëren op basis van de Zoekpaden 1 en 2, ook de dienst opvragen van persoonsgegevens op basis van een ingevoerd BSN inbouwen. ;  Bij het overnemen van de gegevens uit de SBV-Z moet het voor de gebruiker mogelijk zijn om de geboortedatum aan te passen voor het opslaan, indien het systeem meldt dat de gegevens niet in de database kunnen worden opgeslagen. ;  Bij het aanpassen van de geboortedatum in een databasegeaccepteerde datum moet er een indicatie komen dat de geboortedatum handmatig is aangepast. (bijvoorbeeld andere kleur of een indicatie erbij). Nog mooier is de opgeleverde datum opslaan in een (apart) tekstveld. ;  De dienst 'opvragen persoonsgegevens op basis van BSN' moet kunnen worden uitgevoerd, ook als er al persoonsgegevens bekend zijn maar de verificatie mislukt is vanwege de geboortedatum. Hierbij kan er een dialoogvenster wordt getoond waarbij de gegevens van de SBV-Z worden vergeleken met die uit de database van de zorgverlener. ; Een aanpassing van de geboortedatum mag niet leiden tot 'het niet geverifieerd zijn van het BSN'. Dit geldt echter alleen tijdens de dialoog van vergelijken. Indien de geboortedatum buiten de dialoog om aangepast wordt, moet dit wel leiden tot het vervallen van de verificatie. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Voorlopig koppelen van patiëntgegevens aan een BSN

**Alias**: GBX.IDA.e4020

| Details ; |
| --- |
| **Eis:** ; Het systeem moet een gebruiker de mogelijkheid bieden het door een burgerregister geretourneerde BSN te koppelen aan de identificerende gegevens in de lokale patiëntenindex waarbij bij het overgenomen BSN automatisch wordt vastgelegd: ;  de bron van het BSN; ;  datum en tijd van koppelen; ;  UZI-nummer of andere identificatie van de gebruiker. ; Er is dan sprake van een voorlopige koppeling tussen BSN en patiëntgegevens. ; **Toelichting bij eis:** ; Dit is nodig opdat een zorgverlener/medewerker kan voldoen aan de wettelijke verplichting van de zorgaanbieder om het BSN op te nemen in zijn administratie, zie Wbsn-z artikel 8.Voor het landelijk uitwisselen van medische patiëntgegevens moet de SBV-Z of de GBA / BRP zijn geraadpleegd. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Definitief koppelen van patiëntgegevens aan een BSN

**Alias**: GBX.IDA.e4030

| Details ; |
| --- |
| **Eis:** ; Het systeem moet voor een geselecteerde patiënt/cliënt de gebruiker: ;  de mogelijkheid bieden gewaarschuwd te worden indien nog niet is vastgesteld dat het BSN hoort bij de patiënt/cliënt; ;  de mogelijkheid bieden in de lokale patiëntenindex vast te leggen dat hij heeft vastgesteld dat het betreffende BSN hoort bij de patiënt/cliënt, onder vermelding van: ;  de manier van vaststellen: ; i. Controle van echtheid en geldigheidsdatum van WID en de gelijkenis van de in de WID genoemde identificerende gegevens, ; ii. Vergewissen, ;  Datum en tijd van vaststellen, ;  2. indien beschikbaar het UZI-nummer of anders een unieke identificatie van de gebruiker, en het UZI-nummer van mandaterende zorgverlener indien van toepassing. ;  zorgaanbieder-id van de gebruiker; ;  in geval van WID-controle: aard en nummer van het WID. ; Daarmee is het BSN definitief gekoppeld. ; **Toelichting bij eis:** ; Dit is belangrijk voor een zorgaanbieder die (geautomatiseerd) wil vaststellen of is voldaan aan de eventuele wettelijke verplichting om de identiteit vast te stellen aan de hand van een WID. ; <ac:structured-macro ac:name="unmigrated-wiki-markup" ac:schema-version="1" ac:macro-id="0d572124-6409-4149-9e8b-99c2fbf859ce"><ac:plain-text-body><![CDATA[Merk op dat de toelichting op [Bbsn-z] artikel 26 een grote verantwoordelijkheid legt bij de zorgaanbieder voor de afweging wel/niet WID controleren. Daarom is geautomatiseerde ondersteuning belangrijk. \]](https://vzvz.atlassian.net/wiki/pages/createpage.action?spaceKey=A8&title=Merk%20op%20dat%20de%20toelichting%20op%20%5BBbsn-z%5D%20artikel%2026%20een%20grote%20verantwoordelijkheid%20legt%20bij%20de%20zorgaanbieder%20voor%20de%20afweging%20wel%2Fniet%20WID%20controleren.%20Daarom%20is%20geautomatiseerde%20ondersteuning%20belangrijk.%20%5C%5D)></ac:plain-text-body></ac:structured-macro> ; Manier van vaststellen: ;  Vaststellen identiteit; Bij inschrijving van een patiënt waar nog geen behandelrelatie mee is, is het verplicht de identiteit van de patiënt vast te stellen aan de hand van een Wettelijk Identificatie Document (WID): een paspoort, Nederlands rijbewijs, Nederlandse ID-kaart of Nederlands vreemdelingendocument. ;  WID-controle; Indien er wordt getwijfeld over de geldigheid van een identiteitsdocument, kan bij de Sectorale Berichten Voorziening in de Zorg (SBV-Z) een WID-controle worden uitgevoerd. Dit kan via een zorginformatiesysteem of via de website van SBV-Z. ;  Opvragen/verifiëren BSN; Hierna moet het BSN geverifiëerd worden en registreren worden dat deze verificatie heeft plaatsgevonden. Alle door VZVZ geaccepteerde zorginformatiesystemen ondersteunen deze mogelijkheid. Komt BSN van een patiënt via een andere zorgverlener? Dan hoeft het niet opnieuw geverifiëerd te worden. Ook als het nummer direct uit de BRP komt , kunt BSN-verificatie achterwege worden gelaten. ; Het systeem kan hierna overgaan tot het vrijgeven en aanmelden van de bij de patiënt/cliënt behorende gegevens. ; |

**Vzvz_Moscow**: Optioneel  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Controleren geldigheid van een WID

**Alias**: GBX.IDA.e4040

| Details ; |
| --- |
| **Eis:** ; Het systeem moet voor een geselecteerde patiënt/cliënt de gebruiker de mogelijkheid bieden: ;  het 'in omloop mogen zijn' van het WID te controleren door raadplegen van de SBV-Z op basis van aard en nummer van het WID; ;  in de lokale patiëntenindex vast te leggen dat hij 'het in omloop mogen zijn' van het WID heeft gecontroleerd, onder vermelding van: ;  resultaat van de controle, ;  datum en tijd, ;  indien beschikbaar het UZI-nummer of anders een unieke identificatie van de gebruiker, ;  aard en nummer van het WID. ;  de onder 2. vastgelegde informatie op elk gewenst moment te raadplegen. ; **Toelichting bij eis:** ; Dit is belangrijk voor een zorgverlener/medewerker die in geval van twijfel over de echtheid of geldigheid van een WID wil nagaan of deze in omloop mag zijn. Hiertoe biedt de SBV-Z een dienst om te kunnen controleren of een bepaald WID in omloop is. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Opzoeken en tonen patiëntgegevens

**Alias**: GBX.IDA.e4010.1

| Details ; |
| --- |
| **Eis:** ; Het systeem moet een gebruiker de mogelijkheid bieden een patiënt op te zoeken in de lokale patiëntadministratie van de zorgaanbieder, door het invoeren van identificerende gegevens, waarna wordt getoond: ;  of de patiënt/cliënt is gevonden, en zo ja ;  of het BSN wel/niet is opgevraagd of geverifieerd bij de SBV-Z ;  de datum en tijd van koppelen ;  de manier van vaststellen van de identiteit: ;  Controle van echtheid en geldigheidsdatum van WID en de gelijkenis van de in de WID genoemde identificerende gegevens ;  Vergewissen, ;  indien beschikbaar het UZI-nummer of anders een unieke identificatie van de gebruiker en het UZI-nummer van mandaterende zorgverlener indien van toepassing ;  in geval van WID-controle: aard en nummer van het WID. ; **Toelichting bij eis:** ; Deze eis voorkomt dat de SBV-Z telkens opnieuw wordt geraadpleegd. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Gebruik van geverifieerde BSN's

**Alias**: GBX.IDA.e4060.1

| Details ; |
| --- |
| **Eis:** ; Het systeem moet aan [Opzoeken en tonen patiënteninformatie](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-BK_1292305474), [Voorlopig koppelen van patiëntgegevens aan een BSN](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-BK_874324176), [Controleren geldigheid van een WID](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-BK_64071816), en [Bijhouden behandelrelatie](pve-bronsysteem-tbv-medmij.md#PvEBronsysteemtbvMedMij-BK_591027313) voldoen of (bij implementatie in een GBZ) een koppeling kunnen leggen met een derde systeem dat aan die eisen voldoet. ; Een systeem die gebruik maakt van een extern patiëntadministrerend systeem is verplicht om te controleren of een BSN daadwerkelijk aan alle AORTA eisen voldoet m.b.t. het BSN. ; **Toelichting bij eis:** ; Ieder GBZ moet over een patiëntadministratie beschikken, maar een XIS hoeft die niet per se in te bouwen. Het staat een GBZ vrij een eigen patiëntadministrerend systeem te kiezen dat voldoet aan de genoemde eisen. De systeemrol van Patiëntadministrerend systeem is daarmee niet verplicht voor XIS-typekwalificatie, maar een GBZ moet wel aantoonbaar over een dergelijk systeem beschikken en dit met het gebruikte XIS hebben gekoppeld om zodoende te kunnen garanderen dat er in de XIS-instantie met geverifieerde BSN's gewerkt wordt. Die gerefereerde eisen hoeven dan niet voor de XIS-typekwalificatie te worden ingebouwd. ; Hoe de controle wordt gedaan op de geldigheid van een BSN is aan de XIS-applicatie. Het is denkbaar dat de XIS-applicatie het patiëntadministrerende systeem actief benaderd, maar het is ook mogelijk dat de XIS-applicatie de statussen van een BSN toegezonden krijgt. Er mogen in géén geval BSN's in een bericht worden opgenomen die niet voldoen aan de AORTA eisen. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: n/a

### Eisen XIS-leverancier

![Diagram](../../../../assets/b1312cd679bc51ded2d7a67b0b674780cf043e6b7aa0a4523425f16d6d122a9b.png)  
*Figure 12 : Eisen XIS-leverancier*

#### Beschikbaarheid XIS-servicedesk

**Alias**: XIS.SVD.e4010

| Details ; |
| --- |
| **Eis:** ; Een ingericht XIS-Servicedesk moet tijdens kantoortijden beschikbaar zijn voor vragen vanuit VZVZ. ; **Toelichting bij eis:** ; Voor de oplostijden en de precieze beschikbaarheid van het XIS-servicedesk wordt verwezen naar de in de toekomst op te stellen DAP. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Business

#### Inrichten XIS-servicedesk

**Alias**: XIS.SVD.e4030

| Details ; |
| --- |
| **Eis:** ; De XIS-leverancier moet een 'XIS-servicedesk' inrichten die als aanspreekpunt fungeert voor problemen m.b.t. het XIS. De XIS-servicedesk moet onderdeel uitmaken van het ketenbeheerproces. ; **Toelichting bij eis:** ; Via de GBZ-Servicedesks is niet altijd een goede voortgang te boeken met betrekking tot het oplossen van XIS gerelateerde problemen. Het ontbreken van voortgang wordt met name veroorzaakt doordat de GBZ-beheerder ; geen invloed heeft op de planning bij de leveranciers en doordat het precieze probleem en de ernst van het probleem niet altijd duidelijk doorkomen bij de XIS-leverancier.​ Daarnaast ontbreekt het de GBZ-beheerder ; in sommige gevallen aan de technische kennis, die nodig is om bepaalde problemen te detecteren en/of te benoemen. ; De XIS-servicedesk moet de GBZ-beheerder ondersteunen bij het oplossen van eventuele technische bevindingen van het XIS. Daarnaast moet het XIS-servicedesk benaderbaar zijn voor VZVZ om bepaalde problemen en oplossingstijden ; te bespreken en de voortgang te bewaken. Het doel is om tot betere kwaliteit van de software te komen en om problemen in de keten effectiever op te lossen. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Business

#### Gebruik Supportal

**Alias**: XIS.SVD.e4020

| Details ; |
| --- |
| **Eis:** ; De XIS-leverancier moet voor in gebruik name van een applicatie in productie, het XIS-aanspreekpunt en contactgegevens beschikbaar gesteld hebben via Supportal. ; **Toelichting bij eis:** ; Om een goed beheerproces te kunnen implementeren is het van belang dat de verantwoordelijke aanspreekpunten vindbaar en benaderbaar zijn. Het huidige ketenbeheerproces maakt voor communicatie binnen de keten gebruik van Supportal. ; Het is van belang dat ook het XIS-aanspreekpunt vindbaar is in Supportal. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Business

### Eisen specifieke gegevensdienst

![Diagram](../../../../assets/674a09f8b9a41c19c7d44fa1e0d32177a265a5f1afb6e143d8da0906aa4bf9d2.png)  
*Figure 13 : Eisen MedMij gegevensdienst - Verzamelen Huisartsgegevens 2.0*

#### Implementeren gegevensdienst Verzamelen Huisartsgegevens 2.0

**Alias**: GBZ.VEHU.e4010

| Details ; |
| --- |
| **Eis:** ; Gegevensdienst Verzamelen Huisartsgegevens 2.0 met gegevensdienstid 49, dient ondersteund te worden door het bronsysteem. ; **Toelichting bij eis:** ; De specificaties van de te implementeren interfaces zijn te vinden via ;  [https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus](https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus) ;  . ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/15f9e74a6cced8984edb52bec78dd3646a2ca0fb34b7e0c843c432b88a2e6cb9.png)  
*Figure 14 : Eisen MedMij gegevensdienst - Verzamelen Medicatiegegevens 9.0*

#### Implementeren gegevensdienst Verzamelen Medicatiegegevens 9.0

**Alias**: GBZ.VEME.e4010

| Details ; |
| --- |
| **Eis:** ; Gegevensdienst Verzamelen Medicatiegegevens 9.0 met gegevensdienstid 31, dient ondersteund te worden door het bronsysteem. ; **Toelichting bij eis:** ; De specificaties van de te implementeren interfaces zijn te vinden via ;  [https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus](https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus) ;  . ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/2ce47ef4803bf7082f5979d75e5716a262548e6bb38e4dc2f9064632a6c77234.png)  
*Figure 15 : Eisen MedMij gegevensdienst - Verzamelen Medicatiegerelateerde Overgevoeligheden 2.A*

#### Implementeren gegevensdienst Verzamelen Medicatiegerelateerde Overgevoeligheden 2.A

**Alias**: GBZ.VEMO.e4010

| Details ; |
| --- |
| **Eis:** ; Gegevensdienst Verzamelen Medicatiegerelateerde Overgevoeligheden 2.A met gegevensdienstid 58, dient ondersteund te worden door het bronsysteem. ; **Toelichting bij eis:** ; De specificaties van de te implementeren interfaces zijn te vinden via ;  [https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus](https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus) ;  . ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/db21bd8624531982539b33f6ad8245edd6f13ea9f2d7378aaf74ce282cdb811f.png)  
*Figure 16 : Eisen MedMij gegevensdienst - Verzamelen Basisgegevens GGZ 2.0*

#### Implementeren gegevensdienst Verzamelen Basisgegevens GGZ 2.0

**Alias**: GBZ.BGGZ.e4010

| Details ; |
| --- |
| **Eis:** ; Gegevensdienst Verzamelen Basisgegevens GGZ 2.0 met gegevensdienstid 50, dient ondersteund te worden door het bronsysteem. ; **Toelichting bij eis:** ; De specificaties van de te implementeren interfaces zijn te vinden via ;  [https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus](https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus) ;  . ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/e58f83b985dd102b3ac1b9b10fdc70aeebb0d2c07eb9b1fcf0a2301db35851c7.png)  
*Figure 17 : Eisen MedMij gegevensdienst - Verzamelen Basisgegevens zorg 3.0*

#### Implementeren gegevensdienst Verzamelen Basisgegevens zorg 3.0

**Alias**: GBZ.VBGZ.e4010

| Details ; |
| --- |
| **Eis:** ; Gegevensdienst Verzamelen Basisgegevens zorg 3.0 met gegevensdienstid 48, dient ondersteund te worden door het bronsysteem. ; **Toelichting bij eis:** ; De specificaties van de te implementeren interfaces zijn te vinden via ;  [https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus](https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus) ;  . ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/1db9a29b164dcf6d205c50de540f5739f95cc1953a30d46b012d46e63bd07b30.png)  
*Figure 18 : Eisen MedMij gegevensdienst - Delen antwoorden op vragenlijsten 2.0*

#### Implementeren gegevensdienst Delen antwoorden op vragenlijsten 2.0

**Alias**: GBZ.DAOV.e4020

| Details ; |
| --- |
| **Eis:** ; Gegevensdienst Delen antwoorden op vragenlijsten 2.0 met gegevensdienstid 60, dient ondersteund te worden door het bronsysteem. ; **Toelichting bij eis:** ; De specificaties van de te implementeren interfaces zijn te vinden via ;  [https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus](https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus) ;  . ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Implementeren Ontvankelijkheidstoets

**Alias**: GBZ.ONTV.e4010

| Details ; |
| --- |
| **Eis:** ; Het XIS moet een ontvankelijkheidstoets-bericht kunnen ontvangen en beantwoorden. Hiervoor dient de implementatie gevolgd te worden zoals beschreven in de implementatiehandleiding van het ontvankelijkheidstoets-bericht. ; **Toelichting bij eis:** ; Momenteel wordt nog gewerkt aan de implementatiehandleiding voor de implementatie van het ontvankelijkheidstoets-bericht. Deze eis dient dan ook vooralsnog als 'kapstokeis' en kan worden uitgebreid en/of aangescherpt. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Controleren behandelrelatie

**Alias**: GBZ.ONTV.e4020

| Details ; |
| --- |
| **Eis:** ; Het systeem mag alleen gegevens ontvangen indien er in het patiëntadministrerende systeem een behandelrelatie met de patiënt staat geregistreerd. ; **Toelichting bij eis:** ; Er moet voorkomen worden, dat een patiënt onverhoopt gegevens stuurt naar een zorgaanbieder waar hij niet (meer) behandeld wordt. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Bijhouden behandelrelatie

**Alias**: GBX.IDA.e4050

| Details ; |
| --- |
| **Eis:** ; Het systeem moet een gebruiker de volgende mogelijkheden bieden in de lokale patiëntadministratie voor een patiënt/cliënt. ; De status van de behandelrelatie inzien, waarbij wordt getoond: ;  of een behandelrelatie bestaat, en zo ja met welke zorgverleners een behandelrelatie bestaat; ;  ten behoeve van welke zorgaanbieder (URA) de behandelrelatie wordt onderhouden. ; Een nieuwe behandelrelatie beginnen, waarbij wordt vastgelegd: ;  begindatum; ;  UZI-nummer van de zorgverlener; ;  de URA van de zorgaanbieder ten behoeve van wie de behandelrelatie onderhouden wordt. ; Een bestaande behandelrelatie beëindigen, waarbij wordt vastgelegd: ;  einddatum; ;  UZI-nummer van de zorgverlener. ; **Toelichting bij eis:** ; De zorgverlener onderhoudt de behandelrelatie hetzij ten behoeve van de zorgaanbieder waarvoor hij werkzaam is, hetzij als zorgaanbieder indien het een zelfstandig werkende beroepsbeoefenaar betreft. ; Een zorgverlener die de patiënt/cliënt niet ziet, bijvoorbeeld in een laboratorium, legt een behandelrelatie vast in de zin van een verklaring dat hij werkt in opdracht van een andere zorgverlener die een behandelrelatie met de patiënt/cliënt heeft. ; |

**Vzvz_Moscow**: Optioneel  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/62a7656fa1794c8c530341b6c3374e3cca743bd9f62dcf96fc718d87a33752bb.png)  
*Figure 19 : Eisen MedMij gegevensdienst - Delen Meetwaarden vitale functies 2.0*

#### Implementeren gegevensdienst Delen Meetwaarden vitale functies 2.0

**Alias**: GBZ.DMVF.e4010

| Details ; |
| --- |
| **Eis:** ; Gegevensdienst Delen Meetwaarden vitale functies 2.0 met gegevensdienstid 53, dient ondersteund te worden door het bronsysteem. ; **Toelichting bij eis:** ; De specificaties van de te implementeren interfaces zijn te vinden via ;  [https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus](https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus) ;  . ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/53cddc74ded81f7e1686bfb4b487075cca8c6f3b4efdc324ead7050097809ada.png)  
*Figure 20 : Eisen MedMij gegevensdienst - Verzamelen Afspraken 2.0*

#### Implementeren gegevensdienst Verzamelen Afspraken 2.0

**Alias**: GBZ.VAf.e4010

| Details ; |
| --- |
| **Eis:** ; Gegevensdienst Verzamelen Afspraken 2.0 met gegevensdienstid 47, dient ondersteund te worden door het bronsysteem. ; **Toelichting bij eis:** ; De specificaties van de te implementeren interfaces zijn te vinden via ;  [https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus](https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus) ;  . ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/32a7d03c79aaae7d549c602d614c6a20e3fab0a84eb7efb3a60520456d3510c7.png)  
*Figure 21 : Eisen MedMij gegevensdienst - Verzamelen Documenten 3.0*

#### Implementeren gegevensdienst Verzamelen Documenten 3.0

**Alias**: GBZ.VDo.e4010

| Details ; |
| --- |
| **Eis:** ; Gegevensdienst Verzamelen Documenten 3.0 met gegevensdienstid 51, dient ondersteund te worden door het bronsysteem. ; **Toelichting bij eis:** ; De specificaties van de te implementeren interfaces zijn te vinden via ;  [https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus](https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus) ;  . ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/3371081480a8da1d39c133a82f6acbba90becd1ff99116e666ab8feb230a930b.png)  
*Figure 22 : Eisen MedMij gegevensdienst - Verzamelen Meetwaarden vitale functies 2.0*

#### Implementeren gegevensdienst Meetwaarden vitale functies 2.0

**Alias**: GBZ.MVF.e4010

| Details ; |
| --- |
| **Eis:** ; Gegevensdienst Delen Meetwaarden vitale functies 2.0 met gegevensdienstid 53, dient ondersteund te worden door het bronsysteem. ; **Toelichting bij eis:** ; De specificaties van de te implementeren interfaces zijn te vinden via ;  [https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus](https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus) ;  . ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/21091d502222f83016079e44727c19fe05c2e8f7a47ff46f0bf4a425440809c7.png)  
*Figure 23 : Eisen MedMij gegevensdienst - Verzamelen verwijzingen naar vragenlijsten 2.0*

#### Implementeren gegevensdienst Verzamelen verwijzingen naar vragenlijsten 2.0

**Alias**: GBZ.VVV.e4010

| Details ; |
| --- |
| **Eis:** ; Gegevensdienst Verzamelen verwijzingen naar vragenlijsten 2.0 met gegevensdienstid 59, dient ondersteund te worden door het bronsysteem. ; **Toelichting bij eis:** ; De specificaties van de te implementeren interfaces zijn te vinden via ;  [https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus](https://vzvz.atlassian.net/wiki/display/MMCatalogus/Actuele+Catalogus) ;  . ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
<span id="latestPvEBronsysteemtbvMedMij-INSERT_Section1End"></span><span id="INSERT_Section1End"></span>End
