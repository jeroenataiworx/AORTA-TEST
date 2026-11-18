[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBZ AORTA_Auth_IH_Contracttoken](../gbz-aorta_auth_ih_contracttoken.md)

# Inleiding contracttoken

## Doel en scope

Dit document heeft tot doel een handleiding te geven voor de implementatie van het koppelvlak tussen twee partijen die onderling een contract willen afsluiten voor wat betreft de toe te passen technieken voor de authenticatie van beide partijen. Partij A (de contractnemer) stuurt hierbij een request voor een concept-contracttoken naar partij B (de te contracteren partij). Partij B neemt gegevens over uit het request, stelt het concept contract op, ondertekend dit en stuurt het terug naar partij A. Partij A neemt het gehele concept contracttoken op in het uiteindelijke contracttoken, ondertekend dit en stuurt het contracttoken terug naar partij B. Met behulp van dit token mag partij B handelen namens partij A. Indien het Uitwisselsysteem een register van tokens bijhoudt dient partij A het contracttoken tevens naar dit register te sturen.

Dit document beschrijft zowel het concept-contracttoken als het (definitieve) contracttoken.

## Doelgroep voor dit document

Dit document is bedoeld voor softwareontwikkelaars van goed beheerde zorgsystemen, en het LSP, die op grond van de toegelaten berichtstandaarden en op grond van dit document berichten willen uitrusten met het contracttoken.

Daarnaast wordt in dit document het plaatsen van de digitale handtekening besproken (zie ook [IH tokens generiek]).

## Documenthistorie

| **Versie** ; | **Datum** ; | **Omschrijving** ; |
| --- | --- | --- |
| 8.3.0.0 ; | 1 nov 2023 ; | Initieel document. ; |
| 8.3.0.0 ; | 9 nov 2023 ; | OrganisatieID gewijzigd in Subject Distinguished Name ; |
