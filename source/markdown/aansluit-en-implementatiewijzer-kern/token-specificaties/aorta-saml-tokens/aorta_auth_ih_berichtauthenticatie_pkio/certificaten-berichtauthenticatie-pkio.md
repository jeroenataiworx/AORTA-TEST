[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [AORTA_Auth_IH_Berichtauthenticatie_PKIO](../aorta_auth_ih_berichtauthenticatie_pkio.md)

# Certificaten Berichtauthenticatie PKIO

## Te gebruiken certificaat en attributen

Voor het tekenen van het SAML authenticatietoken worden persoonsgebonden authenticiteitcertificaten uit de PKIoverheid hiërarchie gebruikt. Dit certificaat bevat een RSA publieke sleutel. Met de privé sleutel wordt de digitale handtekening gegenereerd.

De attributen in het authenticiteitcertificaat worden gegeven in de vorm van een Distinguished Name (DN) en het serienummer, zie [IH tokens generiek].

**Tabel AORTA.STK.t3310 – Certificaat attributen**

| **Attribuut** ; | **Omschrijving** ; | **Waarde** ; |
| --- | --- | --- |
| **CN** ; | Subject.commonName ; | <Volledige naam van de persoon, zie [CP PKIO] deel 3a> ; |
| **OU** ; | Subject.organizationalUnitName ; | Klantenloket ; |
| **O** ; | Subject.organizationName ; | Vereniging van Zorgaanbieders voor Zorgcommunicatie ; |
| **C** ; | Subject.countryName ; | C=NL ;  <zie [CP PKIO] deel 3a> ; |
| **Serienummer** ; | SerialNumber. Wordt door de certificaatdienstverlener vastgelegd ; | <zie [CP PKIO] deel 3a> ; |

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | De issuer.commonName verschilt per ‘generatie’ PKIO-passen. ;  De root en de domeinen die het door NCSC als “goed” beoordeelde SHA algoritme gebruiken, worden aangemerkt als G2, waarbij G staat voor generatie. De Issuer DN kan alleen dynamisch afgeleid worden uit het gebruikte authenticatie certificaat. De verschillende generaties PKIO-passen kunnen bij een klantenloket naast elkaar gebruikt worden. ; |
| --- | --- |

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Het serialNumber van het authenticiteitscertificaat van de pas wordt gebruikt in combinatie met de attributen O en OU om een klantenloketmedewerker te identificeren. ; |
| --- | --- |

Om de digitale handtekening bij het LSP te verifiëren, moet de ontvanger over de bijbehorende publieke sleutel beschikken, zie [IH tokens generiek]. Voor verificatie is gekozen door het certificaat met de publieke sleutel mee te zenden in KeyInfo van het SAML authenticatietoken, zie ook [IH tokens generiek].

Noot: In samenspraak met Nictiz en andere betrokken partijen kan de keuze voor het meezenden van het certificaat nog heroverwogen worden.

Noot: In het testtraject worden ook PKIO-passen gebruikt.
