[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBZ AORTA_Auth_IH_Contracttoken](../gbz-aorta_auth_ih_contracttoken.md)

# Token afhandeling contracttoken

## Verificatie van het bericht

Het is belangrijk vast te stellen dat de velden in het SAML concept-contracttoken en het SAML contracttoken een correcte waarde hebben en geldig ondertekend zijn. Wanneer dit niet zou gebeuren, kan een kwaadwillende met een gestolen token nog steeds gegevens opvragen van bv. ieder willekeurig burger servicenummer (BSN).

### Controles op het concept-contracttoken

Het SAML concept-contracttoken wordt door de ontvanger uit het betreffende attribuut van het contracttoken gehaald, Base64 gedecodeerd en vervolgens gevalideerd.

Bij de validatie van het SAML concept-contracttoken moet de ontvanger controleren of:

- De aanduiding voor de versie van SAML gedefinieerd is op "2.0", zie paragaaf 2.4.1 Uniekheid;

- De juiste Subject Distinguished Name is opgenomen die deze assertion heeft gecreëerd en de gebruiker heeft geauthenticeerd, zie paragraaf 2.4.2 Afzender. De Subject Distinguished Name dient overeen te komen met de Subject Distinguished Name uit het servercertificaat.

- De Assertion correct is ondertekend door de Signature te valideren met het meegestuurde certificaat.

- Het gebruikte certificaat waarmee de ondertekening heeft plaatsgevonden geldig was ten tijde van de ondertekening.

- Indien het certificaat op de CRL is geplaatst, dan dient dit plaats te hebben gevonden nadat het token gegenereerd en ondertekend is.

- De relevante certificaatketen te valideren op geldigheid.

- De geldigheidsperiode van het token, zie paragraaf 2.4.4 Geldigheid, niet langer is dan 10 jaar;

- Het bericht ontvangen is binnen de geldigheidsperiode van het token, zie paragraaf 2.4.4 Geldigheid;

- De afnemer van het SAML concept-contracttoken (audience) minimaal de ZIM is, zie paragraaf 2.4.5 Ontvanger;

- Alleen die attributen zijn gedefinieerd, die zijn beschreven in paragraaf 2.4.7 Attributen;

Het tokenID dient in de log van de ZIM opgenomen te worden.

### Controles op het contracttoken

Het SAML contracttoken wordt door de ontvanger gevalideerd.

Bij de validatie van het SAML contracttoken moet de ontvanger controleren of:

- De aanduiding voor de versie van SAML gedefinieerd is op "2.0", zie paragaaf 2.4.1 Uniekheid;

- De juiste Subject Distinguished Name is opgenomen die deze assertion heeft gecreëerd en de gebruiker heeft geauthenticeerd, zie paragraaf 2.4.2 Afzender. De Subject Distinguished Name dient overeen te komen met de Subject Distinguished Name uit het servercertificaat.

- De Assertion correct is ondertekend door de Signature te valideren met het meegestuurde certificaat.

- Het gebruikte certificaat waarmee de ondertekening heeft plaatsgevonden geldig was ten tijde van de ondertekening.

- Indien het certificaat op de CRL is geplaatst, dan dient dit plaats te hebben gevonden nadat het token gegenereerd en ondertekend is.

- De relevante certificaatketen te valideren op geldigheid.

- De geldigheidsperiode van het token, zie paragraaf 2.4.4 Geldigheid, niet langer is dan 10 jaar;

- Het bericht ontvangen is binnen de geldigheidsperiode van het token, zie paragraaf 2.4.4 Geldigheid;

- De afnemer van het SAML concept-contracttoken (audience) minimaal de ZIM is, zie paragraaf 2.4.5 Ontvanger;

- Alleen die attributen zijn gedefinieerd, die zijn beschreven in paragraaf 2.4.7 Attributen;

- Het AttributeCertificate geldig is, de bijbehorende CRL opgehaald kan worden en het AC niet op deze CRL staat.

Het tokenID dient in de log van de ZIM opgenomen te worden.

### Controles tussen concept-contract token en contracttoken

Om te controleren dat het concept-contracttoken en het contracttoken daadwerkelijk bij elkaar horen dienen de volgende controles uitgevoerd te worden:

- De issuer uit het concept-contracttoken komt overeen met het subject van het contracttoken

- De issuer uit het contracttoken komt overeen met het subject van het concept-contracttoken

- De _Scope in beide tokens is identiek

Als aan één van de bovenstaande condities niet is voldaan, moet het contracttoken door de ontvanger geweigerd worden en een SOAP foutmelding aan het verzendende systeem afgegeven worden, zie foutafhandeling in [IH tokens generiek].
