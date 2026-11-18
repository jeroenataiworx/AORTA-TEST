[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBZ AORTA_Auth_IH_Inschrijftoken](../gbz-aorta_auth_ih_inschrijftoken.md)

# Token afhandeling inschrijftoken

## Verificatie van het bericht

Het is belangrijk vast te stellen dat de velden in het SAML inschrijftoken een correcte waarde hebben en geldig ondertekend zijn. Wanneer dit niet zou gebeuren, kan een kwaadwillende met een gestolen token nog steeds gegevens opvragen van bv. ieder willekeurig Burgerservicenummer.

De ontvanger controleert of de WS-Security SOAP Header voor hem bestemd is, zie soap attribuut actor.

Het SAML inschrijftoken wordt door de ontvanger uit de WS-Security SOAP Header gehaald indien de WS-Security SOAP Header voor de ontvanger bestemd is en dat de ontvanger deze moet verwerken. Bij gebruik van het SAML inschrijftoken moet de ontvanger controleren of:

- De aanduiding voor de versie van SAML gedefinieerd is op "2.0", zie [Uniekheid](het-saml-inschrijftoken.md#uniekheid) ;

- De juiste organisatieID is opgenomen die deze assertion heeft gecreëerd en de gebruiker heeft geauthentiseerd, zie [Afzender](het-saml-inschrijftoken.md#afzender). Het zorgaanbiederID in het token dient overeen te komen met de zorgaanbiederID in het bericht. Tevens dient de zorgaanbiederID overeen te komen met:De URA van het transactietokenDe URA uit het mandaattoken

- Het BSN uit het Subject zie [Onderwerp](het-saml-inschrijftoken.md#onderwerp) overeenkomt met het BSN uit het transactietoken en het BSN uit het HL7-bericht;

- De Assertion correct is ondertekend door de Signature te valideren met het gerefereerde certificaat.

- Het gebruikte certificaat waarmee de ondertekening heeft plaatsgevonden geldig was ten tijde van de ondertekening.

- Indien het certificaat op de CRL is geplaatst, dan dient dit plaats te hebben gevonden nadat het token gegenereerd en ondertekend is.

- De relevante certificaatketen te valideren op geldigheid.

- De geldigheidsperiode van het token, zie [Geldigheid](het-saml-inschrijftoken.md#geldigheid) , niet langer is dan 1,5 jaar;

- Het bericht ontvangen is binnen de geldigheidsperiode van het token, zie [Geldigheid](het-saml-inschrijftoken.md#geldigheid) ;

- De afnemer van het SAML inschrijftoken (audience) minimaal de ZIM is, zie [Ontvanger](het-saml-inschrijftoken.md#ontvanger) ;

- De zorgverlener/zorgmedewerker is geauthentiseerd via het voor gedefinieerde authenticatiemiddel, de SmartCardPKI, zoals beschreven in [Authenticatie](het-saml-inschrijftoken.md#authenticatie) ;

- Alleen die attributen zijn gedefinieerd, die zijn beschreven in [Attributen](het-saml-inschrijftoken.md#attributen) ;

- Indien het inschrijftoken ondertekend is met een UZI certificaat: de attribuutwaarde van Uitvoerder overeenkomt met het UZI-nummer van het gerefereerde certificaat, zie [Attributen](het-saml-inschrijftoken.md#attributen) ;

- Indien het inschrijftoken ondertekend is met het authenticiteit certificaat van ZORG-ID Mobile CA (CA) dienen de volgende extra controles plaats te vinden:Het attribuut Scantoken dient aanwezig te zijn met hierin het Base64 gecodeerde scantokenHet scantoken dient gedecodeerd en vervolgens gevalideerd te worden, zie [[Scantoken](https://vzvz.atlassian.net/wiki/x/v4ltN)].Het verleningstoken dient gedecodeerd en vervolgens gevalideerd te worden, indien het attribuut Verlengingstoken aanwezig is.Het subject uit het inschrijftoken (BSN) dient overeen te komen met de waarde van het subject uit het scantoken.De AuthnInstant uit het inschrijftoken (DatumTijd) dient overeen te komen met de waarde van het AuthnInstant attribuut uit het scantoken.De attribuutwaarde van Uitvoerder overeenkomt met de Common Name van het meegestuurde certificaat, zie [Attributen](het-saml-inschrijftoken.md#attributen)

- Indien het inschrijftoken ondertekend is met het authenticiteit certificaat van ZORG-ID Token CA (CA) dienen de volgende extra controles plaats te vinden:Van het gebruikte certificaat moet het extensie bewijs (proofValue) gecontroleerd worden dat dit met een geldige UZI-medewerkerspas op naam is gebeurd ten tijde van de ondertekening.De proofValue extensie heeft de volgende OID: 2.16.840.1.113883.2.4.3.111.20.5 (Custom Extension copied Certificate)De proofValue is een JSON Web Token dat uit drie delen bestaat: `header.payload.signature`Om het bewijs te controleren, moet uit het header element `x5c`, het X.509 certificaat geëxtraheerd worden, met Base64, waar vervolgens de publieke sleutel gehaald wordt.Gebruik de publieke sleutel om de JWT-handtekening te valideren met de algoritme die uit het header element `alg` is vastgelegd.Controleer of het geëxtraheerde certificaat ondertekend is door de vertrouwde CA (Certificate Authority)Decodeer de payload met Base64.Controleer de claims uit de payload, met die van het authenticiteit certificaat van ZORG-ID Token CA:"ura"""uziNumber""roleCode"

- Het inschrijftoken mag meerdere malen gebruikt worden.

- Het tokenID dient in de log van de ZIM opgenomen te worden.

- Als aan één van de bovenstaande condities niet is voldaan, moet het bericht door de ontvanger geweigerd worden en een SOAP foutmelding aan het verzendende systeem afgegeven worden, zie foutafhandeling in [IH tokens generiek].

- Als wel aan alle condities is voldaan, wordt het HL7v3 bericht verder verwerkt.
