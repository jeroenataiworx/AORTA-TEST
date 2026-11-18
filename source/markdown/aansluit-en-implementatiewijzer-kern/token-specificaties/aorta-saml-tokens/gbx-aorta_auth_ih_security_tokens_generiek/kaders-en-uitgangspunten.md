[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBx AORTA_Auth_IH_Security_tokens_generiek](../gbx-aorta_auth_ih_security_tokens_generiek.md)

# Kaders en uitgangspunten

## Externe normen en kaders

Op het gebied van beveiliging in de zorg zijn verschillende normen en wetten van kracht, zowel op Europees als Nederlands niveau. De NEN 7510-norm is de Nederlandse norm voor informatiebeveiliging in de zorg en is van toepassing op alle zorgaanbieders.   
Bij de uitwisseling van informatie in de zorg speelt de wetgeving een belangrijke rol. Een uitgebreide behandeling hiervan valt buiten de reikwijdte van dit document, echter de Wet gebruik burgerservicenummer in de zorg (Wbsn-z) wordt hier kort benoemd.   
De Wbsn-z (sinds 2008) regelt dat in alle berichtgevingen tussen zorgaanbieders onderling het *burgerservicenummer* (BSN) aanwezig **moet** zijn om persoonsverwisseling en daardoor medische fouten te voorkomen. Een burgerservicenummer mag door de zorgaanbieder worden geregistreerd nadat de betrokkene zich heeft gelegitimeerd met een wettelijk identificatiedocument.

## Relatie met AORTA-principes en –beslissingen

In dit hoofdstuk worden de architectuurprincipes weergegeven waaraan de AORTA-document moet voldoen.   
Architectuurprincipe AORTA.ALG.p1010: aan aangesloten zorgsystemen worden uitsluitend eisen gesteld die noodzakelijk zijn voor veilige gestandaardiseerde uitwisseling van gegevens.   
Architectuurprincipe AORTA.ALG.p1020: voor toegang tot patiëntgegevens moeten zorgverleners persoonlijk worden *geïdentificeerd* en *geauthenticeerd*

## Namespaces

Wanneer in dit document in voorbeeld fragmenten niet gedeclareerde namespace prefixes worden gebruikt, worden de volgende namespaces bedoeld.

| **Prefix** ; | **Namespace URI** ; |
| --- | --- |
| **ao** ; | http://www.aortarelease.nl/805/ ; |
| **ds** ; | http://www.w3.org/2000/09/xmldsig# ; |
| **soap** ; | http://schemas.xmlsoap.org/soap/envelope/ ; |
| **wsu** ; | http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd ; |
| **wss** ; | "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" ; |
| **saml** ; | urn:oasis:names:tc:SAML:2.0:assertion ; |

## Namespaces

De volgende namespaces worden gebruikt in de security header. De prefixen zijn niet normatief maar worden in dit document als voorbeelden gebruikt.   
**Tabel AORTA.STK.t3140 - Namespaces**

| **Prefix** ; | **Namespace URI** ; |
| --- | --- |
| **soap** ; | http://schemas.xmlsoap.org/soap/envelope/ ; |
| **ds** ; | http://www.w3.org/2000/09/xmldsig# ; |
| **saml** ; | urn:oasis:names:tc:SAML:2.0:assertion ; |
| **wss** ; | [http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd](http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd) ; |
| **ao** ; | http://www.aortarelease.nl/805/ ; |

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | In XML mag een prefix veranderd worden (mits consequent toegepast). Na ondertekening kan dit echter niet meer, dit zou de handtekening ongeldig maken. ; |
| --- | --- |
