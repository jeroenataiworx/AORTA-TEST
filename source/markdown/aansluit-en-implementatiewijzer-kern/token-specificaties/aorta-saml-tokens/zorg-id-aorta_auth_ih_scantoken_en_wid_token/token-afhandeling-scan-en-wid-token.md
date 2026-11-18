[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [ZORG-ID AORTA_Auth_IH_Scantoken_en_WID_token](../zorg-id-aorta_auth_ih_scantoken_en_wid_token.md)

# Token afhandeling Scan en WID token

## Token afhandeling

### Verificatie van het bericht

Het is belangrijk vast te stellen dat de velden in het SAML scantoken een correcte waarde hebben en geldig ondertekend zijn. Wanneer dit niet zou gebeuren, kan een kwaadwillende met een gestolen token nog steeds gegevens opvragen van bv. ieder willekeurig burgerservicenummer.

#### Controles op het scantoken

Het SAML scantoken wordt door de ontvanger uit het betreffende attribuut van het inschrijftoken gehaald, Base64 gedecodeerd en vervolgens gevalideerd.

Bij de validatie van het SAML scantoken moet de ontvanger controleren of:

- De aanduiding voor de versie van SAML gedefinieerd is op "2.0", zie [Uniekheid](het-saml-scan-en-wid-token.md#uniekheid) ;

- De juiste organisatieID (URA) is opgenomen die deze assertion heeft gecreëerd en de gebruiker heeft geauthenticeerd, zie [Afzender](het-saml-scan-en-wid-token.md#afzender) .

- Het BSN uit het Subject zie [Onderwerp](het-saml-scan-en-wid-token.md#onderwerp) overeenkomt met het BSN uit het inschrijftoken;

- De Assertion correct is ondertekend door de Signature te valideren met het meegestuurde certificaat.

- Het gebruikte certificaat waarmee de ondertekening heeft plaatsgevonden geldig was ten tijde van de ondertekening.

- Indien het certificaat op de CRL is geplaatst, dan dient dit plaats te hebben gevonden nadat het token gegenereerd en ondertekend is.

- De relevante certificaatketen te valideren op geldigheid.

- De geldigheidsperiode van het token, zie [Geldigheid](het-saml-scan-en-wid-token.md#geldigheid) , niet langer is dan 10 jaar;

- Het bericht ontvangen is binnen de geldigheidsperiode van het token, zie [Geldigheid](het-saml-scan-en-wid-token.md#geldigheid) ;

- De afnemer van het SAML scantoken (audience) minimaal de ZIM is, zie [Ontvanger](het-saml-scan-en-wid-token.md#ontvanger) ;

- De zorgverlener/zorgmedewerker is geauthenticeerd via het voorgedefinieerde authenticatiemiddel, het X509 identiteitscertificaat, zoals beschreven in [Authenticatie](het-saml-scan-en-wid-token.md#authenticatie);

- Alleen die attributen zijn gedefinieerd, die zijn beschreven in [Attributen](het-saml-scan-en-wid-token.md#attributen) ;

Het scantoken mag meerdere malen gebruikt worden.

Het tokenID dient in de log van de ZIM opgenomen te worden.

#### Controles op het WID_token

Het SAML WID_token wordt door de ontvanger uit het betreffende attribuut van het scantoken gehaald, Base64 gedecodeerd en vervolgens gevalideerd.

Bij de validatie van het SAML WID_token moet de ontvanger controleren of:

- De aanduiding voor de versie van SAML gedefinieerd is op "2.0", zie [Uniekheid](het-saml-scan-en-wid-token.md#uniekheid) ;

- De juiste organisatieID (URA) is opgenomen die deze assertion heeft gecreëerd en de gebruiker heeft geauthenticeerd, zie [Afzender](het-saml-scan-en-wid-token.md#afzender) .

- Het BSN uit het Subject zie [Onderwerp](het-saml-scan-en-wid-token.md#onderwerp) overeenkomt met het BSN uit het scantoken;

- De Assertion correct is ondertekend door de Signature te valideren met het meegestuurde certificaat.

- Het gebruikte certificaat waarmee de ondertekening heeft plaatsgevonden geldig was ten tijde van de ondertekening.

- Indien het certificaat op de CRL is geplaatst, dan dient dit plaats te hebben gevonden nadat het token gegenereerd en ondertekend is.

- De relevante certificaatketen te valideren op geldigheid.

- De geldigheidsperiode van het token, zie [Geldigheid](het-saml-scan-en-wid-token.md#geldigheid) , niet langer is dan 10 jaar;

- Het bericht ontvangen is binnen de geldigheidsperiode van het token, zie [Geldigheid](het-saml-scan-en-wid-token.md#geldigheid) ;

- De afnemer van het SAML WID_token (audience) minimaal de ZIM is, zie [Ontvanger](het-saml-scan-en-wid-token.md#ontvanger) ;

- De waarde van @AuthnInstant binnen het AuthnStatement van het WID_token identiek is aan de waarde van @AuthnInstant binnen het AuthnStatement van het Scan_token

- Alleen die attributen zijn gedefinieerd, die zijn beschreven in [Attributen](het-saml-scan-en-wid-token.md#attributen) ;

#### Controles op de WID_raw_data

Vooralsnog hoeven de WID_raw_data niet gevalideerd te worden.

Als aan één van de bovenstaande condities niet is voldaan, moet het inschrijftoken door de ontvanger geweigerd worden en een SOAP foutmelding aan het verzendende systeem afgegeven worden, zie foutafhandeling in [IH tokens generiek].
