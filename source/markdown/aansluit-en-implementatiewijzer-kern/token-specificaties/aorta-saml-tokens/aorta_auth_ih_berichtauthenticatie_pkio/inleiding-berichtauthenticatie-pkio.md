[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [AORTA_Auth_IH_Berichtauthenticatie_PKIO](../aorta_auth_ih_berichtauthenticatie_pkio.md)

# Inleiding Berichtauthenticatie PKIO

### Doel en scope

Dit document heeft tot doel een handleiding te geven voor de implementatie van het koppelvlak tussen het goed beheerd klantenloket (GBK) en het landelijk schakelpunt (LSP) voor wat betreft de toe te passen technieken voor de authenticatie van klantenloketmedewerkers.

### Doelgroep voor dit document

Dit document is bedoeld voor softwareontwikkelaars van het goed beheerd klantenloket en het LSP, die op grond van de HL7v3 communicatiestandaard en op grond van dit document berichten willen uitrusten met het SAML authenticatietoken. Daarnaast wordt het plaatsen van de digitale handtekening besproken (zie ook [IH tokens generiek]).

### Documenthistorie

| **Versie** ; | **Datum** ; | **Omschrijving** ; |
| --- | --- | --- |
| 6.10.0.0 ; | 12-okt-2011 ; | RfC 46142: SOAP Headers van tokens worden uitgebreid met soap:actor. ; |
| 6.11.0.0 ; | 12-okt-2012 ; | Ongewijzigde herpublicatie als onderdeel van AORTA-Infrastructuur v6·11 ; |
| 6.12.0.0 ; | 17-juni-2013 ; | RfC 58592: Subject.organizationName gewijzigd naar Vereniging van Zorgaanbieders voor Zorgcommunicatie. ; |
| 8.0.1.0 ; | 15-mei-2017 ; | Opgenomen in publicatie 8.0.1.0 ; |
| 8.0.2.0 ; | 31-januari-2018 ; | RfC 76680: Uitbreiding DigiD authenticatieniveaus ; |
| 8.0.3.0 ; | 15-nov-2018 ; | Opgenomen in publicatie 8.0.3.0 ; |
| 8.2.0.0 ; | 7-okt-2020 ; | Opgenomen in publicatie 8.2.0.0 ; |

## Legenda

Deze implementatiehandleiding gebruikt de volgende symbolen:

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | **Let op! Dit is een aandachtpunt.** ; **Een opmerking die de aandacht vestigt op een bepaald opvallend aspect.** ; |
| --- | --- |
| ![Diagram](../../../../../assets/eaa300f77606e1141147b9e3abcc5dd05d9a937feb73b0a5f30faf3328b4f07d.png) | Dit is een 'open issue' of 'known issue'. ; Een kwestie die nog open ligt voor discussie, maar onderkend is. ; |
| ![Diagram](../../../../../assets/a97ade543f8dcfc1117fee4aa9a043d68d08ff1225c023e65b4911cb911f20f7.png) | Dit is een frequently asked question (FAQ) met antwoord. ; |
