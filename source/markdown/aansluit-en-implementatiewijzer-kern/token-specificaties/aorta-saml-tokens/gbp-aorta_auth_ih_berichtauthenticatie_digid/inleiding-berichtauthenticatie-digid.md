[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBP AORTA_Auth_IH_Berichtauthenticatie_DigiD](../gbp-aorta_auth_ih_berichtauthenticatie_digid.md)

# Inleiding berichtauthenticatie DigiD

## Doel en scope

Dit document heeft tot doel een handleiding te geven voor de implementatie van het koppelvlak tussen het goed beheerd patiënten portaal (GBP) en het landelijk schakelpunt (LSP) voor wat betreft de toe te passen technieken voor de authenticatie van patiënten.   
Dit document specificeert het SAML (Security Assertion Markup Language) authenticatietoken voor patiënten die zich bij DigiD laten authenticeren.

## Doelgroep voor dit document

Dit document is bedoeld voor softwareontwikkelaars van het goed beheerd patiënten portaal en het LSP, die op grond van de HL7v3 communicatiestandaard en op grond van dit document berichten willen uitrusten met het SAML authenticatietoken. Daarnaast wordt het plaatsen van de digitale handtekening besproken (zie ook [IH tokens generiek]).

## Documenthistorie

| **Versie** ; | **Datum** ; | **Omschrijving** ; |
| --- | --- | --- |
| **6.10.0.0** ; | 12 oktober 2011 ; | RfC 46142: SOAP Headers van tokens worden uitgebreid met soap:actor. ; |
| **6.11.0.1** ; | 29 januari 2013 ; | Aanpassingen ten behoeve van DigiD v4.0 koppelvlak SAML ; |
| **8.0.1.0** ; | 28 mei 2014 ; | Geactualiseerd en mogelijkheid van DigiD om assertions te tekenen verwerkt ; |
| **8.0.1.0** ; | 15 mei 2017 ; | RfC 76206: SSL verwijderen ; |
| **8.0.1.0** ; | 13 sep 2017 ; | RfC 78296: Aanpassing KeyInfo veld in DigiD SAML assertion ; |
| **8.0.2.0** ; | 31 januari 2018 ; | RfC 76680: DigiD authenticatiesterktes uitbreiden ; |
| **8.0.2.0** ; | 31 januari 2018 ; | RfC 77951: Controle op SubjectConfirmation door LSP ; |
| **8.0.3.0** ; | 1 juli 2018 ; | INI-8527: Kleine aanpassingen m.b.t. authenticatiesterktes in hoofdstuk 2.3.6. en Bijlage B. ; Aanpassing referentie m.b.t. Logius koppelvlakspecificatie DigiD. ; INI-8792: ZIM als audience in DigiD-token verwijderen ; |
| **8.2.0.0** ; | 7-okt-2020 ; | Opgenomen in publicatie 8.2.0.0 ; |
