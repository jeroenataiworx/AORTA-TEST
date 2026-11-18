[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [AORTA_Auth_IH_Berichtauthenticatie_UZI](../aorta_auth_ih_berichtauthenticatie_uzi.md)

# Bijlage C Token implementatie

Deze bijlage met een voorbeeld van het tekenen gaat uit van het gebruik van een door NCSC als “goed” beoordeelde SHA algoritme.

## Maak een signedData blok

Het token moet aangemaakt worden en voorzien van de gegevens uit het bericht.

Het volgende is een voorbeeld van een token:

```
<signedData xmlns="http://www.aortarelease.nl/805/"

xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"

wsu:Id="_2.16.528.1.1007.3.3.1234567.1_0123456789">

<authenticationData>

<messageId>

<root>2.16.528.1.1007.3.3.1234567.1</root>

<extension>0123456789</extension>

</messageId>

<notBefore>20070128173600</notBefore>

<notAfter>20070128174059</notAfter>

<addressedParty>

<root>2.16.840.1.113883.2.4.6.6</root>

<extension>1</extension>

</addressedParty>

</authenticationData>

<coSignedData>

<triggerEventId>QURX_TE990011NL</triggerEventId>

<patientId>

<root>2.16.840.1.113883.2.4.6.3</root>

<extension>012345672</extension>

</patientId>

</coSignedData>

</signedData>
```

De tekstwaarden (Id, root, notBefore, notAfter, triggerEventId en extension) worden vervangen door de waarden voor het betreffende bericht. De overige teksten zijn ‘vaste’ teksten (voor communicatie met de ZIM). De tekst kan aangemaakt worden in ASCII of UTF-8. Gebruik wederom bij voorkeur een lange string zonder regeleinden.

## Maak het signedData blok canoniek

Het signedData blok moet canoniek gemaakt worden volgens [EXCC14N]. Bovenstaand voorbeeld is canoniek (m.u.v. regeleinden voor de leesbaarheid). Voor de canonieke vorm zijn de volgende zaken van belang:

- Het Id attribuut moet double quoted zijn.

- De namespaces moeten voor het wsu:Id attribuut staan. Deze specificatie vermijdt het gebruik van attributen zoveel mogelijk om de canonicalisatie makkelijker te maken: in dit ene geval is dit niet mogelijk. Let op dat namespaces en wsu:Id gescheiden zijn met een enkele spatie: dit is in het voorbeeld hierboven niet meer zichtbaar.

- De namespaces moeten alfabetisch gerangschikt zijn.

- Alle regeleinden moeten met linefeed worden gedaan. Door de standaardtools voor bewerking van platte tekst zal op Unix-systemen een linefeed gebruikt worden, op MacIntosh een carriage return en op Windows carriage return + linefeed. Eenvoudiger is alle whitespace (regeleinden, tabs, spaties) weg te laten uit de signedData. In de voorbeeldbestanden is dat ook gedaan. Voor de leesbaarheid worden hier wel nieuwe regels gebruikt. (maar: alle berekeningen zijn gedaan zonder whitespace, dus voor het narekenen van bijvoorbeeld een door NCSC als “goed” beoordeelde SHA algoritme digest moeten de regeleinden wel verwijderd worden.)  
In het algemeen geldt dat whitespace tussen de verschillende <tag>s significant is: XML is immers een documentformaat, waar whitespace een belangrijk deel van de opmaak is. Whitespace tussen de tags is dus toegestaan: een conformant XML processor zal deze ook nooit "zomaar" wijzigen. Veel XML-toepassingen als de DOM en XSLT maken het mogelijk expliciet aan te geven hoe met whitespace omgegaan moet worden. Bij verwerking van digitale handtekeningen is het altijd nodig "preserveWhitespace" of vergelijkbare attributen op "True" te zetten. Exclusive Canonicalization zal niets met de whitespace tussen tags doen (wél met whitespace binnenin tags).

- Het door NCSC als “goed” beoordeelde SHA algoritme wordt berekend over het signedData element, dus er mag ook geen whitespace of newline voor of na het element meegetekend worden.

- Gebruik geen whitespace binnenin de tags, met uitzondering van een enkele spatie voor de attributen.

- Sla signedData op als ASCII of UTF-8. Dat is mogelijk omdat alle gegevens getallen of codes zijn (en niet bijv. namen van patiënten). Eigenlijk moeten bestanden die getekend worden in UTF-8 encoding zijn. De eerste 128 karakters (0 t/m 127) van UTF-8 hebben echter dezelfde hexadecimale waarden als ASCII. Er mogen beslist geen karakters in voorkomen uit de range 128-256 van b.v. ISO-Latin of Windows-1292: deze zijn niet hetzelfde in UTF-8. Voor het authenticatietoken zijn ook geen andere waarden nodig dan de eerste 128 ASCII karakters.

- Geen Byte Order Mark (BOM) toevoegen. UTF-8 staat het gebruik van een BOM toe. Applicaties kunnen deze gebruiken om te bepalen of de byte-ordering Little Endian of Big Endian is. Canonieke XML staat echter geen BOM toe – dat is ook geen probleem, aangezien UTF-8 verplicht is. Bij het gebruik van UTF-8 strings is het bij het wegschrijven dus van belang geen BOM te schrijven. Het gebruik van een BOM kan gedetecteerd worden door het bestand waarin de signedData is weggeschreven te openen: als de eerste drie octets EF BB BF zijn, is dit de BOM, en is het bestand niet correct. Als de eerste octets anders zijn, is er geen BOM gebruikt.

Of (in plaats van het bovenstaande)

- Maak het signedData blok canoniek volgens Exclusive XML Canonicalization met een geschikte library.

## Bereken de SHA digest van het signedData blok

Van de signedData moet een door NCSC als “goed” beoordeelde SHA algoritme digest berekend worden. Deze digest – een verzameling octets – wordt gecodeerd met Base 64.

## Maak het SignedInfo blok

XML Signature maakt gebruik van een SignedInfo blok voor de digitale handtekening. Dit ziet er als volgt uit:

```
<SignedInfo xmlns="http://www.w3.org/2000/09/xmldsig#">

<CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">

</CanonicalizationMethod>

<SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha512">

</SignatureMethod>

<Reference URI="#_2.16.528.1.1007.3.3.1234567.1_0123456789">

<Transforms>

<Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"></Transform>

</Transforms>

<DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha512"></DigestMethod>

<DigestValue>xx5...Gus2g=</DigestValue>

</Reference>

</SignedInfo>
```

Wederom is in de voorbeeldbestanden een string gebruikt zonder linefeeds, maar zijn deze hier voor de leesbaarheid toegevoegd.

Dit hele blok tekst kan als ASCII of UTF-8 string in de code gebruikt worden. Er zijn twee delen die vervangen moeten worden.

In de Reference ("#_2.16.528.1.1007.3.3.1234567.1_0123456789") moet de juiste Id worden toegevoegd: dit is de waarde van het Id-attribuut uit het signedData element.

In DigestValue (xx5...Gus2g=) wordt de in de vorige paragraaf berekende door NCSC als “goed” beoordeelde SHA algoritme digest, in Base 64 vorm, geplaatst.

De SignedInfo strings moeten een SignedInfo blok opleveren in canonieke vorm. Het bovenstaande blok is in canonieke vorm, wanneer tenminste alle regeleinden verwijderd worden. Verder zijn nog twee zaken van belang:

- Lege tags: <tag att="1"/> moeten voorzien worden van een expliciete eind-tag: <tag att="1"></tag>

- De namespace van XML Signature moet opgenomen zijn in het SignedInfo element. Bij genereren van een XML Signature uit een toolkit zal deze namespace vaak in het omliggende <Signature> element opgenomen zijn. Bij gebruik van [EXCC14N] wordt deze bij het canoniek maken van <SignedInfo> hier toegevoegd.

## Selecteer het authenticatiecertificaat en de bijbehorende private key

De volgende cryptografische objecten op de UZI-pas zijn noodzakelijk bij berichtauthenticatie:

- Het authenticatiecertificaat.

- De private key behorende bij het authenticatiecertificaat. Deze key wordt gebruikt om de DigestValue te ondertekenen. Deze bewerking wordt op de UZI-pas zelf uitgevoerd.

Globaal zijn de volgende stappen nodig.

- Zoek het authenticatiecertificaat:

- Normaalgesproken met de PKCS#11 functie C_FindObjects;

- Certificaten zijn uit elkaar te houden op basis van de X.509 keyUsage;

Er zijn ook hulpfuncties beschikbaar in de [AETSDK] waarmee eenvoudig het juiste certificaat is te selecteren, waaronder C_FindAuthenticationCertificate.

- Zoek de bij het authenticatiecertificaat behorende private key:

- Deze sleutel kan bij het certificaat worden gezocht op basis van het CKA_ID attribuut

- Normaalgesproken met C_FindObjects...

Er zijn ook hulpfuncties beschikbaar in de [AETSDK] die eenvoudige selectie van de juiste private key bij een bepaald certificaat mogelijk maken: C_FindCertificatePrivateKey.

In de [AETSDK] is een nadere toelichten te vinden van bovenstaande (hulp)functies.

## Bereken de "RSA with SHA" waarde over SignedInfo

Bereken de "RSA with SHA" SignatureValue over het SignedInfo blok met het certificaat en plaats deze in een <Signature> element. Zorg ervoor dat de signature in Big Endian vorm wordt gemaakt. Bij netwerkcommunicatie wordt altijd Big Endian gebruikt. O.a. Windows gebruikt normaal Little Endian. Bewerk de resulterende octets volgens Base 64:

```
<SignatureValue>DpB...GW7A==</SignatureValue>
```

Base 64 staat wel whitespace zoals spaties en regeleinden toe, dus ook met regeleinden is de waarde geldig.

Base64 moet gebruikt worden zoals gespecificeerd in [MIME].

Wanneer SHA-256 wordt gebruikt, wordt "RSA with SHA-256" als type voor de SignatureValue gekozen.

## Neem het juiste certificaat op

De volgende string wordt aangemaakt voor de certificaatverwijzing. Uiteraard wordt de juiste referentie naar het gebruikte certificaat ingevoegd in het voorbeeld.

```
<KeyInfo>

<wss:SecurityTokenReference>

<ds:X509Data xmlns:ds="http://www.w3.org/2000/09/xmldsig#">

<ds:X509IssuerSerial>

<ds:X509IssuerName>CN=TEST UZI-register Zorgverlener CA G21, O=agentschap Centraal Informatiepunt Beroepen Gezondheidszorg, C=NL</ds:X509IssuerName>

<ds:X509SerialNumber>359...195</ds:X509SerialNumber>

</ds:X509IssuerSerial>

</ds:X509Data>

</wss:SecurityTokenReference>

</KeyInfo>
```

Uitgangspunt is dat de WSS namespace gedeclareerd is zoals hierboven opgenomen. Afhankelijk van de gebruikte pas moet de eerste string "TEST UZI-register Zorgverlener CA G21" vervangen worden door de betreffende CA (zie AORTA.STK.t3220 en AORTA.STK.t3230). De tweede string "359...195" wordt vervangen door het serial number van de pas (decimaal).
