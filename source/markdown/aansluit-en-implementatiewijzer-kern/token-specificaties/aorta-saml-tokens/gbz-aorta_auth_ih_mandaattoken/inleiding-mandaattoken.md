[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBZ AORTA_Auth_IH_Mandaattoken](../gbz-aorta_auth_ih_mandaattoken.md)

# Inleiding mandaattoken

## Doel en scope

Dit document betreft een specificatie van het mandaattoken. Het betreft hier een mandaattoken voor gebruik bij communicatie tussen het goed beheerde Zorgsystemen (GBZ) en het landelijk schakelpunt (LSP).

## Doelgroep voor dit document

Dit document is bedoeld voor softwareontwikkelaars van goed beheerde zorgsystemen en het LSP, die op grond van de HL7v3 communicatiestandaard en op grond van dit document berichten willen uitrusten met het SAML mandaattoken. Daarnaast wordt het plaatsen van de digitale handtekening besproken (zie ook [IH tokens generiek]).

## Documenthistorie

| **Versie** ; | **Datum** ; | **Omschrijving** ; |  |
| --- | --- | --- | --- |
| V8.0.2.0 ; | 31-januari-2018 ; |  | Initieel document. ; |
| V8.0.3.0 ; | 1-juli-2018 ; |  | INI-8462: Plaatsing Mandaattoken naast het Transactietoken ; |
| V8.0.3.0 ; | 1-jan-2019 ; |  | INI-8769: Verduidelijken <security>-header ; |
| V8.0.3.0 ; | 1-jan-2019 ; |  | INI-8771: Aanpassen controle geldigheid Mandaattoken ; |
| V8.0.3.0 ; | 1-jan-2019 ; |  | INI-8754: Uitbreiden voorbeeld m.b.t. verwijzing naar certificaatgegevens en verwijzing naar het juiste certificaat met keyUsage non-repudiation (0x40) ; |
| V8.2.0.0 ; | 7-okt-2020 ; |  | Controle op overseer in hoofstuk 5.1 aangepast. ; |
