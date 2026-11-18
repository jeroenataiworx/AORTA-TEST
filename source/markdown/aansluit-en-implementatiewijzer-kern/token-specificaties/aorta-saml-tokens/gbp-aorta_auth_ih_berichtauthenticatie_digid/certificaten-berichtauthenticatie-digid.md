[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBP AORTA_Auth_IH_Berichtauthenticatie_DigiD](../gbp-aorta_auth_ih_berichtauthenticatie_digid.md)

# Certificaten berichtauthenticatie DigiD

## Te gebruiken certificaat en attributen

Voor het tekenen van het SAML authenticatietoken wordt het authenticiteitcertificaat van de identity provider DigiD gebruikt. Dit certificaat bevat een RSA publieke sleutel. Met de privé sleutel wordt de digitale handtekening gegenereerd.

De attributen in het authenticiteitcertificaat worden gegeven in de vorm van een Distinguished Name*(*DN) en het serienummer, zie [IH tokens generiek].

De volgende attribuutwaarden zijn voorbeelden en moeten in samenspraak met VZVZ en ander betrokken partijen (zoals de certificaatdienstverlener) nog bepaald en vastgelegd worden.

**Tabel AORTA.STK.t3410 – Certificaat attributen**

| **Attribuut** ; | **Omschrijving** ; | **Waarde** ; |
| --- | --- | --- |
| CN ; | Subject.commonName ; | as.digid.nl ; |
| OU ; | Subject.organizationalUnitName ; | Digid ; |
| O ; | Subject.organizationName ; | Stichting ICTU ; |
| C ; | Subject.countryName ; | NL ; |
| Serienummer ; | SerialNumber. Wordt door de certificaatdienstverlener vastgelegd ; | PK070001000868195 ; (voorbeeld) ; |

Om de digitale handtekening bij de ZIM te verifiëren, moet de ontvanger over de bijbehorende publieke sleutel beschikken, zie [IH tokens generiek]. Voor verificatie is gekozen door een verwijzing naar het authenticiteitcertificaat in het SAML authenticatietoken als KeyInfo mee te zenden; de ontvanger moet deze dan met bijvoorbeeld het LDAP protocol ophalen, zie ook [IH tokens generiek].

Noot: In samenspraak met VZVZ en andere betrokken partijen kan de keuze voor opnemen van een verwijzing naar het certificaat nog heroverwogen worden.
