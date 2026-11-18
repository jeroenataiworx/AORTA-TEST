[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBZ AORTA_Auth_IH_Contracttoken](../gbz-aorta_auth_ih_contracttoken.md)

# Het SAML contracttoken

## Structuur

Het SAML concept-contracttoken is een afgegeven SAML assertion van partij B met betrekking tot het af te sluiten contract tussen beide partijen. Het concept-contracttoken wordt in zijn geheel Base64 geëncodeerd toegevoegd aan het contracttoken die gebruikt wordt bij berichtauthenticatie voor het landelijk EPD. Het SAML concept-contracttoken is ondertekend met behulp van het server-certificaat (UZI of EV/OV) van partij B. Het SAML contracttoken is ondertekend met behulp van het server-certificaat (UZI of EV/OV) van partij A. Het contracttoken is qua structuur en inhoud vrijwel identiek aan het concept-contracttoken. Enige verschillen zijn:

- De issuer van het concept-contracttoken is de Subject Distinguished Name van partij B; de issuer van het contracttoken is de Subject Distinguished Name van partij A.

- Het subject is de Subject Distinguished Name van de tegenpartij, dus: in het concept-contracttoken de Subject Distinguished Name van partij A; in het contracttoken de Subject Distinguished Name van partij B

- Het contracttoken bevat (optioneel) een attribuut _CTR_locatie

- Het contracttoken bevat een attribuut _Concept-contract_token

- Het contracttoken bevat een attribuut _AC

- Beide tokens bevatten een attribuut _FQDN. Hierin is de FQDN van de tegenpartij opgenomen.

Dientengevolge kan overal waar in de hiernavolgende tekst concept-contracttoken vermeld staat ook contracttoken gelezen worden tenzij in de paragraaf duidelijk onderscheid gemaakt wordt.

## Het request

Het request is een simpel XML bericht aan de te contracteren organisatie en bevat de Subject Distinguished Name van de contractnemer.

Noot: alhoewel het geen authenticatieverzoek betreft is het wel een verzoek om een SAML assertion. Hiermee wordt dus afgeweken van het zuivere SAML protocol.

Voorbeeld request:

```
<samlp:AuthnRequest
xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
ID="identifier_1"
Version="2.0"
IssueInstant="2004-12-05T09:21:59Z"
AssertionConsumerServiceIndex="1">
<saml:Issuer>https://sp.example.com/SAML2</saml:Issuer>
<samlp:NameIDPolicy
AllowCreate="true"
Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient"/>
<samlp:Subject>
<value>
Subject Distiguished Name A
</value>
</samlp:Subject>
</samlp:AuthnRequest>
```

## Assertion

De SAML assertion heeft de volgende structuur (de waarden die in het token gebruikt worden zijn fictief):

| **Element/@Attribute** ; | **0..1** ; | **Omschrijving** ; |
| --- | --- | --- |
| @ID ; | 1 ; | Unieke identificatie van de Assertion ; |
| @Version ; | 1 ; | Versie van het SAML Protocol. Vaste waarde moet zijn 2.0 ; |
| @IssueInstant ; | 1 ; | Tijdstip van uitgifte van de Assertion. ; |
| Issuer ; | 1 ; | Concept-contracttoken: De Subject Distinguished Name van de te contracteren partij (partij B). ;  Contracttoken: De Subject Distinguished Name van de contractnemer (partij A) ; |
| @NameQualifier ; | 0 ; | Niet gebruiken ; |
| @SPNameQualifier ; | 0 ; | Niet gebruiken ; |
| @Format ; | 1 ; | Format="urn:oasis:names:tc:SAML:2.0:nameid-format:entity" ; |
| @SPProviderID ; | 0 ; | Niet gebruiken ; |
| Signature ; | 1 ; | Beide tokens kunnen ondertekend worden door zowel een UZI-servercertificaat als een EV/OV servercertificaat. ;  Concept-contracttoken: Bevat de handtekening over de assertion zoals gezet met behulp van het servercertificaat van partij B. ;  Contracttoken: Bevat de handtekening over de assertion zoals gezet met behulp van het servercertificaat van partij A. ; |
| Subject ; | 1 ; | Subject Distinguished Name van de tegenpartij: concept-cotracttoken: Subject Distinguished Name van partij A; contracttoken: Subject Distinguished Name van partij B. ; |
| BaseID ; | 0 ; | Niet gebruiken ; |
| NameID ; | 1 ; | Bevat de Subject Distinguished Name. ; |
| EncryptedID ; | 0 ; | Niet gebruiken ; |
| SubjectConfirmation ; | 1 ; | Moet aanwezig zijn. ; |
| @Method ; | 1 ; | 'urn:oasis:names:tc:SAML:2.0:cm:sender-vouches’ ; |
| SubjectConfirmationData ; | 1 ; | Bevat Keyinfo ; |
| @Recipient ; | 0 ; | Niet gebruiken ; |
| @NotOnOrAfter ; | 0 ; | Niet gebruiken ; |
| @InResponseTo ; | 0 ; | Niet gebruiken ; |
| @NotBefore ; | 0 ; | Niet gebruiken ; |
| @Address ; | 0 ; | Niet gebruiken ; |
| KeyInfo ; | 1 ; | Voor beide tokens: Bevat het publieke deel van het X509 servercertificaat ; |
| Conditions ; | 1 ; | Moet aanwezig zijn. ; |
| @NotBefore ; | 1 ; | Moet aanwezig zijn. ; |
| @NotOnOrAfter ; | 1 ; | Moet aanwezig zijn. Mag maximaal 10 jaar na @NotBefore liggen. ; |
| Condition ; | 0 ; | Niet gebruiken ; |
| AudienceRestriction ; | 1 ; | Moet aanwezig zijn ; |
| Audience ; | 1..* ; | Minimaal 1 element: urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:1 (is de ZIM). Voor het concept-contracttoken tevens de urn naar de contractnemer (partij A). Meerdere audiences zijn toegestaan. ; |
| ProxyRestriction ; | 0 ; | Niet gebruiken ; |
| Advice ; | 0 ; | Niet gebruiken ; |
| AuthnStatement ; | 1 ; | Moet aanwezig zijn ; |
| @AuthnInstant ; | 1 ; | Tijdstip van aanmaak. ; |
| @SessionIndex ; | 0 ; | Niet gebruiken ; |
| AuthnContext ; | 1 ; | Moet aanwezig zijn ; |
| AuthnContextClassRef ; | 1 ; | urn:oasis:names:tc:SAML:2.0:ac:classes:X509 ; |
| AttributeStatement ; | 1 ; | Moet aanwezig zijn ; |
| Attribute ; | 0..1 ; | Optioneel aanwezig; alleen in contracttoken. ; |
| @Name ; | 1 ; | Vaste waarde: “_CTR_locatie” ; |
| AttributeValue ; | 0..1 ; | De URL naar het Contracttokenregister ; |
| Attribute ; | 1 ; | Moet aanwezig zijn alleen in contracttoken. ; |
| @Name ; | 1 ; | Vaste waarde: “_Concept-contract_token” ; |
| AttributeValue ; | 1 ; | Base64 representatie van het WID_token ; |
| Attribute ; | 1 ; | Moet aanwezig zijn alleen in contracttoken. ; |
| @Name ; | 1 ; | Vaste waarde: “_AC” ; |
| AttributeValue ; | 1 ; | Bevat een X.509 Attribute certificate ; |
| Attribute ; | 1 ; | Moet aanwezig zijn in beide tokens ; |
| @Name ; | 1 ; | Vaste waarde: “_Scope” ; |
| AttributeValue ; | 1 ; | Bevat de scope (dienst) van het contract ; |

N.B.: bovenstaande tabel bevat de meest gebruikte elementen van SAML assertions en is derhalve niet volledig. Voor niet genoemde elementen geldt: Niet gebruiken.

## Namespaces

Het SAML concept-contracttoken die gebruikt wordt bij berichtauthenticatie maakt gebruik van de volgende namespaces. De prefixen zijn niet normatief maar worden in dit document als voorbeelden gebruikt.

**Tabel AORTA.STK.t3300 - Namespaces**

| **Prefix** ; | **Namespace URI** ; |
| --- | --- |
| ds ; | [http://www.w3.org/2000/09/xmldsig#](http://www.w3.org/2000/09/xmldsig#) ; |
| saml ; | urn:oasis:names:tc:SAML:2.0:assertion ; |
| samlp ; | urn:oasis:names:tc:SAML:2.0:protocol ; |
| wss ; | [http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd](http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd) ; |

Bij het gebruik van de namespace-prefixes is het van belang deze na het ondertekenen niet meer te veranderen, dit maakt de digitale handtekening ongeldig.

## Inhoud

De volgende paragrafen beschrijven de verschillende kenmerken en beveiligingsgerelateerde gegevens die het SAML (concept-)contracttoken onderscheiden, zoals in [IH tokens generiek] beschreven is.

```
<saml:Assertion ... xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">
```

Het SAML (concept-)contracttoken begint met het Assertion element en een verwijzing naar de XML SAML namespace voor SAML 2.0 assertions. De attributen behorende bij het Assertion element wordt in paragraaf 2.4.1 Uniekheid beschreven.

### Uniekheid

```
ID="token_dd1c1f96-f0b0-4026-a978-4d724c0a0a4f"
IssueInstant="2009-06-24T11:47:34Z"
Version="2.0">
```

De volgende attributen van het SAML assertion element maken van de SAML assertion een uniek gegeven, uitgegeven door de verzender van het bericht. Het attribuut ID identificeert op een unieke wijze de assertion. De waarde moet *mondiaal uniek* zijn voor alle berichten, zodat bij samenvoegen van meerdere XML bestanden (in een HL7v3 batch of anderszins) de waarde uniek blijft.

Het wordt aanbevolen een UUID (Universally Unique Identifier) te gebruiken. Bij het gebruik van andere vormen is er een kans, hoe klein ook, dat een ID samenvalt met een ID gemaakt volgens een andere methode van een andere leverancier).

Een ID in XML mag niet met een cijfer beginnen. Bij het gebruik van een UUID is het dus aan te raden een prefix te gebruiken, welke met een letter of underscore (‘_’) begint.

Het attribuut IssueInstant is een tijdsmoment van uitgifte van de SAML assertion. De tijdswaarde is gecodeerd in UTC. Het attribuut Version is de gebruikte SAML versie van de SAML assertion. De aanduiding voor de versie van SAML gedefinieerd in deze specificatie is "2.0".

### Afzender

```
<saml:Issuer>
 <!-- De Issuer verwijst naar de organisatie die het token heeft gegenereerd.-->
     VOORBEELD ziekenhuis ABC
</saml:Issuer>
```

In de issuer dient de Subject Distinguished Name uit het servercertificaat waarmee het token is ondertekend overgenomen te worden.

### Onderwerp

```
<saml:Subject>
  <saml:NameID>
   VOORBEELD Vendor XYZ
  </saml:NameID>
  <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:sender-vouches ">
  </saml:SubjectConfirmation>
</saml:Subject>
```

De `Subject`verwijst naar de door de organisatorische (tegen) partij waarmee het contract afgesloten wordt. Dus voor de contractnemer de te contracteren partij; voor de contractgever de contractnemer.

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

Het attribuut *NotBefore* is de tijd waarop de SAML assertion geldig wordt. NotBefore moet altijd op of na de aanvang van de geldigheidsdatum van het certificaat (waarmee het concept-contracttoken is getekend) liggen.

Wordt een bericht met een concept-contracttoken ontvangen voor *NotBefore* is aangevangen, dan **moet** dit bericht geweigerd worden.

Het attribuut *NotOnOrAfter* is de tijd waarop de SAML assertion vervalt. *NotOnOrAfter*mag na het verstrijken van de geldigheid van het certifcaat (waarmee het concept-contracttoken is getekend) liggen.

Wordt een bericht met een concept-contracttoken ontvangen op of nadat *NotOnOrAfter* is verstreken, dan **moet** dit bericht geweigerd worden.

Deze tijd is als bovenstaande tijd geformatteerd. Het maximaal toegestane verschil tussen *NotBefore* en *NotOnOrAfter* is tien jaar.

De geldigheidsduur van een concept-contracttoken (*NotOnOrAfter* minus *NotBefore*) kan langer zijn dan de geldigheidsduur van het identiteitscertificaat waarmee het token wordt getekend.

Bij het ondertekenen van het concept-contracttoken moet er een geldig certificaat gebruikt worden. Indien bij ondertekening van het concept-contracttoken het certificaat al op de CRL is geplaatst, dan dient het concept-contracttoken wel geweigerd te worden.

Indien het certificaat vóór ondertekening van het concept-contracttoken op de CRL is geplaatst, dan dient het concept-contracttoken geweigerd te worden door het LSP.

Indien het certificaat na ondertekening van het concept-contracttoken op de CRL is geplaatst, dan dient het concept-contracttoken niet geweigerd te worden.

Het inperken van bepaalde partijen (`AudienceRestriction`) waarvoor de assertion bedoeld is wordt beschreven in paragraaf 2.4.5 Ontvanger.

### Ontvanger

```
<saml:AudienceRestriction>
  <!-- Root en extensie van de ZIM -->
  <saml:Audience>urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:1</saml:Audience>
</saml:AudienceRestriction>
```

In de `AudienceRestriction`wordt beschreven aan wie de SAML assertion is gericht. In ieder geval dient de ZIM als audience voor te komen (`IIext:1`). Meerdere Audience elementen is toegestaan.

Voor de `<Audience>` parameter is gekozen voor URN. De URN string is opgebouwd uit een IIroot en een IIext. "II" staat voor het HL7v3 datatype Instance Indentifier. Om de namespace in URN uniek te krijgen is II als prefix voor de root en ext geplaatst.

AORTA Applicatie-id’s worden uitgedrukt als een id onder het identificatiesysteem “2.16.840.1.113883.2.4.6.6”. Het correcte applicatie-id voor de GBZ-applicatie wordt toegekend bij aansluiting op de AORTA. Stel dat dit “300” zou zijn, dan ziet de URN er als volgt uit:

`urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:300`

### Authenticatie

```
<saml:AuthnStatement
 AuthnInstant="2009-06-24T11:47:34"
 SessionIndex="token_2.16.528.1.1007.3.3.1234567.1_0123456789">
```

Het subject, de contactpartij binnen het contract, in de SAML assertion is geauthenticeerd door middel van het X509 servercertificaat van de betreffende organisatie.

```
<saml:AuthnContext>
  <saml:AuthnContextClassRef
>urn:oasis:names:tc:SAML:2.0:ac:classes:X509</saml:AuthnContextClassRef>
</saml:AuthnContext>

</saml:AuthnStatement>
```

Afsluiting authentication statement.

### Attributen

```
<saml:AttributeStatement>
```

De volgorde van de attributen in het AttributeStatement is niet relevant. Er mogen geen andere attributen opgenomen worden in het AttributeStatement dan hier beschreven is.

**_CTR_locatie (optioneel, alleen in contracttoken)**

```
<saml:Attribute Name="_CTR_locatie">
  <saml:AttributeValue> 
      http://aorta-zorg.nl/contractregister
  </saml:AttributeValue>
</saml:Attribute>
```

Het attribuut _CTR_locatie geeft de locatie aan van een contractregister aan indien het uitwisselsysteem van zo een register gebruikt maakt. Binnen AORTA is dit:

`http://aorta-zorg.nl/contractregister`

Het attribuut is optioneel en dient alleen voor te komen in het contracttoken.

**_Concept-contract_token (alleen in contracttoken)**

```
<saml:Attribute Name="_Concept-contract_token">
  <saml:AttributeValue> 
      Base64 representatie van het WID_token
  </saml:AttributeValue>
</saml:Attribute>
```

Het attribuut WID_token bevat de gehele SAML assertion van het concept-contract Base64 geëncodeerd.

**_FQDN (beide tokens)**

```
<saml:Attribute Name="_FQDN">
  <saml:AttributeValue> 
      FQDN uit servercertificaat
  </saml:AttributeValue>
</saml:Attribute>
```

Het attribuut _FQDN bevat de FQDN uit het servercertificaat waarmee het token is ondertekend, dus van de issuer.

**_Scope (beide tokens)**

```
<saml:Attribute Name="_Scope">
  <saml:AttributeValue> 
urn:IIroot:2.16.840.1.113883.2.4.6.10:IIext:”<code>”
  </saml:AttributeValue>
</saml:Attribute>
```

Het attribuut _Scope bevat de code van de dienst waar het contract betrekking op heeft.

De lijst met diensten en bijbehorende codes wordt gemeenschappelijk bijgehouden en aangevuld.

De in het voorbeeld genoemde OID (`2.16.840.1.113883.2.4.6.10`) is fictief en dient nog nader vastgesteld te worden.

**_AC (alleen in contracttoken)**

```
<saml:Attribute Name="_AC">
  <saml:AttributeValue> 
      Attribute certificate 
  </saml:AttributeValue>
</saml:Attribute>
```

Het attribuut _AC bevat een, door de contractnemer gegenereerd, X.509 certificate een AttributeCertificate (AC)

Een AC heeft geen eigen sleutelpaar maar wordt ondertekend met het private certificate van de uitgever ervan. Bij wijze van trust wordt verwacht dat een AC-verifier de publieke sleutel heeft bijvoorbeeld door die eenmalig uit te wisselen.

Standaard attributen van een AC zijn:

- Version = v2

- Holder: De FQDN van de gecontracteerde

- Issuer: het issuerserial van de uitgever van het AC meer concreet: de issuerserial van het UZI-servercertificaat van de zorgverlener. Met dit certificaat moet het AC ondertekend worden. Indien geen UZI-partij, dan dient het publieke deel van het EV/OV servcertificaat eenmalig uitgewisseld te worden.

- Serialnumber: Uniek nummer gegenereerd door de uitgever (issuer)

- Validity period: Voorlopig vaststellen op 10 jaar?

- CRL: locatie waar de Certificate Revocation List gevonden kan worden

- De signature

Het cerificaat waarmee het AC ondertekend is dient geldig te zijn (geweest) ten tijde van de ondertekening.

Het contract kan opgezegd worden door het AttributeCertificate op de CRL te plaatsen.

Tenslotte wordt het attributen statement blok afgesloten met

```
</saml:AttributeStatement>
```

**attributeStatement blok**

Het attributen statement blok ziet er dan bijvoorbeeld zo uit (de volgorde van de attributen is niet relevant):

```
<saml:AttributeStatement>
<saml:Attribute Name="_CTR_locatie">
  <saml:AttributeValue> 
      http://aorta-zorg.nl/contractregister
  </saml:AttributeValue>
</saml:Attribute>
<saml:Attribute Name="_Concept-contract_token">
  <saml:AttributeValue> 
      Base64 representatie van het WID_token
  </saml:AttributeValue>
</saml:Attribute>
<saml:Attribute Name="_FQDN">
  <saml:AttributeValue> 
      FQDN uit servercertificaat
  </saml:AttributeValue>
</saml:Attribute>
<saml:Attribute Name="_Scope">
  <saml:AttributeValue> 
urn:IIroot:2.16.840.1.113883.2.4.6.10:IIext:”<code>”
  </saml:AttributeValue>
</saml:Attribute>
<saml:Attribute Name="_AC">
  <saml:AttributeValue> 
      Attribute certificate 
  </saml:AttributeValue>
</saml:Attribute>
</saml:AttributeStatement>
```

## Algoritmes

Om de integriteit en onweerlegbaarheid van het SAML concept-contracttoken te waarborgen wordt een XML Signature geplaatst, zoals beschreven in [IH tokens generiek]. Na plaatsen van de XML Signature kan de ontvanger, met gebruikmaking van het publieke deel van het servercertificaat, onomstotelijk vaststellen dat het SAML concept-contracttoken ondertekend is met de privé sleutel behorend bij het gebruikte severcertificaat van de te contracteren organisatie en dat het contracttoken ondertekend is met de privé sleutel van het servercertificaat van de contractnemer.

De XML Signature van het SAML concept-contracttoken die gebruikt wordt bij berichtauthenticatie met behulp van het identiteitscertificaat maakt gebruik van de volgende algoritmes, zoals beschreven in [IH tokens generiek]:

- Voor het berekenen van de hashwaarde wordt SHA-256 gebruikt.

- Voor de digitale handtekening in AORTA wordt gebruik gemaakt van een RSA handtekening over een SHA-256 digest.

Omdat de XML Signature onderdeel is van het SAML concept-contracttoken en in het SAML concept-contracttoken geplaatst wordt, moet er een "enveloped-signature" transformatie uitgevoerd worden die de Signature tags uit het SAML concept-contracttoken verwijderd gevolgd door een “exc-c14n transformatie” (zie ook [SAML Core] §5.4.3 en §5.4.4).

## Opbouw

### De headers

Eerst wordt het SAML concept-contracttoken – het `<saml:Assertion ...>` element aangemaakt en gevuld met die elementen, zoals beschreven in paragraaf 2.4 Inhoud.

```
<saml:Assertion
   ID="token_2.16.528.1.1007.3.3.1234567.1_0123456789"
   IssueInstant="2009-06-24T11:47:34Z"
   Version="2.0"
   xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">
 ... Zie paragraaf 2.4 Inhoud ...
</saml:Assertion>
```

Het XML Signature blok is onderdeel van het SAML concept-contracttoken. Het XML Signature blok komt na het `<saml:Issuer>` element. Na de Signature volgt de rest van de inhoud van de assertion.

```
<saml:Assertion
   ID="token_2.16.528.1.1007.3.3.1234567.1_0123456789"
   IssueInstant="2009-06-24T11:47:34Z"
   Version="2.0"
   xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">
  <saml:Issuer Format="urn:oasis:names:tc:SAML:2.0:nameid-format:entity">
   Subject Distinguished Name
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
  </ds:Signature>  ...
  ... Zie paragraaf 2.3 Inhoud ...
</saml:Assertion>
```

Indien de Signature aangemaakt wordt moet niet meer met de strings (saml:Assertion en SignedInfo) gemanipuleerd worden, maar ze moeten octet-voor-octet overgenomen worden in het bericht. Strikt genomen is het toegestaan wijzigingen aan te brengen die door canonicalisatie bij de ontvanger weer opgeheven worden, maar wanneer de digitale handtekening door middel van strings wordt opgebouwd, is het een foutgevoelige handeling.

Lange Base 64 waarden zijn afgekort. Wederom kan dit als strings worden behandeld, waarbij drie waarden vervangen moeten worden.

Deze drie waarden worden ingevuld:

- Neem het SignedInfo blok op.

- Neem de SignatureValue op.

- Neem certificaatgegevens in het KeyInfo blok op, in de vorm van het volledige publieke certificaat (in het concept-contracttoken het servercertificaat van de te contracteren partij; in het contracttoken het servercertificaat van de contractnemer).

Wanneer een bericht een SAML assertion bevat, moet dat bericht precies één bijbehorende digitale handtekening bevatten.

Het maken van de XML Signature uit strings levert de SAML assertion op met daarin de Signature.

### Plaats van het SAML token en de digitale handtekening

Het SAML concept-contracttoken met daarin de digitale handtekening wordt Base64-geëncodeerd in het attribuut “_Concept-contract_token” van het contracttoken gezet.

Het gehele contracttoken wordt ondertekend met het servercertificaat van de contractnemer.
