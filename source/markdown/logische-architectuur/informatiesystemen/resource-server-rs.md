[AORTA 8.5.2](../../index.md) / [Logische architectuur](../../logische-architectuur.md) / [Informatiesystemen](../informatiesystemen.md)

# Resource Server (RS)

De Resource Server (XIS) verleent alleen toegang tot patiëntgegevens, indien een vraag tot patiëntgegevens wordt begeleid met een geldig access (JWT) token met de juiste scope.

Naast het access token kan conditioneel ook door een initiërende partij een consent token meegestuurd worden. Een token dat wordt meegezonden is in sommige gevallen een XML SAMLv2 Assertion, en in andere situaties een JSON Web Token (JWT). In het token, dat wordt ontvangen in een "Authorization" HTTP header, is informatie opgenomen over welke type inhoudelijk token het betreft en welke versie, dus bijvoorbeeld dat het gaat om een AORTA access (JWT) token.

De Resource Server ondersteunt de standaard FHIR interacties zoals Read, Search, Create, Update, Batch, Transaction en een aangepaste FHIR operatie $is-allowed waarmee een resource client kan achterhalen of een zorgaanbieder bepaalde gegevens beschikbaar stelt of ontvankelijk is voor bepaalde gegevens.

Veder biedt de Resource Server een HL7v3 interface aan.
