[AORTA 8.5.2](../../index.md) / [Processen](../../processen.md) / [Vereenvoudigd gebruik UZI-pas (VGU)](../vereenvoudigd-gebruik-uzi-pas-vgu.md)

# Vereenvoudigd proces UZI-pas

## Probleem

Het gebruik van de UZI-pas leidt in sommige zorgprocessen tot vertragingen en vanuit informatiebeveiligingsoogpunt tot onveilige werksituaties als gevolg van onjuist gebruik. Uit verschillende reacties van leveranciers, zorgverleners en andere betrokkenen is dan ook de wens gekomen om de werkwijze met de UZI-pas te herzien. Met name binnen ziekenhuizen en zorgbehandelcentra is gebleken dat de werkwijze m.b.t. de UZI-pas niet aansluit bij de zorgprocessen; men wil patiëntinformatie reeds opgevraagd hebben voordat de patiënt langs komt voor behandeling (het zogenaamde 'prefetching').  
Binnen AORTA is een oplossing geïntroduceerd waardoor het gebruik van de UZI-pas sterk vereenvoudigd kan worden. Het gaat hierbij om een generieke oplossing die het werkproces van een zorgaanbieder kan ondersteunen. Het werkproces kan binnen een zorgtoepassing en zelfs per instelling sterk verschillen. Het is dus aan een individuele instelling om te bepalen hoe men gebruik wil maken van de oplossing zoals binnen AORTA is opgenomen.

## Generieke oplossing

Met de generieke oplossing is het mogelijk om vooraf een aantal waarborgen af te geven, waarmee een zorgverlener op het moment van het versturen van een bericht (bijvoorbeeld een bevraging van patiëntgegevens, het versturen van patiëntgegevens of het afsluiten van een abonnement) geen UZI-pas meer nodig heeft. Het wordt mogelijk om op basis van bepaalde triggers het systeem berichten te laten versturen.

### Tokens

Voor interactie met het LSP zonder het gebruik van de UZI-pas op het moment van de interactie worden er drie verschillende waarborgen onderscheiden. Deze waarborgen komen in de vorm van zogenaamde tokens en moeten worden meegestuurd met een interactie Het selecteren en toevoegen van de tokens is niet een handeling dat een zorgverlener hoeft uit te voeren. Dit zal geautomatiseerd door de XIS-applicatie aan een uitgaande interactie worden toegevoegd. . Elk token staat voor een ander waarborg en kunnen op verschillende momenten in de tijd worden aangemaakt. De combinatie van waarborgen zorgen voor een vergelijkbaar beveiligingsniveau als een interactie verstuurt met een UZI-pas.   
Met het **inschrijftoken** wordt gewaarborgd dat een patiënt is ingeschreven bij een organisatie. Van een ingeschreven patiënt dient een token te worden gegenereerd door middel van het gebruik van een UZI-pas. Een technische beschrijving van het inschrijftoken is opgenomen in de IH Inschrijftoken.  
Een verantwoordelijke zorgverlener geeft in een **mandaattoken** aan welke zorgverleners of onder welke omstandigheden het systeem onder zijn verantwoordelijkheid een interactie mag versturen. Een technische beschrijving van het mandaattoken is opgenomen in de IH Mandaattoken.  
Het **transactietoken** is een waarborg dat wordt aangemaakt door het systeem op het moment van uitsturen van een bericht. Het transactietoken waarborgt dat een interactie met betrekking tot een specifieke patiënt wordt verstuurd onder verantwoordelijkheid van een verantwoordelijke zorgverlener. Het transactietoken koppelt het inschrijftoken, het mandaattoken en het uit te sturen bericht aan elkaar. Een gebruiker van het systeem heeft geen weet van het transactietoken. Het genereren van het transactietoken wordt gedaan door het systeem met behulp van het UZI-servercertificaat. Een technische beschrijving van het transactietoken is opgenomen in de IH Transactietoken.

### Triggers

Een XIS-applicatie kan Indien een zorgverlener via het mandaattoken toestemming heeft gegeven om het systeem onder zijn verantwoordelijkheid te laten opvragen. op basis van verschillende triggers een bericht uitsturen met betrekking tot een specifieke patiënt. Deze triggers zijn niet vast voor gedefinieerd, maar kunnen verschillen per zorgtoepassingen en/of per werkproces. Voorbeelden van triggers zijn:

- Het ontvangen van een signaal als gevolg van een afgenomen abonnement; een zorgaanbieder heeft nieuwe informatie beschikbaar gesteld via het LSP en het LSP stuurt een signaal naar alle abonneehouders.

- Een agenda-afspraak met een patiënt; een patiënt heeft die dag een afspraak en het systeem krijgt hiermee het verzoek om de patiëntgegevens van die patiënt op te vragen.

- Een bepaalde tijdsperiode; elke eerste van de maand bevraagt het systeem bepaalde gegevens t.b.v. bijvoorbeeld een bewakings- of rapportageproces.

- Het openen van een dossier; een geautoriseerde zorgverlener opent een dossier van een patiënt en het systeem zorgt ervoor dat de zorgverlener de meest actuele gegevens opgeleverd krijgt door alle nieuwe informatie op te vragen.

- Een handeling door een daarvoor geautoriseerde gebruiker; een zorgverlener kan het systeem actief opdracht geven om een bevraging te doen m.b.t. een specifieke patiënt.

Het is mogelijk dat een XIS-applicatie meerdere triggers ondersteunt. Binnen een zorgtoepassing zal worden bepaald welke triggers van belang zijn en welke potentiële eisen er gelden m.b.t. deze triggers. Op verzoek van een XIS-leverancier kan in overleg met VZVZ worden nagedacht over mogelijke andere triggers. Deze zullen echter altijd in een zorgtoepassing opgenomen moeten worden en een XIS zal altijd moeten worden geaccepteerd voor deze nieuwe trigger. Het kan dus voor een zorgaanbieder interessant zijn om met zijn XIS-leverancier in gesprek te gaan over de implementatie van VGU in de diverse werkprocessen.
