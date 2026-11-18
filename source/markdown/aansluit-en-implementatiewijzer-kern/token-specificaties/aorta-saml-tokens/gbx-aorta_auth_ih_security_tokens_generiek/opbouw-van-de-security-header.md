[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBx AORTA_Auth_IH_Security_tokens_generiek](../gbx-aorta_auth_ih_security_tokens_generiek.md)

# Opbouw van de security header

WS-Security is een OASIS standaard en biedt een normatief raamwerk voor de beveiliging van het berichtenverkeer aan. Voor het toepassen van WS-Security, moet er een SOAP Header in de SOAP Envelope worden opgenomen. Deze SOAP Header omvat de WS-Security informatie en de XML Signature.

```
<soap:Envelope ...>
  <soap:Header ...>
    <wss:Security ...>
      <!-- Security header-->

      ...
    </wss:Security>
  </soap:Header >

  </soap:Body >

    <!--HL7v3 (payload)-->
    ...

  </soap:Body >
</soap:Envelope >
```

## Plaats van het security token

Voor ieder type security token bestaat er een aparte beveiligingsimplementatie handleiding in AORTA. Een dergelijke handleiding specificeert waar het security token in het bericht geplaatst wordt.

Zie de WS-Security profielen X.509 Certificaat Token en SAML Token.

```
<wss:Security ...>
  <wss:BinarySecurityToken>
    <!—X.509 certificaat als security token-->
  </wss:BinarySecurityToken >

  ...

  <saml:Assertion ...>
    <!— SAML Assertion als security token-->
  </saml:Assertion >
  ...
</wss:Security>
```

## Plaats van de digitale handtekening

Digitale handtekeningen worden in de WS-Security SOAP Header gezet. Eén of meerdere digitale handtekeningen kunnen onderdeel zijn van het security token.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Wanneer een bericht uitgerust is met een security token, *moet* dat bericht minimaal één bijbehorende digitale handtekening bevatten om de integriteit en de onweerlegbaarheid van het security token te waarborgen. ; |
| --- | --- |

```
<soap:Header ...>

  ...

  <wss:Security ...>

    <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">

      <ds:SignedInfo>

      ...

      </ds:SignedInfo>

      <ds:SignatureValue>Wuwn...5e4=</ds:SignatureValue>

      <ds:KeyInfo>

        ...

      </ds:KeyInfo>

    </ds:Signature>

  </wss:Security>

</soap:Header>
```
