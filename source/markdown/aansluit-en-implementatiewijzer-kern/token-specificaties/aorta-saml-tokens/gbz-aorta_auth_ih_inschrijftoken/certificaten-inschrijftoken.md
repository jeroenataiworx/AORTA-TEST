[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBZ AORTA_Auth_IH_Inschrijftoken](../gbz-aorta_auth_ih_inschrijftoken.md)

# Certificaten Inschrijftoken

## Te gebruiken certificaat en attributen UZI

De UZI-pas kent een aantal modellen:

**Tabel AORTA.STK.t3210 – UZI pastype**

| **Naam UZI-pastype** ; | **Codering Pastype** ; |
| --- | --- |
| **Zorgverlenerpas** ; | Z ; |
| **Medewerkerpas op naam** ; | N ; |
| **Medewerkerpas niet op naam** ; | M ; |
| **Servercertificaat** ; | S ; |

De UZI-pas die gebruikt wordt voor het ondertekenen van een inschrijftoken moet een zorgverlener- of een medewerkerspas op naam zijn. Hoewel het pastype gecodeerd is opgenomen in het authenticiteit certificaat (in het subjectAltName attribuut), dient een applicatie op basis van de uitgevende CA vast te stellen wat het pastype van de UZI-pas is.

De signature wordt gezet met de sleutel voor authenticiteit (keyUsage=digitalSignature, hexadecimaal 0x80).

De attributen in het authenticiteit certificaat worden gegeven in de vorm van een Distinguished Name*(*DN), zie [IH tokens generiek].

De waarden van deze attributen voor de relevante UZI-passen zijn:

**Tabel AORTA.STK.t3220 – DN attributen van zorgverlenerspas**

| **Attribuut** ; | **Omschrijving** ; | **Waarde** ; |
| --- | --- | --- |
| **CN** ; | Issuer.commonName ; | *Derde generatie:* UZI-register Zorgverlener CA G3 ; Voor mogelijke volgende generaties wordt verwezen naar het UZI-register: ;  [https://www.uziregister.nl/](https://www.uziregister.nl/) ; |
| **O** ; | Issuer.organisationName ; | agentschap Centraal Informatiepunt Beroepen Gezondheidszorg ; |
| **C** ; | Issuer.countryName ; | NL ; |

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | De issuer.commonName verschilt per 'generatie' UZI-passen. Het is mogelijk dat verschillende 'generatie' UZI-passen door elkaar worden gebruikt. Daarom dient de Issuer DN dynamisch afgeleid te worden uit het gebruikte authenticatie certificaat. ; |
| --- | --- |

**Tabel AORTA.STK.t3230 – DN attributen van medewerkerpas op naam van de UZI-pas**

| **Attribuut** ; | **Omschrijving** ; | **Waarde** ; |
| --- | --- | --- |
| **CN** ; | Issuer.commonName ; | *Derde generatie:* UZI-register Medewerker op naam CA G3 ; Voor mogelijke volgende generaties wordt verwezen naar het UZI-register: ;  [https://www.uziregister.nl/](https://www.uziregister.nl/) ; |
| **O** ; | Issuer.organisationName ; | agentschap Centraal Informatiepunt Beroepen Gezondheidszorg ; |
| **C** ; | Issuer.countryName ; | NL ; |

**Tabel AORTA.STK – DN attributen van medewerkerpas op naam van de ZORG-ID Smartcard**

| **Attribuut** ; | **Omschrijving** ; | **Waarde** ; |
| --- | --- | --- |
| **CN** ; | Issuer.commonName ; | ZORG-ID Token CA ; |
| **O** ; | Issuer.organisationName ; | ZORG-ID ; |
| **C** ; | Issuer.countryName ; | NL ; |
| **Extensions** ; | OID ; | 2.16.840.1.113883.2.4.3.111.20.5 ; |
| **proofValue** ; | Cryptografisch bewijs om herkomst van een credential te verifiëren ; | z58.......ktZ ; |

Om de digitale handtekening bij het LSP te verifiëren, moet de ontvanger over de bijbehorende publieke sleutel beschikken, zie [IH tokens generiek].

Voor verificatie is gekozen een verwijzing naar het authenticiteit certificaat mee te zenden; de ontvanger moet deze dan met bijvoorbeeld het LDAP protocol ophalen in de directory van het UZI-register of ZORG-ID.

Zie voor de verdere beschrijving van de passen [UZI pas].

Noot: uiteraard mogen in het testtraject alleen UZI-testpassen gebruikt worden. Het gebruik hiervan wordt verder niet uitgewerkt in deze handleiding. De werking is identiek.

### Te gebruiken authenticiteit certificaat en attributen

ZORG-ID geeft unieke authenticiteit certificaten uit, gebaseerd op X.509, aan medewerkers. De waarden van de properties voor deze authenticiteit certificaten zijn:

**Tabel ZORG-ID – properties van de authenticiteit certificaat**

| **Property** ; | **Omschrijving** ; | **Waarde** ; |
| --- | --- | --- |
| **Name** ; | Authenticiteit certificaat van een medewerker ; | Person certificate ; |
| **Subject DN** ; | Onderwerp aan wie dit authenticiteit certificaat is uitgegeven. Volgende velden zijn gebruikt: ;  Common Name (CN) ;  Country C ; | CN=Voornaam Achternaam:ZIDnummer ;  C=NL ; |
| **Issuer DN** ; | Uitgever van het authenticiteit certificaat. Volgende velden zijn gebruikt: ;  - CommonName (CN) ;  - Organisatie (O) ;  - Country (C) ; | CN=ZORG-ID Person CA ;  O=ZORG-ID ;  C=NL ; |

De CommonName van het Subject DN wordt ingevuld als AttributeValue bij het attribuut “Uitvoerder” in het inschrijftoken als dit door ZORG-ID wordt aangemaakt of wordt verlengd.

Zie voor de verdere beschrijving [UZI pas](https://vzvz.atlassian.net/wiki/pages/createpage.action?spaceKey=A8&title=UZI%20pas)
