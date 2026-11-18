[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBZ AORTA_Auth_IH_Mandaattoken](../gbz-aorta_auth_ih_mandaattoken.md)

# Het SAML mandaattoken

In dit hoofdstuk wordt de inhoud van het SAML mandaattoken besproken die bij mandatering en de berichtauthenticatie met behulp van de UZI-pas wordt gebruikt. Het SAML mandaattoken bevat informatie over de mandaatgever in relatie tot de gemandateerde zorgmedewerker. Het SAML mandaattoken is een op XML gebaseerd SAML assertion en heeft tot doel de *assertions* (bewijs van een bewering) over te brengen tussen partijen.

Alle XML voorbeelden in het document dienen door de betrokken partijen tijdens het bouwen van de uitwisseling getest, en waar nodig, in samenspraak met VZVZ aangepast te worden voor een juiste optimale werking.

Voor het verkrijgen van het SAML mandaattoken en het aanbieden van dit token aan het LSP worden de volgende profielen gebruikt:

- Het gebruik van het SAML mandaattoken (security token) in het kader van het WSS SOAP berichten profiel voor het veilig stellen en uitwisseling van authentieke SOAP berichten.

Dit profiel raakt het koppelvlak:

- goed beheerd zorgsysteem (GBZ) – het landelijk schakelpunt (LSP)

Dit profiel wordt in de volgende paragrafen verder uitgewerkt.

## Structuur

Het SAML mandaattoken is een afgegeven SAML assertion die gebruikt wordt bij mandatering en berichtauthenticatie met behulp van de UZI-pas binnen AORTA. Er wordt gebruik gemaakt van SAML v2.0 [SAML Core].

### Assertion

De assertion heeft de volgende structuur (de waarden die in het token gebruikt worden zijn fictief):

| **Element/@Attribute** ; | **0..1** ; | **Omschrijving** ; |
| --- | --- | --- |
| @ID ; | 1 ; | Unieke identificatie van de Assertion ; |
| @Version ; | 1 ; | Versie van het SAML Protocol. Vaste waarde moet zijn 2.0 ; |
| @IssueInstant ; | 1 ; | Tijdstip van registratie van het mandaat. ; |
| Issuer ; | 1 ; | De zorgverlener die het mandaat afgeeft. ; |
| @NameQualifier ; | 0 ; | Niet gebruiken ; |
| @SPNameQualifier ; | 0 ; | Niet gebruiken ; |
| @Format ; | 1 ; | Format="urn:oasis:names:tc:SAML:2.0:nameid-format:entity" ; |
| @SPProviderID ; | 0 ; | Niet gebruiken ; |
| Signature ; | 1 ; | Bevat de handtekening over de assertion zoals gezet met behulp van de UZI pas van de zorgverlener die het mandaat verleent (de mandaterende). De handtekening dient geplaatst te zijn met behulp van het handtekening-certificaat op de pas. ; |
| Subject ; | 1 ; | Bevat de Organisatie (URA) waarbinnen het mandaat geldig is. Let op: Indien dit veld gevuld wordt bij het uitlezen van de UZI pas, dan zal dit veld in het geval van gastgebruik niet de juiste URA bevatten. Er wordt aanbevolen dit veld met de URA uit het gebruikte servercertificaat te vullen. ; |
| BaseID ; | 0 ; | Niet gebruiken ; |
| NameID ; | 1 ; | Bevat de URA ; |
| EncryptedID ; | 0 ; | Niet gebruiken ; |
| SubjectConfirmation ; | 1 ; | Moet aanwezig zijn ; |
| @Method ; | 1 ; | 'urn:oasis:names:tc:SAML:2.0:cm:sender-vouches' ; |
| SubjectConfirmationData ; | 0 ; | Niet gebruiken ; |
| @Recipient ; | 0 ; | Niet gebruiken ; |
| @NotOnOrAfter ; | 0 ; | Niet gebruiken ; |
| @InResponseTo ; | 0 ; | Niet gebruiken ; |
| @NotBefore ; | 0 ; | Niet gebruiken ; |
| @Address ; | 0 ; | Niet gebruiken ; |
| KeyInfo ; | 0 ; | Niet gebruiken ; |
| Conditions ; | 1 ; | Moet aanwezig zijn ; |
| @NotBefore ; | 1 ; | Moet aanwezig zijn. ; |
| @NotOnOrAfter ; | 1 ; | Moet aanwezig zijn. ; |
| Condition ; | 0 ; | Niet gebruiken ; |
| AudienceRestriction ; | 1 ; | Moet aanwezig zijn ; |
| Audience ; | 1 ; | Bij AORTA/LSP en AoF: ;  `urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:1 (`1 is de applicatie-id van de ZIM) ;  Bij MITZ ;  `"urn:oid:2.16.840.1.113883.2.4.3.111.2.1"`(is MITZ) ;  **Obsolete**: Bij de verzendende GBZ-applicatie ;  `urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:<AppId>`(is de verzendende GBZ-applicatie) ;  **WIJZIGINGSVOORSTEL**: ;  De verschillende Audience samenvoegen en er ;  `<saml:Audience>urn:generic:audience</saml:Audience>` ;  van maken. ; |
| ProxyRestriction ; | 0 ; | Niet gebruiken ; |
| Advice ; | 0 ; | Niet gebruiken ; |
| AuthnStatement ; | 0 ; | Niet gebruiken ; |
| AttributeStatement ; | 1 ; | Moet aanwezig zijn ; |
| Attribute ; | 1 ; | Moet aanwezig zijn ; |
| @Name ; | 1 ; | Vaste waarde: "autorisatieregel/context" ; |
| AttributeValue ; | 1 ; | URI waar de autorisatieregel/context gevonden kan worden waarbinnen het mandaat gegeven wordt. ; |

N.B.: bovenstaande tabel bevat de meest gebruikte elementen van SAML assertions en is derhalve niet volledig. Voor niet genoemde elementen geldt: Niet gebruiken.

## Namespaces

Het SAML mandaattoken maakt gebruik van de volgende namespaces. De prefixen zijn niet normatief maar worden in dit document als voorbeelden gebruikt.

**Tabel AORTA.STK.t3300 – Namespaces**

| **Prefix** ; | **Namespace URI** ; |
| --- | --- |
| ds ; | http://www.w3.org/2000/09/xmldsig# ; |
| saml ; | urn:oasis:names:tc:SAML:2.0:assertion ; |
| wss ; | http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd ; |

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Bij het gebruik van de namespace-prefixes is het van belang deze na het ondertekenen niet meer te veranderen, dit maakt de digitale handtekening ongeldig. ; |
| --- | --- |

## Inhoud

De volgende paragrafen beschrijven de verschillende kenmerken en beveiligingsgerelateerde gegevens die het SAML mandaattoken onderscheiden, zoals in [IH tokens generiek] beschreven is.

```
<saml:Assertion ... xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">
```

Het SAML mandaattoken begint met het Assertion element en een verwijzing naar de XML SAML namespace voor SAML 2.0 assertions. De attributen behorende bij het Assertion element wordt in paragraaf [Uniekheid](het-saml-mandaattoken.md#uniekheid) beschreven.

### Uniekheid

```
ID="token_2.16.528.1.1007.3.3.1234567.1_0123456789"

IssueInstant="2009-06-24T11:47:34Z"

Version="2.0">
```

De volgende attributen van het SAML assertion element maken van de SAML assertion een uniek gegeven, uitgegeven door de verzender van het bericht. Het attribuut ID identificeert op een unieke wijze de assertion. De assertion mag meerdere malen als token gebruikt worden. De waarde moet *mondiaal uniek* zijn voor AORTA berichten, zodat bij samenvoegen van meerdere XML bestanden (in een HL7v3 batch of anderszins) de waarde uniek blijft.

Het wordt aanbevolen een UUID (Universally Unique Identifier)[^1] te gebruiken. Bij het gebruik van andere vormen is er een kans, hoe klein ook, dat een ID samenvalt met een ID gemaakt volgens een andere methode van een andere leverancier).

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Een ID in XML mag niet met een cijfer beginnen. Bij het gebruik van een UUID is het dus aan te raden een prefix te gebruiken, welke met een letter of underscore (‘_’) begint. ; |
| --- | --- |

[^1]: Zie het RfC4122 opgesteld door het IETF: A Universally Unique Identifier (UUID) URN Namespace

Het attribuut IssueInstant is een tijdsmoment van uitgifte van de SAML assertion, in andere woorden: het tijdstip van ondertekening. De tijdswaarde is gecodeerd in UTC. Het attribuut Version is de gebruikte SAML versie van de SAML assertion. De aanduiding voor de versie van SAML gedefinieerd in deze specificatie is "2.0".

### Afzender

```
<saml:Issuer>

  123456789:01.015

</saml:Issuer>
```

De Issuer verwijst naar de UZI van de zorgverlener/medewerker die het mandaat registreert (de mandaatgever) in combinatie met de rolcode van diezelfde zorgverlener/medewerker gescheiden door een dubbele punt (:).

### Onderwerp

```
<saml:Subject>

  <saml:NameID>

     urn:IIroot:2.16.528.1.1007.3.3:IIext:12345678

  </saml:NameID>

  <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:sender-vouches">

  </saml:SubjectConfirmation>

</saml:Subject>
```

De Subject verwijst naar de organisatie waarbinnen het mandaat geldig is.

De URA wordt uitgedrukt met behulp van een URN (Uniform Resource Name). De URN is opgebouwd uit:

"urn:IIroot:"<OID voor UZI organisatieIds>":IIext:"<URA>

De URN string is opgebouwd uit een IIroot en een IIext. "II" staat voor het HL7v3 datatype Instance Indentifier. Om de namespace in URN uniek te krijgen is II als prefix voor de root en ext geplaatst.

URA’s worden uitgedrukt als een id onder het identificatiesysteem “2.16.528.1.1007.3.3”. De URA wordt toegekend door het UZI-register. Stel dat de URA de waarde “12345678” heeft, dan ziet de URN er als volgt uit:

urn:IIroot:2.16.528.1.1007.3.3:IIext:12345678

Vervolgens moet de SubjectConfirmation nog toegevoegd worden:

```
  <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:sender-vouches">

  </saml:SubjectConfirmation>
```

### Geldigheid

```
<saml:Conditions

 NotBefore="2009-06-24T11:47:34Z"

 NotOnOrAfter="2009-09-24T11:47:34Z">
```

Het attribuut *NotBefore* is de tijd waarop de SAML assertion geldig wordt. Dit hoeft niet de tijd te zijn waarop het mandaat is aangemaakt. Het is mogelijk *NotBefore* in de toekomst te zetten. NotBefore moet altijd op of na de aanvang van de geldigheidsdatum van het certificaat (waarmee het mandaat is getekend) liggen.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Wordt een bericht met een mandaat ontvangen wordt voor *NotBefore* is aangevangen, dan **moet** dit bericht geweigerd worden. ; |
| --- | --- |

Het attribuut *NotOnOrAfter* is de tijd waarop de SAML assertion vervalt. *NotOnOrAfter* moet altijd voor het verstrijken van de geldigheid van het certifcaat (waarmee het mandaat is getekend) liggen.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Wordt een bericht met een mandaat ontvangen wordt op of nadat *NotOnOrAfter* is verstreken, dan **moet** dit bericht geweigerd worden. ; |
| --- | --- |

Deze tijd is als bovenstaande tijd geformatteerd. Richtlijn voor het verschil tussen *NotBefore* en *NotOnOrAfter* is niet vastgesteld.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | De geldigheidsduur van een mandaattoken (*NotOnOrAfter* minus *NotBefore*) kan nooit langer zijn dan de geldigheidsduur van het handtekeningcertificaat waarmee het token wordt getekend. ; |
| --- | --- |

Indien het certificaat waarmee het mandaat is getekend op de CRL is geplaatst, dan dient het mandaattoken niet geweigerd te worden door het LSP. Het is op de CRL niet inzichtelijk om welke reden een certificaat op de CRL is geplaatst. Dit kunnen uiteenlopende redenen zijn zoals een verloren pas of een intrekking van een BIG-registratie. Om het zorgproces niet te frustreren wordt deze controle procesmatig opgepakt door Security Management.   
Echter, bij het ondertekenen van het mandaattoken moet er een geldig certificaat gebruikt worden. Indien bij ondertekening van het mandaattoken het certificaat al op de CRL is geplaatst, dan dient het mandaattoken wel geweigerd te worden.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Indien het certificaat vóór ondertekening van het mandaattoken op de CRL is geplaatst, dan dient het mandaattoken geweigerd te worden door het LSP. ; |
| --- | --- |

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Indien het certificaat na ondertekening van het mandaattoken op de CRL is geplaatst, dan dient het mandaattoken niet geweigerd te worden. ; |
| --- | --- |

Het inperken van bepaalde partijen (AudienceRestriction) waarvoor de assertion bedoeld is wordt beschreven in paragraaf [Ontvanger](het-saml-mandaattoken.md#ontvanger).

De subelementen OneTimeUse en ProxyRestriction worden niet gebruikt binnen het <Conditions> element bij het mandaattoken.

### Ontvanger

In de AudienceRestriction wordt beschreven aan wie de SAML assertion is gericht. Aangezien het mandaattoken bedoeld is voor gebruik door een verzendende applicatie en bedoeld is om door de ZIM begrepen te worden, worden er binnen de AudienceRestriction twee Audience elementen opgenomen, één voor de ZIM en één voor de verzendende GBZ-applicatie.

Het applicatie-id binnen de AudienceRestriction wordt uitgedrukt met behulp van een URN (Uniform Resource Name). De URN is opgebouwd uit:

"urn:IIroot:"<OID voor AORTA Applicatie-id’s>":IIext:"<applicatie-id GBZ>

De URN string is opgebouwd uit een IIroot en een IIext. "II" staat voor het HL7v3 datatype Instance Indentifier. Om de namespace in URN uniek te krijgen is II als prefix voor de root en ext geplaatst.

AORTA Applicatie-id’s worden uitgedrukt als een id onder het identificatiesysteem “2.16.840.1.113883.2.4.6.6”. Het correcte applicatie-id voor het GBZ wordt toegekend bij aansluiting op de AORTA. Stel dat dit “300” zou zijn, dan ziet de URN er als volgt uit:

urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:300

De volledige AudienceRestriction wordt dan:

```
<saml:AudienceRestriction>

  <!-- Root en extensie van de ZIM -->

  <saml:Audience>urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:1</saml:Audience>

  <!-- Root en extensie van de Applicatie -->

  <saml:Audience>urn:IIroot: 2.16.840.1.113883.2.4.6.6:IIext:300</saml:Audience>

</saml:AudienceRestriction>
```

### Attributen

```
<saml:AttributeStatement>
```

Het volgende attribuut betreft aanvullende gegevens met betrekking tot het mandaat. Er mogen geen andere attributen opgenomen worden in het AttributeStatement dan hier beschreven is.

```
<saml:Attribute Name="autorisatieregel/context">

  <saml:AttributeValue>https://goedbeheerdziekenhuis/autorisatieregels/medicatiecontext/v2</saml:AttributeValue>

</saml:Attribute>
```

Via de URI dient de lokale autorisatieregel en/of de context opgehaald te kunnen worden waarbinnen het mandaat is uitgegeven. In het voorbeeld is voor een URL gekozen.

Tenslotte wordt het attributen statement blok afgesloten met

```
</saml:AttributeStatement>
```

## Algoritmes

Om de integriteit en onweerlegbaarheid van het SAML mandaattoken te waarborgen wordt een XML Signature geplaatst, zoals beschreven in [IH tokens generiek]. Na plaatsen van de XML Signature kan de ontvanger, met gebruikmaking van de publieke sleutel van het UZI handtekening-certificaat van de verzender onomstotelijk vaststellen dat de getekende SAML assertion ondertekend is met de privé sleutel behorend bij het gebruikte UZI handtekening-certificaat van de UZI-pas van de zorgverlener.

De publieke sleutel van het UZI handtekening-certificaat bevindt zich in de LDAP van het het UZI- register.

De XML Signature van het SAML mandaattoken die gebruikt wordt bij berichtauthenticatie met behulp van de UZI-pas maakt gebruik van de volgende algoritmes, zoals beschreven in [IH tokens generiek]:

- Voor het berekenen van de hashwaarde wordt SHA-256 gebruikt.

- Voor de digitale handtekening in AORTA wordt gebruik gemaakt van een RSA handtekening over een SHA-256 digest.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Omdat de XML Signature onderdeel is van het SAML mandaattoken en in het SAML mandaattoken geplaatst wordt, moet er een "enveloped-signature" transformatie uitgevoerd worden die de Signature tags uit het SAML authenticatietoken verwijderd gevolgd door een “exc-c14n transformatie” (zie ook [SAML Core] §5.4.3 en §5.4.4). ; |
| --- | --- |

## Opbouw

### De headers

Eerst wordt het SAML mandaattoken – het <saml:Assertion ...> element aangemaakt en gevuld met die elementen, zoals beschreven in paragraaf [Inhoud](het-saml-mandaattoken.md#inhoud).

```
<saml:Assertion

   ID="token_2.16.528.1.1007.3.3.1234567.1_0123456789"

   IssueInstant="2009-06-24T11:47:34Z"

   Version="2.0"

   xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">

 ... Zie paragraaf 2.3 Inhoud ...

</saml:Assertion>
```

Het XML Signature blok is onderdeel van het SAML mandaattoken. Het XML Signature blok komt na het <saml:Issuer> element.

```
<saml:Assertion

   ID="token_2.16.528.1.1007.3.3.1234567.1_0123456789"

   IssueInstant="2009-06-24T11:47:34Z"

   Version="2.0"

   xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">

  <saml:Issuer>

   123456789:01.015

  </saml:Issuer>

  <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">

    <ds:SignedInfo>

    ...

    </ds:SignedInfo>

    <ds:SignatureValue>Wuwn...5e4=</ds:SignatureValue>

    <ds:KeyInfo>

      <ds:X509Data>

        <X509IssuerSerial>

          <X509IssuerName>CN=De Auteur CA,O=Nictiz,C=NL</X509IssuerName>

          <X509SerialNumber>359724...41160195</X509SerialNumber>

        </X509IssuerSerial>

      </ds:X509Data>

    </ds:KeyInfo>

  </ds:Signature>  ...

  ... Zie paragraaf 2.3 Inhoud ...

</saml:Assertion>
```

Indien de Signature aangemaakt wordt mogen de strings (saml:Assertion en SignedInfo) inhoudelijk niet meer gewijzigd worden. Ze moeten octet-voor-octet overgenomen worden in het bericht. Strikt genomen is het toegestaan wijzigingen aan te brengen die door canonicalisatie bij de ontvanger weer opgeheven worden, maar wanneer de digitale handtekening door middel van strings wordt opgebouwd, is het een foutgevoelige handeling.

Lange Base 64 waarden zijn in het voorbeeld afgekort. Wederom kunnen dit als strings worden behandeld, waarbij drie waarden vervangen moeten worden.

Deze drie waarden worden ingevuld:

- Neem het SignedInfo blok op.

- Neem de SignatureValue op.

- Neem certificaatgegevens in het KeyInfo blok op.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Wanneer een bericht een SAML assertion bevat, moet dat bericht precies één bijbehorende digitale handtekening bevatten. ; |
| --- | --- |

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Voor mandaattokens mag er niet meer dan één SAML assertion voorkomen met de gegevens van een daarbij behorende X.509 certificaat als KeyInfo. ; |
| --- | --- |

Het maken van de XML Signature uit strings levert de SAML assertion op met daarin de Signature.

### Plaats van het SAML token en de digitale handtekening

Het SAML authenticatietoken met daarin de digitale handtekening wordt in het WS-Security SOAP Header gezet. Deze dient altijd te bestaan als aparte SAML-assertion naast het Transactietoken [IH Transactietoken].

Het mandaattoken dient tezamen met het transactietoken ([IH transactietoken]) in het zelfde security-element opgenomen te zijn conform de [[IH tokens generiek](https://vzvz.atlassian.net/wiki/x/q42Obg)].
