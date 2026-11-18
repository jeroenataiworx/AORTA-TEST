[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBZ AORTA_Auth_IH_Inschrijftoken](../gbz-aorta_auth_ih_inschrijftoken.md)

# Inleiding inschrijftoken

## Doel en scope

Dit document heeft tot doel een handleiding te geven voor de implementatie van het koppelvlak tussen het goed beheerde Zorgsystemen (GBZ) en het landelijk schakelpunt (LSP) voor wat betreft de toe te passen technieken voor de authenticatie van zorgverleners en medewerkers.

## Doelgroep voor dit document

Dit document is bedoeld voor softwareontwikkelaars van goed beheerde zorgsystemen en het LSP, die op grond van de HL7v3 communicatiestandaard en op grond van dit document berichten willen uitrusten met het SAML inschrijftoken. Het SAML inschrijftoken is met name vereist bij gebruik van een conditionele query.

Daarnaast wordt in dit document het plaatsen van de digitale handtekening besproken (zie ook [IH tokens generiek]).

## Documenthistorie

| **Versie** ; | **Datum** ; | **Omschrijving** ; |
| --- | --- | --- |
| v8.1.0.0 ; | 21-juli-2019 ; | Initieel document. ; |
| v8.1.1.0 ; | 4-februari-2020 ; | INI-9137: MessageID WID/SBV-controle verwijderen uit inschrijftoken ; |
| v8.1.1.0 ; | 11-maart-2020 ; | INI-9169: Inschrijftoken is 1.5 jaar geldig ondanks geldigheid certificaat ; |
| v8.2.0.0 ; | 1-oktober-2020 ; | INI-9355: Aanpassingen doorgevoerd t.b.v. werkprocesondersteuning: ;  Uitvoerder optioneel gemaakt; ;  BSN validatietijd mag timestamp zijn van aanmaken inschrijftoken; ;  SubjectConfirmationData verplicht gesteld; ; * ; |
| 8.2.0.1 ; | 14-november-2021 ; | Inschrijftoken op basis van inscannen WID ; |
| 8.3.0.0 ; | 9-februari-2022 ; | De controle “De Issuer uit het inschrijftoken (URA) dient overeen te komen met de waarde van het attribuut “Zorgaanbieder” uit het scantoken” verwijderd om het gebruik van het scantoken bij een andere zorgaanbieder toe te staan. ; |
| 8.3.0.1 ; | 6-februari-2024 ; | Inschrijftoken o.b.v. UZI-pas of Scantoken verlengen via ZORG-ID Smart. ; |
| 8.3.0.2 ; | 4-september-2024 ; | Kleine aanpassing op @AuthnInstant en "Uitvoerder" bij verlenging van Inschrijftoken. ; |
| 8.4.0.0 ; | 2025 ; | Inschrijftoken o.b.v. ZORG-ID Smartcard. ; |
