[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBx AORTA_Auth_IH_Security_tokens_generiek](../gbx-aorta_auth_ih_security_tokens_generiek.md)

# Afhandeling van het security token

## Bestemming en verwerking

WS-Security informatie kan voor verschillende bestemmingen (GBx’en en ZIM) bedoeld zijn. In [IH Transport] wordt uitleg gegeven over het gebruik van de bestemming en verwerking attributen. In [IH Transport] wordt aangegeven welke soap:actor attributen gebruikt moeten worden per bestemming.

Het volgende blok is een implementatievoorbeeld van de bestemming en verwerking van WS-Security.

```
<soap:Header ...>

  ...

  <wss:Security xmlns:wss=

    "http://docs.oasis-open.org/wss/oasis-wss-wssecurity-secext-1.1.xsd"

    soap:actor="http://www.aortarelease.nl/actor/zim" soap:mustUnderstand="1">

    ...

  </wss:Security>

</soap:Header>
```

Er is één WS-Security header per bestemming. Er zijn dus maximaal twee WS-Security headers: één voor de ZIM, één voor het GBx. Een security header kan meer dan één security token bevatten. De security header gericht aan de ZIM wordt bij voorkeur vóór de security header van een GBZ geplaatst; daarmee kunnen ze verwerkt worden in de volgorde waarin ze nodig zijn.

## Verificatie en controle

In de verschillende beveiligingsimplementatie handleidingen in AORTA en in

[IH Transport] worden aanvullende voorwaarden gesteld i.h.k.v. verificatie en controle.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | De WBSN-z regelt dat voor berichten die betrekking hebben op een persoon waarvan het burgerservicenummer (BSN) bekend is, het BSN als gegeven in het security token op te nemen. ; |
| --- | --- |

Bij ontvangst van het security token dient de ontvanger de volgende controles uit te voeren:

- voldoet de XML Signature aan de eisen die er in [XMLSIG] aan gesteld worden;

- voldoet het security token aan de eisen die er in dit document aan gesteld worden;

- valideert de signature over het security token conform de eisen die er in dit document aan gesteld worden;

- is het gebruikte certificaat correct getekend, evenals de certificaten tot een vertrouwd certificaat;

- is het gebruikte certificaat geldig, niet verlopen en niet ingetrokken;

- als het gebruikte certificaat afkomstig is van "ZORG-ID Token CA" dan controle uitvoeren van de proof-extensie in het certificaat of deze overeenkomen met de verwachte waarden.

- is er een match tussen het bericht en de claims in het security token conform de eisen die de (zorg)toepassing daaraan stelt.

Indien één van de controles niet bevestigd wordt, wordt een SOAP fout gegenereerd, zie [paragraaf 6.3](https://vzvz.atlassian.net/wiki/spaces/AORTA84/pages/879593320/Afhandeling+van+het+security+token#Afhandelingvanhetsecuritytoken-Foutafhandeling) Foutafhandeling. Indien een SOAP fout wordt gegenereerd *mag* het bericht door de ontvangende partij verder verwerkt worden wanneer de betreffende toepassing dat vereist.

## Foutafhandeling

De volgende SOAP fouten zijn van toepassing bij security tokens. Op de eerste SOAP foutmelding na, zijn ze onderdeel van WS-Security.

**Tabel AORTA.STK.t3150**

| **Omschrijving (faultstring)** ; | **Faultcode** ; |
| --- | --- |
| **Er is een (WS-Security) header aanwezig die niet bekend is, maar met mustUnderstand = "1". In dit geval moet deze Fault gegenereerd worden.** ; | soap:MustUnderstand ; |
| **An unsupported token was provided** ; | wss:UnsupportedSecurityToken ; |
| **An unsupported signature or encryption algorithm was used** ; | wss:UnsupportedAlgorithm ; |
| **An error was discovered processing the <wss:Security> header** ; | wss:InvalidSecurity ; |
| **An invalid security token was provided** ; | wss:InvalidSecurityToken ; |
| **The security token could not be authenticated or authorized** ; | wss:FailedAuthentication ; |
| **The signature or decryption was invalid** ; | wss:FailedCheck ; |
| **Referenced security token could not be retrieved** ; | wss:SecurityTokenUnavailable ; |
| **The message has expired** ; | wss:MessageExpired ; |

De volgende foutmeldingen worden daar aan toegevoegd.

**Tabel AORTA.STK.t3160**

| **Omschrijving (faultstring)** ; | **Faultcode** ; |
| --- | --- |
| Authenticatietoken en bericht stemmen niet overeen ; | ao:AuthTokenMessageMismatch ; |
| Authenticatietoken is niet valide of compleet ; | ao:AuthTokenInvalid ; |
| Authenticatietoken buiten geldigheidsduur ontvangen ; | ao:ExpirationTimeError ; |
| Nonce is reeds gebruikt ; | ao:NonceRejected ; |
| Proof Extension Invalid ; | ao:ProofInvalid ; |

De volgende statuscodes (URI referenties) worden door SAML onderkend en geretourneerd [SAML Core].

Een statuscode is een Uniforme Resource Name (URN) en is als volgt opgebouwd:

"urn:"<Namespace Identifier>":"<Name Specific String>

Voorbeeld:

"urn:oasis:names:tc:SAML:2.0:status:Success"

In de <statuscode> tabel AORTA.STK.t3170 wordt alleen de omschrijving en de specifieke string (<Name Specific String>) getoond. <StatusDetail> kan daarnaast gebruikt worden om een specifieke leesbare melding te retourneren (zie [SAML Core]).

**Tabel AORTA.STK.t3170**

| **Omschrijving** ; | **Name Specific String** ; |
| --- | --- |
| **The request could not be performed due to an error on the part of the requester.** ; | Requester ; |
| **The request could not be performed due to an error on the part of the SAML responder or SAML** ; | Responder ; |
| **The SAML responder could not process the request because the version of the request message was incorrect.** ; | VersionMismatch ; |
| **The responding provider was unable to successfully authenticate the principal.** ; | AuthnFailed ; |
| **The specified authentication context requirements cannot be met by the responder.** ; | NoAuthnContext ; |
| **The SAML responder or SAML authority is able to process the request but has chosen not to respond.** ; | RequestDenied ; |
| **The SAML responder or SAML authority does not support the request.** ; | RequestUnsupported ; |
| **The SAML responder cannot process any requests with the protocol version specified in the request.** ; | RequestVersionDeprecated ; |
| **The SAML responder cannot process the request because the protocol version specified in the request message is a major upgrade from the highest protocol version supported by the responder.** ; | RequestVersionTooHigh ; |
| **The SAML responder cannot process the request because the protocol version specified in the request message is too low.** ; | RequestVersionTooLow ; |
| **The resource value provided in the request message is invalid or unrecognized.** ; | ResourceNotRecognized ; |
| **The response message would contain more elements than the SAML responder is able to return.** ; | TooManyResponses ; |
| **The responding provider does not recognize the principal specified or implied by the request.** ; | UnknownPrincipal ; |
| **The SAML responder cannot properly fulfill the request using the protocol binding specified in the request.** ; | UnsupportedBinding ; |

## Loggen

Per security token wordt bepaald wat er gelogd moet worden door het LSP. Dit is opgenomen in de IH's van de verschillende tokens. In ieder geval dient van elk op het LSP binnenkomend token die getekend is door een PKI(o) certificaat, het certifcaatID van hetPKI(o) certificaat gelogd te worden.
