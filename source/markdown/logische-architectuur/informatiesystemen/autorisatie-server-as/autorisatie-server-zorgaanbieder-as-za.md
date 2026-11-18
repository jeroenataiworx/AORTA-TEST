[AORTA 8.5.2](../../../index.md) / [Logische architectuur](../../../logische-architectuur.md) / [Informatiesystemen](../../informatiesystemen.md) / [Autorisatie Server (AS)](../autorisatie-server-as.md)

# Autorisatie Server Zorgaanbieder (AS ZA)

- De Autorisatie Server van Zorgaanbieder ondersteunt het verkrijgen of uitgeven van een AORTA access token (toegangstoken)

- De Autorisatie Server Zorgaanbieder ondersteunt het inwisselen van een Zorgaanbieder token (combinatie van transactie-, inschrijf- en eventueel mandaat token) voor een AORTA (JWT) access token (benodigd bij de Resource Broker Zorgaanbieder). Deze dienst zal slechts worden aangeroepen via de ZA-in component van de resource broker.

- De AORTA Token Interface is gebaseerd op [OAuth token exchange](https://tools.ietf.org/html/rfc8693)

{}De AORTA Token Interface is gebaseerd op [OAuth token exchange](https://tools.ietf.org/html/rfc8693).
