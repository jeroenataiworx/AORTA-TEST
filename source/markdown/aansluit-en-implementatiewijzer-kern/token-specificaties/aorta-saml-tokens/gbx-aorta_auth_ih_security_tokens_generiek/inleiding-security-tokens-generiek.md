[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBx AORTA_Auth_IH_Security_tokens_generiek](../gbx-aorta_auth_ih_security_tokens_generiek.md)

# Inleiding Security tokens generiek

## Doel en scope

Dit document legt de basis voor de verschillende beveiligingsimplementatie handleidingen waarin security tokens voor specifieke toepassing concreet beschreven worden. Dit document beschrijft wat security tokens zijn, wat het doel is van security tokens en hoe security tokens in de AORTA-architectuur worden ingezet.   
Dit document is normatief, behalve de hoofdstukken en paragrafen waarin wordt aangegeven dat ze informatief zijn.

## Doelgroep voor dit document

Dit document is bedoeld voor softwareontwikkelaars van XIS’en.

De lezer wordt verondersteld kennis te hebben van [XML], [Namespaces], [SOAP], [HTTP], [WSDL] en [IH Transport].

## Documenthistorie

| **Versie** ; | **Datum** ; | **Omschrijving** ; |
| --- | --- | --- |
| 6.10.0.0 ; | 12-okt-2011 ; | RfC 36422: SHA-256 in tokenauthenticatie. Voor het bere­ken­en van hashwaarden wordt SHA-1 òf SHA-256 gebruikt. ; RfC 46142: SOAP Headers van tokens worden uitgebreid met soap:actor. ; RfC 46183: soap:actor moet zijn gbx ipv gbz. Verwijzing naar [IH Transport] opgenomen en tekst in Par 6.1 aangepast. ; |
| 6.11.0.0 ; | 12-okt-2012 ; | Ongewijzigde herpublicatie als onderdeel van AORTA-Infrastructuur v6·11 ; |
| 8.0.1.0 ; | 15-mei-2017 ; | RfC 65898 en RfC 36422 SHA1 delen van AORTA_Auth_IH_Berichtauthenticatie_UZI.doc bijwerken met SHA256 en bij voorbeelden SHA256 in IH Security tokens generiek toegelicht. ; |
| 8.0.1.0 ; | 15-mei-2017 ; | RfC 71719: PKIO/UZI certificaten gaan over naar de Public G3/Private G1 generatie ; |
| 8.0.1.0 ; | 15-mei-2017 ; | RfC 76206: SSL verwijderen ; |
| 8.0.3.0 ; | 15-nov-2018 ; | Opgenomen in publicatie 8.0.3.0 ; |
| 8.1.0.0 ; | 1-aug-2019 ; | INI-8877: Conditionele query ; |
| 8.1.0.0 ; | 1-aug-2019 ; | INI-8811: Loggen UZI-CertificaatID ; |
| 8.2.0.0 ; | 7-okt-2020 ; | Opgenomen in publicatie 8.2.0.0 ; |
| 8.4.0.0 ; | 2025 ; | Uitbreiding op Security tokens n.a.v. ZORG-ID CA (Certificate Authority). De CA speelt een cuciale rol in de digitale beveiliging, met name in de PKI. ; |

## Legenda

Deze implementatiehandleiding gebruikt de volgende symbolen:

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | **Let op! Dit is een aandachtpunt.** ; **Een opmerking die de aandacht vestigt op een bepaald opvallend aspect.** ; |
| --- | --- |
| ![Diagram](../../../../../assets/eaa300f77606e1141147b9e3abcc5dd05d9a937feb73b0a5f30faf3328b4f07d.png) | Dit is een 'open issue' of 'known issue'. ; Een kwestie die nog open ligt voor discussie, maar onderkend is. ; |
| ![Diagram](../../../../../assets/a97ade543f8dcfc1117fee4aa9a043d68d08ff1225c023e65b4911cb911f20f7.png) | Dit is een frequently asked question (FAQ) met antwoord. ; |
