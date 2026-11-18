[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBP AORTA_Auth_IH_Berichtauthenticatie_DigiD](../gbp-aorta_auth_ih_berichtauthenticatie_digid.md)

# Het SAML authenticatietoken DigiD

In dit hoofdstuk wordt de inhoud van het gecreëerde SAML authenticatietoken van DigiD [DigiD Koppel] besproken ,dat bij berichtauthenticatie voor patiënten wordt gebruikt. Het SAML authenticatietoken bevat informatie over de toegepaste authenticatie en identificatie van de patiënt. Het SAML authenticatietoken is een op XML gebaseerde SAML assertion en heeft tot doel de *assertions* (beweringen over authenticatie) over te brengen tussen partijen (service- en identity provider) die een vertrouwensrelatie hebben.

Alle XML voorbeelden in het document dienen door de betrokken partijen tijdens het bouwen van de uitwisseling getest, en waar nodig, in samenspraak met VZVZ aangepast te worden voor een juiste optimale werking.

Voor het verkrijgen van het SAML authenticatietoken en het aanbieden van dit token aan de ZIM worden de volgende profielen gebruikt:

- Een op Webbrowsers gebaseerd profiel van het authenticatie verzoek protocol (Authentication Request Protocol) is gedefinieerd ter ondersteuning van Single Sign-On. Dit profiel raakt de koppelvlakken:patiënt ondersteuning (PC) - goed beheerd patiëntenportaal (GBP)goed beheerd patiëntenportaal (GBP)- identity provider (neemt als vertrouwde autoriteit, de diensten van DigiD waar)

Dit profiel is niet normatief en is terug te vinden in [Bijlage B](https://aorta.public.vzvz.nl/wiki/pages/createpage.action?spaceKey=AORTA8&title=%288.5.2%29%20SSO%20%28profiel%2C%20verificatie%2C%20meldingen%29&linkCreation=true&fromPageId=2167079948).

- Het gebruik van het SAML authenticatietoken (security token) in het kader van het WSS SOAP berichten profiel voor het veilig stellen en uitwisseling van authentieke SOAP berichten. Dit profiel raakt het koppelvlak:goed beheerd patiëntenportaal (GBP) – het landelijk schakelpunt (LSP)

Dit profiel wordt in de volgende paragrafen verder uitgewerkt.

## Structuur

Het SAML authenticatietoken is een door een vertrouwde Identity Provider (DigiD) gecreëerde SAML assertion die gebruikt wordt bij berichtauthenticatie van patiënten voor het LSP. DigiD ondertekent zowel de ArtifactResponse als de Assertion. De Assertion wordt vervolgens door het GBP als authenticatietoken in het bericht opgenomen.

### Assertion

De assertion heeft de volgende structuur (de waarden die in het token gebruikt worden zijn fictief):

```
<saml:Assertion

    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
    xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#"  
    Version="2.0"
    ID="_dc9f793e2811b86f8e5cdf43ab5fd47d1fe0e61c"
    IssueInstant="2012-12-20T18:50:27Z">
    <saml:Issuer>SamlIssuer</saml:Issuer>
    <saml:Subject>
        <saml:NameID>s00000000:12345678</saml:NameID>
        <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
            <saml:SubjectConfirmationData
                InResponseTo="_7afa6d9f9ff28ca9233ada1d9ec2aa1bd6c5ce49"
                Recipient="http://example.com/artifact_url"
                NotOnOrAfter="2012-12-20T18:52:27Z"/>
        </saml:SubjectConfirmation>
    </saml:Subject>
    <saml:Conditions
        NotBefore="2012-12-20T18:48:27Z"
        NotOnOrAfter="2012-12-20T18:52:27Z">
        <saml:AudienceRestriction>
            <saml:Audience>

                 urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:1

            </saml:Audience>
        </saml:AudienceRestriction>
    </saml:Conditions>
    <saml:AuthnStatement
        SessionIndex="17"
        AuthnInstant="2012-12-20T18:50:27Z">
        <saml:SubjectLocality Address="127.0.0.1"/>
        <saml:AuthnContext>
            <saml:AuthnContextClassRef>
                urn:oasis:names:tc:SAML:2.0:ac:classes:MobileTwoFactorContract
            </saml:AuthnContextClassRef>
        </saml:AuthnContext>
    </saml:AuthnStatement>
</saml:Assertion>
```

## Namespaces

Het door een vertrouwde Identity Provider afgegeven SAML authenticatietoken dat gebruikt wordt bij berichtauthenticatie, maakt gebruik van de volgende namespaces. De prefixen zijn niet normatief maar worden in dit document als voorbeelden gebruikt.   
**Tabel AORTA.STK.t3400 - Namespaces**

| **Prefix** ; | **Namespace URI** ; |
| --- | --- |
| **ds** ; | http://www.w3.org/2000/09/xmldsig# ; |
| **ec** ; | http://www.w3.org/2001/10/xml-exc-c14n# ; |
| **saml** ; | urn:oasis:names:tc:SAML:2.0:assertion ; |

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Bij het gebruik van de namespace-prefixes is het van belang deze na het ondertekenen niet meer te veranderen, dit maakt de digitale handtekening ongeldig. ; |
| --- | --- |

## Inhoud

De volgende paragrafen beschrijven de verschillende kenmerken en beveiligingsgerelateerde gegevens die het SAML authenticatietoken onderscheiden, zoals in [IH tokens generiek] beschreven is.

<saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" xmlns:ds="[http://www.w3.org/2000/09/xmldsig#](http://www.w3.org/2000/09/xmldsig)" xmlns:ec="[http://www.w3.org/2001/10/xml-exc-c14n#](http://www.w3.org/2001/10/xml-exc-c14n)" … >

Op de plaats van de drie punten (…) worden Uniekheidattributen opgenomen ten aanzien van de Assertion. Deze attributen worden beschreven in [paragraaf 2.3.1](het-saml-authenticatietoken-digid.md#uniekheid) Uniekheid.

### Uniekheid

```
<saml:Assertion

  Version="2.0"

  ID="_dc9f793e2811b86f8e5cdf43ab5fd47d1fe0e61c"

  IssueInstant="2012-12-20T18:50:27Z">
```

De attributen van het SAML assertion element maken van de afgegeven SAML assertion een uniek gegeven. Het attribuut ID identificeert op een unieke wijze de assertion. Het attribuut IssueInstant is een tijdsmoment van uitgifte van de SAML assertion. De tijdswaarde is gecodeerd in UTC. Het attribuut Version is de gebruikte SAML versie van de SAML assertion. De aanduiding voor de versie van SAML gedefinieerd in deze specificatie is "2.0".

### Onderwerp

```
<saml:Subject>
  <saml:NameID>s00000000:12345678</saml:NameID>
  <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
     <saml:SubjectConfirmationData

        InResponseTo="_7afa6d9f9ff28ca9233ada1d9ec2aa1bd6c5ce49"

        Recipient="http://example.com/artifact_url"

        NotOnOrAfter="2012-12-20T18:52:27Z"/>
  </saml:SubjectConfirmation>

</saml:Subject>
```

Het onderwerp <Subject> bij berichtauthenticatie met DigiD is een referentie naar een authenticatieverzoek van een patiënt dat door het goed beheerd patiëntenportaal is geïnitieerd. Het onderwerp bevat een uniek authenticatienummer, het <NameID> element.

DigiD neemt in het element <NameID> het sectoraal nummer op in het formaat <sectorcode>:<sectoraal nummer>

Indien de sectorcode de waarde ‘S00000000’ heeft, dan is het sectoraal nummer een BurgerServiceNummer.

Het InResponseTo attribuut en het Recipient attribuut in de bevestiging van het onderwerp <SubjectConfirmation> worden niet gebruikt door het LSP. Deze attributen worden echter wel opgenomen in de assertion.

Verder heeft de bevestiging van het onderwerp een geldigheidsduur (het NotOnOrAfter attribuut). De geldigheidsduur geeft de duur van een sessie aan tussen het goed beheerd patiëntenportaal en de identity provider (DigiD).

Voor deze bevestigingsmethode (het Method attribuut) moet de URN waarde "urn:oasis:names:tc:SAML:2.0:cm:bearer" (assertion drager) worden gebruikt.

### Geldigheid

```
<saml:Conditions

 NotBefore="2012-12-20T18:48:27Z"

 NotOnOrAfter="2012-12-20T18:52:27Z">
  …
</saml:Conditions>
```

Op de plaats van de drie punten (…) dient een AudienceRestriction te worden toegevoegd zoals beschreven in [paragraaf 2.3.5](het-saml-authenticatietoken-digid.md#ontvanger) Ontvanger).

Het attribuut *NotBefore* is de tijd waarop de afgegeven SAML assertion geldig wordt.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Wordt een bericht ontvangen op of nadat *NotOnOrAfter* is verstreken, dan **moet** dit bericht geweigerd worden[^1]. ;  [[1]](het-saml-authenticatietoken-digid.md#_ftnref1) Met de configuratie parameter "*ZIM*-*max-BSN-gracetijd*" van de ZIM kan de geldigheidtermijn van een SAML assertion vergroot worden waarbij de begintijd*(NotBefore)*vervroegd en de eindtijd (*NotOnOrAfter)* verlaat mag worden. ; |
| --- | --- |

Het attribuut *NotOnOrAfter* is de tijd waarop de afgegeven SAML assertion vervalt.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Wordt een bericht ontvangen op of nadat *NotOnOrAfter* is verstreken, dan **moet** dit bericht geweigerd worden Met de configuratie parameter "*ZIM*-*max-BSN-gracetijd*" van de ZIM kan de geldigheidtermijn van een SAML assertion vergroot worden waarbij de begintijd *(NotBefore)* vervroegd en de eindtijd (*NotOnOrAfter)* verlaat mag worden. . ; |
| --- | --- |

Aangezien DigiD deze waarden interpreteert als tijdstip van authenticatie wordt de geldigheidtermijn (d.i. de eindtijd NotOnOrAfter) opgehoogd met een "ZIM-max-BSN-gracetijd" van 15 minuten.

Het tijdsverschil tussen NotOnOrAfter en NotBefore bedraagt maximaal 4 minuten in DigiDv4.0-SAML. De tijden worden bepaald op het afgiftemoment van de assertion bij DigiD waarbij NotBefore de waarde afgiftemoment - 2 minuten en NotOnOrAfter de waarde afgiftemoment + 2 minuten krijgt.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | De geldigheidsduur van een token (*NotOnOrAfter* minus *NotBefore*) mag niet langer dan 4 minuten zijn. Wordt een bericht ontvangen waarin deze geldigheidsduur overschreden is, dan **moet** dat bericht geweigerd worden, ook al is het tijdstip *NotOnOrAfter* nog niet verstreken. ; |
| --- | --- |

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Van het GBP wordt verwacht dat zij een timer bijhoudt die op het moment dat een gebruiker van het Portaal (de burger) via een redirect vanuit DigiD terugkeert in het LSP-portaal gestart moet worden en de gebruiker na 10 minuten (als de gebruiker op dat moment een nieuwe actie wil doen) weer terugstuurt naar DigiD voor herauthenticatie. Tevens dient het GBP op grond van deze timer een eventueel nog aanwezig ArtefactResponse token te verwijderen. ; |
| --- | --- |

De subelementen OneTimeUse en ProxyRestriction worden niet gebruikt binnen het <Conditions> element bij Berichtauthenticatie met DigiD.

### Afzender

```
<saml:Issuer Format="urn:oasis:names:tc:SAML:2.0:nameid-format:entity">

  https://federatie.overheid.nl/aselectserver/server/

</saml:Issuer>
```

De afzender is de authenticatie autoriteit (DigiD) die de assertion heeft afgegeven en de patiënt heeft geauthenticeerd. De Issuer wordt in dit fictieve voorbeeld uitgedrukt met behulp van een URL.

Noot: In samenspraak met VZVZ en andere betrokken partijen kan het formaat en inhoud van de Issuer in de assertion heroverwogen worden, zie volgende opmerking.

De Issuer kan ook uitgedrukt worden met behulp van URN (Uniform Resource Name). De URN is opgebouwd uit:

"urn:IIroot:"<OID van het coderingssysteem>":IIext:"<extensie>

De URN string is opgebouwd uit een IIroot en een IIext. "II" staat voor Instance Indentifier. Binnen AORTA is de IIroot een oid (Object IDentifier), die een identificatie- of coderingssysteem weergeeft, en dat leidt in HL7v3 XML tot een element met twee attributen, een root met de uitgegeven codering en een extensie (ext). Om de namespace in URN uniek te krijgen is II als prefix voor de root en ext geplaatst.

Indien de keuze door de betrokken partijen gemaakt wordt om de Issuer als URN uit te drukken, moet de root en extensie door de GBP organisatie aangevraagd en geregeld worden.

Het goed beheerd patiëntenportaal past een TLS-sessie toe bij het opvragen van de assertion bij de identity provider.

### Ontvanger

```
  <saml:AudienceRestriction>
     <!-- Root en extensie van de ZIM en het patiëntenportaal -->

     <saml:Audience>urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:1</saml:Audience>
  </saml:AudienceRestriction>
```

In de AudienceRestriction wordt beschreven aan welke ontvangende partijen (service providers) de SAML assertion is gericht. De waarden in de elementen zijn (voorlopig) vaste waarden. Voor de <Audience> parameter is (ook) gekozen voor URN, zie voor de opbouw van de URN [paragraaf 2.3.4](het-saml-authenticatietoken-digid.md#afzender) Afzender.

Vooralsnog staat DigiD niet toe dat er meerdere audiences in het token worden teruggegeven. De root en extensie van de ZIM zullen niet zijn opgenomen in de assertion. Het LSP zal zo geconfigureerd moeten worden dat tokens waarbij als audience het patiëntenportaal is opgenomen ook toegelaten worden.

### Authenticatie

```
<saml:AuthnStatement

  SessionIndex="17"

  AuthnInstant="2012-12-20T18:50:27Z">
  …

</saml:AuthnStatement>
```

Op de plaats van de drie punten (…) worden de <SubjectLocality> en de <AuthnContext> toegevoegd zoals hieronder beschreven.

Het onderwerp (Subject), een patiënt, in de SAML assertion is geauthenticeerd doormiddel van een authenticatiemiddel op een gegeven moment.

<saml:SubjectLocality Address="127.0.0.1"/>

De SubjectLocality is gevuld met het IP-adres (Address attribuut) van de PC van de gebruiker en is onderdeel van het AuthnStatement. Deze wordt gebruikt om te verifiëren of de patiënt een vervolg verzoek vanaf hetzelfde IP-adres doet als zijn initiële verzoek tijdens het benaderen van het patiëntenportaal.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Bij communicatie tussen de computer van de patiënt en het patiëntenportaal mag het adres van de computer van de patiënt tijdens een sessie niet wijzigen. Bij wijziging van het adres (Address attribuut) tijdens de sessie in de SubjectLocality, wordt dit als malafide activiteit aangemerkt en wordt de sessie beëindigd en is herauthenticatie vereist. ; |
| --- | --- |

```
<saml:AuthnContext>
  <saml:AuthnContextClassRef>

      urn:oasis:names:tc:SAML:2.0:ac:classes:MobileTwoFactorContract

  </saml:AuthnContextClassRef>
</saml:AuthnContext>
```

Binnen de SAML specificatie is het mogelijk om een authenticatie-context (*AuthnContext*) mee te geven die de context aangeeft van het gebruikte authenticatiemiddel. Binnen de SAML specificatie zijn een aantal contexten gespecificeerd, zie [SAML Authn Context], die gebruikt kunnen worden als referentiekader voor communicatie tussen de ZIM en andere componenten zoals het goed beheerd patiëntenportaal.

Het LSP moet de volgende DigiD-betrouwbaarheidsniveau’s ondersteunen:

- Basis[^1]: “urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport”; Burger krijgt toegang tot dienst met authenticatiesterkte 10 t/m 19;

- Midden: "urn:oasis:names:tc:SAML:2.0:ac:classes:MobileTwoFactorContract"; Burger krijgt toegang tot dienst met authenticatiesterkte 20 t/m 24;

- Substantieel: "urn:oasis:names:tc:SAML:2.0:ac:classes:Smartcard”;Burger krijgt toegang tot dienst met authenticatiesterkte 25 t/m 29;

- Hoog[^2]: "urn:oasis:names:tc:SAML:2.0:ac:classes:SmartcardPKI”Burger krijgt toegang tot dienst met authenticatiesterkte 30 en hoger.

Het LSP controleert op de geldigheid en correctheid van het DigiD-token.

[^1]: Het LSP ondersteunt geen diensten die gebruik maken van betrouwbaarheidsniveau basis.

[^2]: Het LSP ondersteunt geen diensten die gebruik maken van betrouwbaarheidsniveau hoog.

## Algoritmes

Om de integriteit en onweerlegbaarheid van het SAML authenticatietoken te waarborgen wordt een XML Signature geplaatst, zoals beschreven in [IH tokens generiek]. Na plaatsen van de XML Signature kan de ontvanger, met gebruikmaking van het PKIoverheid-certificaat van de verzender onomstotelijk vaststellen dat de getekende SAML assertion ondertekend is met de privé sleutel behorend bij het gebruikte PKIoverheid-certificaat.

De XML Signature van het SAML authenticatietoken die gebruikt wordt bij berichtauthenticatie met behulp van DigiD maakt gebruik van de volgende algoritmes, zoals beschreven in [IH tokens generiek].

- Voor het berekenen van de hashwaarde wordt SHA-256 gebruikt.

- Voor de digitale handtekening in AORTA wordt gebruik gemaakt van een RSA handtekening over een SHA-256 digest.

- Omdat de XML Signature onderdeel is van het SAML authenticatietoken en in het SAML authenticatietoken geplaatst wordt, moet er een "enveloped-signature" transformatie uitgevoerd worden die de Signature tags uit het SAML authenticatietoken verwijderd.

## Opbouw

Na authenticatie en toegangsverlening van een patiënt op het GBP moet het GBP er zorg voor dragen dat het SAML authenticatietoken wordt toegevoegd bij de berichten die van het GBP naar het landelijk schakelpunt worden verzonden.

Het SAML authenticatietoken – het <saml:Assertion ...> element is aangemaakt en gevuld met die elementen, zoals beschreven in de voorgaande paragrafen.

### De digitale handtekening

Het XML Signature blok is onderdeel van het SAML authenticatietoken. Het XML Signature blok komt na het <saml:Issuer> element van de <saml:Assertion>.

```
<ds:Signature>
    <ds:SignedInfo>
        <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
        <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
        <ds:Reference URI="#_b2728a3aa52c4779c4c77ab8dd8a7dda604c94c7">
            <ds:Transforms>
                <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
                <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                    <ec:InclusiveNamespaces PrefixList="ds saml xs"/>
                </ds:Transform>
            </ds:Transforms>
            <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
            <ds:DigestValue>675ga8KqGFqJSGgSJHzoVU+kgrlWqYLpTxJ28gWLPkQ=</ds:DigestValue>
        </ds:Reference>
    </ds:SignedInfo>
    <ds:SignatureValue>ecXG...igg==</ds:SignatureValue>
    <ds:KeyInfo>
        <ds:KeyName>e37ee2522de410c633b3700835727ebf1834cd88</ds:KeyName>

 <ds:X509Data>

       <ds:X509Certificate>

       …DATA…

       </ds:X509Certificate>

 </ds:X509Data>
    </ds:KeyInfo>
</ds:Signature>
```

Het certificaat waarmee de assertion is getekend is opgenomen in het X509Data element.

Het in het metadatadocument gebruikte entity_id wordt gebruikt als Issuer in de Assertion.

Om van DigiD een ondertekende assertion te verkrijgen is het nodig dat de dienstaanbieder (het GBP) éénmalig in de uitwisseling van metadata van de dienstaanbieder met DigiD binnen het element <SPSSODescriptor> het attribuut WantAssertionsSigned op “true” zet.

```
<md:SPSSODescriptor WantAssertionsSigned="true" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
```

### Plaats van het SAML token in het SOAP bericht.

Het gehele SAML authenticatietoken met daarin de digitale handtekening worden in het WS-Security SOAP Header gezet.

Op het <wss:Security> element **moet** een soap:mustUnderstand="1" vlag opgenomen worden, die aangeeft dat de ontvanger dit security element **moet** verwerken en een soap:actor="[http://www.aortarelease.nl/actor/zim](http://www.aortarelease.nl/actor/lsp)" die aangeeft dat de ZIM dit security element verwerkt.

```
<soap:Header xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

  ...

  <wss:Security xmlns:wss=

    "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"

    soap:actor="http://www.aortarelease.nl/actor/zim" soap:mustUnderstand="1">

    <saml:Assertion ...>

     <saml:Issuer>SamlIssuer</saml:Issuer>




      <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">

        <ds:SignedInfo>

        ...

        </ds:SignedInfo>

        <ds:SignatureValue>Wuwn...5e4=</ds:SignatureValue>

        <ds:KeyInfo>

                   <ds:KeyName>e37ee2522de410c633b3700835727ebf1834cd88</ds:KeyName>          

        </ds:KeyInfo>

      </ds:Signature>

    ... Zie paragraaf 2.3 Inhoud ...

    </saml:Assertion ...>

  </wss:Security>

</soap:Header>

<soap:Body>

   ...

</soap:Body>
```
