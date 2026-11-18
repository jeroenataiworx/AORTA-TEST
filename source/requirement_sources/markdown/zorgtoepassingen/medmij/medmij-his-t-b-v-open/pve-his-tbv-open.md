[AORTA 8.5.2](../../../index.md) / [Zorgtoepassingen](../../../zorgtoepassingen.md) / [MedMij](../../medmij.md) / [MedMij HIS t.b.v. OPEN](../medmij-his-t-b-v-open.md)

# PvE HIS tbv OPEN

| Datum: 8-10-2025 ; |
| --- |
| Status: Definitief ; |
| Versie: ; |
| Classificatie: Openbaar ; |
| Revisie: 2.0 ; |

### Documenthistorie

*Documentversies*

| **Datum** ; | **Status** ; | **Versie** ; | **Omschrijving** ; |
| --- | --- | --- | --- |
| 15 juni 2022 ; | Definitief ; | 1.0 ; | Eerste opzet PvE Huisartsinformatiesysteem tbv Open ; |
| 8-10-2025 ; | Definitief ; | 2.0 ; | TLS-versies aangepast op basis van NCSC richtlijnen (2025-05) ; |

Inhoudsopgave   
[Documenthistorie](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776503)  
[1 Inleiding](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776504)  
[2 Eisen HIS t.b.v. OPEN](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776505)  
[2.1 AORTA Eisen Infrastructurele Systeemrollen](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776506)  
[2.1.1 Systeemrollen - Infrastructuur - Applicatiebeheer](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776507)  
[2.1.2 Systeemrollen - Infrastructuur - Gegevens ontvangend systeem](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776508)  
[2.1.3 Systeemrollen - Infrastructuur - Gegevens opleverend systeem](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776509)  
[2.1.4 Systeemrollen - Infrastructuur - Patiëntadministratie](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776510)  
[2.2 AORTA Eisen Kwaliteit Aangesloten Systemen](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776511)  
[2.2.1 Genereren time-out](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776512)  
[2.2.2 Tijdige verwerking van berichten](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776513)  
[2.2.3 Borgen van minimale verwerkingssnelheid](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776514)  
[2.2.4 Borgen van de betrouwbaarheid bij grote storingen](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776515)  
[2.2.5 Borgen van de betrouwbaarheid bij kleine storingen](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776516)  
[2.2.6 Minimaliseren van de impact van gepland onderhoud](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776517)  
[2.2.7 Borgen van de beschikbaarheid van een GBx](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776518)  
[2.2.8 Beveiligde opslag](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776519)  
[2.2.9 Een GBx beschikt over een geldig UZI/PKIO-servercertificaat](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776520)  
[2.2.10 Borgen van plicht tot uitwisselen van patiëntgegevens](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776521)  
[2.2.11 Beveiliging van patiëntgegevens in het GBx](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776522)  
[2.2.12 Borgen betrouwbare koppeling tussen pas en applicatie](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776523)  
[2.2.13 Aansluiting op productie-omgeving LSP](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776524)  
[2.2.14 Tijdsynchronisatie GBx en ZIM](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776525)  
[2.2.15 Gebruik van IP en DNS](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776526)  
[2.2.16 Communicatie met het LSP via een GZN](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776527)  
[2.3 AORTA Eisen Kwaliteit Applicatie](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776528)  
[2.3.1 Toegangslog bijhouden (FHIR)](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776529)  
[2.3.2 Hardening](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776530)  
[2.3.3 Opzetten beveiligde verbinding vanuit de ZIM met een GBx](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776531)  
[2.3.4 Opzetten en gebruiken van TLS-sessies](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776532)  
[2.3.5 Instellen configuratieparameters t.b.v. communicatie en authenticatie van de ZIM](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776533)  
[2.3.6 Bijhouden van een gebruikersregistratie](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776534)  
[2.3.7 Opzetten beveiligde verbinding met de ZIM](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776535)  
[2.3.8 Toegangslog bijhouden](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776536)  
[2.3.9 Afbreken van een gebruikerssessie](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776537)  
[2.3.10 Blokkeren van ingetrokken, verlopen en niet authentieke passen](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776538)  
[2.3.11 Inloggen op vertrouwensniveau midden](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776539)  
[2.3.12 Afhandelen transactietoken](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776540)  
[2.3.13 Protocolstack voor gegevensuitwisseling o.b.v. FHIR](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776541)  
[2.3.14 Kenbaar maken Certificate Authorities](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776542)  
[2.3.15 Ondersteunen servercertificaten en ondertekeningalgoritmen](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776543)  
[2.3.16 Bevorderen interoperabiliteit bij berichtuitwisseling](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776544)  
[2.3.17 Juiste afhandeling van SOAP headers](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776545)  
[2.3.18 Protocolstack voor berichtuitwisseling](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776546)  
[2.4 AORTA Eisen Organisatie van een GBX](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776547)  
[2.4.1 Afmelden patiënt na overlijden](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776548)  
[2.4.2 Wijzigen logging](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776549)  
[2.4.3 Vernietigen loggegevens](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776550)  
[2.4.4 Uitschakelen logging](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776551)  
[2.4.5 Toegangsbeheer tot logging](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776552)  
[2.4.6 Loggen toegangsregeling](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776553)  
[2.4.7 Loggen inzage logging](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776554)  
[2.4.8 Bewaartermijn loggegevens](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776555)  
[2.4.9 Voldoen aan wet- en regelgeving](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776556)  
[2.4.10 Vernietigen materialen volgens standaarden](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776557)  
[2.4.11 Een GBx valt onder Nederlandse wet- en regelgeving](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776558)  
[2.4.12 Kennisvergaring m.b.t. GBX-beheer](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776559)  
[2.4.13 Bijhouden van een beheerlog](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776560)  
[2.4.14 Beperking inzage door beheerder](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776561)  
[2.4.15 Actueel houden van het applicatieregister](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776562)  
[2.4.16 Systeembeheer van een GBx](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776563)  
[2.4.17 Beheren van en toegang verschaffen tot de toegangslog](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776564)  
[2.4.18 Toekennen functiescheiding tussen systeemgebruikers](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776565)  
[2.4.19 Verantwoordelijk UZI-pasbeleid](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776566)  
[2.4.20 Instrueren systeemgebruikers over beveiligingsbeleid](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776567)  
[2.4.21 Ondersteuning van gebruikers bij problemen met de landelijke uitwisseling van informatie](pve-his-tbv-open.md#PvEHIStbvOPEN-_Toc101776568)  
<span id="latestPvEHIStbvOPEN-INSERT_Section1"></span><span id="INSERT_Section1"></span>Section: Section1

## Inleiding

<span id="latestPvEHIStbvOPEN-INSERT_Section1End"></span><span id="INSERT_Section1End"></span>End   
  
<span id="latestPvEHIStbvOPEN-INSERT_Section2"></span><span id="INSERT_Section2"></span>Section: Section2

## Eisen HIS t.b.v. OPEN

### AORTA Eisen Infrastructurele Systeemrollen

#### Systeemrollen - Infrastructuur - Applicatiebeheer

![Diagram](../../../../assets/3a6e1e53922bca09bfcb870ef8017d7f8a6a46befeb82417d146d132d70bd867.png)  
*Figure 1 : Eisen Infrastructurele Systeemrollen - Applicatiebeheer*

##### Bevestigen applicatiekoppeling o.b.v. FHIR

**Alias**: GBX.APR.e4080

| Details ; |
| --- |
| **Eis:** ; Het XIS moet een applicatiekoppelingverificatie-bericht kunnen ontvangen en/of versturen. Hiervoor dient de implementatie gevolgd te worden zoals beschreven in de implementatiehandleiding van het applicatiekoppelingverificatie-bericht. ; **Toelichting bij eis:** ; Momenteel wordt nog gewerkt aan de implementatiehandleiding voor de implementatie van het applicatiekoppelingverificatie-bericht.. Deze eis dient dan ook vooralsnog als 'kapstokeis' en kan worden uitgebreid en/of aangescherpt. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Wijzigen TKID applicatie o.b.v. FHIR

**Alias**: GBX.APR.e4070.1

| Details ; |
| --- |
| **Eis:** ; Het XIS moet op basis van het beherenTKID-bericht aangeven welke FHIR resources de bron kan opleveren en/of kan verwerken. Hiervoor dient de implementatie gevolgd te worden zoals beschreven in de implementatiehandleiding van het TKID-bericht. ; **Toelichting bij eis:** ; Momenteel wordt nog gewerkt aan de implementatiehandleiding voor de implememantie van het TKID-bericht. Deze eis dient dan ook vooralsnog als 'kapstokeis' en kan worden uitgebreid en/of aangescherpt. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Bevestigen applicatiekoppeling

**Alias**: GBX.APR.e4160

| Details ; |
| --- |
| **Beginsituatie** ; Het systeem beschikt over de voor deze functie vereiste vertrouwensmiddelen. ; **Trigger** ; Het systeem ontvangt een verifiërenApplicatiekoppeling bericht conform [IH AORTA.](https://decor.nictiz.nl/pub/vzvz/aorta-vzvz-html-20200821T140325/) ; **Interacties** ; Het systeem stuurt een verifiërenApplicatiekoppelingAntwoord terug naar de verzender conform [IH AORTA.](https://decor.nictiz.nl/pub/vzvz/aorta-vzvz-html-20200821T140325/) ; **Resultaat** ; Het antwoordbericht is teruggestuurd naar de verzender. ; **Uitzonderingen** ; Uitzonderingen zijn beschreven in de [Foutentabel](https://www.aorta-lsp.nl/media/downloads/foutentabel-aorta-v8200xlsx/download). ; **Opties** ; Het bericht moet een authenticatietoken kunnen bevatten. ; **Responsetijd** ;  **Betrouwbaarheid** ;  **Toelichting** ; - ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Verifiëren applicatiekoppeling

**Alias**: GBX.APR.e4140

| Details ; |
| --- |
| **Beginsituatie** ; De gebruiker is lokaal ingelogd op vertrouwensniveau laag of hoger. ; **Trigger** ; De gebruiker initieert de functie via het systeem. ; **Interacties** ;  Het systeem verzendt en verifiërenApplicatiekoppeling bericht naar de ZIM of een ander GBX conform [IH APR](https://decor.nictiz.nl/pub/vzvz/aorta-vzvz-html-20200821T140325/). ;  Het systeem ontvangt een verifiërenApplicatiekoppelingAntwoord bericht conform [IH APR](https://decor.nictiz.nl/pub/vzvz/aorta-vzvz-html-20200821T140325/). ; **Resultaat** ; De opgeleverde gegevens zijn door het systeem: ;  gepresenteerd aan de gebruiker, of ;  verwerkt tot een beslissing (die is gepresenteerd aan de gebruiker). ; **Uitzonderingen** ; Uitzonderingen zijn beschreven in de [Foutentabel](https://www.aorta-lsp.nl/media/downloads/foutentabel-aorta-v8200xlsx/download). ; **Opties** ; Het bericht moet een authenticatietoken kunnen bevatten. ; **Responsetijd** ;  **Betrouwbaarheid** ; Garantie geven dat versturen van gegevens niet zonder kennisgeving gestaakt wordt ; **Toelichting** ; - ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Wijzigen TKID applicatie

**Alias**: GBX.APR.e4060, GBX.APR.e4170.1

| Details ; |
| --- |
| **Beginsituatie** ; De gebruiker is lokaal ingelogd op vertrouwensniveau laag of hoger. ; **Trigger** ; De gebruiker initieert de functie via het systeem. ; **Interacties** ;  Het systeem verzendt een *beherenTKID-*bericht naar de ZIM conform [HL7v3 IH APR](https://www.aortadocumentatie.nl/Documenten/AORTA_ApBh_IH_Applicatieregister_HL7.pdf). ;  Het systeem ontvangt een ontvangstbevestiging conform [HL7v3 IH APR](https://www.aortadocumentatie.nl/Documenten/AORTA_ApBh_IH_Applicatieregister_HL7.pdf). ; **Resultaat** ; Het LSP heeft de in het bericht opgenomen TKID's opgenomen in het applicatieregister. ; **Uitzonderingen** ; Uitzonderingen zijn beschreven in de Foutentabel. ; **Opties** ;  **Responsetijd** ;  **Betrouwbaarheid** ;  **Toelichting** ; De logische attributen van dit bericht zijn te vinden in het [Ontwerp Applicatieregister](https://www.vzvz.nl/uploaded/FILES/htmlcontent/AORTA2015/AORTA_ApBh_Ontw_Applicatieregister.pdf). ; Vanuit het XIS-acceptatieproces wordt er een typekwalificatieID (TKID) gegenereerd. In overleg tussen de XIS-leverancier en het VZVZ-acceptatieteam wordt de granulariteit van een TKID bepaald. Het is mogelijk dat er voor een XIS-applicatie één of meerdere TKID's worden uitgegeven. ; Aan elk TKID zijn één of meerdere specifieke systeemrol(len) gekoppeld. Aan elk systeemrol zijn één of meerdere interactieID's gekoppeld. Een zorgaanbiederapplicatie (een bij de zorgaanbieder geïnstalleerde versie van een XIS-applicatie) kan meerdere TKID's ondersteunen. Zie het [ONTW APR](https://www.aorta-lsp.nl/media/downloads/ontwerp-applicatieregister-aorta-v8200pdf/download) voor het gegevensmodel en een beschrijving m.b.t. TKID's. ; In het geval een zorgaanbiederapplicatie gebruik wil maken van de functionaliteit van een bepaalde systeemrol, dient de zorgaanbiederapplicatie aan de betreffende TKID (behorende bij de specifieke systeemrol(len)) gekoppeld te worden. Vanuit de applicatie dient met het 'beheren TKID'-bericht, het gewenste TKID ingestuurd te worden. ; Er mogen alleen TKID's ingestuurd worden, die door de afgenomen XIS-applicatiesoftware zijn verkregen naar aanleiding van een positieve acceptatie. De beheerder of het systeem van een bij een zorgaanbieder geïnstalleerde applicatie dient alleen die TKID's in te sturen waarvan alle systeemrollen ook daadwerkelijk door de geïnstalleerde applicatie ondersteund worden. ; Er kunnen meerdere TKID's in het bericht opgenomen worden. Zodra een TKID niet bekend is, wordt er een foutcode (INVALIDETKID) met bijbehorende foutmelding (zie [Foutentabel](https://www.aorta-lsp.nl/media/downloads/foutentabel-aorta-v8200xlsx/download)) gegenereerd. De mogelijk overige correcte TKID's worden niet verwerkt in het applicatieregister. Alle TKID's dienen opnieuw ingestuurd te worden. ; Bij elk door het LSP succesvol ontvangen 'beheren TKID'-bericht, worden de bestaande TKID-koppelingen met de zorgaanbiederapplicatie verwijderd en worden er koppelingen gemaakt met de in het bericht opgenomen TKID's. Hierbij geldt dat een bestaande status van reeds aanwezige systeemrollen (gekoppeld aan een TKID) niet wordt veranderd. Koppelingen die nog niet bekend waren binnen het applicatieregister krijgen direct de status 'actief'. ; In principe geldt dat er bij elk nieuw verkregen TKID, als gevolg van een acceptatie van een applicatiewijziging of –uitbreiding, er één of meerdere TKID's opnieuw ingestuurd moeten worden. Denkbare situaties zijn: ;  Installeren nieuwe functionaliteit; ;  Initiële installatie; ;  Nieuwe acceptatie van de XIS-applicatie. ;  Terugzetten oude functionaliteit (met een eerder verkregen TKID). ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Systeemrollen - Infrastructuur - Gegevens ontvangend systeem

![Diagram](../../../../assets/82aad65eaeee39ae646e40b4063f6c3e4d0ab87262a59e57023de80867046228.png)  
*Figure 2 : Eisen Infrastructurele Systeemrollen - Primaire interacties - ontvangend systeem*

##### Voorkomen van foutmeldingen en onverwachts gedrag van een applicatie

**Alias**: GBX.OPV.e4190

| Details ; |
| --- |
| **Eis:** ; Waardes in velden die conform het XSD-schema zijn, maar niet kunnen worden verwerkt door het ontvangende systeem moeten kunnen worden genegeerd door de ontvangende applicatie. ; **Toelichting:** ; Om succesvol bouwstenen te kunnen uitwisselen moet er een versiebeheer mechanisme worden toegepast. Dit versiebeheer mechanisme verplicht opvragende systemen velden die zij niet kunnen verwerken, maar die wel volgens het schema zijn toegestaan te kunen negeren. Hierdoor zijn systemen voorbereid op wijzigingen die in de toekomst doorgevoerd kunnen worden. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Opslaan ontvangen patiëntgegevens

**Alias**: GBX.STU.e4520

| Details ; |
| --- |
| **Eis:** ; Wanneer patiëntgegevens, die conform [Ontvangen en verwerken van opgestuurde patiëntgegevens](pve-his-tbv-open.md#PvEHIStbvOPEN-BK_282514849) zijn ontvangen, ongewijzigd in de eigen patiëntadministratie worden opgenomen en de patiëntgegevens niet ontvangen zijn in het kader van een dossieroverdracht, dan moet worden vastgelegd dat het een kopie betreft. ; **Toelichting bij eis:** ; Gewoonlijk zullen patiëntgegevens die via het LSP worden ontvangen in de eigen patiëntadministratie worden opgenomen. Wanneer dit automatisch gebeurt is het raadzaam om de geadresseerde gebruiker van de verwerkte berichten op de hoogte te stellen. ; In het verlengde hiervan kan de zorgverlener eigen aantekeningen toevoegen, of de ontvangen gegevens wijzigen. Gewijzigd overgenomen gegevens worden beschouwd als eigen dossiergegevens. ; Om redundantie van informatie te voorkomen mogen als kopie aangemerkte patiëntgegevens niet bij de verwijsindex worden aangemeld en niet worden opgeleverd bij het verwerken van een opvraagverzoek. ; Wanneer een gebruiker, als kopie aangemerkte, gegevens raadpleegt is het raadzaam om aan te geven dat het een kopie betreft, en dat de gegevens mogelijk zijn verouderd. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Ontvangen en verwerken van opgestuurde patiëntgegevens

**Alias**: GBX.STU.e4510

| Details ; |
| --- |
| **Condities** ;  **Beginsituatie** ; Het systeem beschikt over de voor deze functie vereiste vertrouwensmiddelen. ; **Trigger** ; Het systeem ontvangt een versturenPatiëntgegevens-bericht ; **Interacties** ; Het systeem stuurt een bevestiging naar de afzender conform [AORTA_Wrp_IH_Berichtwrappers_HL7](https://www.aortadocumentatie.nl/Documenten/AORTA_Wrp_IH_Berichtwrappers_HL7.pdf). ; **Resultaat** ; De ontvangen patiëntgegevens zijn verwerkt. ; **Uitzonderingen** ; Uitzonderingen zijn beschreven in de Foutentabel. ; **Opties** ; Een systeem dat berichten in de nieuwste versie ondersteunt, dient ook berichten in de eerst lagere versie te ondersteunen. ; **Responsetijd** ; Het systeem dient in staat te zijn kilobytes aan berichtinhoud per seconde te verwerken. ; **Betrouwbaarheid** ;  **Toelichting** ; Berichten kunnen zijn geadresseerd aan een applicatie die niet de applicatie is van de zorgverlener die het bericht moet krijgen. Het GBX moet er in dat geval voor zorgen het bericht bij de juiste applicatie wordt afgeleverd. ; Indien het verplicht is voor het ontvangen bericht om het patient-id in de transmissionwrapper te vermelden, dan dient dat gelijk te zijn aan het patient-id in de inhoud van het bericht. Indien dit niet het geval is, moet een foutmelding worden teruggestuurd en moet de verwerking worden afgebroken. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Ontvangen Zelfmetingen

**Alias**: GBX.ONT.e4170

| Details ; |
| --- |
| **Eis:** ; Het systeem moet delenZelfmetingen (ZTZM_IN000004NL01) kunnen verwerken en na ontvangst een Accept Acknowledgement (MCCI_IN000002) terugsturen. ; **Toelichting bij eis:** ; DelenZelfmetingen wordt verstuurd vanuit een PGO aan een HIS. Het HIS dient de zelfmetingen in zijn systeem te kunnen verwerken. Na ontvangst van delenZelfmetingen dient de HIS een accept acknowledgement terug te sturen. ; De specificatie van delenZelfmetingen is opgenomen in de art-decorpublicatie van de specifieke zorgtoepassing. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Afhandelen Ontvankelijkheidstoets

**Alias**: GBX.OPV.e4220

| Details ; |
| --- |
| **Eis:** ; Het XIS dient het antwoord op de ontvankelijkheidstoets te baseren op: ;  de leeftijd van de patiënt; de patiënt moet 16 jaar of ouder zijn; ;  aanwezigheid van een geregistreerde behandelrelatie met de patiënt; er dient een behandelrelatie te zijn met een patiënt om zijn gegevens te mogen ontvangen; ;  {optioneel} de zelfmetinginstelling van de zorgverlener; de zorgverlener moet expliciet aangeven of het open staat om gegevens van een specifieke patiënt te ontvangen (zie eis GBX.OPV.e4210). ; **Toelichting bij eis:** ; Om zelfmetingen te mogen ontvangen dienen aan een aantal randvoorwaarden te worden voldaan. Deze randvoorwaarden dienen gecontroleerd te worden op het moment dat een ontvankelijkheidstoets wordt ontvangen. Afhankelijk van de uitkomsten van de controle van de randvoorwaarden, dient er een positief of negatief antwoord verstuurd te worden. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Verwerken Zelfmetingen

**Alias**: GBX.OPV.e4230

| Details ; |
| --- |
| **Eis:** ; Zelfmetingen die ontvangen zijn na een positieve ontvankelijkheidstoets dienen verwerkt en opgeslagen te kunnen worden in het XIS van de zorgaanbieder. Overige zelfmetingen dienen door het XIS geweigerd te worden. ; **Toelichting bij eis:** ; Verwerking en opslaan van zelfmetingen houdt in ieder geval in dat zelfmetinggegevens opgeslagen moeten kunnen worden en door een zorgverlener op een later moment in de tijd inzichtelijk gemaakt kan worden. Hierbij dient rekening te worden gehouden met de eisen zoals beschreven in het Normenkader-ICT-basiseisen-OPEN-02-2021. ; Deze eis zegt verder niets over de logica hoe verder om te moeten gaan met deze gegevens. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Instellen te ontvangen bestanden

**Alias**: GBX.OPV.e4210

| Details ; |
| --- |
| **Eis:** ; Een zorgverlener moet in zijn XIS kunnen aangeven of het zelfmetingen van een specifieke patiënt wil ontvangen. ; **Toelichting bij eis:** ; Het is denkbaar dat een zorgverlener alleen maar zelfmetingen wil ontvangen van die patiënten, waarmee hij een bepaalde behandelafspraak heeft gemaakt. Het moet mogelijk zijn om in het XIS per patiënt aan te geven of het ontvangen zelfmetingen moet gaan verwerken. ; Het is denkbaar dat er in de toekomst nog meer gegevens kunnen worden verstuurd met als afzender de patiënt. Er zou dus al nagedacht kunnen worden over een generieke oplossing. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Systeemrollen - Infrastructuur - Gegevens opleverend systeem

![Diagram](../../../../assets/0bd1285e4ed741bf60a7ceab17c047e3a90bf1ff8edf62beff5034a81b3cf006.png)  
*Figure 3 : Eisen infrastructurele systeemrollen - Opleverend systeem*

##### Verwerken en beantwoorden opvraag

**Alias**: GBX.OPV.e4590

| Details ; |
| --- |
| **Eis:** ; Het opleverende systeem dient een opvraag te kunnen verwerken en een antwoord te kunnen versturen zoals gespecificeerd in de implementatiehandleiding van de zorgtoepassing. ; **Toelichting bij eis:** ; De implementatiehandleiding van een zorgtoepassing is opgenomen in Art-Decor ( ;  [https://decor.nictiz.nl/pub/vzvz/](https://decor.nictiz.nl/pub/vzvz/) ;  ). Hierin is voor elke systeemrol gespecifieerd welke interacties er ondersteund dienen te worden. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Opleveren specifieke correspondentie

**Alias**: GBX.OPV.e4640

| Details ; |
| --- |
| **Eis:** ; Het bronsysteem moet, voor zover van toepassing binnen de applicatie, minimaal de volgende correspondentie kunnen opleveren: ;  Specialistenberichten (ontvangen als MedSpe berichten); ;  Radiologieberichten (ontvangen als MedRad berichten); ;  Verwijsbrieven. ; De hierboven genoemde correspondentie dient in één van de onderstaande MIME types opgeleverd te worden: ;  application/pdf; ;  application/msword; ;  application/vnd.openxmlformats-officedocument.wordprocessingml.document; ;  text/plain ;  application/rtf. ; **Toelichting bij eis:** ; De in deze eis benoemde correspondentie betreft een minimale lijst. Een bronsysteem is in principe niet beperkt tot het soort correspondentie dat het mag opleveren. Voor andere dan in de eis genoemde soorten correspondentie geldt niet de verplichting om op te leveren in één van de genoemde MIME types. ; MedMij vereist dat correspondentie wordt opgeleverd aan een PGO o.b.v. de standaard PDF/A. Om bronsystemen te ontlasten biedt LSP+ de functionaliteit om de in de eis beschreven MIME types te vertalen naar de PDF/A standaard. ; **Conditie:** ;  Indien een bronsysteem correspondentie beschikbaar stelt t.b.v. LSP+, dan geldt deze eis; ;  Indien een bronsysteem wil voldoen aan de OPEN vereisten. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Afschermen correspondentie

**Alias**: GBX.OPV.e4650

| Details ; |
| --- |
| **Eis:** ; Correspondentie moet kunnen worden afgeschermd op basis van een bepaalde tijdsperiode. Hierdoor moet het voor de systeemgebruiker mogelijk worden om alleen gegevens beschikbaar te stellen die zijn opgenomen na een specifieke datum. ; Het afschermen op basis van een bepaalde tijdsperiode moet mogelijk zijn voor: ;  de gehele patiëntenpopulatie als geheel; ;  per individuele patiënt. ; **Toelichting bij eis:** ; De NHG heeft een richtlijn 'Online inzage in het H-EPD door patiënt' opgesteld voor het beschikbaar stellen van patiëntgegevens t.b.v. de patiënt. Eén van de voorwaarden die is opgenomen in de richtlijn dient ingebouwd te worden in de XIS-applicaties die dienen als bronsysteem voor correspondentie. Het gaat er hierbij expliciet om dat een gebruiker de mogelijkheid krijgt om alleen correspondentie beschikbaar te stellen vanaf 1 juli 2020. Indien een gebruiker dat wenst, moeten ook eerder verkregen correspondentie beschikbaar gesteld kunnen worden. ; **Conditie:** ;  Indien een bronsysteem correspondentie beschikbaar stelt t.b.v. LSP+, dan is deze eis verplicht; ;  Indien een bronsysteem wil voldoen aan de OPEN vereisten. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Versiebeheer bouwstenen

**Alias**: GBX.OPV.e4580

| Details ; |
| --- |
| **Eis:** ; Bronsystemen, die bevraagd worden voor bouwsteentypes, dienen de bouwsteeninstanties die opgeleverd worden altijd zo volledig mogelijk te vullen met informatie. Hierbij dient het bronsysteem alle velden altijd met indien mogelijk alle waardes die beschikbaar zijn te vullen. ; **Toelichting:** ; Om succesvol bouwstenen te kunnen uitwisselen moet er een versiebeheer mechanisme worden toegepast. Dit versiebeheer mechanisme verplicht opleverende systemen alle velden die zij kunnen vullen te vullen met waardes. Hierdoor zijn opleverende systemen ontkoppeld van de context of toepassing waarin de opvrager een vraag stelt via AORTA. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Leeftijdscontrole patiënt

**Alias**: GBX.OPV.e4570

| Details ; |
| --- |
| **Eis:** ; Indien de opvrager een patiënt is, dan dient het systeem te controleren of de leeftijd van de persoon van wie gegevens worden opgevraagd minimaal 16 jaar is. ; Indien de opvrager jonger is dan 16 jaar, dan dient het systeem de opvraag te beantwoorden met een foutmelding (PATLFT). ; **Toelichting bij eis:** ; Een patiënt jonger dan 16 jaar is niet gerechtigd om zijn eigen gegevens op te vragen zonder toestemming van bijvoorbeeld een ouder of voogd. Op dit moment is het voor een patiënt niet mogelijk om een opvraag te doen onder mandaat. ; De controle of de opvrager een patiënt is moet gebeuren op basis van de rolcode van de 'overseer' van het bericht. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Afschermen patiëntgegevens voor bevraging patiënt

**Alias**: GBX.OPV.e4537

| Details ; |
| --- |
| **Eis:** ; Afscherming van patiëntgegevens voor bevraging door een patiënt moet op dossierniveau kunnen worden ingesteld door de zorgverlener. ; **Toelichting bij eis:** ; Naast de aggregatieniveaus die zijn beschreven in de domeinspecificaties (zoals beschreven in eis Afschermen van patiëntgegevens ) dient het mogelijk te zijn om op verzoek van een patiënt of op inzicht van een zorgverlener het complete dossier af te schermen voor bevraging door een patiënt. ; Het afschermen van patiëntgegevens voor een patiënt is niet gebonden aan het afschermen van patiëntgegevens voor een zorgverlener (en vice versa). ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Afschermen patiëntgegevens op doelgroep

**Alias**: GBX.OPV.e4535.1

| Details ; |
| --- |
| **Eis:** ; Patiëntgegevens dienen afgeschermd te kunnen worden voor bevragingen door patiënten en/of door zorgverleners. ; **Toelichting bij eis:** ; Het aggregatieniveau van afscherming voor beide doelgroepen is opgenomen in eis Afschermen van patiëntgegevens . ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Afhandelen bouwstenen door een bronsysteem

**Alias**: GBX.OPV.e4514

| Details ; |
| --- |
| **Eis:** ; Een XIS dat bouwsteentypen oplevert, moet van die bouwsteentypen alle mogelijke bouwsteeninstantiaties kunnen opleveren. ; **Toelichting bij eis:** ; Een zorgtoepassing bepaalt welke context(en) er opgevraagd kunnen worden. Er dienen gehele bouwstenen afgehandeld te kunnen worden en niet alleen de specifieke bouwsteeninstantiaties zoals beschreven in de zorgtoepassing. Dit is van belang om eventuele compatibiliteit met andere zorgtoepassingen te kunnen garanderen. Daarnaast leiden eventuele aanpassingen in de SDS tabellen niet noodzakelijk tot wijzigingen bij het bronsysteem. ; Deze eis garandeert snellere doorlooptijden aan de kant van een XIS met betrekking tot de implementatie van nieuwe zorgtoepassingen en/of wijzigingen aan de SDS. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Retourneren van opgevraagde patiëntgegevens o.b.v bouwstenen

**Alias**: GBX.OPV.e4513.2

| Details ; |
| --- |
| **Beginsituatie** ;  Het reagerende systeem beschikt over de voor deze functie vereiste vertrouwensmiddelen. ;  Het reagerende systeem heeft de opgevraagde patiëntgegevens aangemeld bij de VWI. ;  Voor de op te leveren patiëntgegevens is sprake van een definitieve koppeling met BSN. ;  Er is een opt-in geregistreerd in het systeem. ; **Trigger** ; Het systeem ontvangt een opvragenBouwsteeninstantiaties-bericht ; **Interacties** ; Het systeem retourneert een opleverenBouwsteeninstantiaties-bericht, zoals beschreven in de eisen aan de concrete systeemrol. ; **Resultaat** ; Het bericht is afgehandeld en de opgevraagde gegevens zijn, indien toegestaan, binnen de gestelde responstijd geretourneerd. ; **Uitzonderingen** ; Uitzonderingen zijn beschreven in de Foutentabel. ; **Opties** ; Het retourbericht bevat alle, in het systeem aanwezige, vrijgegeven patiëntgegevens, die voldoen aan de criteria die zijn meegegeven in het opvragenBouwsteeninstantiaties-bericht. Dit kunnen criteria zijn die zijn overgenomen uit het opvragenPatiëntgegevensContext-bericht (vraagparameters) of door het LSP zijn bepaald (selectieparameters) en toegevoegd aan het opvragenBouwsteeninstantiaties-bericht. De criteria zijn beschreven in de eisen aan de zorgtoepassingen. ; In het geval het bronsysteem, om welke reden dan ook, niet alle opgevraagde gegevens kan retourneren, dient er een foutmelding te worden verstuurd. Deze foutmelding dient door het bronsysteem te worden verstuurd tezamen met de patiëntgegevens die wel opgeleverd kunnen worden. ; Als kopie aangemerkte gegevens mogen niet worden geretourneerd. ; **Responsetijd** ; Bij het beantwoorden van een opvragenBouwsteeninstantiaties-bericht moet rekening gehouden worden met dat dit gebeurt vòòr het tijdstip dat in het bericht is meegegeven ( uiterste-oplevertijd-gbz). Indien het niet mogelijk is om de gevraagde gegevens tijdig op te leveren, dient zo snel mogelijk een melding naar de ZIM gestuurd te worden. ; Het systeem dient in staat te zijn gbx-opleversnelheid kilobytes aan berichtinhoud per seconde te retourneren. ; **Toelichting** ; - ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Opleveren correspondentie

**Alias**: GBX.OPL.e4130

|  | Details ; |
| --- | --- |
| **Eis:** ; Het XIS moet een opvraag correspondentie (QUCO_IN990001NL01) kunnen ontvangen en verwerken. Op basis van deze opvraag dient het XIS een antwoord correspondentie (QUCO_IN990003NL01) te versturen. ; **Toelichting bij eis:** ; <ac:structured-macro ac:name="unmigrated-wiki-markup" ac:schema-version="1" ac:macro-id="ccbc0250-82f8-4e4e-9651-89df57eb8b83"><ac:plain-text-body><![CDATA[Het is mogelijk dat de opvraag specifieke parameters bevat. Het XIS moet op basis van het ontvangen bericht met de daarin opgenomen parameters een antwoord samenstellen. Zowel het binnenkomende opvraagbericht als het uitgaande antwoordbericht staan uitgewerkt in [Art-Decor]. ; ]]></ac:plain-text-body></ac:structured-macro> ; <ac:structured-macro ac:name="unmigrated-wiki-markup" ac:schema-version="1" ac:macro-id="a1157966-ed45-4036-935a-431d0d4720d6"><ac:plain-text-body><![CDATA[Indien bij het verwerken van het binnenkomende opvraagbericht een fout optreedt of een andere reden waarom het opvraagbericht niet verwerkt kan worden, dan dient er een (fout)melding geretourneerd te worden volgens de [Foutentabel]. ; | ]]></ac:plain-text-body></ac:st ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Opleveren contactafspraak

**Alias**: GBX.OPL.e4170

| Details ; |
| --- |
| **Eis:** ; Het XIS moet een opvraag contactafspraak (QUAF_IN990001NL01) kunnen ontvangen en verwerken. Op basis van deze opvraag dient het XIS een antwoord contactafspraak (QUAF_IN990003NL01) te versturen. ; **Toelichting bij eis:** ; <ac:structured-macro ac:name="unmigrated-wiki-markup" ac:schema-version="1" ac:macro-id="2d9760ad-7604-41a9-89d8-59ced736b087"><ac:plain-text-body><![CDATA[Het is mogelijk dat de opvraag specifieke parameters bevat. Het XIS moet op basis van het ontvangen bericht met de daarin opgenomen parameters een antwoord samenstellen. Zowel het binnenkomende opvraagbericht als het uitgaande antwoordbericht staan uitgewerkt in [Art-Decor]. ; ]]></ac:plain-text-body></ac:structured-macro> ; <ac:structured-macro ac:name="unmigrated-wiki-markup" ac:schema-version="1" ac:macro-id="813b09fc-4294-4bef-bf55-52a3fd322ea2"><ac:plain-text-body><![CDATA[Indien bij het verwerken van het binnenkomende opvraagbericht een fout optreedt of een andere reden waarom het opvraagbericht niet verwerkt kan worden, dan dient er een (fout)melding geretourneerd te worden volgens de [Foutentabel]. ; ]]></ac:plain-text-body></ac:structured-macro> ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Afzonderlijk instellen afscherming per doelgroep

**Alias**: GBX.OPV.e4536

| Details ; |
| --- |
| **Eis:** ; Afscherming van gegevens voor bevraging door patiënten en zorgverleners moet afzonderlijk ingesteld kunnen worden. ; **Toelichting bij eis:** ; Het kan mogelijk zijn dat een patiënt gegevens voor andere zorgaanbieders wil laten afschermen, maar dat hij die gegevens wel zelf wil kunnen ontvangen (of andersom). ; Het aggregatieniveau van afscherming voor beide doelgroepen is opgenomen in eis GBX.OPV.e4530**.** ; **Condities:** ; Deze eis geldt indien er zowel gegevens beschikbaar worden gesteld aan patiënten en aan zorgaanbieders. ; |

**Vzvz_Moscow**: Conditioneel  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Systeemrollen - Infrastructuur - Patiëntadministratie

![Diagram](../../../../assets/20d99b9aa740b2da0ef102d96cd4f47fff2021a1586080ec873fb832a123c384.png)  
*Figure 4 : Eisen Infrastructurele Systeemrollen - Patiëntadministratie*

##### Gebruik van geverifieerde BSN's

**Alias**: GBX.IDA.e4060.1

| Details ; |
| --- |
| **Eis:** ; Het systeem moet aan [Opzoeken en tonen patiënteninformatie](pve-his-tbv-open.md#PvEHIStbvOPEN-BK_1292305474), [Voorlopig koppelen van patiëntgegevens aan een BSN](pve-his-tbv-open.md#PvEHIStbvOPEN-BK_874324176), [Controleren geldigheid van een WID](pve-his-tbv-open.md#PvEHIStbvOPEN-BK_64071816), en [Bijhouden behandelrelatie](pve-his-tbv-open.md#PvEHIStbvOPEN-BK_591027313) voldoen of (bij implementatie in een GBZ) een koppeling kunnen leggen met een derde systeem dat aan die eisen voldoet. ; Een systeem die gebruik maakt van een extern patiëntadministrerend systeem is verplicht om te controleren of een BSN daadwerkelijk aan alle AORTA eisen voldoet m.b.t. het BSN. ; **Toelichting bij eis:** ; Ieder GBZ moet over een patiëntadministratie beschikken, maar een XIS hoeft die niet per se in te bouwen. Het staat een GBZ vrij een eigen patiëntadministrerend systeem te kiezen dat voldoet aan de genoemde eisen. De systeemrol van Patiëntadministrerend systeem is daarmee niet verplicht voor XIS-typekwalificatie, maar een GBZ moet wel aantoonbaar over een dergelijk systeem beschikken en dit met het gebruikte XIS hebben gekoppeld om zodoende te kunnen garanderen dat er in de XIS-instantie met geverifieerde BSN's gewerkt wordt. Die gerefereerde eisen hoeven dan niet voor de XIS-typekwalificatie te worden ingebouwd. ; Hoe de controle wordt gedaan op de geldigheid van een BSN is aan de XIS-applicatie. Het is denkbaar dat de XIS-applicatie het patiëntadministrerende systeem actief benaderd, maar het is ook mogelijk dat de XIS-applicatie de statussen van een BSN toegezonden krijgt. Er mogen in géén geval BSN's in een bericht worden opgenomen die niet voldoen aan de AORTA eisen. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: n/a

##### Opzoeken en tonen patiëntgegevens

**Alias**: GBX.IDA.e4010.1

| Details ; |
| --- |
| **Eis:** ; Het systeem moet een gebruiker de mogelijkheid bieden een patiënt op te zoeken in de lokale patiëntadministratie van de zorgaanbieder, door het invoeren van identificerende gegevens, waarna wordt getoond: ;  of de patiënt/cliënt is gevonden, en zo ja ;  of het BSN wel/niet is opgevraagd of geverifieerd bij de SBV-Z ;  de datum en tijd van koppelen ;  de manier van vaststellen van de identiteit: ;  Controle van echtheid en geldigheidsdatum van WID en de gelijkenis van de in de WID genoemde identificerende gegevens ;  Vergewissen, ;  indien beschikbaar het UZI-nummer of anders een unieke identificatie van de gebruiker en het UZI-nummer van mandaterende zorgverlener indien van toepassing ;  in geval van WID-controle: aard en nummer van het WID. ; **Toelichting bij eis:** ; Deze eis voorkomt dat de SBV-Z telkens opnieuw wordt geraadpleegd. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Bijhouden behandelrelatie

**Alias**: GBX.IDA.e4050

| Details ; |
| --- |
| **Eis:** ; Het systeem moet een gebruiker de volgende mogelijkheden bieden in de lokale patiëntadministratie voor een patiënt/cliënt. ; De status van de behandelrelatie inzien, waarbij wordt getoond: ;  of een behandelrelatie bestaat, en zo ja met welke zorgverleners een behandelrelatie bestaat; ;  ten behoeve van welke zorgaanbieder (URA) de behandelrelatie wordt onderhouden. ; Een nieuwe behandelrelatie beginnen, waarbij wordt vastgelegd: ;  begindatum; ;  UZI-nummer van de zorgverlener; ;  de URA van de zorgaanbieder ten behoeve van wie de behandelrelatie onderhouden wordt. ; Een bestaande behandelrelatie beëindigen, waarbij wordt vastgelegd: ;  einddatum; ;  UZI-nummer van de zorgverlener. ; **Toelichting bij eis:** ; De zorgverlener onderhoudt de behandelrelatie hetzij ten behoeve van de zorgaanbieder waarvoor hij werkzaam is, hetzij als zorgaanbieder indien het een zelfstandig werkende beroepsbeoefenaar betreft. ; Een zorgverlener die de patiënt/cliënt niet ziet, bijvoorbeeld in een laboratorium, legt een behandelrelatie vast in de zin van een verklaring dat hij werkt in opdracht van een andere zorgverlener die een behandelrelatie met de patiënt/cliënt heeft. ; |

**Vzvz_Moscow**: Optioneel  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Controleren geldigheid van een WID

**Alias**: GBX.IDA.e4040

| Details ; |
| --- |
| **Eis:** ; Het systeem moet voor een geselecteerde patiënt/cliënt de gebruiker de mogelijkheid bieden: ;  het 'in omloop mogen zijn' van het WID te controleren door raadplegen van de SBV-Z op basis van aard en nummer van het WID; ;  in de lokale patiëntenindex vast te leggen dat hij 'het in omloop mogen zijn' van het WID heeft gecontroleerd, onder vermelding van: ;  resultaat van de controle, ;  datum en tijd, ;  indien beschikbaar het UZI-nummer of anders een unieke identificatie van de gebruiker, ;  aard en nummer van het WID. ;  de onder 2. vastgelegde informatie op elk gewenst moment te raadplegen. ; **Toelichting bij eis:** ; Dit is belangrijk voor een zorgverlener/medewerker die in geval van twijfel over de echtheid of geldigheid van een WID wil nagaan of deze in omloop mag zijn. Hiertoe biedt de SBV-Z een dienst om te kunnen controleren of een bepaald WID in omloop is. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Definitief koppelen van patiëntgegevens aan een BSN

**Alias**: GBX.IDA.e4030

| Details ; |
| --- |
| **Eis:** ; Het systeem moet voor een geselecteerde patiënt/cliënt de gebruiker: ;  de mogelijkheid bieden gewaarschuwd te worden indien nog niet is vastgesteld dat het BSN hoort bij de patiënt/cliënt; ;  de mogelijkheid bieden in de lokale patiëntenindex vast te leggen dat hij heeft vastgesteld dat het betreffende BSN hoort bij de patiënt/cliënt, onder vermelding van: ;  de manier van vaststellen: ; i. Controle van echtheid en geldigheidsdatum van WID en de gelijkenis van de in de WID genoemde identificerende gegevens, ; ii. Vergewissen, ;  Datum en tijd van vaststellen, ;  2. indien beschikbaar het UZI-nummer of anders een unieke identificatie van de gebruiker, en het UZI-nummer van mandaterende zorgverlener indien van toepassing. ;  zorgaanbieder-id van de gebruiker; ;  in geval van WID-controle: aard en nummer van het WID. ; Daarmee is het BSN definitief gekoppeld. ; **Toelichting bij eis:** ; Dit is belangrijk voor een zorgaanbieder die (geautomatiseerd) wil vaststellen of is voldaan aan de eventuele wettelijke verplichting om de identiteit vast te stellen aan de hand van een WID. ; <ac:structured-macro ac:name="unmigrated-wiki-markup" ac:schema-version="1" ac:macro-id="f2c2a335-529c-4d4c-b43e-b16fec91add8"><ac:plain-text-body><![CDATA[Merk op dat de toelichting op [Bbsn-z] artikel 26 een grote verantwoordelijkheid legt bij de zorgaanbieder voor de afweging wel/niet WID controleren. Daarom is geautomatiseerde ondersteuning belangrijk. \]](https://vzvz.atlassian.net/wiki/pages/createpage.action?spaceKey=A8&title=Merk%20op%20dat%20de%20toelichting%20op%20%5BBbsn-z%5D%20artikel%2026%20een%20grote%20verantwoordelijkheid%20legt%20bij%20de%20zorgaanbieder%20voor%20de%20afweging%20wel%2Fniet%20WID%20controleren.%20Daarom%20is%20geautomatiseerde%20ondersteuning%20belangrijk.%20%5C%5D)></ac:plain-text-body></ac:structured-macro> ; Manier van vaststellen: ;  Vaststellen identiteit; Bij inschrijving van een patiënt waar nog geen behandelrelatie mee is, is het verplicht de identiteit van de patiënt vast te stellen aan de hand van een Wettelijk Identificatie Document (WID): een paspoort, Nederlands rijbewijs, Nederlandse ID-kaart of Nederlands vreemdelingendocument. ;  WID-controle; Indien er wordt getwijfeld over de geldigheid van een identiteitsdocument, kan bij de Sectorale Berichten Voorziening in de Zorg (SBV-Z) een WID-controle worden uitgevoerd. Dit kan via een zorginformatiesysteem of via de website van SBV-Z. ;  Opvragen/verifiëren BSN; Hierna moet het BSN geverifiëerd worden en registreren worden dat deze verificatie heeft plaatsgevonden. Alle door VZVZ geaccepteerde zorginformatiesystemen ondersteunen deze mogelijkheid. Komt BSN van een patiënt via een andere zorgverlener? Dan hoeft het niet opnieuw geverifiëerd te worden. Ook als het nummer direct uit de BRP komt , kunt BSN-verificatie achterwege worden gelaten. ; Het systeem kan hierna overgaan tot het vrijgeven en aanmelden van de bij de patiënt/cliënt behorende gegevens. ; |

**Vzvz_Moscow**: Optioneel  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Voorlopig koppelen van patiëntgegevens aan een BSN

**Alias**: GBX.IDA.e4020

| Details ; |
| --- |
| **Eis:** ; Het systeem moet een gebruiker de mogelijkheid bieden het door een burgerregister geretourneerde BSN te koppelen aan de identificerende gegevens in de lokale patiëntenindex waarbij bij het overgenomen BSN automatisch wordt vastgelegd: ;  de bron van het BSN; ;  datum en tijd van koppelen; ;  UZI-nummer of andere identificatie van de gebruiker. ; Er is dan sprake van een voorlopige koppeling tussen BSN en patiëntgegevens. ; **Toelichting bij eis:** ; Dit is nodig opdat een zorgverlener/medewerker kan voldoen aan de wettelijke verplichting van de zorgaanbieder om het BSN op te nemen in zijn administratie, zie Wbsn-z artikel 8.Voor het landelijk uitwisselen van medische patiëntgegevens moet de SBV-Z of de GBA / BRP zijn geraadpleegd. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

##### Verwerken geboortedatums waarin nullen zijn opgenomen

**Alias**: GBX.IDA.e4015

| Details ; |
| --- |
| **Eis:** ; Een geboortedatum die teruggegeven wordt door de SBV-Z kan nullen bevatten (jjjjmm00, jjjj0000 of 00000000). Het XIS moet in staat zijn hiermee adequaat om te gaan zonder dat de applicatie vastloopt. ; **Toelichting bij eis:** ; Deze eis leidt tot de volgende aanvullende eisen: ;  Alle XISsen moeten naast de mogelijkheid om een BSN op te vragen of te verifiëren op basis van de Zoekpaden 1 en 2, ook de dienst opvragen van persoonsgegevens op basis van een ingevoerd BSN inbouwen. ;  Bij het overnemen van de gegevens uit de SBV-Z moet het voor de gebruiker mogelijk zijn om de geboortedatum aan te passen voor het opslaan, indien het systeem meldt dat de gegevens niet in de database kunnen worden opgeslagen. ;  Bij het aanpassen van de geboortedatum in een databasegeaccepteerde datum moet er een indicatie komen dat de geboortedatum handmatig is aangepast. (bijvoorbeeld andere kleur of een indicatie erbij). Nog mooier is de opgeleverde datum opslaan in een (apart) tekstveld. ;  De dienst 'opvragen persoonsgegevens op basis van BSN' moet kunnen worden uitgevoerd, ook als er al persoonsgegevens bekend zijn maar de verificatie mislukt is vanwege de geboortedatum. Hierbij kan er een dialoogvenster wordt getoond waarbij de gegevens van de SBV-Z worden vergeleken met die uit de database van de zorgverlener. ; Een aanpassing van de geboortedatum mag niet leiden tot 'het niet geverifieerd zijn van het BSN'. Dit geldt echter alleen tijdens de dialoog van vergelijken. Indien de geboortedatum buiten de dialoog om aangepast wordt, moet dit wel leiden tot het vervallen van de verificatie. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

### AORTA Eisen Kwaliteit Aangesloten Systemen

![Diagram](../../../../assets/95e4e9288263c4e956318afd5c93f5d605be3f3129938d8dc092c6caaf92052d.png)  
*Figure 5 : AORTA Eisen Kwaliteit aangesloten systemen - Prestatie-efficiëntie*

#### Genereren time-out

**Alias**: GBX.PST.e4020

| Details ; |
| --- |
| **Eis:** ; Het bronsysteem moet binnen 60 seconden na ontvangst van een opvraagbericht een antwoord gegeven. Indien het bronsysteem constateert dat het niet binnen 60 seconden kan antwoorden, dan dient het bronsysteem een foutmelding te genereren. ; **Toelichting bij eis:** ; Om te voorkomen dat TLS-verbindingen onnodig lang tussen het LSP en GBx-en blijven bestaan, worden de TLS-verbindingen automatisch door het LSP verbroken. Het LSP zal na 60 seconden de verbinding met een bronsysteem verbreken en een foutmelding (time-out) terugsturen naar het initiërende systeem. ; Indien het bronsysteem zelf kan vaststellen dat er niet binnen de in de eis opgegeven tijd een antwoord verstuurd kan worden, dan dient het bronsysteem een foutmelding (timeout) te versturen. Op deze manier kan voorkomen worden, dat een initiërend systeem onnodig lang hoeft te wachten. ; De waarde voor de time-out is gebaseerd op voorgaande AORTA-versies. Hierbij is nog geen rekening gehouden met aansluiting op MedMij, die vereist dat een DVZA binnen 60 seconden een antwoord moet geven aan een PGO. Vooralsnog blijft de waarde zoals opgenomen in deze eis gehandhaaft. Het DVZA zal in dat geval na 60 seconden een time-out versturen naar het PGO. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Tijdige verwerking van berichten

**Alias**: GBX.PST.e4015

| Details ; |
| --- |
| **Eis:** ; Een GBx dient voor gebruikersinteracties, na het commando van een gebruiker of een daaropvolgende ontvangst van een bericht van de ZIM, binnen 0,3 seconden het aangegeven resultaat te hebben bereikt. ; **Toelichting bij eis:** ; Deze eis is nodig om te voorkomen dat een zorgaanbieder bij zijn GZN of het LSP gaat klagen over te lange responstijden terwijl de oorzaak misschien ligt bij bijv. een eigen computer die in beslag wordt genomen door andere toepassingen of een lokaal netwerk met onvoldoende bandbreedte. ; Deze eis betekent voor de zorgaanbieder dat hij zijn XIS-applicatie moet installeren op ICT-voorzieningen met voldoende prestaties. Zonodig moeten bijv. de computers worden ingeregeld op de behoefte van deze XIS-applicatie, bijv. als ze ook worden gebruikt voor andere toepassingen. Wellicht kan zijn XIS-leverancier helpen bij het selecteren en inregelen van ICT-voorzieningen. Indien de zorgaanbieder een ASP-leverancier heeft geselecteerd voor zijn XIS, kan hij dit voor de centrale ICT-voorzieningen wellicht overlaten aan die ASP-leverancier, maar moeten de lokale werkplekken niet vergeten worden. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
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
*Figure 6 : AORTA Eisen Kwaliteit aangesloten systemen - Betrouwbaarheid*  
ISO 25010 definieert Betrouwbaarheid als: De mate waarin een systeem, product of component gespecificeerde functies uitvoert onder gespecificeerde condities gedurende een gespecificeerde hoeveelheid tijd.

#### Borgen van de betrouwbaarheid bij grote storingen

**Alias**: GBX.BET.e4020.1

| Details ; |
| --- |
| **Eis:** ; Grote storingen in een GBx mogen niet meer dan gemiddeld 2 keer per jaar voorkomen en dienen dan binnen 1 dag te zijn opgelost. ; **Toelichting bij eis:** ; De term 'grote storing' is niet SMART gedefineerd. Het kan vele soorten storingen betreffen. Het doel van deze eis is om te voorkomen dat een GBx na een ernstige storing zeer lang onbeschikbaar blijft. Onbeschikbaarheid zou bijvoorbeeld kunnen komen omdat er geen onderhoudscontract is en daardoor de hulp slechts langzaam op gang komt. ; Deze eis betekent voor de zorgaanbieder dat hij behalve professioneel beheer ook snel moet kunnen terugvallen op zijn XIS-leverancier, GZN en/of andere ICT-leveranciers. Zo moet bij ernstige storing, snel een leverancier beschikbaar zijn om het probleem te verhelpen. Wellicht kunnen zijn ICT-leveranciers hem een 24-uurs onderhoudscontract bieden. Indien de zorgaanbieder een ASP-leverancier heeft geselecteerd voor zijn XIS, zal hij dit wellicht geheel delegeren aan die ASP-leverancier. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Borgen van de betrouwbaarheid bij kleine storingen

**Alias**: GBX.BET.e4010.1

|  | Details ; |
| --- | --- |
| **Eis:** ; Kleine storingen in een GBx mogen niet meer dan gemiddeld 1 keer per maand voorkomen en dienen dan binnen 10 werkdagen te zijn opgelost. ; **Toelichting bij eis:** ; De term 'kleine storing' is niet SMART gedefinieerd. Het kan vele soorten storingen betreffen. Het doel van deze eis is om te voorkomen dat een GBZ te vaak uitvalt en na een eenvoudig te verhelpen storing meteen langere tijd onbeschikbaar blijft. ; <ac:structured-macro ac:name="unmigrated-wiki-markup" ac:schema-version="1" ac:macro-id="d3ac455e-4a17-4530-974d-d745dbf01642"><ac:plain-text-body><![CDATA[Deze eis betekent voor de zorgaanbieder dat zijn ICT-voorzieningen professioneel moet (laten) beheren. Dit vergt periodieke controle met eventueel preventief onderhoud. Verder moet een onverhoopte storing meteen worden gesignaleerd, zodat een GBZ-beheerder snel beschikbaar kan zijn om het probleem te verhelpen. Wellicht kan zijn XIS-leverancier hem daarbij helpen. Indien de zorgaanbieder een ASP-leverancier heeft geselecteerd voor zijn XIS, zal hij dit wellicht geheel delegeren aan die ASP-leverancier. De afspraken en procedures zoals opgenomen in de [AORTA DAP] dienen hierbij gevolgd te worden. ; | ]]></ac:plain-text-body></ac:structured-macro> ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Minimaliseren van de impact van gepland onderhoud

**Alias**: GBX.BES.e4020.2

| Details ; |
| --- |
| **Eis:** ; Gepland onderhoud van een GBX-applicatie mag niet meer dan twaalf keer per jaar voorkomen en dient niet langer dan een uur te duren. Gepland onderhoud wordt bij voorkeur uitgevoerd binnen aangetoonde daluren. ; De beheerders van de ZIM moeten twee weken van te voren worden ingelicht door de systeembeheerder. ; **Toelichting bij eis:** ; Deze eis is nodig om te voorkomen dat een GBx wegens onderhoud onnodig lang onbereikbaar is, ze betekent voor de organisatie dat onderhoud van de ICT-voorzieningen zoveel mogelijk wordt gepland en zodanig voorbereid dat het GBx slechts kort onbeschikbaar hoeft te zijn. ; **Implicaties:** ; Deze eis betekent voor de organisatie dat onderhoud van de ICT-voorzieningen zoveel mogelijk wordt gepland en zodanig voorbereid dat het GBX slechts kort onbeschikbaar hoeft te zijn. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Borgen van de beschikbaarheid van een GBx

**Alias**: GBX.BES.e4010

| Details ; |
| --- |
| **Eis:** ; Met uitzondering van gepland onderhoud dient een GBx-applicatie te allen tijde beschikbaar te zijn voor het afhandelen van berichten. ; {GBZ} {GBP} De totale beschikbaarheid is minimaal 99,5%. ; {GBK} De totale beschikbaarheid is minimaal 90,0%. ; {GBO} De beschikbaarheid van het systeem is afhankelijk van procedurele afspraken tussen de uitwisselende partijen. ; **Toelichting bij eis:** ; Deze eis is nodig om te voorkomen dat een organisatie, die patiëntgegevens beschikbaar stelt of bereikbaar moet zijn om patiëntgegevens te ontvangen, de voor deze zaken benodigde systemen aan het eind van de werkdag uitschakelt. Deze eis betekent dat deze ICT-voorzieningen nagenoeg continu operationeel moeten zijn. De beschikbaarheid wordt als een voortschrijdend gemiddelde berekend. Omdat het GBK signaleringen kan ontvangen, is de eis verplicht voor GBK. ; **Implicaties:** ; Deze eis betekent dat deze ICT-voorzieningen nagenoeg continu operationeel moeten zijn. De beschikbaarheid wordt als een voortschrijdend gemiddelde berekend. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/499d0ca9ba39ae88655a651897355eef7ae62fc87c51d48dc1f6843b267e50de.png)  
*Figure 7 : AORTA Eisen Kwaliteit aangesloten systemen - Beveiligbaarheid*  
ISO 25010 definieert Beveiligbaarheid als: De mate waarin een product of systeem informatie en gegevens beschermt zodat personen, andere producten of systemen de juiste mate van gegevenstoegang hebben passend bij hun soort en niveau van autorisatie.  
   
Dit schema toont de subcategorieën van Beveilgbaarheid volgens ISO 25010.

#### Beveiligde opslag

**Alias**: SYS.BVL.e4010.1

| Details ; |
| --- |
| **Eis:** ; Data die persoonsgegevens bevatten dienen versleuteld en beveiligd te worden opgeslagen. Het gaat hierbij om alle opgeslagen data (bv. logging en backups). ; **Toelichting bij eis:** ; In principe moet alle data met persoonsgegevens worden geëncrypted. Dit betreft o.a. gegevens die worden opgeslagen ten behoeve van een autorisatiesessie. Mocht hiervan met het oog op systeemprestaties van afgeweken worden, dan dient dit overlegt te worden met VZVZ. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Audit  
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

#### Borgen van plicht tot uitwisselen van patiëntgegevens

**Alias**: GBX.BVL.e4070

| Details ; |
| --- |
| **Eis:** ; Als een GBx voor een systeemrol is aangesloten op de ZIM, moet dat GBx patiëntgegevens in het kader van die systeemrol ook daadwerkelijk uitwisselen onder de regie van de ZIM. ; **Toelichting bij eis:** ; Alle aan AORTA deelnemende partijen zijn gebaat bij een zo volledig mogelijk beeld van relevante patiëntgegevens, daarom is het van belang dat aangesloten partijen hun gegevens ook daadwerkelijk beschikbaar maken via AORTA. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Beveiliging van patiëntgegevens in het GBx

**Alias**: GBX.BVL.e4060

| Details ; |
| --- |
| **Eis:** ; Voor een GBx moet zijn gedefinieerd: ;  welke landelijke toepassingen en systeemrollen worden ondersteund en gebruikt; ;  hoe de grenzen van het GBx lopen door de ICT-voorzieningen van de organisatie; ;  hoe en wanneer patiëntgegevens die grenzen kunnen passeren; ;  hoe wordt gewaarborgd dat patiëntgegevens in de dossiers en postbussen niet kunnen lekken naar onbetrouwbare bestemmingen; ;  hoe wordt gewaarborgd dat patiëntgegevens uit onbetrouwbare bronnen niet kunnen terechtkomen in de dossiers en postbussen of de ZIM; ;  hoe wordt gewaarborgd dat anderen dan bevoegde gebruikers geen fysieke toegang tot (delen van) het GBx kunnen krijgen. ; **Toelichting bij eis:** ; Deze eis is nodig om te voorkomen dat patiëntgegevens, bijvoorbeeld via een andere applicatie, door willekeurige medewerkers kunnen worden benaderd terwijl de organisatie zijn GBx heeft beveiligd met firewalls, authenticatie- en vertrouwensmiddelen. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Documentverificatie  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Borgen betrouwbare koppeling tussen pas en applicatie

**Alias**: GBX.BVL.e4050.1

| Details ; |
| --- |
| **Eis:** ; Een GBx moet zodanig zijn ingericht dat: ;  passen met SHA-256-certificaten gelezen en gebruikt kunnen worden; ;  paslezers gekoppeld zijn aan werkplekken van gebruikers; ;  de PIN-code die ten behoeve van een authenticatiemiddel wordt ingetoetst op een werkplek, exclusief wordt aangeboden aan de gekoppelde paslezer, ;  {GBx} alle gegevens in berichten die ten behoeve van een gebruiker worden ontvangen exclusief aan die gebruiker worden gepresenteerd; ;  {GBK} alle gegevens in HL7-berichten die ten behoeve van een patiëntopdracht worden ontvangen exclusief gekoppeld worden aan de betreffende patiëntopdracht. ;  geborgd wordt dat: ;  {GBx} het in het bericht vermelde UZI-nummer en de rolcode van de auteur overeenkomen met de UZI-pashouder die het bericht heeft geïnitieerd; ;  {GBK} het in het bericht vermelde certificaatnummer en CA van de auteur overeenkomen met de PKIO-pashouder die het bericht heeft geïnitieerd; ;  {GBx} de auteur inderdaad is gemandateerd door de in het bericht vermelde (eind)verantwoordelijke, of dezelfde persoon is; ;  {GBx} de in het bericht vermelde URA van auteur, (eind)verantwoordelijke en zorginstelling aan elkaar gelijk zijn; ;  {GBK} de in het bericht vermelde instellingsindicatie van de auteur het klantenloket is; ;  {GBK} de instelling van de verantwoordelijke niet ingevuld is. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Audit  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/75448c0d298dbf9ac29fd4e35eba49135602db468df984e154a1b131875aea0e.png)  
*Figure 8 : AORTA Eisen Kwaliteit aangesloten systemen - Uitwisselbaarheid*  
ISO 25010 definieert Uitwisselbaarheid als: De mate waarin een product, systeem of component informatie uit kan wisselen met andere producten, systemen of componenten, en/of het de gewenste functies kan uitvoeren terwijl het dezelfde hard- of software-omgeving deelt.  
Dit diagram toont de subcategorieën zoals gedefinieerd door ISO 25010.

#### Aansluiting op productie-omgeving LSP

**Alias**: GBX.CON.e4120

| Details ; |
| --- |
| **Eis:** ; GBZ-beheerder moet er namens de eigenaar van het GBZ op toezien dat uitsluitend productiesystemen gekoppeld worden aan de productie-omgeving van het LSP. Overtredingen van deze eis zullen gemeld worden aan de eigenaar van het GBZ. ; **Toelichting bij eis:** ; Vanwege mogelijke beveiligingsrisico's en kwaliteitgaranties in de keten mogen er alleen GBZ-en met een geaccepteerde XIS-applicatie aansluiten op de productie-omgeving van het LSP . ; Bij het niet naleven van bovenstaande eis behoudt VZVZ zich het recht voor op aanvullende sancties. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

#### Tijdsynchronisatie GBx en ZIM

**Alias**: GBX.CON.e4030.2

| Details ; |
| --- |
| **Eis:** ; Een GBx dient NTP te gebruiken voor tijdsynchronisatie met de ZIM. De tijdklok van een GBx mag niet meer dan een halve seconde afwijken van de tijdklok van de ZIM. ; **Toelichting bij eis:** ; Deze eis is nodig om te voorkomen dat de tijdklok van het GBx gaat afwijken van de tijdklok van de ZIM. Voor eenzelfde interactie tussen een GBx en de ZIM moeten beide systemen immers dezelfde tijdstempels loggen. Dit is belangrijk wanneer de toezichthouder of patiënt een geval van vermeend onrechtmatige uitwisseling van patiëntgegevens wil onderzoeken en daartoe zowel de lokale toegangslog van het GBx als de centrale toegangslog van het LSP wil raadplegen. ; Deze eis betekent voor de organisatie dat er binnen het GBx een NTP-client is geïnstalleerd en dat deze is afgestemd op de NTP-server van de ZIM. Ook is het mogelijk dat de GZN een gezamenlijke NTP-client beheert voor alle aangesloten zorgaanbieders en op een andere wijze klaarspeelt dat de tijdklok van hun GBx'en gelijk lopen met die van de ZIM. ; Deze eis betekent voor de organisatie dat het GBx periodiek moet synchroniseren tegen een NTP-server om synchroon te blijven met de ZIM. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Monitoring  
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

#### Communicatie met het LSP via een GZN

**Alias**: GBX.CON.e4010, GBX.CON.e4010.1

| Details ; |
| --- |
| **Eis:** ; Een GBx dient via een DCN van een gekwalificeerde GZN te communiceren met het LSP. ; **Toelichting bij eis:** ; Organisaties kunnen bij VZVZ verifiëren of een netwerkaanbieder over een GZN-kwalificatie beschikt. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Aansluittoets  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product

### AORTA Eisen Kwaliteit Applicatie

![Diagram](../../../../assets/a3dd7c7c5aa4dfb5697246e7e9ad4e5cc1b3ff29ed34d94baa4ca07ca16e5a92.png)  
*Figure 9 : AORTA Eisen Kwaliteit applicatie - Beveiligbaarheid*  
ISO 25010 definitieert Beveiligbaarheid als: De mate waarin een product of systeem informatie en gegevens beschermt zodat personen, andere producten of systemen de juiste mate van gegevenstoegang hebben passend bij hun soort en niveau van autorisatie.

#### Toegangslog bijhouden (FHIR)

**Alias**: GBX.LOG.e4016

| Details ; |
| --- |
| **Eis:** ; Het systeem moet alle binnenkomende en uitgaande berichten loggen in de toegangslog. Hierbij dienen onderstaande gegevens gelogd te worden, indien aanwezig in het bericht: ;  de identiteit van de patiënt/cliënt/burger (BSN) waar het bericht betrekking op heeft; ;  de identiteit van de organisatie waar het bericht vandaan komt of naar toe wordt gestuurd; ;  de functie en identiteit van de zorgverlener, medewerker of patiënt zoals opgenomen in het verstuurde en/of ontvangen bericht. De functie is de aorta-rolcode zoals opgenomen in het claim-element van het transactietoken. ;  de gebruikersinteractieID. Dit is een combinatie van HTTP-operatie, de URL inclusief de ontvangen zoekparameters en de contentVersion uit de AORTA-Version header; ;  het tijdstip en tijdzone (ten opzichte van UTC) van het moment dat het bericht ontvangen/verstuurd is; ;  de bericht-id van het ontvangen/verstuurde bericht. Dit is het messageID in de HTTP header; ;  het initiële bericht-id van het ontvangen/verstuurde bericht. Dit is het initialMessageID in de HTTP header; ;  de aan het bericht gekoppelde gegevensdienst. Dit is de waarde zoals opgenomen in de scope van het transactietoken; ;  een indicatie van eventueel opgetreden foutsituaties met betrekking tot het ontvangen en verzenden van de berichten. Hierbij dient de HTTP-foutcode, alle informatie in de eventueel aanwezige operationOutcome en de enventuele WWW-Authenticate HTTP response header gelogd te worden. ; **Toelichting bij eis:** ; Het doel van de logging is het inzichtelijk kunnen maken van de datastroom door de gehele keten. Het inzichtelijk maken van de loggegevens kan van belang zijn voor auditredenen of beheerwerkzaamheden zoals het oplossen van fouten in de keten. Deze eis is conform de vereisten zoals beschreven in de NEN7513. ; |

**Vzvz_Moscow**: n/a  
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

#### Opzetten beveiligde verbinding vanuit de ZIM met een GBx

**Alias**: GBX.CON.e4090.2

| Details ; |
| --- |
| **Eis:** ; Het GBx dient voor het landelijk uitwisselen van patiëntgegevens een TLS-sessie met de ZIM met de volgende kenmerken te accepteren: ;  tweezijdige authenticatie met behulp van het UZI-servercertificaat van het GBZ en het servercertificaat van de ZIM, ;  tijdelijke sleutels die elke 5 minuten ververst worden, ;  gebruikmakend van Cipher Suites die door het NCSC minimaal worden gekenmerkt als goed en tevens worden ondersteund door de ZIM.Voor encryptie moet altijd de sterkste vorm als eerste worden geprobeerd, ;  een maximale sessieduur van 8 uur, ;  een ten hoogste ongebruikte TLS-sessie van 15 minuten. ; **Toelichting bij eis:** ; Dit is nodig opdat de ZIM een voldoende hoog beveiligingsniveau kan afdwingen bij het opzetten van een TLS-sessie met een GBx. ; Dit betekent voor de zorgaanbieder dat hij of zijn XIS-leverancier de bovenstaande parameters moet instellen in de TLS-library in de betrokken XIS-applicatie(s) en/of de eventuele communicatieserver. ; |

**Vzvz_Moscow**: Conditioneel.  
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

#### Instellen configuratieparameters t.b.v. communicatie en authenticatie van de ZIM

**Alias**: GBX.FBH.e4050.3

| Details ; |
| --- |
| **Eis:** ; De GBx-beheerder moet de volgende configuratieparameters in het GBx kunnen instellen: ;  URI en hostnaam van de ZIM, ;  applicatie-id van de eigen applicatie, ;  applicatie-id van het productieschakelpunt waarop kan worden aangesloten. ; **Toelichting bij eis:** ; Dit is nodig opdat een GBx deze parameters kan gebruiken bij de HTTP-communicatie met en authenticatie van de ZIM. ; De in het GBx ingestelde waarden komen overeen met de in het applicatieregister van de ZIM geregistreerde gegevens. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Bijhouden van een gebruikersregistratie

**Alias**: GBX.FBH.e4030

| Details ; |
| --- |
| **Eis:** ; Binnen het GBx dient te worden bijgehouden welke UZI-passen worden toegelaten voor gebruik. Deze gebruikersregistratie is uitsluitend toegankelijk voor gebruikers van de gastheerinstelling, na authenticatie op basis van een sterk authenticatiemiddel (2 factorauthenticatie bijvoorbeeld via een UZI-pas) van diezelfde gastheerinstelling. ; **Toelichting bij eis:** ; Dit is nodig om te voorkomen dat een willekeurig persoon de gebruikersregistratie kan aanpassen. Deze bevoegdheid komt bij een specifiek persoon te liggen. ; Dit betekent voor de zorgaanbieder dat hij moet zorgen dat de bovenstaande rol van autorisatiebeheerder door een van zijn medewerkers wordt ingevuld. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Opzetten beveiligde verbinding met de ZIM

**Alias**: GBX.CON.e4080.5

| Details ; |
| --- |
| **Eis:** ; Het GBx dient voor het landelijk uitwisselen van patiëntgegevens een TLS-sessie met de ZIM met de volgende kenmerken op te zetten: ;  tweezijdige authenticatie met behulp van het servercertificaat van de ZIM en ;  (indien tokenauthenticatie) het servercertificaat van het GBx voor vertrouwensniveau midden ;  het servercertificaat van het GBx voor vertrouwensniveau laag {GBK} en midden ;  tijdelijke sleutels die elke 5 minuten ververst worden door middel van TLS Secure Renegotiation; ;  gebruikmakend van Cipher Suites die door het NCSC minimaal worden gekenmerkt als goed; ;  gebruikmakend van de sterkste cipher suite die gedeeld wordt met de ZIM; ;  gebruikmakend van de hoogste toegestane TLS-versie die door beide partijen wordt ondersteunt; ;  een ongebruikte TLS-sessie van maximaal 15 minuten. ; **Toelichting bij eis:** ; Dit is nodig opdat een GBx een voldoende hoog beveiligingsniveau kan afdwingen bij het opzetten van een TLS-sessie met de ZIM. ; Dit betekent voor de organisatie dat hij of zijn XIS-leverancier de bovenstaande parameters moet instellen in de TLS-library in de betrokken applicatie(s) en/of de eventuele communicatieserver. Het GBx is niet in staat te controleren of de ZIM daadwerkelijk het (server)certificaat van de GBx opvraagt, maar mag er impliciet van uitgaan dat dit gebeurt en dat de ZIM het certificaat ook controleert. Hiermee wordt tweezijdige authenticatie bewerkstelligd. ; |

**Vzvz_Moscow**: Conditioneel.  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Toegangslog bijhouden

**Alias**: GBX.LOG.e4015.1

| Details ; |
| --- |
| **Eis:** ; Het systeem moet de volgende berichtuitwisselingen loggen: ;  Ontvangen opvraagberichten en de daarop verzonden antwoorden; ;  Verzonden opvraagberichten en daarop verkregen antwoorden; ;  Verzonden opdrachtberichten en kennisgevingberichten. ; De log bevat per berichtuitwisseling tenminste: ;  de identiteit van de patiënt/cliënt (BSN) ;  identiteit van de opvragende/versturende en bestemde organisatie ;  de functie en identiteit van de opvragende of versturende zorgverlener of medewerker of patiënt. ;  type van de uitgevoerde gebruikersinteractie ;  het tijdstip en tijdzone (ten opzichte van UTC) van de gebruikersinteractie ;  de bericht-id van het ontvangen (opvraag- of bevestig-) bericht ;  de bericht-id van het verzonden (oplever- of opdracht-) bericht ;  de gegevenssoorten of contextcodes van de verzonden en ontvangen patiëntstukken; ;  een indicatie van eventueel opgetreden foutsituaties met betrekking tot het ontvangen en verzenden van de berichten. ; **Toelichting bij eis:** ; Dit is nodig opdat aan de hand van de berichtuitwisseling precies achterhaald kan worden: ;  {GBx}{GBO}wat voor soort patiëntstukken wanneer zijn opgevraagd door welke zorgverlener/medewerker van welke andere zorgaanbieder; ;  {GBK} wat voor soort opvragingen, opdrachten en kennisgevingen wanneer zijn verzonden resp. ontvangen door welke klantenloketmedewerker; ;  wat voor soort patiëntstukken wanneer zijn toegestuurd aan welke andere zorgaanbieder of ZIM; ;  welke inhoud die patiëntstukken precies hadden; ;  wat voor soort patiëntstukken wanneer zijn opgevraagd door welke patiënt vanuit welke organisatie. ; Dit betekent voor de zorgaanbieder dat hij of zijn XIS-leverancier deze berichtenlogfunctie moet inbouwen in de betrokken XIS-applicatie(s) of de eventuele communicatieserver. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Afbreken van een gebruikerssessie

**Alias**: GBX.IDA.e4090.1

| Details ; |
| --- |
| **Eis:** ; Het systeem moet een gebruikerssessie voor het landelijk uitwisselen van patiëntgegevens op vertrouwensniveau laag of midden afsluiten: ;  op commando van de gebruiker (zoals een muisklik of toetsencombinatie); ;  door uitnemen van het vertrouwensmiddel door de zorgverlener/medewerker; ;  wanneer de applicatie gedurende maximaal 60 minuten niet is gebruikt. Deze tijd dient instelbaar te zijn in het syteem, maar mag niet de 60 minuten overschrijden; ;  wanneer de sessie gedurende 1 uur open staat; ;  IP-adres van gebruiker gedurende een sessie wijzigt. ; **Toelichting bij eis:** ; Dit is nodig opdat een gebruiker zelf zijn gebruikerssessie kan uitloggen met de zekerheid dat niemand anders zijn sessie kan voortzetten en vervolgens zijn bevoegdheden kan misbruiken. Daarnaast is deze eis nodig om te tegen te gaan dat een in onbruik geraakte sessie door een onbevoegde kan worden misbruikt. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Blokkeren van ingetrokken, verlopen en niet authentieke passen

**Alias**: GBX.IDA.e4085.2

| Details ; |
| --- |
| **Eis:** ; Het GBx dient het starten van een gebruikersessie op vertrouwensniveau midden te weigeren indien: ;  de geldigheidstermijn van het transactietoken is verlopen of nog niet is aangevangen; ;  het transactietoken niet correct is ondertekend; ;  het certificaat, waarmee het transactietoken is getekend, op een geldige lijst staat van ingetrokken certificaten (CRL) van het UZI-register; ;  het transactietoken is geweigerd door het LSP. ; **Toelichting bij eis:** ; Deze eis is conform de regels van PKI Overheid. Er moet voorkomen worden dat een GBZ toegang geeft als gevolg van een ongeldige UZI-pas. ; Alleen een gebruiker die een UZI-pas heeft en de pincode weet, kan een geldig transactietoken genereren. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Inloggen op vertrouwensniveau midden

**Alias**: GBX.IDA.e4080.3

| Details ; |
| --- |
| **Eis:** ; Het systeem moet een gebruiker de mogelijkheid bieden een gebruikerssessie op vertrouwensniveau midden te starten door: ;  {GBx}{GBK}het invoeren van zijn vertrouwensmiddel op de werkplek en het invoeren van de bijbehorende toegangscode; ;  {GBP} zich op niveau DigiD-midden te authenticeren. ; {GBx} Een GBx dient hierbij een UZI-pas toe te laten indien: ;  de UZI-pas is vastgelegd in de gebruikerstabel (zie ook eis GBX.FBH.e4030); ;  het passen betreft die zijn uitgegeven onder de op dat moment geldende certificaatboom of –bomen. (SHA-256). ; Hierbij dient de applicatie te controleren of het certificaat op de pas niet op de CRL staat. ; {GBK} Een GBK dient hierbij een PKIO-pas toe te laten indien de betreffende medewerker geautoriseerd is voor toegang tot de GBK-applicatie en te weigeren in de overige gevallen. ; **Toelichting bij eis:** ; Dit is nodig opdat gebruikers in staat worden gesteld tot het landelijk uitwisselen van gegevens op vertrouwensniveau midden. ; VZVZ levert gratis generiek tooling in de vorm van Zorg-ID om de implementatie van het authenticeren met de UZI-pas te ondersteunen. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Audit  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product  
   
![Diagram](../../../../assets/c46fdaae5d9c0803311fd24cd93927239a7b99dc0fb6897fb756d01c503f2a7b.png)  
*Figure 10 : AORTA Eisen Kwaliteit applicatie - Uitwisselbaarheid*  
ISO 25010 definieert Uitwisselbaarheid als: De mate waarin een product, systeem of component informatie uit kan wisselen met andere producten, systemen of componenten, en/of het de gewenste functies kan uitvoeren terwijl het dezelfde hard- of software-omgeving deelt.

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
| **Eis:** ; Het GBx dient voor berichtuitwisseling met de ZIM de volgende protocolstack te gebruiken: ;  HL7 FHIR ;  JWT ;  HTTP v1.1/HTTP v2.0 ;  TCP ;  IPv4 ; **Toelichting bij eis:** ; Het is niet toegestaan om een lagere protocolversie te hanteren dan die in deze protocolstack vermeld is. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Acceptatietest  
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

#### Ondersteunen servercertificaten en ondertekeningalgoritmen

**Alias**: GBX.CON.e4110.2

| Details ; |
| --- |
| **Eis:** ; Het GBx dient UZI/PKIo-servercertificaten van de (verschillende) generatie(s) te ondersteunen zoals beschikbaar wordt gesteld door het UZI-Register. ; Er moet gebruik worden gemaakt van het SHA-256 ondertekeningsalgoritme. ; **Toelichting bij eis:** ; Het UZI-register geeft UZI-servercertificaten uit onder één of meerdere certificaatbomen. In het geval er onder diverse certificaatbomen UZI-servercertificaten wordt uitgegeven, is het zaak om alle servercertificaten uitgegeven onder de diverse certificaatbomen te kunnen ondersteunen. ; Een GBX-communicatieserver dient te zijn ingericht op het ondertekeningalgoritme SHA-256. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Bevorderen interoperabiliteit bij berichtuitwisseling

**Alias**: GBX.CON.e4066

| Details ; |
| --- |
| **Eis:** ; Het GBX volgt voor berichtuitwisseling als bedoeld in eis GBX.CON.e4060 de WS-I Basic Profile 1.0 specificaties. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Juiste afhandeling van SOAP headers

**Alias**: GBX.CON.e4065

| Details ; |
| --- |
| **Eis:** ; Het GBx volgt voor de afhandeling van SOAP-headers in berichten de aanwijzingen zoals beschreven in implementatiehandleiding Berichttransport. ; **Toelichting bij eis:** ; Het gaat hierbij onder andere om het op de juiste wijze in acht nemen van SOAP-headerattributen 'mustUnderstand' and 'actor'. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Acceptatietest  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Protocolstack voor berichtuitwisseling

**Alias**: GBX.CON.e4060.2

| Details ; |
| --- |
| **Eis:** ; Het GBx dient voor berichtuitwisseling met de ZIM de volgende protocolstack te gebruiken: ;  HL7v3 ;  SOAP v1.1 ;  SAML 2.0 ;  HTTP v1.1 ;  TLS-verbindingen met NCSC beveiligingsniveau “goed” ;  TCP ;  IPv4 ; **Toelichting bij eis:** ; Het is niet toegestaan om een lagere protocolversie te hanteren dan die in deze protocolstack vermeld is, zoals bv SSLv2 en SSLv3. ; Voor de versie van TLS geldt dat de beveiligingsrichtlijnen van NCSC worden gevolgd indien redelijkerwijs mogelijk. Alle deelnemers dienen beveiligingsniveau "goed" te ondersteunen, tenzij beveiligingsniveau "voldoende" nodig is voor de ondersteuning van oudere clients. Bij de TLS-handshake dient de hoogste toegestane TLS-versie gekozen te worden die beide partijen ondersteunen. ; Het GBX volgt voor berichtuitwisseling de WS-I Basic Profile 1.0 specificaties. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Aansluittoets  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

### AORTA Eisen Organisatie van een GBX

![Diagram](../../../../assets/b951ce2861c83d85f9864b4418b83b670c1a1d5d642723198081de7d350907d0.png)  
*Figure 11 : Eisen aan de beheerorganisatie van een GBX*

#### Afmelden patiënt na overlijden

**Alias**: GBX.FBH.e4090

| Details ; |
| --- |
| **Eis:** ; Patiënten dienen na overlijden binnen een maand te worden afgemeld in het LSP, tenzij expliciet anders vereist wordt. ; **Toelichting bij eis:** ; Afmelding in het LSP beslaat het (mogelijk) afmelden in de verwijsindex en het abonnementenregister. ; Het streven is om het abonnementenregister zuiver te houden ten behoeve van de kwaliteit van AORTA en de garanties met betrekking tot de prestaties. Indien abonnementen niet meer gebruikt worden, dan dienen deze afgemeld te worden in het abonnementregister. ; Het is de verantwoordelijkheid van de zorgaanbieder om zorg te dragen voor de informatiebeschikbaarheid van zijn patiënten. Echter, om te voorkomen dat gegevens van overleden patiënten onnodig in de verwijsindex blijven staan, is het wenselijk om de verwijzing te verwijderen. Het is mogelijk dat bepaalde informatie na overlijden nog voor een beperkte duur beschikbaar moet blijven. Het is aan de zoraanbieder om deze inschatting te maken. ; Vooralsnog is er een tijdsbestek van een maand voorgesteld, waarbinnen de afmeldingen gedaan dienen te worden. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Business

#### Wijzigen logging

**Alias**: AGE.LOG.e4060

| Details ; |
| --- |
| **Eis:** ; Gegevens in de log mogen niet wijzigbaar of verwijderbaar (alleen in het kader van eis **AGE.LOG.e4050**) zijn. Het niet kunnen wijzigen/verwijderen van loggegevens moet worden afgedwongen door technische maatregelen. ; **Toelichting** ; Conform NEN 7513:2018 Paragraaf 6.4.3 ; |

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

#### Uitschakelen logging

**Alias**: AGE.LOG.e4030

| Details ; |
| --- |
| **Eis:** ; Het loggen van de berichtuitwisseling in de toegangslog en het loggen van acties op de toegangslog mogen niet uitgeschakeld kunnen worden. ; **Toelichting bij eis:** ; Conform NEN 7513:2018 Paragraaf 6.4.2 ; |

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

#### Loggen toegangsregeling

**Alias**: AGE.LOG.e4070

| Details ; |
| --- |
| **Eis:** ; Elke wijziging in de toegangsregeling dient te worden gelogd. Hierbij moet onweerlegbaar kunnen worden vastgesteld welke persoon met welke rol welke specifieke aanpassing heeft doorgevoerd. ; **Toelichting** ; Conform NEN 7513:2018 Paragraaf 6.3 ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: n/a  
**Vzvz_Req_Soort**: n/a  
**Vzvz_Req_Type**: n/a

#### Loggen inzage logging

**Alias**: AGE.LOG.e4020

| Details ; |
| --- |
| **Eis:** ; Elke inzage van de toegangslog dient gelogd te worden. Hierbij moet onweerlegbaar kunnen worden vastgesteld welke persoon met welke rol inzage heeft gehad in welke specifieke gegevens. ; **Toelichting** ; Deze eis is conform NEN 7513:2018. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Audit  
**Vzvz_Req_Soort**: Functional  
**Vzvz_Req_Type**: Product

#### Bewaartermijn loggegevens

**Alias**: AGE.LOG.e4010

| Details ; |
| --- |
| **Eis:** ; De bewaartermijn van de toegangsloggegevens is *<toegangslog_bewaartermijn>.* Voor de overige logs (technische logs) geldt een bewaartermijn van *<systeemlog_bewaartermijn>.* ; **Toelichting bij eis:** ; Voor de toegangslog (log met betrekking tot patiëntgegevens) geldt (mogelijk) een andere bewaartermijn dan voor de systeemlog. Conform NEN 7513:2018 paragraaf 8.5 kan een patiënt binnen een bepaalde tijdsperiode nog aanspraak maken op inzage in de loggegevens. Deze tijdsperiode kan voor de technische log echter onnodig lang zijn en daarmee onnodig veel opslagcapaciteit verbruiken. ; De waarden *<toegangslog_bewaartermijn>* en *<systeemlog_bewaartermijn>* kunnen per afsprakenstelsel/architectuur afgesproken worden. Indien deze waarden niet expliciet ingevuld worden door het afsprakenstelsel/architectuur, dan geldt voor beide de waarde 5 jaar. ; |

**Vzvz_Moscow**: n/a  
**Vzvz_Req_Verificatie**: Monitoring  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Business

#### Voldoen aan wet- en regelgeving

**Alias**: GBX.ALG.e4010

| Details ; |
| --- |
| **Eis:** ; Een GBX dient te voldoen aan de NEN7510, NEN7512 en NEN7513 normen. ; **Toelichting bij eis:** ;  In de wet gebruik BSN in de zorg Artikel 2 Lid 4a is afgedwongen dat de gegevensverwerking, zoals bedoelt in de bijbehorende wet, aantoonbaar moet voldoen aan de NEN7510. ;  In de concept AMvB aanvullende bepalingen verwerking persoonsgegevens in de zorg wordt in artikel 5 gesteld dat de netwerkverbindingen (intern netwerk en GZN) moeten voldoen aan het bepaalde in NEN 7512 en in artikel 7 wordt gesteld dat de logging van zorgaanbieders moet voldoen aan het bepaalde in NEN 7513. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Eigenverklaring  
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

#### Een GBx valt onder Nederlandse wet- en regelgeving

**Alias**: GBX.CON.e4050.1

| Details ; |
| --- |
| **Eis:** ; De technische infrastructuur van het GBX dient zich in de Europese Unie te bevinden. De voertaal met de zorgaanbieder en de organisatie die het GBx beheert en exploiteert is Nederlands. Met betrekking tot de contracten tussen de zorgaanbieder en bovengenoemde moet de Nederlandse wet-en regelgeving van toepassing zijn. ; De zorgaanbieder en de organisatie's die het GBX beheert en exploiteert dient in Nederland gevestigd te zijn. ; In de contracten tussen de zorgaanbieder en bovengenoemde moet de Nederlandse wet- en regelgeving van toepassing zijn. ; **Toelichting bij eis:** ; Dit is nodig om er voor te zorgen dat de infrastructuur en dienstverlening volledig onder Nederlandse wet- en regelgeving valt. De exploitant dient waarborgen actief te hebben die voorkomen dat gegevens oneigenlijk gebruikt kunnen worden en te voldoen aan de privacy wetgeving. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Aansluittoets  
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

#### Bijhouden van een beheerlog

**Alias**: GBX.SBH.e4050

| Details ; |
| --- |
| **Eis:** ; Beheerhandelingen moeten worden vastgelegd in een beheerlog. De organisatie dient de opdrachtgever en toezichthouder inzage te geven in deze beheerlog. In het beheerlog wordt bijgehouden welke systeembeheerder de inhoud van welke berichten heeft ingezien. ; **Toelichting bij eis:** ; De beheerlog ondersteunt de controle op de juiste werking van systemen en de controle op het volgen van procedures. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Acceptatietest  
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

#### Actueel houden van het applicatieregister

**Alias**: GBX.SBH.e4030

| Details ; |
| --- |
| **Eis:** ; GBX-beheer moet de beheerde GBX-applicatie(s) bij LSP-beheer aanmelden zodat deze in het applicatieregister kan worden opgenomen en zodat GBX-beheer de status ervan actueel kan houden in [Supportal](https://supportal.vzvz.nl). ; **Toelichting bij eis:** ; Deze eis is nodig om te kunnen participeren in berichtuitwisselingen via AORTA. Het actueel houden van het applicatieregister is belangrijk voor een correcte afhandeling van berichten. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Documentverificatie  
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

#### Beheren van en toegang verschaffen tot de toegangslog

**Alias**: GBX.SBH.e4010

| Details ; |
| --- |
| **Eis:** ; De organisatie moet een toegangslogbeheerder benoemen. De toegangslogbeheerder moet verzoeken van de toezichthouder om de lokale toegangslog te raadplegen inwilligen. ; **Toelichting bij eis:** ; Deze eis is nodig omdat de toezichthouder op AORTA voor het uitvoeren van haar bevoegdheden informatie nodig kan hebben over de gebeurtenissen waarbij het GBx met het LSP informatie heeft uitgewisseld. ; {GBx} Deze toegangslogbeheerder kan door alle zorgverleners worden gemandateerd om de toegangslog te raadplegen, om zo te voorkomen dat hij voor een verzoek tot raadplegen van de lokale toegangslog inzake een bepaalde patiënt/cliënt steeds de behandelende zorgverleners moet inschakelen. ; {GBK} Deze toegangslogbeheerder kan worden gemandateerd om de toegangslog te raadplegen door de GBK-verantwoordelijke. ; {GBP} Deze Logbeheerder dient vóór de aansluiting aan het LSP te worden doorgegeven aan VZVZ. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Audit  
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

#### Verantwoordelijk UZI-pasbeleid

**Alias**: GBX.FBH.e4017

| Details ; |
| --- |
| **Eis:** ; Een organisatie moet zorgdragen dat er voldoende UZI-passen binnen een organisatie actief zijn. Het aantal benodigde UZI-passen is afhankelijk van de organisatiestructuur en de toepassing waarbinnen een UZI-pas wordt gebruikt. ; **Toelichting:** ; Zorgaanbieders waar veel zorgverleners werkzaam zijn mogen niet uit kostenoverwegingen besparen op UZI-passen en daarom bijvoorbeeld de mandatering in de gehele organisatie bij een of enkele specialisten leggen. Er dient goed afgewogen te worden wie verantwoordelijk is voor bepaalde interacties met het LSP. Verantwoordelijkheid wordt onder andere bepaald door de rol van de zorgverlener en het hebben van een (afgeleide) behandelrelatie met een patiënt. ; |

**Vzvz_Moscow**: Verplicht  
**Vzvz_Req_Verificatie**: Monitoring  
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

#### Ondersteuning van gebruikers bij problemen met de landelijke uitwisseling van informatie

**Alias**: GBX.FBH.e4010

| Details ; |
| --- |
| **Eis:** ; De GBx-servicedesk dient gebruikers te ondersteunen bij GBx-, GZN- en LSP-gerelateerde problemen. De GBx-servicedesk dient: ;  Gebruikers een inschatting te geven van de verwachte oplostermijn; ;  Gebruikers regelmatig te informeren over de voortgang van de oplossing; ;  Tijdens kantooruren telefonisch bereikbaar te zijn voor gebruikers, GZN-leveranciers en het LSP-beheer; ;  Voor noodgevallen telefonisch bereikbaar te zijn voor gebruikers, de GZN en het LSP; ;  Incidenten en problemen te registreren en beheren; ;  een procedure geïmplementeerd te hebben voor het melden en afhandelen van incidenten en wijzigingsverzoeken conform het Dossier Afspraken en Procedures ([AORTA DAP](https://www.vzvz.nl/uploaded/FILES/htmlcontent/AORTA_DAP_20140130_v2.3.pdf)); ;  Nederlandstalig te zijn. ; **Toelichting bij eis:** ; Het doel van deze eis is om de landelijke elektronisch uitwisseling van gegevens door gebruikers te bevorderen, de diensten van AORTA te verbeteren en verstoringen te signaleren, voorkomen en verhelpen. ; |

**Vzvz_Moscow**: Verplicht (Must)  
**Vzvz_Req_Verificatie**: Aansluittoets  
**Vzvz_Req_Soort**: Non-Functional  
**Vzvz_Req_Type**: Product  
   
<span id="latestPvEHIStbvOPEN-INSERT_Section2End"></span><span id="INSERT_Section2End"></span>End
