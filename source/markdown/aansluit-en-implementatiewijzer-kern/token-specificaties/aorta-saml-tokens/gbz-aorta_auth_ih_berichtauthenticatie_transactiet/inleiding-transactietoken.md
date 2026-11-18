[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBZ AORTA_Auth_IH_Berichtauthenticatie_Transactietoken](../gbz-aorta_auth_ih_berichtauthenticatie_transactiet.md)

# Inleiding transactietoken

## Doel en scope

Dit document heeft tot doel een handleiding te geven voor de implementatie van het koppelvlak tussen het goed beheerde Zorgsystemen (GBZ) en het landelijk schakelpunt (LSP) voor wat betreft de toe te passen technieken voor de authenticatie van zorgverleners en medewerkers.

## Doelgroep voor dit document

Dit document is bedoeld voor softwareontwikkelaars van goed beheerde zorgsystemen en het LSP, die op grond van de HL7v3 communicatiestandaard en op grond van dit document berichten willen uitrusten met het SAML transactietoken. Daarnaast wordt het plaatsen van de digitale handtekening besproken (zie ook [IH tokens generiek]).

## Documenthistorie

| **Versie** ; | **Datum** ; | **Omschrijving** ; |
| --- | --- | --- |
| v8.0.2.0 ; | 31-januari-2018 ; | Initieel document. ; |
| v8.0.3.0 ; | 15-nov-2018 ; | Opgenomen in publicatie 8.0.3.0 ; |
| v8.1.0.0 ; | 26-juni-2019 ; | INI-8877: Aanpassing ten behoeve van de conditionele query ; |
| V8.1.0.0 ; | 13-september-2019 ; | INI-9019: Optioneel gebruik BSN ; |
| V8.1.1.0 ; | 30-januari-2020 ; | In hoofdstuk 3.1 verduidelijkt hoe om te gaan met het ondertekenen met een server certificaat. ; |
| V8.1.1.0 ; | 30-januari-2020 ; | Op verschillende plekken in het document aangescherpt dat er ook ondertekend kan worden met een UZI-servercertificaat. ; |
| V8.2.0.0 ; | 22-juli-2020 ; | Controle op overseer in hoofstuk 4.1 aangepast. ; |
| V8.4 ; | 2025 ; | Transactietoken o.b.v. ZORG-ID Smartcard. ; |

## Legenda

Deze implementatiehandleiding gebruikt de volgende symbolen:

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | **Let op! Dit is een aandachtpunt.** ; **Een opmerking die de aandacht vestigt op een bepaald opvallend aspect.** ; |
| --- | --- |
| ![Diagram](../../../../../assets/eaa300f77606e1141147b9e3abcc5dd05d9a937feb73b0a5f30faf3328b4f07d.png) | Dit is een 'open issue' of 'known issue'. ; Een kwestie die nog open ligt voor discussie, maar onderkend is. ; |
| ![Diagram](../../../../../assets/a97ade543f8dcfc1117fee4aa9a043d68d08ff1225c023e65b4911cb911f20f7.png) | Dit is een frequently asked question (FAQ) met antwoord. ; |
