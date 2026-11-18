[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [AORTA_Auth_IH_Berichtauthenticatie_UZI](../aorta_auth_ih_berichtauthenticatie_uzi.md)

# Certificaten Berichtauthenticatie UZI

## Te gebruiken certificaat en attributen

De UZI-pas kent een aantal modellen:

Tabel AORTA.STK.t3210 – UZI pastype

| **Naam UZI-pastype** ; | **Codering Pastype** ; |
| --- | --- |
| **Zorgverlenerpas** ; | Z ; |
| **Medewerkerpas op naam** ; | N ; |
| **Medewerkerpas niet op naam** ; | M ; |
| **Servercertificaat** ; | S ; |

De pas die gebruikt wordt voor het ondertekenen van een authenticatietoken moet een zorgverlenerpas of een medewerkerpas op naam zijn. Hoewel het pastype gecodeerd is opgenomen in het authenticiteitcertificaat (in het subjectAltName attribuut), dient een applicatie op basis van de uitgevende CA vast te stellen wat het pastype van de UZI-pas is.

De signature wordt gezet met de sleutel voor authenticiteit (keyUsage=digitalSignature, hexadecimaal 0x80).

De attributen in het authenticiteitcertificaat worden gegeven in de vorm van een Distinguished Name*(*DN), zie [IH tokens generiek].

De waarden van deze attributen voor de relevante UZI-passen zijn:

Tabel AORTA.STK.t3220 – DN attributen van zorgverlenerspas

| **Attribuut** ; | **Omschrijving** ; | **Waarde** ; |
| --- | --- | --- |
| **CN** ; | Issuer.commonName ; | SHA-2 generatie (G21): ;  UZI-register Zorgverlener CA G21 ;  Generatie Public G3: ;  UZI-register Zorgverlener CA G3 ; |
| **O** ; | Issuer.organisationName ; | SHA-2 generatie (G21): ;  agentschap Centraal Informatiepunt Beroepen Gezondheidszorg ;  Public G3/Private G1 generatie: ;  CIBG ; |
| **C** ; | Issuer.countryName ; | NL ; |

Tabel AORTA.STK.t3230 – DN attributen van medewerkerpas op naam

| **Attribuut** ; | **Omschrijving** ; | **Waarde** ; |
| --- | --- | --- |
| **CN** ; | Issuer.commonName ; | SHA-2 generatie (G21): ;  UZI-register Medewerker op naam CA G21 ;  Generatie Public G3: ;  UZI-register Medewerker op naam CA G3 ; |
| **O** ; | Issuer.organisationName ; | SHA-2 generatie (G21): ;  agentschap Centraal Informatiepunt Beroepen Gezondheidszorg ;  Public G3/Private G1 generatie: ;  CIBG ; |
| **C** ; | Issuer.countryName ; | NL ; |

Om de digitale handtekening bij het LSP te verifiëren, moet de ontvanger over de bijbehorende publieke sleutel beschikken, zie [IH tokens generiek].

Voor verificatie is gekozen een verwijzing naar het certificaat mee te zenden; de ontvanger moet deze dan met bijvoorbeeld het LDAP protocol ophalen in de directory van het UZI-register.

Zie voor de verdere beschrijving van de passen [UZI pas].

Noot: uiteraard mogen in het testtraject alleen UZI-testpassen gebruikt worden. Het gebruik hiervan wordt verder niet uitgewerkt in deze handleiding. De werking is identiek.
