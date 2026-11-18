[AORTA 8.5.2](../index.md) / [Processen](../processen.md)

# Abonnement- en signaalfunctie

De abonnement‑ en signaalfunctie is bedoeld voor situaties waarin zorgverleners actief over een actueel medisch dossier willen beschikken. De wijze waarop de abonnement- en signaalfunctie wordt ingericht is afhankelijk van de zorgtoepassing, sector-specifieke keuzes en de wijze waarop de leverancier van het informatiesysteem de functionaliteit heeft ingezet en ingericht. In onderstaande documentatie wordt de generieke werking beschreven.

## Gebruik abonnement

### Registreren abonnement

Een zorgverlener kan met een systeem een abonnement registreren voor het verkrijgen van een signaal indien er nieuwe gegevens beschikbaar worden gesteld van een specifieke patiënt. Hiervoor dient het systeem onder verantwoordelijkheid van een zorgverlener een ‘Registreren abonnement’-bericht te versturen. Dit kan geïnitieerd worden door:

- een zorgverlener zelf op basis van zijn UZI-pas of ZORG-ID Smart;

- een medewerker die onder mandaat werkt van de betreffende zorgverlener;

- Vereenvoudigd gebruik UZI-pas (VGU) in combinatie met een mandaattoken getekend door de verantwoordelijke zorgverlener.

Een abonnement wordt centraal in het abonnementenregister geregistreerd op basis van de unieke combinatie van:

- PatiëntID;

- Contextcode of gegevenssoort;

- ApplicatieID;

- Organisatie;

- Gebeurtenistype (dit zal altijd betrekking hebben op een wijziging in de verwijsindex).

- Rolcode

De precieze invulling van het ‘Registreren abonnement’-bericht is opgenomen in DECOR informatie voor project: [DECOR informatie voor project: AORTA (aorta-vzvz-) (nictiz.nl)](https://decor.nictiz.nl/pub/vzvz/index.php?prefix=aorta-vzvz-). Hierbij is in ieder geval de geldigheidsduur van het abonnement verplicht. Een abonnement mag niet langer geldig zijn dan 1,5 jaar. Indien dit wel het geval is, wordt dit abonnement afgewezen en wordt een foutmelding geretourneerd.  
Daarnaast dient het abonnement lokaal in het systeem geregistreerd te worden, zodat functionaliteiten als verlengen en beëindigen van het abonnement mogelijk worden.

#### Registreren abonnement o.b.v. VGU-functionaliteit

Met gebruik van de VGU-functionaliteit is het mogelijk om automatisch een abonnement af te sluiten op basis van een bepaalde trigger. Voorbeelden van triggers:

- Er wordt een behandelrelatie geregistreerd voor een patiënt;

- Een zorgverlener sluit zelf expliciet een abonnement af;

- Een zorgverlener geeft aan medicatiebewaking te willen doen voor een patiënt.

Voor het afsluiten van een abonnement op basis van de VGU-functionaliteit zijn een aantal randvoorwaarden van toepassing:

- Er dient een inschrijftoken aanwezig te zijn van de patiënt van wie een abonnement afgesloten dient te worden;

- Er dient een behandelrelatie te zijn tussen de abonneenemer en de patiënt op het moment van afsluiten van een abonnement;

- Er dient een mandaattoken te zijn van de abonneenemer t.b.v. de VGU-functionaliteit;

- Een zorgverlener dient de juiste autorisaties te hebben om een abonnement te mogen afsluiten.

Autorisaties worden centraal bepaald op basis van de rolcode van een zorgverlener, de contextcode (in het geval van een bevraging) en interactieID. Elke rolcode kan in theorie andere autorisaties kennen voor een bevraging van een specifieke contextcode of een andere invulling van de te bevragen medische gegevens (conform de Selectie en Determinatie tabel).

#### Toepassingen voor registreren abonnement

Er zijn verschillende toepassingen voor gebruik van de signaalfunctie:

- Medicatiebewaking;

- Vereenvoudigd gebruik UZI-pas (VGU);

- Bepalen actualiteit van gegevens.

Ten behoeve van medicatiebewaking is het van belang om een signaal te krijgen indien er een aanpassing is geweest in de medicatiegegevens van een patiënt die onder medicatiebewaking staat. Het ontvangen van een signaal dient te leiden tot een expliciet signaal aan de abonnementhouder.

Indien een abonnement wordt afgesloten om de VGU-functionaliteit te ondersteunen, dan zal het signaal een trigger zijn voor automatische bevraging,

Het is mogelijk om aan de hand van de signaalfunctie lokaal vast te stellen of er nieuwe gegevens zijn van een bepaalde patiënt. Hierbij hoeft een zorgverlener dus alleen zijn UZI-pas (het gebruik van de UZI-pas kan geautomatiseerd worden i.c.m. de VGU-functionaliteit) te gebruiken indien er eerder al een signaal is ontvangen.

#### Aandachtspunten m.b.t. registreren abonnement

Een abonnement wordt niet afgesloten op basis van een specifieke zorgverlener en diens rol, maar op basis van een zorgaanbieder (o.b.v. applicatieID). Echter, het ‘Registreren abonnement’-bericht wordt wel geautoriseerd op basis van de autorisatie van de zorgverlener, die verantwoordelijk is voor het versturen van het ‘Registreren abonnement’-bericht (het versturen van het ‘Registreren abonnement’-bericht kan ook onder mandaat gebeuren). Autorisatie gebeurt op basis van rolcode en contextcode.

Deze rolcode bepaalt welke signalen het systeem ontvangt. Als systeem kun je maar één abonnement nemen op een patiënt voor een bepaalde contextcode en rolcode. Het is dus van belang dat nagedacht wordt onder wiens verantwoordelijkheid een abonnement wordt afgesloten. Daarom moet ook in het lokale systeem het abonnement geregistreerd worden, waarbij in ieder geval de ingangsdatum van het abonnement dient te worden bijgehouden. Een abonnement mag niet langer dan 1,5 jaar geldig zijn. Dit moet lokaal worden bijgehouden (kunnen meerdere zorgverleners zijn), zodat bijvoorbeeld bij einde dienstverband duidelijk is of een abonnement nog geldig is of dat er een nieuw abonnement moet worden genomen. Uiteraard zal ook lokaal de behandelrelatie gecontroleerd moeten worden.

### Verlengen Abonnement

Zoals aangegeven heeft een geregistreerd abonnement een beperkte geldigheidsduur van maximaal 1,5 jaar. Indien gewenst door een zorgverlener, dan dient dit abonnement te worden verlengd. Hiervoor kan het systeem onder verantwoordelijkheid van een zorgverlener een ‘Registreren abonnement’-bericht versturen. Dit kan geïnitieerd worden door:

- een zorgverlener op basis van zijn UZI-pas;

- een medewerker met UZI-pas die onder mandaat werkt van de betreffende zorgverlener;

- Vereenvoudigd gebruik UZI-pas (VGU) in combinatie met een mandaattoken getekend door de verantwoordelijke zorgverlener.

De zorgverlener onder wiens verantwoordelijkheid het abonnement verlengd wordt, hoeft niet dezelfde zorgverlener te zijn onder wiens verantwoordelijkheid het abonnement initieel is genomen.

Voor het verlengen van het abonnement wordt hetzelfde bericht gebruikt als voor het afsluiten van het abonnement. Indien het AORTA abonnementenregister een ‘Registreren abonnement’-bericht ontvangt met een reeds bestaande combinatie van patiëntID, Contextcode/Gegevenssoort, Rolcode, Gebeurtenistype en applicatieID, dan zal de geldigheidsduur in het AORTA abonnementenregister worden bijgewerkt op basis van de geldigheidsduur zoals opgenomen in het ‘Registreren abonnement’-bericht.

Er zijn geen voorschriften over hoe de momenten van verlengen dienen te worden gekozen. Wel zijn hiervoor Best Practices opgenomen.

#### Aandachtspunten m.b.t. verlengen abonnement

In het geval een abonnement wordt verlengd door middel van VGU, dan dienen er nog wel geldige tokens t.b.v. de VGU aanwezig zijn. Daarnaast dient nog steeds sprake van een behandelrelatie te zijn.

Indien een abonnement niet verlengd wordt, dient dit abonnement te worden verwijderd, zowel lokaal als in het abonnementenregister.

## Verwijderen Abonnement

Een verlopen abonnement zal na het verstrijken van de geldigheidsduur niet automatisch verwijderd worden uit het abonnementenregister. Een gebruiker is zelf verantwoordelijk voor het verwijderen van een abonnement. Hiervoor dient het systeem onder verantwoordelijkheid van een zorgverlener een ‘Opzeggen abonnement’-bericht te versturen. Dit kan geïnitieerd worden door:

- De abonneehouder zelf op basis van zijn UZI-pas;

- Een zorgverlener op basis van zijn UZI-pas met de juiste autorisaties (die hoeft dus niet de abonneehouder te zijn);

- Een medewerker met UZI-pas die onder mandaat werkt van de betreffende zorgverlener of abonneehouder;

- Vereenvoudigd gebruik UZI-pas (VGU) in combinatie met een mandaattoken getekend door een abonneehouder of een zorgverlener met de juiste autorisaties.

Het verwijderen van een abonnement gebeurt op basis van het abonnementID dat door het systeem is verkregen na het registreren van een abonnement. Bij verwijdering uit het abonnementenregister wordt gecontroleerd of de zorgverlener (rolcode) geautoriseerd is om een abonnement te verwijderen.

De precieze invulling van het ‘Opzeggen abonnement’-bericht is opgenomen in [DECOR informatie voor project: AORTA (aorta-vzvz-) (nictiz.nl)](https://decor.nictiz.nl/pub/vzvz/index.php?prefix=aorta-vzvz-).

#### Aandachtspunten m.b.t. verwijderen abonnement

Het verwijderen van een abonnement is niet evident:

- Er kunnen meerdere zorgverleners gebruik maken van één afgesloten abonnement, nl. zorgverleners met dezelfde rolcode;

- Een abonnement is afgesloten door een zorgverlener t.b.v. VGU.

Voordat een abonnement wordt verwijderd, dient dus met zekerheid te worden vastgesteld, dat het verwijderen van het abonnement géén impact heeft op het zorgproces.

Het abonnement dient zowel lokaal als uit het abonnementenregister verwijderd te worden. Lokaal mag er dan niet ook nog eenzelfde abonnement bij een andere zorgverlener bestaan. Er kunnen lokaal meerdere abonneehouders lokaal geregistreerd staan, die gebruik maken van hetzelfde abonnement. Voordat de applicatie een abonnement daadwerkelijk centraal laat verwijderen, dient er gecontroleerd te worden of er lokaal nog andere abonneehouders zijn, die gebruik maken van het abonnement. Indien dat het geval is, dan dient het abonnement centraal niet verwijderd te worden. Het verwijderen van een abonnement binnen een organisatie kan alleen als er geen abonneehouder meer is voor de combinatie patiënt, gegevenssoort/contextcode en applicatieID, rolcode of zorgverlener-ID.

In het geval een zorgaanbiederorganisatie gebruik maakt van VGU in combinatie met de signaalfunctie als trigger, dan is het aannemelijk dat er een abonnement staat geregistreerd voor elke patiënt waarvan een behandelrelatie staat geregistreerd. Van die patiënten dient dus goed overwogen te worden of een abonnement verlengd dient te worden i.p.v. verwijderd.

In het geval de signaalfunctie wordt toegepast t.b.v. de medicatiebewaking van een patiënt, dan dient er altijd een abonnement op aanpassingen van medicatiegegevens van die specifieke patiënt te zijn geregistreerd. Een abonnement zal in dit geval pas verwijderd worden indien de medicatiebewaking wordt gestopt.

## Synchronisatie met Abonnementenregister

Om te voorkomen dat de lokale abonnementenregistratie uit de pas loopt met de AORTA abonnementenregistratie, is het van belang dat er een synchronisatieproces wordt geïmplementeerd. Hiervoor wordt hetzelfde mechanisme zoals is geïntroduceerd voor de VWI-synchronisatie toegepast. De definitieve uitwerking hiervan volgt.

## Lokaal abonnementenregister

Het lokale abonnementenregister moet de systeemgebruiker inzichtelijk maken wie welke abonnementen op welke patiënten heeft afgesloten voor welke gegevens. Daarnaast dient de geldigheidsduur van het abonnement te worden bijgehouden.

| **Attribuut** ; | **Beschrijving** ; | **Cardinaliteit** ; |
| --- | --- | --- |
| **AbonnementID** ; | Het abonnementID dat is verkregen na het afsluiten van een abonnement ; | 1..1 ; |
| **PatiëntID** ; | De identifier (BSN) van de patiënt waarop een abonnement is genomen. ; | 1..1 ; |
| **Context**[**[1]**](abonnement-en-signaalfunctie.md) ; | De context waarvoor een abonnement is afgesloten. ; | 1..1 ; |
| **Gegevenssoort**[**[2]**](abonnement-en-signaalfunctie.md) ; | De gegevenssoort waarvoor een abonnement is afgesloten ; | 0 .. 1 ; |
| **Abonneehouder** ; | De abonneehouder die lokaal een abonnement heeft afgesloten. Dit omvat een abonneehouderID en afhankelijk van het XIS-type de rolcode van de betreffende abonneehouder[[3]](abonnement-en-signaalfunctie.md). ; | 1..* ; |
| **ApplicatieID** ; | ApplicatieID waarvoor een abonnement is afgesloten ; | 0 .. 1 ; |
| **Geldigheidsduur** ; | Geldigheidsduur van een abonnement ; | 1 .. 1 ; |

[[1]](abonnement-en-signaalfunctie.md) Verplicht aanwezig indien hier ook daadwerkelijk een abonnement op is afgesloten.

[[2]](abonnement-en-signaalfunctie.md) Optioneel aanwezig indien hier ook daadwerkelijk een abonnement op is afgesloten.

[[3]](abonnement-en-signaalfunctie.md) Het opnemen van een rolcode staat verder uitgewerkt in het hoofdstuk voor het opvragen n.a.v. een signaal.

## Afhandelen signalen

### Ontvangen signalen

Een signaal als gevolg van een abonnement bevat de volgende attributen die van belang zijn voor de verwerking van het signaal:

- PatiëntID;

- Gegevenssoort of bouwsteentype;

- AbonnementID.

De precieze invulling van het ‘afleveren abonnementsignaal’-bericht is opgenomen in [DECOR informatie voor project: AORTA (aorta-vzvz-) (nictiz.nl)](https://decor.nictiz.nl/pub/vzvz/index.php?prefix=aorta-vzvz-). Het systeem dient dit signaal te verwerken op de manier zoals is opgenomen in het PvE van de zorgtoepassing. Op hoofdlijnen geldt dat een signaal is verwerkt indien:

- als gevolg van het signaal de gegevens o.b.v. de VGU-functionaliteit zijn opgevraagd (afhankelijk van de toepassing kan dit direct gebeuren of op een later moment in de tijd);

- als gevolg van het signaal kunnen een of meerdere abonneehouders op de hoogte worden gesteld van het beschikbaar zijn van nieuwe gegevens, waarna een abonneehouder zelf een bevraging kan initiëren.

#### Aandachtspunten m.b.t. ontvangen signaal

In het signaal wordt géén contextcode opgenomen. Een signaal bevat het bouwsteentype dat is aangepast. Op basis van het abonnementID dat is opgenomen in het signaal, dient in het lokale abonnementenregister te worden opgezocht welke contextcode bij dit abonnement hoort. Het systeem mag maar één bevraging doen per abonnement. Het systeem zal dus moeten voorkomen dat hij op elk signaal direct een zelfde bevraging doet.

### Afhandelen signaal verlopen abonnement

Indien de geldigheidsduur van een abonnement verlopen is, dan zal het XIS als gevolg hiervan een signaal ontvangen. In dat geval is de gebeurtenis-type in het signaal gevuld met het kenmerk ‘geldigheidsduur verlopen’. De precieze invulling van het ‘niet abonneerbaar signaal’ is opgenomen in [DECOR informatie voor project: AORTA (aorta-vzvz-) (nictiz.nl)](https://decor.nictiz.nl/pub/vzvz/index.php?prefix=aorta-vzvz-).

Een abonnerend systeem zal dit signaal moeten kunnen verwerken. Op basis van dit signaal zal een abonneehouder op de hoogte moeten worden gesteld, dat zijn abonnement verlengd of verwijderd dient te worden. Het is ook mogelijk dat het systeem op basis van dit signaal het abonnement automatisch verlengd met behulp van de VGU-functionaliteit.

### Opvragen n.a.v. signalen

De afhandeling van een signaal is afhankelijk van de toepassing waarvoor een abonnement is afgesloten. Indien een signaal dient als trigger voor het initiëren van de VGU-functionaliteit, dan dient het systeem onder verantwoordelijkheid van een zorgverlener een opvraagbericht te versturen met de juiste contextcode.

Het is ook mogelijk dat een zorgverlener zelf of onder mandaat een opvraag initieert n.a.v. een ontvangen signaal. Het moet dan wel inzichtelijk zijn voor de zorgverlener of gemandateerde, dat er nieuwe gegevens op te vragen zijn.

#### Aandachtspunten m.b.t. opvragen n.a.v. signalen

##### Autorisatie

Autorisatie voor het opvragen van gegevens gebeurt op basis van de rolcode van een verantwoordelijke zorgverlener. Het is mogelijk dat er meerdere abonneehouders met verschillende rolcodes een abonnement hebben afgesloten voor een zelfde combinatie van patiënt, contextcode en applicatieID.

Het is zaak om de AORTA infrastructuur niet overmatig te bevragen. Dit kan namelijk een bronsysteem zodanig belasten, dat het de gegevensstroom niet meer kan verwerken. Echter, het is ook van belang om alle informatie op te vragen die een abonneehouder verwacht; een bevraging o.b.v. een rolcode met een autorisatiebeperking mag niet leiden tot het missen van medische gegevens.

VZVZ dient een lijst beschikbaar te stellen met vergelijkbare autorisaties. Deze is te vinden in de autorisatierichtlijn Medicatieveiligheid. Hierin dient te zijn opgenomen welke rolcode voor welke contextcode eenzelfde autorisatie kent. Een opvragend systeem moet op basis van deze lijst zo efficiënt als mogelijk bevragingen uit sturen.

##### Minimale bevraging o.b.v. contextcode

Een contextcode bestaat uit één of meerdere bouwsteentypes. Het kan dus zijn dat er voor één abonnementID meerdere signalen nagenoeg tegelijkertijd ontvangen worden. Indien de XIS-applicatie een signaal verwerkt op basis van de VGU-functionaliteit, dan dient de applicatie binnen een tijdsbestek van 5 seconden éénmaal een bevraging te doen t.b.v. dit abonnementID. Er dient dus niet op elk signaal met hetzelfde abonnementID te worden gereageerd. Indien de XIS-applicatie de abonneehouder op de hoogte stelt van het ontvangen van een signaal, dan dient er als gevolg van initiatie van een bevraging door een abonneehouder, maar één bevraging gedaan te worden per abonnementID.

Een bouwsteentype kan voor komen in meerdere contextcodes. Indien er voor meerdere contextcodes een abonnement is afgesloten, dan kan dit er toe leiden dat er meerdere bevragingen tegelijkertijd gedaan dient te worden met deze contextcodes.

### Tonen verwerking signaal aan gebruiker

Een abonneehouder moet afhankelijk van de toepassing van de signaalfunctie inzichtelijk krijgen of er nieuwe gegevens zijn opgevraagd (i.h.g.v. VGU) of opvraagbaar zijn. Voor medicatiebewaking is het van belang dat een abonneehouder heel expliciet een melding krijgt van nieuwe gegevens op het moment van ontvangen van een signaal.

Voor de overige situatie is het afhankelijk van de situatie of zorgverlener op de hoogte gesteld moet worden van nieuw opgevraagde gegevens. Een zorgverlener moet zich in ieder geval bewust zijn, dat er door middel van de VGU op elk moment nieuwe gegevens opgevraagd kunnen zijn van een patiënt.

### Hybride situatie

Een abonnement kan zowel op contextcode als op gegevenssoort worden afgesloten. Afhankelijk van de situatie, dient een systeem zowel een abonnement af te sluiten op contextcode als op gegevenssoort.

Indien een abonnement afgesloten wordt op gegevenssoort, dan zullen er alleen signalen ontvangen worden indien een bronsysteem een gegevenssoort (her)aanmeldt of verwijdert. In het signaal is opgenomen welk specifieke gegevenssoort en welk abonnementID het betreft. Op basis van de gegevenssoort moet worden bepaald welke interactie eruit gestuurd dient te worden. De XIS-applicatie moet de vertaling van gegevenssoort naar interactieID geconfigureerd hebben in zijn applicatie.

Indien een abonnement afgesloten wordt op contextcode, dan zullen er alleen signalen ontvangen worden indien een bronsysteem een bouwsteen (her)aanmeldt of verwijdert. In het signaal is opgenomen welk specifieke bouwsteentype en welk abonnementID het betreft. Op basis van het abonnementID dient de XIS-applicatie te bepalen welk contextcode dient te worden opgenomen in de bevraging.

Het nemen van het niveau waarop een abonnement genomen moet worden, is afhankelijk van de specifieke versie van de zorgtoepassing dat geïmplementeerd wordt door de XIS-leverancier. Er is een overgangsperiode waarbij bronnen binnen die zorgtoepassing alleen nog op gegevenssoort aanmelden, op gegevenssoort en bouwsteentype of alleen nog maar op bouwsteentype. Afhankelijk van hoe de bronnen binnen een zorgtoepassing aanmelden, dient er op contextcode of gegevenssoort een abonnement te worden afgesloten.

Indien er tegelijkertijd meerdere signalen wordt ontvangen van een systeem met bouwstenen en gegevenssoorten, dan is het afdoende om alleen een vraag te stellen met de bijbehorende contextcode.

## Processen m.b.t. signaalfunctie

### Proces na verlopen geldigheidsduur abonnement

Om het zorgproces niet in gevaar te brengen, zullen abonnementen na de geldigheidsduur niet automatisch verwijderd worden. Deze abonnementen zullen actief blijven en de signaalfunctie zal dus blijven werken. Echter, het is wel van belang dat een abonneehouder actie onderneemt om het abonnement te verwijderen of te verlengen. Er zijn diverse processen om te borgen dat dit ook daadwerkelijk gebeurt.

#### Rol GBZ-beheerder

Indien de geldigheidsduur van een abonnement is verlopen, dan zal dit kenbaar worden gemaakt aan de daarvoor verantwoordelijke rollen binnen VZVZ. Deze zullen contact opnemen met de GBZ-beheerder die verantwoordelijk is voor het systeem waarin de abonnementen staan geregistreerd. De GBZ-beheerder dient vervolgens met de betreffende abonnementID’s te achterhalen welke abonnementen verlengd of verwijderd dienen te worden en dient de verantwoordelijke abonneehouder hierop aan te spreken.

#### Proces binnen applicatie

Indien een abonnement verlopen is, dan zal het systeem hiervan op de hoogte worden gebracht door een ‘niet abonneerbaar signaal’. Het ‘niet abonneerbaar signaal’ zal een melding bevatten dat een specifiek abonnement (o.b.v. abonnementID) is verlopen. Een abonneehouder dient deze melding getoond te krijgen en dient hier op te acteren door middel van het verlengen of verwijderen van een abonnement.

#### Best Practice

Om te voorkomen dat een abonnement verloopt is het aan te raden om een abonneehouder vroegtijdig op de hoogte te stellen van het verlopen van een abonnement. Op basis van de lokaal geregistreerde geldigheidsduur van een abonnement kan het systeem een melding genereren, die getoond wordt aan de abonneehouder. Een abonneehouder kan hier dan op reageren door het abonnement te verlengen of te verwijderen.

Indien het systeem werkt met de VGU-functionaliteit, dan is het mogelijk om het verlopen van de geldigheidsduur als trigger te laten werken voor het verlengen van het abonnement. In dat geval dient wel een behandelrelatie en een inschrijftoken aanwezig te zijn van de patiënt op wiens gegevens geabonneerd dient te worden. Daarnaast dient het systeem de beschikking te hebben over een geldig mandaattoken van de abonneehouder.

Het automatisch verwijderen van een abonnement o.b.v. de VGU-functionaliteit wordt beschreven in ‘Proces m.b.t. VGU’.

### Uitdiensttreding zorgverlener

Indien een zorgverlener uit dienst treedt, dient een abonnement die centraal onder zijn verantwoordelijkheid staat geregistreerd verwijderd te worden.

Mogelijk dient dit abonnement opnieuw te worden afgesloten door de vervangende zorgverlener of een reeds geregistreerde abonneehouder. Bij ‘het verwijderen van een abonnement’ staat beschreven waar men op moet letten in het geval een abonnement wordt verwijderd.
