[AORTA 8.5.2](../../index.md) / [Logische architectuur](../../logische-architectuur.md) / [Informatiesystemen](../informatiesystemen.md)

# Autorisatie Server (AS)

De Autorisatie Server (AS) implementeert specificaties van OAuth2 om toepassingen toegang te geven tot de interfaces van de Resource Broker (RB) of Resource Server (RS). Dit in overeenstemming met de toegangsregels zoals opgenomen in de diverse autorisatierichtlijnen van de op AORTA geïmplementeerde zorgtoepassingen en indien van toepassing de patiënttoestemming zoals opgenomen in Mitz.

De metadata, dat benaderbaar is via het publieke internet, van de Autorisatie Server kan, conform [RFC 8414](https://tools.ietf.org/html/rfc8414), worden opgehaald op een well-known URL die kan worden geconstrueerd m.b.v. de <iss> claim uit het token (zie ook [section-3.1 van RFC8414](https://datatracker.ietf.org/doc/html/rfc8414#section-3.1)).
