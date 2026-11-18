[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBZ AORTA_Auth_IH_Berichtauthenticatie_Transactietoken](../gbz-aorta_auth_ih_berichtauthenticatie_transactiet.md)

# Certificaten transactietoken

## Te gebruiken certificaat en attributen

De smartcard certificaat, gebaseerd op PKI, kent een aantal modellen:

**Tabel AORTA.STK.t3210 – UZI pastype**

| **Naam UZI-pastype/certificaat** ; | **Codering Pastype/certificaat** ; |
| --- | --- |
| **Zorgverlenerpas** ; | Z ; |
| **Medewerkerpas op naam** ; | N ; |
| **Medewerkerpas niet op naam** ; | M ; |
| **Servercertificaat** ; | S ; |

De smartcard of het certificaat die gebruikt wordt voor het ondertekenen van een transactietoken moet een zorgverlener pas, een medewerker pas op naam zijn of een servercertificaat. Hoewel het pastype gecodeerd is opgenomen in het authenticiteit certificaat (in het subjectAltName attribuut), dient een applicatie op basis van de uitgevende CA vast te stellen wat het pastype van de UZI-pas is.

Indien gebruik gemaakt wordt van een servercertificaat, dan geldt het volgende: een GBZ dient voor transportbeveiliging bij voorkeur een ander servercertificaat te gebruiken dan voor berichtauthenticatie. Dit is met name van toepassing wanneer ondertekening niet via een zelfde key-store verloopt dan dat van de TLS-verbinding. De verschillende certificaten horen daarbij in verschillende componenten ondergebracht te zijn in de architectuur van het XIS.

De signature wordt gezet met de sleutel voor authenticiteit (keyUsage=digitalSignature, hexadecimaal 0x80).

De attributen in het authenticiteit certificaat worden gegeven in de vorm van een Distinguished Name*(*DN), zie [IH tokens generiek].

De waarden van deze attributen voor de relevante UZI-certificaten zijn:

**Tabel AORTA.STK.t3220 – DN attributen van UZI-certificaten**

| **Attribuut** ; | **Omschrijving** ; | **Waarde** ; |
| --- | --- | --- |
| **CN** ; | Issuer.commonName ; | *Derde generatie:* UZI-register Zorgverlener CA G3 ; Voor mogelijke volgende generaties wordt verwezen naar het UZI-register: ;  [https://www.uziregister.nl/](https://www.uziregister.nl/) ; |
| **O** ; | Issuer.organisationName ; | agentschap Centraal Informatiepunt Beroepen Gezondheidszorg ; |
| **C** ; | Issuer.countryName ; | NL ; |

**Tabel AORTA.STK – DN attributen van ZORG-ID certificaten, gebaseerd op PKI**

| **Attribuut** ; | **Omschrijving** ; | **Waarde** ; |
| --- | --- | --- |
| **CN** ; | Issuer.commonName ; | ZORG-ID Token CA ; |
| **O** ; | Issuer.organisationName ; | ZORG-ID ; |
| **C** ; | Issuer.countryName ; | NL ; |
| **Extensions** ; | OID ; | 2.16.840.1.113883.2.4.3.111.20.5 ; |
| **proofValue** ; | Cryptografisch bewijs om herkomst van een credential te verifiëren ; | z58.......ktZ ; |

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | De issuer.commonName verschilt per 'generatie' UZI-passen. Het is mogelijk dat verschillende 'generatie' UZI-passen door elkaar worden gebruikt. Daarom dient de Issuer DN dynamisch afgeleid te worden uit het gebruikte authenticatiecertificaat. ; |
| --- | --- |

Om de digitale handtekening bij het LSP te verifiëren, moet de ontvanger over de bijbehorende publieke sleutel beschikken, zie [IH tokens generiek].

Voor verificatie is gekozen een verwijzing naar het authenticiteit certificaat mee te zenden; de ontvanger moet deze dan met bijvoorbeeld het LDAP protocol ophalen in de directory van het UZI-register of ZORG-ID.

Zie voor de verdere beschrijving van de passen [UZI pas].

Noot: uiteraard mogen in het testtraject alleen UZI-testpassen en UZI-testcertificaten gebruikt worden. Het gebruik hiervan wordt verder niet uitgewerkt in deze handleiding. De werking is identiek.
