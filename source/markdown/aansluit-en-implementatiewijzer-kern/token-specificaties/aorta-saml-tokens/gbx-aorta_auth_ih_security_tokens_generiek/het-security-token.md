[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBx AORTA_Auth_IH_Security_tokens_generiek](../gbx-aorta_auth_ih_security_tokens_generiek.md)

# Het security token

Dit hoofdstuk is niet normatief.   
Berichten die worden uitgewisseld binnen AORTA kunnen worden uitgerust met ondertekende security tokens om de integriteit, authenticiteit en onweerlegbaarheid ervan te waarborgen.   
Een security token is opgebouwd uit de volgende componenten:

- verzameling authentieke kenmerken met de daarbij behorende waarden,

- een digitale handtekening,

- randvoorwaarden zoals transformaties, matchingregels, certificaten, etc.

Een security token is niet op te stellen zonder de privé sleutel waarmee het security token wordt ondertekend.   
Een security token kan op verschillende manieren worden gebruikt:

- Het security token is aan één of door één entiteit uitgegeven (persoon, machine, etc.) en dient voor bepaalde (authenticatie, autorisatie of logging) doeleinden. Het security token bevat informatie over de afzender en bevat bepaalde kenmerken over een gegeven onderwerp.

- Het security token geeft het recht (autorisatie) om een bepaalde activiteit uit te voeren. Het security token wordt gekoppeld aan interacties.

Voor AORTA zijn voor de verschillende actoren (zorgverleners, patiënten, klantenloketmedewerkers, etc.) rollen gedefinieerd die bepaalde interacties kunnen uitvoeren. Voor elk van deze rollen zijn verschillende soorten tokens gedefinieerd waarmee een actor met een voorgedefinieerde rol voor verdere actie en afhandeling bij het landelijk schakelpunt kunnen aanmelden. De volgende soorten tokens worden binnen AORTA toegepast:

- Een authenticatietoken waarmee de identiteit van een persoon of object wordt vastgesteld en gekoppeld aan uitgewisselde gegevens ([IH BA Trans]);

- Een inschrijftoken waarmee gegarandeerd wordt dat een patiënt d.m.v. een gevalideerd BSN is ingeschreven bij een bepaalde zorgaanbieder door een specifieke medewerker ([IH Inschrijf]);

- Een mandaattoken waarmee een mandaterende zorgverlener een set gegevens elektronisch ondertekend om onweerlegbaar zijn autorisaties over te kunnen dragen aan een gemandateerde ([IH Man]).

Opbouw

Het security token bevat een aantal basiskenmerken en beveiligingsgerelateerde gegevens. Het security token inclusief digitale handtekening mag dan zonder de privé sleutel niet na te maken zijn, het is wel te kopiëren. Gekopieerde tokens kunnen opnieuw gebruikt of misbruikt worden voor andere acties. De volgende basiskenmerken en beveiligingsgerelateerde gegevens horen bij het security token:

- Uniekheid. Per toepassing moet aangegeven worden of het security token *mondiaal uniek* identificeerbaar moet zijn. Dit kan worden gerealiseerd door een nonce (**N**umber used **ONCE**) in het bericht te stoppen.

- Onderwerp. Het security token heeft een onderwerp waarover de uitgewisselde (beveiligingsgerelateerde) gegevens gaan. Het onderwerp wordt uniek geïdentificeerd en gebruikt bij dialogen tussen partijen (bijvoorbeeld: authenticiteit van een bericht vaststellen op basis van een bericht-id).

- Geldigheid. Elk security token voldoet aan bepaalde condities en geldigheidsvoorwaarden.

- Afzender. De afzender of leverende partij van het security token. Het token bevat een unieke identificatie van de afzender.

- Ontvanger. Afnemer of gebruiker van het security token. Het token bevat een unieke identificatie van de ontvanger. Het doel hiervan is dat de ontvanger de uniciteit van de nonce moet kunnen controleren en de mogelijkheid van hergebruik van een security token bij derden moet worden voorkomen. Echter bij ongeadresseerde verzendingen waarbij het security token wordt gebruikt, is de ontvanger niet bekend.

- Authenticatie. Geeft aan binnen welke authenticatie-context het security token gebruikt wordt als referentiekader voor communicatie tussen de afzender en de ontvanger van het token. De authenticatie-context kan informatie bevatten over de actuele authenticatie methode (bijvoorbeeld de "sterkte" van het gebruikte authenticatiemiddel).

- Middel waarmee het onderwerp in het security token is geauthenticeerd (SAML definieert de details van meer dan 20 verschillende authenticatie methodes).

- Attributen. Aanvullende (essentiële) attributen die een sterkere relatie leggen tussen het bericht en het security token.

Afhankelijk van het type security token, worden bovenstaande componenten in het security token impliciet dan wel expliciet vastgelegd. De componenten worden als aparte paragrafen per beveiligingsimplementatie handleiding verder uitgewerkt.
