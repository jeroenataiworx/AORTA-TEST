[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [AORTA_Auth_IH_Berichtauthenticatie_UZI](../aorta_auth_ih_berichtauthenticatie_uzi.md)

# Het SAML authenticatietoken Berichtauthenticatie UZI

In dit hoofdstuk wordt concreet de inhoud van het authenticatietoken besproken die bij berichtauthenticatie met behulp van de UZI-pas wordt gebruikt.

## Structuur

Het authenticatietoken die gebruikt wordt bij berichtauthenticatie met behulp van de UZI-pas voor het landelijk EPD heeft de volgende structuur:

```
<signedData xmlns="http://www.aortarelease.nl/805/"

  xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"

  wsu:Id="token_2.16.528.1.1007.3.3.1234567.1_0123456789">

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

## Namespaces

Het authenticatietoken die gebruikt wordt bij berichtauthenticatie met behulp van de UZI-pas maakt gebruik van de volgende namespaces. De prefixen zijn niet normatief maar worden in dit document als voorbeelden gebruikt.

Tabel AORTA.STK.t3200 – Namespaces

| **Prefix** ; | **Namespace URI** ; |
| --- | --- |
| **-** ; | [http://www.aortarelease.nl/805/](http://www.aortarelease.nl/805/) ; |
| **-** ; | [http://www.w3.org/2000/09/xmldsig#](http://www.w3.org/2000/09/xmldsig) ; |
| **soap** ; | [http://schemas.xmlsoap.org/soap/envelope/](http://schemas.xmlsoap.org/soap/envelope/) ; |
| **wsu** ; | [http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd](http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd) ; |

In de voorbeelden wordt voor de eenvoud gewerkt zonder namespace-prefixes, dus:

<signedData xmlns="[http://www.aortarelease.nl/805/](http://www.aortarelease.nl/805/)..."

in plaats van:

<ao:signedData xmlns:ao="[http://www.aortarelease.nl/805/](http://www.aortarelease.nl/805/)..."

Namespace prefixes mogen echter wel gebruikt worden, dus ontvangers moeten tokens met prefixes goed kunnen verwerken. Bij het gebruik van prefixes is het wel van belang deze na ondertekening niet meer te veranderen, dit maakt de digitale handtekening ongeldig.

```
<signedData xmlns="http://www.aortarelease.nl/805/"

  xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"

  wsu:Id="token_2.16.528.1.1007.3.3.1234567.1_0123456789">
```

Het token begint bij het <signedData> element. Het <signedData> element is geen HL7v3 element, maar gedefinieerd binnen deze specificatie.

De AORTA namespace "[http://www.aortarelease.nl/805/](http://www.aortarelease.nl/805/)" is verplicht en wordt als standaard namespace ingesteld voor de berichtauthenticatie met UZI-pas.

Een *Id* attribuut is verplicht (ook de hoofdletter I en kleine letter d). Voor het Id wordt de WS-Security 1.0 richtlijn van een Id in de wsu namespace gevolgd. De waarde van het wsu:Id attribuut moet uniek zijn in het hele XML bestand. De waarde moet *globaal uniek* zijn voor AORTA berichten, zodat bij samenvoegen van meerdere XML bestanden (in een HL7v3 batch of anderzins) de waarde uniek blijft.

## Inhoud

```
<authenticationData>
```

De volgende paragrafen beschrijven de verschillende basis kenmerken en beveiligingsgerelateerde gegevens die het authenticatietoken onderscheiden, zoals in [IH tokens generiek] beschreven is.

### Uniekheid

```
<messageId>

  <root>2.16.528.1.1007.3.3.1234567.1</root>

  <extension>0123456789</extension>

</messageId>
```

Een uniek gegeven, uitgegeven door de verzender van het bericht. Deze moet gelijk zijn aan het uiteindelijk gebruikte HL7v3 message.Id.

### Geldigheid

```
<notBefore>20070128173600</notBefore>
```

De tijd waarop het authenticatietoken geldig wordt. Dit hoeft niet de tijd te zijn waarop het bericht is aangemaakt. Vaak zal het complete bericht pas later aangemaakt worden. In principe is het mogelijk *notBefore* in de toekomst te zetten, en het bericht na deze tijd pas te verzenden. Wordt een bericht ontvangen voor *notBefore*is aangevangen, dan **moet** dit bericht geweigerd worden.

De tijd moet doorgegeven worden als Coordinated Universal Time (UTC), volgens de ook in HL7v3 gebruikte ISO 8601 notatie. Deze notatie is YYYYMMDDHHMMSS, bijvoorbeeld "20080225134130" zonder tussenvoegsels als "T", ":" etc. Er wordt geen gebruik gemaakt van timezones, dus "20080225134130+1" is niet toegestaan. De verzender en ontvanger zijn verantwoordelijk voor het eventueel converteren van lokale tijd naar UTC, en dus daarbij rekening houden met zomer- en wintertijd. De precisie is in seconden.

```
<notAfter>20070128174059</notAfter>
```

De tijd waarop het authenticatietoken vervalt. Wordt een bericht ontvangen nadat *notAfter*is verstreken, dan **moet** dit bericht geweigerd worden. Deze tijd is als bovenstaande tijd geformatteerd. Het aanbevolen verschil tussen *notBefore* en *notAfter* is 5 minuten. Het maximaal toegestane verschil is 90 minuten. Dit maximum dient voor berichten die niet direct, maar bijvoorbeeld 's nachts verzonden worden, of kort voor de aanvang van een consult, zodat er iets ruimere mogelijkheden voor batchgewijze processen zijn. Het wordt sterk aanbevolen dat voor berichten die direct verzonden worden (dus terwijl de zorgverlener of medewerker achter diens computer zit) niet afgeweken wordt van de periode van vijf minuten. Het gaat immers om het voorkomen van misbruik van onderschepte tokens, en vijf minuten is meer dan voldoende om de hele keten van vraag tot antwoord te doorlopen.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | De geldigheidsduur van een token (*notAfter* minus *notBefore*) mag niet langer dan 90 minuten zijn. Wordt een bericht ontvangen waarin deze maximale geldigheidsduur overschreden is, dan **moet** dat bericht geweigerd worden, ook al is het tijdstip notAfter nog niet verstreken. ; |
| --- | --- |

Richtlijn: de beste geldigheidsduur van een token (*notAfter* minus *notBefore*) voor online bevraging is 5 minuten.

### Ontvanger

```
<addressedParty>

  <root>2.16.840.1.113883.2.4.6.6</root>

  <extension>1</extension>

</addressedParty>
```

Het applicatie-id van het geadresseerde zorgsysteem, hier de ZIM. Het betreft hier het systeem waaraan het authenticatietoken gericht is; dat hoeft niet hetzelfde te zijn als het systeem waaraan het bericht zelf gericht is. De waarden in de elementen zijn (voorlopig) vaste waarden, omdat authenticatie alleen naar de ZIM geschiedt (behoudens testsituaties).

### Attributen

```
<coSignedData>
```

Met de authenticatie meegetekende gegevens uit het bericht. Dit zijn kopieën van gegevens die ook in het bericht voorkomen. Deze zijn vooral wenselijk omdat de authenticatiegegevens op zich niet verhinderen dat het token met een ander bericht (met gelijk message-Id) wordt gebruikt.

```
<triggerEventId>QURX_TE990011NL</triggerEventId>
```

Merk op dat het trigger event geen verplicht element in het HL7v3-bericht zelf is. Het wordt echter altijd opgenomen in het token, omdat bij elke interactie een trigger event gespecificeerd is. De Trigger Event identificeert het *berichttype* uniek, en bepaalt dus de intentie van de verzender. Deze meesturen verhindert veel soorten aanvallen, bijv. een authenticatie van een medicatiequery kapen en pogen deze te hergebruiken voor het opvragen van een waarneemdossier. Het is ook mogelijk de interactionId te gebruiken: deze wijzigt echter tussen versies van berichten, het triggerEventId niet, zodat een nieuwe versie van het bericht geen wijzigingen voor het token tot gevolg heeft. De Trigger Events zijn te vinden in het vocab bestand 2.16.840.1.113883.1.6.xml.

```
<contextCode>

      <codeSystem>2.16.840.1.113883.2.4.3.111.15.1</codeSystem>

      <code>KZDI</code>

</contextCode>
```

In het geval er sprake is van een opvraag op basis van een context dient ook de contextCode meegetekend te worden. Dit is in principe alleen het geval bij de generiekeQueryZorggegevens. Bij deze generieke query is het trigger event niet meer voldoende om de intentie van de verzender aan te geven, aangezien deze altijd gelijk is. Door het toevoegen van de contextCode wordt deze intentie wel weer expliciet gemaakt. De codes zijn te vinden in het vocab bestand 2.16.840.1.113883.2.4.3.111.15.1.xml.

```
<patientId>

  <root>2.16.840.1.113883.2.4.6.3</root>

  <extension>012345672</extension>

</patientId>
```

Voor berichten die betrekking hebben op een enkele patiënt, wordt het burgerservicenummer van de patiënt opgenomen. Dit maakt ook weer vele aanvallen onmogelijk, namelijk gegevens van een andere patiënt proberen op te vragen. Dit geldt voor alle berichten die betrekking hebben op één en niet meer dan één patiënt; ook als het burgerservicenummer niet voorkomt in het bijbehorende schema. Het burgerservicenummer is te vinden in het patientId met root 2.16.840.1.113883.2.4.6.3.

Voor berichten die geen betrekking hebben op een persoon wordt het BSN weggelaten. Het hele coSignedData blok ziet er dan zo uit:

```
<coSignedData>

  <triggerEventId>QURX_TE990011NL</triggerEventId>

</coSignedData>
```

Tenslotte wordt het token afgesloten.

```
</signedData>
```

## Algoritmes

Om de integriteit en onweerlegbaarheid van het authenticatietoken te waarborgen wordt een XML Signature geplaatst, zoals beschreven in [IH tokens generiek]. Na plaatsen van de XML Signature kan de ontvanger, met gebruikmaking van het persoonsgebonden UZI certificaat van de verzender, vaststellen dat het authenticatietoken ondertekend is met de privé sleutel behorend bij het gebruikte en meegezonden certificaat.

De XML Signature van het authenticatietoken die gebruikt wordt bij berichtauthenticatie met behulp van de UZI-pas maakt gebruik van de volgende algoritmes, zoals beschreven in [IH tokens generiek].

Voor het berekenen van de hashwaarde wordt SHA-256 gebruikt. Voor de digitale handtekening wordt RSA gebruikt.

## Opbouw

### De headers

Eerst wordt het token – het <signedData> element aangemaakt. Een voorbeeld:

```
<ao:authenticationTokens xmlns:ao="http://www.aortarelease.nl/805/" soap:actor="http://www.aortarelease.nl/actor/zim" soap:mustUnderstand="1">

  <signedData ...>

  ... Het eerder gedefinieerd signedData blok ...

  </signedData>

</ao:authenticationTokens>
```

Vervolgens moet het XML Signature blok in een WSS 1.0 SOAP Header opgenomen worden. Een voorbeeld:

```
<wss:Security xmlns:wss="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" soap:actor="http://www.aortarelease.nl/actor/zim" soap:mustUnderstand="1">

  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">

   <SignedInfo ...>

     ...

   </SignedInfo>

   <SignatureValue>

     ...

   </SignatureValue>

   <KeyInfo>

     ...

   </KeyInfo>

  </Signature>

</wss:Security>
```

Wanneer er met strings gewerkt wordt bij het zetten van de digitale handtekening, moet hier niet meer met de strings (signedData en SignedInfo) gemanipuleerd worden, maar ze moeten octet-voor-octet overgenomen worden in het bericht. Strikt genomen is het toegestaan wijzigingen aan te brengen die door canonicalisatie bij de ontvanger weer opgeheven worden, maar wanneer de digitale handtekening door middel van strings wordt opgebouwd, is het een foutgevoelige handeling.

Lange Base 64 waarden zijn afgekort. Wederom kan dit als strings worden behandeld, waarbij drie waarden vervangen moeten worden.

Deze drie waarden worden ingevuld:

- Neem het SignedInfo blok op.

- Neem de SignatureValue op.

- Neem certificaatgegevens in het KeyInfo blok op.

Canonicalisatie speelt alleen bij die XML code waarover een SHA digest wordt berekend of waarover RSA handtekeningen worden gezet. Het maken van de XML Signature uit strings levert dus twee blokken tekst op: de signedData en de Signature.

### Plaats van het token

Het authenticatietoken wordt opgenomen in een SOAP Header.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Voor authenticatie doeleinden mag er niet meer dan één authenticatietoken voorkomen. ; |
| --- | --- |

```
<soap:Header xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

  <ao:authenticationTokens xmlns:ao="http://www.aortarelease.nl/805/"

    soap:actor="http://www.aortarelease.nl/actor/zim" soap:mustUnderstand="1">

      <signedData xmlns="http://www.aortarelease.nl/805/" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" wsu:Id="token_2.16.528.1.1007.3.3.1234567.1_0123456789">

      <authenticationData>

        ...

      </authenticationData>

      <coSignedData>

        ...

      </coSignedData>

    </signedData>

  </ao:authenticationTokens>

     ...

</soap:Header>
```

Het token – het <signedData> element – wordt opgenomen in het <authenticationTokens> element van de <soap:Header>. Dit is voor het geval er (in de toekomst) meerdere authenticatietokens in een bericht zouden kunnen voorkomen. Op het <authenticationTokens> element **moet** een soap:mustUnderstand="1" vlag opgenomen worden, die aangeeft dat de ontvanger deze header **moet** verwerken. Bij het <authenticationTokens> element **mag**met een soap:actor="[http://www.aortarelease.nl/actor/zim](http://www.aortarelease.nl/actor/lsp)" worden aangegeven dat de ZIM deze header verwerkt.

Het declareren van de namespace "[http://www.aortarelease.nl/805/](http://www.aortarelease.nl/805/)" bij <signedData> is niet nodig: deze wordt overgeërfd van het bovenliggende element. Bij canonicalisatie zal bij de ontvanger de namespace teruggeplaatst worden voor controle van de digitale handtekening. Voor de duidelijkheid is de namespace declaratie hier tweemaal opgenomen.

### Plaats van de digitale handtekening

De digitale handtekening wordt in een WS-Security 1.0 SOAP Header gezet. Op het <wss:Security> element **moet** een soap:mustUnderstand="1" vlag opgenomen worden, die aangeeft dat de ontvanger dit security element **moet** verwerken. Bij het <authenticationTokens> element **mag**met een soap:actor="[http://www.aortarelease.nl/actor/zim](http://www.aortarelease.nl/actor/lsp)" worden aangegeven dat de ZIM dit security element verwerkt.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Wanneer een bericht een authenticatietoken bevat, moet dat bericht precies één bijbehorende digitale handtekening bevatten. ; |
| --- | --- |

De volgorde van beide headers (authenticatietoken en digitale handtekening) is niet relevant: zowel digitale handtekening vóór het token als token vóór de digitale handtekening zijn geldig.

```
<soap:Header xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

  ...

  <wss:Security xmlns:wss=

    "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"

    soap:actor="http://www.aortarelease.nl/actor/zim" soap:mustUnderstand="1">

    <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">

      <SignedInfo xmlns="http://www.w3.org/2000/09/xmldsig#">

      ...

      </SignedInfo>

      <SignatureValue>...</SignatureValue>

      <KeyInfo>

        <X509Data>

        ...

        </X509Data>

      </KeyInfo>

    </Signature>

  </wss:Security>

</soap:Header>
```
