[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [AORTA_Auth_IH_Berichtauthenticatie_UZI](../aorta_auth_ih_berichtauthenticatie_uzi.md)

# Inleiding Berichtauthenticatie UZI

### Doel en scope

Dit document beschrijft op welke wijze berichten tussen een goed beheerd zorgsysteem (GBZ) en het landelijk schakelpunt (LSP) worden uitgerust met authenticatietokens.

Dit document specificeert het authenticatietoken voor zorgverleners en hun medewerkers dat wordt gemaakt met hun UZI-pas. Daarnaast wordt het plaatsen van de digitale handtekening besproken (zie ook [IH tokens generiek]).

### Doelgroep voor dit document

Dit document is bedoeld voor softwareontwikkelaars van XIS’en.

### Documenthistorie

| **Versie** ; | **Datum** ; | **Omschrijving** ; |
| --- | --- | --- |
| 6.10.0.0 ; | 12-okt-2011 ; | RfC 46142: SOAP Headers van tokens worden uitgebreid met soap:actor. ; |
| 6.11.0.0 ; | 12-okt-2012 ; | Ongewijzigde herpublicatie als onderdeel van AORTA-Infrastructuur v6·11 ; |
| 6.12.0.0 ; | 4-okt-2013 ; | Bijlage technische context (gebruik UZI-pas) weer toegevoegd (zat in v6.0.5.0, maar verdwenen in v6.10) ; |
| 8.0.1.0 ; | 15-mei-2017 ; | RfC 52477: Uitwisseling op basis van bouwstenen. ; |
| 8.0.1.0 ; | 15-mei-2017 ; | RfC 65592: SHA1 encryptiemethoden verwijderd ; |
| 8.0.1.0 ; | 15-mei-2017 ; | RfC 65898 en RfC 36422 SHA1 delen van AORTA_Auth_IH_Berichtauthenticatie_UZI.doc bijwerken met SHA256. Voor nieuwe leveranciers is het gebruik van SHA256 als DigestMethod en als onderdeel van SignatureMethode verplicht. ;  Verwijzingen naar G2 generatie UZI-certificaat hierarchie verwijderd. ; |
| 8.0.1.0 ; | 15-mei-2017 ; | RfC 71719: PKIO/UZI certificaten gaan over naar de Public G3/Private G1 generatie. ; |
| 8.0.1.0 ; | 15-mei-2017 ; | RfC 76206: SSL verwijderen ; |
| 8.0.3.0 ; | 15-nov-2018 ; | Opgenomen in publicatie 8.0.3.0 ; |
| 8.2.0.0 ; | 7-okt-2020 ; | Opgenomen in publicatie 8.2.0.0 ; |

## Legenda

Deze implementatiehandleiding gebruikt de volgende symbolen:

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | **Let op! Dit is een aandachtpunt.** ; **Een opmerking die de aandacht vestigt op een bepaald opvallend aspect.** ; |
| --- | --- |
| ![Diagram](../../../../../assets/eaa300f77606e1141147b9e3abcc5dd05d9a937feb73b0a5f30faf3328b4f07d.png) | Dit is een 'open issue' of 'known issue'. ; Een kwestie die nog open ligt voor discussie, maar onderkend is. ; |
| ![Diagram](../../../../../assets/a97ade543f8dcfc1117fee4aa9a043d68d08ff1225c023e65b4911cb911f20f7.png) | Dit is een frequently asked question (FAQ) met antwoord. ; |
