[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [ZORG-ID AORTA_Auth_IH_Scantoken_en_WID_token](../zorg-id-aorta_auth_ih_scantoken_en_wid_token.md)

# Inleiding Scan en WID token

## Doel en scope

Dit document heeft tot doel een handleiding te geven voor de implementatie van het koppelvlak tussen het Goed Beheerd Zorgsysteem (GBZ), ZORG-ID en het landelijk schakelpunt (LSP) voor wat betreft de toe te passen technieken voor de authenticatie van zorgverleners, medewerkers en burgers (patiënten).

## Doelgroep voor dit document

Dit document is bedoeld voor softwareontwikkelaars van goed beheerde zorgsystemen, ZORG-ID en het LSP, die op grond van de toegelaten berichtstandaarden en op grond van dit document berichten willen uitrusten met het SAML scantoken. Het SAML scantoken is met name toepasbaar bij gebruik van de ZORG-ID app.

Daarnaast wordt in dit document het plaatsen van de digitale handtekening besproken (zie ook [IH tokens generiek]).

## Documenthistorie

| **Versie** ; | **Datum** ; | **Omschrijving** ; |
| --- | --- | --- |
| 8.3.0.0 ; | 11-november-2021 ; | Initieel document. ; |
| 8.3.0.0 ; | 09-februari-2022 ; | Tekst bij figuur 1 aangepast ; |
| 8.3.0.0 ; | 11-februari-2022 ; | Enkele kleine tekstuele wijzigingen ; |
| 8.3.0.0 ; | 31 maart 2022 ; | Structuur wid_raw_data toegevoegd, ; |
