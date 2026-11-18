[AORTA 8.5.2](../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../token-specificaties.md) / [JSON Web tokens](../json-web-tokens.md)

# MedMij Access token

## Inhoud en formaat van het MedMij access_token

**AOF.TS.MAT.100.v1**

Het MedMij access_token is een JWT, die bestaat uit een header, een payload en een signature, waarbij gebruik wordt gemaakt van [JWS Compact Serialization](https://tools.ietf.org/html/rfc7515#section-3.1).

**AOF.TS.MAT.150.v1**

De header van het token bevat de volgende attributen:

| **Claim** ; | **Vaste waarde** ; | **Toelichting** ; |
| --- | --- | --- |
| alg ; | RS256 ; |  |
| typ ; | mat+JWT ; | "mat" is een afkorting voor MedMij access_token ; |
| kid ; | - ; | The identifier of the key-pair used to sign this JWT ; |

**AOF.TS.MAT.200.v1**

Het access_token wordt op basis van RS256 (RSA Signature met SHA-256), digitaal ondertekend met de private key van de Autorisatie Server. De signature wordt geplaatst over de header en de payload.

**AOF.TS.MAT.300.v1**

Het access_token bevat de volgende payload:

| **Claim** ; | **Vaste waarde** ; | **Toelichting** ; |
| --- | --- | --- |
| jti ; | - ; | Unieke ID van het token ; |
| ver ; | 1.0 ; | De versie van de tokendefinitie die wordt gehanteerd ; |
| iss ; | - ; | HTTPS-URL van de Autorisatie Server voor deze versie van het MedMij afsprakenstelsel (interfaceversie) ; |
| exp ; | - ; | Gelijk aan de waarde van *expires_in*in het *access token response* bericht ; |
| scope ; | - ; | Gelijk aan de *scope* in het *access token response* bericht. ;  Wanneer een access_token wordt gegenereerd t.b.v. een interne $is-allowed operation tussen Autorisatie Server en Resource Broker, dan wordt de scope gevuld met ;  $is-allowed/ ;  gevolgd door de *scope* in het *access token response* bericht ;  Bijvoorbeeld: "$is-allowed/eenofanderezorgaanbieder~42" ; |
