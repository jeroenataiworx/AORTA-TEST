[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBZ AORTA_Auth_IH_Inschrijftoken](../gbz-aorta_auth_ih_inschrijftoken.md)

# Het SAML inschrijftoken

In de zorgsector is veilige en betrouwbare identificatie van patiënten essentieel voor correcte gegevensuitwisseling en toegangscontrole. Een **SAML inschrijftoken** speelt hierin een cruciale rol. Het dient als een cryptografisch ondertekend bewijs dat een patiënt is geïdentificeerd en ingeschreven bij een zorgaanbieder.

Het SAML inschrijftoken is gebaseerd op een **XML-gebaseerde SAML assertion** (Security Assertion Markup Language). Deze assertion bevat een verklaring over de identificatie van de patiënt en wordt gebruikt om deze bewering op een veilige en gestandaardiseerde manier over te brengen tussen zorgsystemen. Hierdoor kunnen partijen binnen het zorgnetwerk de inschrijving van een patiënt verifiëren zonder directe heridentificatie.

Het SAML token wordt gegenereerd door een zorgverlener of zorgmedewerker en ondertekend met een **geldig authenticiteitscertificaat** dat zich bevindt op een **authenticatiemiddel** zoals een **UZI-pas**, **ZORG-ID Smartcard** of **ZORG-ID Mobiel**. Dit certificaat garandeert de herkomst en betrouwbaarheid van het token, waardoor zorgsystemen kunnen controleren dat de patiënt correct is ingeschreven.

Een Inschrijftoken is maximaal **1,5 jaar (18 maanden)** geldig. Na deze periode kan het worden vernieuwd zonder dat de patiënt opnieuw fysiek hoeft te worden geïdentificeerd. Dit verlengingsproces maakt gebruik van het oorspronkelijke token of een eerder uitgevoerde **WID-scan** (Wet op de Identificatieplicht), wat de administratieve lasten voor zowel zorgverleners als patiënten verlaagt.

Door het gebruik van SAML inschrijftokens en de onderliggende **SAML assertions** wordt de uitwisseling van medische gegevens veiliger en efficiënter, met een solide balans tussen toegankelijkheid en privacybescherming binnen het zorgdomein.

In dit hoofdstuk wordt de inhoud van het SAML inschrijftoken besproken. Het SAML inschrijftoken bevat de, binnen een zorgorganisatie, gevalideerde BSN en is ondertekend door een zorgverlener of medewerker. Alle XML voorbeelden in het document dienen door de betrokken partijen tijdens het bouwen van de uitwisseling getest, en waar nodig, in samenspraak met VZVZ aangepast te worden voor een juiste optimale werking.

## Structuur

Het SAML inschrijftoken is een afgegeven SAML assertion met betrekking tot de gevalideerde BSN die gebruikt wordt bij berichtauthenticatie voor het landelijk EPD. Het SAML inschrijftoken is ondertekend met behulp van een smartcard (UZI-pas of ZORG-ID Smartcard) van een zorgverlener of medewerker of m.b.v. het authenticiteit certificaat van de medewerker op naam die uitgegeven is door ZORG-ID. Er wordt gebruik gemaakt van SAML v2.0 [SAML Core].

Het UZI-register en ZORG-ID hebben als doel zorgaanbieders bij elektronische communicatie en toegang tot gegevens uniek te identificeren. Zowel het UZI-register als ZORG-ID koppelt hiertoe op unieke wijze de fysieke identiteit aan een elektronische identiteit en legt deze vast in authenticiteit certificaten. Deze certificaten en de hierbij behorende cryptografische sleutels worden vastgelegd op de smartcard. Bij het UZI-register heet dit de 'UZI-pas' en bij ZORG-ID heeft dit de 'ZORG-ID Smartcard'.

### Het gebruik van OID in SAML-assertions.

Een **OID** (Object Identifier) is een unieke identificatie die wordt gebruikt om objecten of entiteiten te identificeren binnen verschillende technische systemen, met name in de wereld van cryptografie, certificaatbeheer, netwerken en softwareontwikkeling. OID's worden vaak gebruikt om standaardconfiguraties, waarden, of zelfs certificaatattributen te identificeren, zoals algoritmen, protocollen en sleutelomgevingen.

Een OID bestaat uit een reeks niet-negatieve gehele getallen, gescheiden door punten (bijv. **2.16.840.1.113883.2.4.3.111**VZVZ service centrum). Volgens de ITU-T X.690-standaard (die ASN.1 BER/DER-codering definieert) en ISO/IEC 9834-1:

Elk getal in de reeks moet zonder voorloopnullen worden weergegeven.  
Bijvoorbeeld, **2.16.84.01** is ongeldig, terwijl **2.16.840.1** correct is.  
Dit voorkomt ambiguïteit en zorgt voor een eenduidige representatie van OIDs in verschillende systemen.

OID’s die worden gebruikt in SAML-assertions moet in het volgende formaat worden opgenomen, ongeacht of het een HL7v3- of FHIR-client is:

- `"urn:IIroot:"<OID voor het betreffende ID-stelsel>":IIext:"<gehanteerde ID binnen dit stelsel>`, bijvoorbeeld `"urn:IIroot:"2.16.528.1.1007.3.3":IIext:"<URA>`

Belangrijk hierbij is dat de <URA> een unieke identificatiecode is voor zorgverleners en gekoppeld is aan het **UZI-register**.

**Obsolete OID formaat**

Het volgende OID formaat is **Obsolete**.

`"urn:oid:"<OID voor het betreffende ID-stelsel>"."<gehanteerde ID binnen dit stelsel>`

`bijvoorbeeld`

`"urn:2.16.528.1.1007.3.3."<URA>`

## Assertion

De assertion heeft de volgende structuur (de waarden die in het token gebruikt worden zijn fictief):

| **Element/@Attribute** ; | **0..1** ; | **Omschrijving** ; |
| --- | --- | --- |
| @ID ; | 1 ; | Unieke identificatie van de Assertion ; |
| @Version ; | 1 ; | Versie van het SAML Protocol. Vaste waarde moet zijn 2.0 ; |
| @IssueInstant ; | 1 ; | Tijdstip van uitgifte van de Assertion. ; |
| Issuer ; | 1 ; | De URA van de zorgaanbieder organisatie waarbinnen de face to face controle heeft plaatsgevonden of waar het inschrijftoken wordt verlengd of waar het WID is ingescand in combinatie met een F2F controle. ; |
| @NameQualifier ; | 0 ; | Niet gebruiken ; |
| @SPNameQualifier ; | 0 ; | Niet gebruiken ; |
| @Format ; | 1 ; | Format="urn:oasis:names:tc:SAML:2.0:nameid-format:entity" ; |
| @SPProviderID ; | 0 ; | Niet gebruiken ; |
| Signature ; | 1 ; | Bevat de handtekening over de assertion zoals gezet met behulp van de smartcard van de zorgverlener (Z) of de smartcard van de medewerker op naam(N). De handtekening dient geplaatst te zijn met behulp van het authenticatie certificaat op de smartcard. ;  De handtekening kan ook gezet zijn met het authenticiteit certificaat van de medewerker die uitgegeven is door ZORG-ID. Bij verlenging van het inschrijftoken wordt alleen gebruik gemaakt van het authenticiteit certificaat van de medewerker op naam die uitgegeven is door ZORG-ID. ; |
| Subject ; | 1 ; | BSN van de patiënt waarvan de BSN gevalideerd is. ; |
| BaseID ; | 0 ; | Niet gebruiken ; |
| NameID ; | 1 ; | Bevat de gevalideerde BSN. ; |
| EncryptedID ; | 0 ; | Niet gebruiken ; |
| SubjectConfirmation ; | 1 ; | Moet aanwezig zijn. ; |
| @Method ; | 1 ; | 'urn:oasis:names:tc:SAML:2.0:cm:sender-vouches' ; |
| SubjectConfirmationData ; | 1 ; | Bevat Keyinfo ; |
| @Recipient ; | 0 ; | Niet gebruiken ; |
| @NotOnOrAfter ; | 0 ; | Niet gebruiken ; |
| @InResponseTo ; | 0 ; | Niet gebruiken ; |
| @NotBefore ; | 0 ; | Niet gebruiken ; |
| @Address ; | 0 ; | Niet gebruiken ; |
| KeyInfo ; | 1 ; | Bevat de X509 Issuer.serial van de medewerkerspas of zorgverlener smartcard of het publieke deel van het door ZORG-ID aangemaakte authenticiteit certificaat. ; |
| Conditions ; | 1 ; | Moet aanwezig zijn. ; |
| @NotBefore ; | 1 ; | Moet aanwezig zijn. ; |
| @NotOnOrAfter ; | 1 ; | Moet aanwezig zijn. Mag maximaal 1,5 jaar (18 maanden) na @NotBefore liggen. ; |
| Condition ; | 0 ; | Niet gebruiken ; |
| AudienceRestriction ; | 1 ; | Moet aanwezig zijn ; |
| Audience ; | 1..* ; | Bij AORTA/LSP en AoF: ;  `urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:1`(1 is de applicatie-id van de ZIM) ;  Bij MITZ ;  `"urn:oid:2.16.840.1.113883.2.4.3.111.2.1"`(is MITZ) ;  **WIJZIGINGSVOORSTEL**: ;  De verschillende Audience samenvoegen en er ;  `<saml:Audience>urn:generic:audience</saml:Audience>` ;  van maken. ; |
| ProxyRestriction ; | 0 ; | Niet gebruiken ; |
| Advice ; | 0 ; | Niet gebruiken ; |
| AuthnStatement ; | 1 ; | Moet aanwezig zijn ; |
| @AuthnInstant ; | 1 ; | Tijdstip van BSN validatie bij een nieuw inschrijftoken. Dit mag t.b.v. het werkproces ook de 'timestamp' zijn van het moment van aanmaken van het inschrijftoken of het tijdstip van inscannen van het WID. Bij een verlenging van een inschrijftoken wordt het originele tijdstip van BSN validatie overgenomen uit de oorspronkelijke inschrijftoken. ; |
| @SessionIndex ; | 0 ; | Niet gebruiken ; |
| AuthnContext ; | 1 ; | Moet aanwezig zijn ; |
| AuthnContextClassRef ; | 1 ; | urn:oasis:names:tc:SAML:2.0:ac:classes:SmartcardPKI of ;  urn:oasis:names:tc:SAML:2.0:ac:classes:X509 (Deze is ondertekend via ZORG-ID Mobiel) ; |
| AttributeStatement ; | 1 ; | Moet aanwezig zijn ; |
| Attribute ; | 1 ; | Moet aanwezig zijn. ; |
| @Name ; | 1 ; | Vaste waarde: "Uitvoerder" ; |
| AttributeValue ; | 1 ; | De smartcard van de zorgverlener of medewerker die het token heeft ondertekend of de Common Name van het meegestuurd authenticiteit certificaat van ZORG-ID indien het scantoken gegenereerd is door ZORG-ID. ; |
| Attribute ; | 0..1 ; | Alleen aanwezig indien het een nieuw inschrijftoken op basis van een ingescand WID betreft. ; |
| @Name ; | 0..1 ; | Vaste waarde “Scantoken” ; |
| AttributeValue ; | 0..1 ; | Het scantoken Base64 gecodeerd. Voor het Scantoken zie AORTA_Auth_IH_Scantoken ; |
| Attribute ; | 0..1 ; | Alleen aanwezig indien het een inschrijftoken wordt *verlengd op basis van een origineel inschrijftoken* aangemaakt op basis van een smartcard van een zorgverlener of medewerker of op basis van een eerdere scantoken op basis van het authenticiteit certificaat van de uitvoerende medewerker uit ZORG-ID. ; |
| @Name ; | 0..1 ; | Vaste waarde “Verlengingstoken” ; |
| AttributeValue ; | 0..1 ; | Het originele inschrijftoken ondertekend op basis van een smartcard of het eerdere WID-scantoken op basis van het authenticiteit certificaat van de uitvoerende zorgverlener/medewerker uit ZORG-ID dat verlengd gaat worden, wordt Base64 gecodeerd. Als er al een origineel inschrijftoken in het "Verlengingstoken" aanwezig is en het inschrijftoken opnieuw verlengd moet worden, dan wordt het bestaande "Verlengingstoken" uit het inschrijftoken hergebruikt voor het nieuwe inschrijftoken. ; |

N.B.: bovenstaande tabel bevat de meest gebruikte elementen van SAML assertions en is derhalve niet volledig. Voor niet genoemde elementen geldt: Niet gebruiken.

## Namespaces

Het SAML inschrijftoken die gebruikt wordt bij berichtauthenticatie maakt gebruik van de volgende namespaces. De prefixen zijn *niet normatief* maar worden in dit document als voorbeelden gebruikt.   
**Tabel AORTA.STK.t3300 – Namespaces**

| **Prefix** ; | **Namespace URI** ; |
| --- | --- |
| ds ; | http://www.w3.org/2000/09/xmldsig# ; |
| saml ; | urn:oasis:names:tc:SAML:2.0:assertion ; |
| wss ; | http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd ; |

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Bij het gebruik van de namespace-prefixes is het van belang deze na het ondertekenen niet meer te veranderen, dit maakt de digitale handtekening ongeldig. ; |
| --- | --- |

## Inhoud

De volgende paragrafen beschrijven de verschillende kenmerken en beveiligingsgerelateerde gegevens die het SAML inschrijftoken onderscheiden, zoals in [IH tokens generiek] beschreven is.

```
<saml:Assertion ... xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">
```

Het SAML inschrijftoken begint met het Assertion element en een verwijzing naar de XML SAML namespace voor SAML 2.0 assertions. De attributen behorende bij het Assertion element wordt in [paragraaf 2.4.1](het-saml-inschrijftoken.md#uniekheid) Uniekheid beschreven.

### Uniekheid

```
ID="token_dd1c1f96-f0b0-4026-a978-4d724c0a0a4f"
IssueInstant="2009-06-24T11:47:34Z"
Version="2.0">
```

De volgende attributen van het SAML assertion element maken van de SAML assertion een uniek gegeven, uitgegeven door de verzender van het bericht. Het attribuut ID identificeert op een unieke wijze de assertion. De waarde moet *mondiaal uniek* zijn voor AORTA berichten, zodat bij samenvoegen van meerdere XML bestanden (in een HL7v3 batch of anderszins) de waarde uniek blijft.

Het wordt aanbevolen een UUID (Universally Unique Identifier) te gebruiken. Bij het gebruik van andere vormen is er een kans, hoe klein ook, dat een ID samenvalt met een ID gemaakt volgens een andere methode van een andere leverancier).

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Een ID in XML mag niet met een cijfer beginnen. Bij het gebruik van een UUID is het dus aan te raden een prefix te gebruiken, welke met een letter of underscore ('_') begint. ; |
| --- | --- |

Het attribuut IssueInstant is een tijdsmoment van uitgifte van de SAML assertion. De tijdswaarde is gecodeerd in UTC. Het attribuut Version is de gebruikte SAML versie van de SAML assertion. De aanduiding voor de versie van SAML gedefinieerd in deze specificatie is "2.0".

### Afzender

```
<saml:Issuer>
    <!-- De Issuer verwijst naar de organisatie waarbinnen de BSN validatie heeft plaats gevonden.-->
    urn:IIroot:2.16.528.1.1007.3.3:IIext:12345678
</saml:Issuer>
```

De URA wordt uitgedrukt met behulp van een URN (Uniform Resource Name). De URN is opgebouwd uit:

"urn:IIroot:"<OID voor UZI organisatieIds>":IIext:"<URA>

De URN string is opgebouwd uit een IIroot en een IIext. "II" staat voor het HL7v3 datatype Instance Indentifier. Om de namespace in URN uniek te krijgen is II als prefix voor de root en ext geplaatst.   
URA's worden uitgedrukt als een id onder het identificatiesysteem "2.16.528.1.1007.3.3". De URA wordt toegekend door het UZI-register. Stel dat de URA de waarde "12345678" heeft, dan ziet de URN er als volgt uit:   
 urn:IIroot:**2.16.528.1.1007.3.3**:IIext:**12345678**

### Onderwerp

```
<saml:Subject>
    <saml:NameID>
    950052413
   </saml:NameID>
    <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:sender-vouches ">
    </saml:SubjectConfirmation>
</saml:Subject>
```

De Subject verwijst naar de door de zorgverlener/medewerker gevalideerde BSN. De BSN validatie dient plaatsgevonden te hebben

1) Aan de balie door:

- Een face to face controle van de patient en diens Wettelijk Identiteits Document (WID)

- Een controle van de geldigheid van het WID bij SBV-Z

- Een controle van de correctheid van het BSN bij SBV-Z

2) Door inlezen van de chip uit het WID waarbij:

- De echtheid van het WID wordt gecontroleerd

- De BSN wordt uitgelezen uit de chip of, bij paspoorten uitgegeven na 1 augustus 2021, de BSN QR code wordt gelezen.

3) Het subject en de daarbij behorende BSN overnemen uit het oorspronkelijke inschrijftoken dat verlengd gaat worden.

Vervolgens moet de SubjectConfirmation nog toegevoegd worden:

```
<saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:sender-vouches ">
</saml:SubjectConfirmation>
```

### Geldigheid

```
<saml:Conditions
    NotBefore="2009-06-24T11:47:34Z"
    NotOnOrAfter="2010-12-24T11:47:34Z">
```

Het attribuut *NotBefore* is de tijd waarop de SAML assertion geldig wordt. NotBefore moet altijd op of na de aanvang van de geldigheidsdatum van het certificaat (waarmee het inschrijftoken is getekend) liggen.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Wordt een bericht met een inschrijftoken ontvangen voor *NotBefore* is aangevangen, dan **moet** dit bericht geweigerd worden. ; |
| --- | --- |

Het attribuut *NotOnOrAfter* is de tijd waarop de SAML assertion vervalt. *NotOnOrAfter* mag na het verstrijken van de geldigheid van het authenticiteit certificaat (waarmee het inschrijftoken is getekend) liggen.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Wordt een bericht met een inschrijftoken ontvangen op of nadat *NotOnOrAfter* is verstreken, dan **moet** dit bericht geweigerd worden. ; |
| --- | --- |

Deze tijd is als bovenstaande tijd geformatteerd. Het maximaal toegestane verschil tussen *NotBefore* en *NotOnOrAfter* is anderhalf jaar.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | De geldigheidsduur van een inschrijftoken (*NotOnOrAfter* minus *NotBefore*) kan langer zijn dan de geldigheidsduur van het authenticiteit certificaat waarmee het token wordt getekend. ; |
| --- | --- |

Indien het authenticiteit certificaat waarmee het inschrijftoken is getekend op de CRL is geplaatst, dan dient het inschrijftoken niet geweigerd te worden door het LSP. Het is op de CRL niet inzichtelijk om welke reden een authenticiteit certificaat op de CRL is geplaatst. Dit kunnen uiteenlopende redenen zijn zoals een verloren pas of een intrekking van een BIG-registratie. Om het zorgproces niet te frustreren wordt deze controle procesmatig opgepakt door Security Management.

Echter, bij het ondertekenen van het inschrijftoken moet er een geldig authenticiteit certificaat gebruikt worden. Indien bij ondertekening van het inschrijftoken het authenticiteit certificaat al op de CRL is geplaatst, dan dient het inschrijftoken wel geweigerd te worden.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Indien het authenticiteit certificaat vóór ondertekening van het inschrijftoken op de CRL is geplaatst, dan dient het inschrijftoken geweigerd te worden door het LSP. ; |
| --- | --- |

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Indien het authenticiteit certificaat na ondertekening van het inschrijftoken op de CRL is geplaatst, dan dient het inschrijftoken niet geweigerd te worden. ; |
| --- | --- |

Het inperken van bepaalde partijen (AudienceRestriction) waarvoor de assertion bedoeld is wordt beschreven in [paragraaf 2.4.5](het-saml-inschrijftoken.md#ontvanger) Ontvanger.

### Ontvanger

```
<saml:AudienceRestriction>
    <!-- Root en extensie van de ZIM -->
    <saml:Audience>urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:1</saml:Audience>
</saml:AudienceRestriction>
```

In de AudienceRestriction wordt beschreven aan wie de SAML assertion is gericht. In ieder geval dient de ZIM als audience voor te komen (IIext:1). Meerdere Audience elementen is toegestaan.

Voor de <Audience> parameter is gekozen voor URN. De URN string is opgebouwd uit een IIroot en een IIext. "II" staat voor het HL7v3 datatype Instance Indentifier. Om de namespace in URN uniek te krijgen is II als prefix voor de root en ext geplaatst.

AORTA Applicatie-id's worden uitgedrukt als een id onder het identificatiesysteem "2.16.840.1.113883.2.4.6.6". Het correcte applicatie-id voor de GBZ-applicatie wordt toegekend bij aansluiting op de AORTA. Stel dat dit "300" zou zijn, dan ziet de URN er als volgt uit:   
 urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:300

### Authenticatie

Een authenticatiemiddel wordt gedefinieerd als een middel waarmee de identiteit van een gebruiker wordt geverifieerd voordat toegang tot een systeem of dienst wordt verleend. Bijvoorbeeld een smartcard koppelt een fysieke identiteit (zorgverlener of medewerker) aan een elektronische identiteit.

```
<saml:AuthnStatement

   AuthnInstant="2009-06-24T11:47:34"

   SessionIndex="token_2.16.528.1.1007.3.3.1234567.1_0123456789">
```

Het subject, de gevalideerde BSN, in de SAML assertion is geauthentiseerd door middel van een authenticatiemiddel van de uitvoerende zorgverlener/medewerker.

Als de zorgverlener/medewerker de smartcard (UZI-pas f ZORG-ID Smartcard) heeft gebruikt als authenticatiemiddel wordt de AuthContextClassRef SmartcardPKI:

```
<saml:AuthnContext>

    <saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:SmartcardPKI</saml:AuthnContextClassRef>

</saml:AuthnContext>
```

Als de zorgverlener/medewerker ZORG-ID Mobiel als authenticatiemiddel heeft gebruikt wordt de AuthContextClassRef X509:

```
<saml:AuthnContext>

    <saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:X509</saml:AuthnContextClassRef>

</saml:AuthnContext>
```

Binnen de gebruikte applicatie beveiligingsstandaarden is er sprake van verschillende vertrouwensniveaus.

Binnen de SAML-specificatie geeft men een authenticatie-context (*AuthnContext*) mee die de context van het gebruikte authenticatiemiddel aangeeft. Hiervoor zijn een aantal contexten gespecificeerd, zie [SAMLAuthnContext], die gebruikt worden als referentiekader voor de communicatie tussen de ZIM en andere componenten zoals GBZ applicaties.

Uitgaande van de beveiligingsniveaus van GBZ, zorgverlener/medewerker en smartcard wordt het "*urn:oasis:names:tc:SAML:2.0:ac:classes:SmartcardPKI*" of "*urn:oasis:names:tc:SAML:2.0:ac:classes:X509*" beveiligingsniveau gehanteerd om het AORTA vertrouwensniveau midden voor zorgverleners weer te geven.

```
</saml:AuthnStatement>
```

Afsluiting authentication statement.

### Attributen

```
<saml:AttributeStatement>
```

De volgorde van de attributen in het AttributeStatement is niet relevant. Er mogen geen andere attributen opgenomen worden in het AttributeStatement dan hier beschreven is.

**Uitvoerder**

```
<saml:Attribute Name="Uitvoerder">
   <saml:AttributeValue>123456789</saml:AttributeValue>
</saml:Attribute>
```

Het attribuut Uitvoerder bevat het UZI-nummer van de zorgverlener en medewerker op naam die de BSN validatie heeft uitgevoerd en het token heeft ondertekend. Indien deze nog niet bekend is bij het aanmaken van het inschrijftoken, dan kan dit veld leeg gelaten worden. Vanuit het authenticiteit certificaat waarmee het token is ondertekend, kan dan worden afgeleid wat het UZI-nummer van de ondertekenaar was. Voor de zorgverlener en de medewerker op naam is het UZI-nummer uniek gekoppeld aan de natuurlijk persoon.

Indien het scantoken is gegenereerd door Zorg-ID, dan kan dit attribuut ook de Common Name (CN) van het authenticiteit certificaat waarmee het token is ondertekend bevatten.

Bijvoorbeeld:

```
 <saml:AttributeValue>Jan Test:91000001</saml:AttributeValue>
```

In dit voorbeeld zijn de volgende waarden te vinden:

Jan Test: Voornaam Achternaam

91000001: Uniek nummer`. Start van 91000000 en hoger.

**Scantoken**

```
<saml:Attribute Name="Scantoken">

   <saml:AttributeValue xsi:type="base64Binary">

    Hier het scantoken base64 gecodeerd.

   </saml:AttributeValue>

</saml:Attribute>
```

Het attribuut Scantoken bevat het Scantoken Base64 gecodeerd. Voor de opbouw van het Scantoken wordt verwezen naar [AORTA_Auth_IH_Scantoken]. Dit attribuut dient alleen aanwezig (en gevuld) te zijn als het gehele inschrijftoken ondertekend is met het identiteitscertificaat van ZORG-ID.

**Verlengingstoken**

```
<saml:Attribute Name="Verlengingstoken">

   <saml:AttributeValue xsi:type="base64Binary">

    Hier het originele inschrijftoken base64 gecodeerd.

   </saml:AttributeValue>

</saml:Attribute>
```

Het attribuut Verlengingstoken bevat het originele Inschrijftoken o.b.v. de smartcard of het scantoken op basis van het authenticiteit certificaat van de uitvoerende medewerker uit ZORG-ID, Base64 gecodeerd. Voor de opbouw van het scantoken wordt verwezen naar [AORTA_Auth_IH_Scantoken]. Het attribuut Verleningstoken dient alleen aanwezig (en gevuld) te zijn als het gehele inschrijftoken ondertekend is met het authenticiteit certificaat van ZORG-ID.

Tenslotte wordt het attributen statement blok afgesloten met

```
</saml:AttributeStatement>
```

## Algoritmes

Om de integriteit en onweerlegbaarheid van het SAML inschrijftoken te waarborgen wordt een XML Signature geplaatst, zoals beschreven in [IH tokens generiek]. Na plaatsen van de XML Signature kan de ontvanger, met gebruikmaking van het persoonsgebonden authenticiteit certificaat van de verzender en de CA certificaten zoals verstrekt door het UZI-register of ZORG-ID, onomstotelijk vaststellen dat het SAML inschrijftoken ondertekend is met de privé sleutel behorend bij het gebruikte certificaat van de zorgmedewerker.

De XML Signature van het SAML inschrijftoken die gebruikt wordt bij berichtauthenticatie met behulp van de smartcard maakt gebruik van de volgende algoritmes, zoals beschreven in [IH tokens generiek]:

- Voor het berekenen van de hashwaarde wordt SHA-256 gebruikt.

- Voor de digitale handtekening in AORTA wordt gebruik gemaakt van een RSA handtekening over een SHA-256 digest.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Omdat de XML Signature onderdeel is van het SAML inschrijftoken en in het SAML inschrijftoken geplaatst wordt, moet er een "enveloped-signature" transformatie uitgevoerd worden die de Signature tags uit het SAML inschrijftoken verwijderd gevolgd door een “exc-c14n transformatie” (zie ook [SAML Core] §5.4.3 en §5.4.4). ; |
| --- | --- |

## Opbouw

### De headers

Eerst wordt het SAML inschrijftoken – het <saml:Assertion ...> element aangemaakt en gevuld met die elementen, zoals beschreven in [paragraaf 2.4](het-saml-inschrijftoken.md#inhoud) Inhoud.

```
<saml:Assertion

   ID="token_2.16.528.1.1007.3.3.1234567.1_0123456789"

   IssueInstant="2009-06-24T11:47:34Z"

   Version="2.0"

   xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">

 ... Zie paragraaf 2.4 Inhoud ...

</saml:Assertion>
```

Het XML Signature blok is onderdeel van het SAML inschrijftoken. Het XML Signature blok komt na het <saml:Issuer> element. Na de Signature volgt de rest van de inhoud van de assertion.

```
<saml:Assertion

   ID="token_2.16.528.1.1007.3.3.1234567.1_0123456789"

   IssueInstant="2009-06-24T11:47:34Z"

   Version="2.0"

   xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">

  <saml:Issuer Format="urn:oasis:names:tc:SAML:2.0:nameid-format:entity">

   urn:IIroot:?:IIext:?

  </saml:Issuer>

  <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">

    <ds:SignedInfo>

    ...

    </ds:SignedInfo>

    <ds:SignatureValue>Wuwn...5e4=</ds:SignatureValue>

    <ds:KeyInfo>

      <wss:SecurityTokenReference>

        <ds:X509Data>

        ...

        </ds:X509Data>

      <wss:SecurityTokenReference>

    </ds:KeyInfo>

  </ds:Signature>  ...

  ... Zie paragraaf 2.3 Inhoud ...

</saml:Assertion>
```

Indien de Signature aangemaakt wordt moet niet meer met de strings (saml:Assertion en SignedInfo) gemanipuleerd worden, maar ze moeten octet-voor-octet overgenomen worden in het bericht. Strikt genomen is het toegestaan wijzigingen aan te brengen die door canonicalisatie bij de ontvanger weer opgeheven worden, maar wanneer de digitale handtekening door middel van strings wordt opgebouwd, is het een foutgevoelige handeling.

Lange Base 64 waarden zijn afgekort. Wederom kan dit als strings worden behandeld, waarbij drie waarden vervangen moeten worden.

Deze drie waarden worden ingevuld:

- Neem het SignedInfo blok op.

- Neem de SignatureValue op.

- Neem certificaatgegevens in het KeyInfo blok op, in de vorm van een verwijzing (X509IssuerSerial).

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Wanneer een bericht een SAML assertion bevat, moet dat bericht precies één bijbehorende digitale handtekening bevatten. ; |
| --- | --- |

Het maken van de XML Signature uit strings levert de SAML assertion op met daarin de Signature.

### Plaats van het SAML token en de digitale handtekening

Het SAML inschrijftoken met daarin de digitale handtekening wordt in het WS-Security SOAP Header gezet. Op het <wss:Security> element **moet** een soap:mustUnderstand="1" vlag opgenomen worden, die aangeeft dat de ontvanger dit security element **moet** verwerken en een soap:actor="[http://www.aortarelease.nl/actor/zim](http://www.aortarelease.nl/actor/zim)" die aangeeft dat de ZIM dit security element verwerkt.

```
<soap:Header xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

  ...

  <wss:Security xmlns:wss=

    "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"

    soap:actor="http://www.aortarelease.nl/actor/zim" soap:mustUnderstand="1">

       <saml:Assertion ... >

       <saml:Issuer>...</saml:Issuer>

       <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">

        <ds:SignedInfo>

        ...

        </ds:SignedInfo>

        <ds:SignatureValue>Wuwn...5e4=</ds:SignatureValue>

        <ds:KeyInfo>

          <ds:X509Data>

          ...

          </ds:X509Data>

        </ds:KeyInfo>

       </ds:Signature>

    ... Zie paragraaf 2.3 Inhoud ...

       </saml:Assertion ... >

  </wss:Security>

</soap:Header>
```
