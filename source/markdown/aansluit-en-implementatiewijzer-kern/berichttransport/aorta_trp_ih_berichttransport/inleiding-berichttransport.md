[AORTA 8.5.2](../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../aansluit-en-implementatiewijzer-kern.md) / [Berichttransport](../../berichttransport.md) / [AORTA_Trp_IH_Berichttransport](../aorta_trp_ih_berichttransport.md)

# Inleiding Berichttransport

## Doel en scope

Dit document specificeert het berichttransport over SOAP/HTTP zoals dat in AORTA wordt toegepast. Het berichttransport vormt de verbinding tussen de HTTP(S)-laag, en de er bovenliggende HL7v3-berichten. Dit document beschrijft:

- hoe HL7v3-interacties worden verpakt in SOAP voor transport op basis van webservices;

- hoe SOAP op hoofdlijnen wordt toegepast binnen AORTA;

- hoe webservices worden gedefinieerd met behulp van WSDL;

- de toepassing van HTTP(S)-transport in relatie tot de webservices;

- versionering van webservices en end point uri’s;

- betrouwbaarheidsaspecten van dat transport.

## Doelgroep voor dit document

Dit document is bedoeld voor softwareontwikkelaars van zorgtoepassingen en de Zorg Informatie Makelaar (ZIM), die op grond van de HL7v3-communicatiestandaard en dit document berichten in AORTA willen transporteren.

De lezer wordt verondersteld kennis te hebben van [XML], [SOAP] en [WSDL]. Lezing van de AORTA-documentatie wordt ten zeerste aanbevolen.

## Documenthistorie

| **Versie** ; | **Datum** ; | **Omschrijving** ; |
| --- | --- | --- |
| 6.10.0.0 ; | 12-okt-2011 ; | Initiële versie na herstructurering AORTA-documentatie. ; RFC 46142: Wijziging in verband met elektronische handtekening: gebruik SOAP Header attributen (§4.3). ; RFC 46691: HTTP Fouten doorgeven door ZIM verduidelijkt in Par 4.5 en 4.5.4. ; |
| 6.10.0.0 ; | 2-apr-2012 ; | RFC 51940: toegestane waarden voor faultactor opgenomen in Par 4.5.2. ; |
| 6.11.0.0 ; | 5-dec-2012 ; | Herpublicatie als onderdeel van AORTA-Infrastructuur v6·11 ; |
| 6.12.0.0 ; | 13-aug-2013 ; | RfC 52089: Fout met ZIM als tussenstation verduidelijkt. ; |
| 8.0.1.0 ; | 15-mei-2017 ; | RfC 52477: Uitwisseling op basis van bouwstenen ; |
| 8.0.1.0 ; | 15-mei-2017 ; | RfC 76206: SSL verwijderen ; |
| 8.0.3.0 ; | 15-nov-2018 ; | Opgenomen in publicatie 8.0.3.0 ; |
| 8.1.0.0 ; | 1-aug-2019 ; | INI-8877: Toevoegen inschrijftoken t.b.v. conditionele query ; |

## Legenda

Dit document gebruikt de volgende symbolen:

| ![Diagram](../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Let op! Dit is een aandachtpunt. ;  Een opmerking die de aandacht vestigt op een bepaald opvallend aspect. ; |
| --- | --- |
| ![Diagram](../../../../assets/eaa300f77606e1141147b9e3abcc5dd05d9a937feb73b0a5f30faf3328b4f07d.png) | Dit is een ‘open issue’ of ‘known issue’. ;  Een kwestie die nog open ligt voor discussie, maar onderkend is. ; |
| ![Diagram](../../../../assets/a97ade543f8dcfc1117fee4aa9a043d68d08ff1225c023e65b4911cb911f20f7.png) | Dit is een frequently asked question (FAQ) met antwoord. ; |

## Structuur

Dit document is als volgt opgebouwd:

- Inleiding (niet normatief).

- Berichtuitwisselingsstandaarden (niet normatief): inleiding in de relevante gebruikte standaarden.

- Informatiestromen (niet normatief): een overzicht van berichtuitwisseling zoals gebruikt bij het landelijk EPD.

- XML, SOAP en HTTP (normatief): richtlijnen voor het gebruik. Voor GBx’en geldt dat §3 alleen verplicht is bij ondersteuning van elektronische handtekening[^1].

- AORTA en WSDL (normatief): algemene toelichting bij de WSDL bestanden.

- Betrouwbaar transport (normatief).

Normatief betekent dat het verplicht is om te conformeren aan de specificaties. De niet normatieve hoofdstukken zijn bedoeld als achtergrondinformatie.

Noot: dit document gebruikt veel voorbeelden van XML materialen (WSDL, XSD, XML), de XML materialen die AORTA publiceert zijn mogelijk recenter, en leidend.

[^1]: De elektronische handtekening wordt binnen AORTA vooralsnog niet toegepast.
