[AORTA 8.5.2](../../index.md) / [Logische architectuur](../../logische-architectuur.md) / [Informatiesystemen](../informatiesystemen.md)

# Zorginformatiesystemen (XIS) en het Goed beheerd zorgsysteem (GBZ)

Een ‘XIS’ is een verzamelterm voor informatiesystemen in het zorgveld, zoals bijvoorbeeld Huisartsinformatiesystemen (HIS) en Apotheekinformatiesystemen (AIS). In de praktijk beschikken zorgaanbieders, afhankelijk van hun werkzaamheden, over verschillende typen informatiesystemen. Dit zijn veelal implementaties van commercieel verkrijgbare informatiesystemen gebouwd door gespecialiseerde softwareleveranciers, maar kunnen ook in eigen beheer zijn ontwikkeld.

Een Goed Beheerd Zorgsysteem (GBZ) is een *concrete* installatie van een XIS of verzameling XIS’en, elk met een XIS-typekwalificatie (zie verderop in deze paragraaf), in gebruik bij één zorgaanbieder, die voldoet aan de implementatie- en exploitatie-eisen voor aansluiting op de ZIM[^1]. Het begrip GBZ is een deelverzameling van het begrip GBx en is in feite een goed beheerd informatiesysteem (GBx) dat gebruikt wordt door een zorgaanbieder.

Om een XIS in te zetten als GBZ moet aan twee soorten eisen worden voldaan:

- Voorwaarden die in algemene zin aan het XIS als *softwareproduct* moeten worden gesteld. In de eerste plaats zijn dit functionele eisen, bijvoorbeeld ten aanzien van de berichtuitwisseling die door een XIS moet worden ondersteund. Ook gelden non-functionele eisen die leiden tot eisen aan het XIS als softwareproduct, bijvoorbeeld wat betreft ondersteuning van twee-factor-authenticatie door het softwareproduct. Producenten van XIS’en kunnen een XIS-typekwalificatie behalen waarbij gecontroleerd wordt of het product aan deze eisen voldoet.

- Voorwaarden die gelden voor een specifieke implementatie van een XIS voor een bepaalde zorgaanbieder. Dit zijn bijvoorbeeld eisen aan de beheersorganisatie of de gebruikersvoorzieningen, zoals de beschikbaarheid van authenticatie-middelen. Deze aanvullende eisen zijn dus implementatieafhankelijk en maken geen deel uit van een XIS-typekwalificatie.

Het GBZ heeft in het kader van berichtenuitwisseling via AORTA enkele belangrijke verantwoordelijkheden[^2]:

- Het GBZ legt de basis voor authenticatie van de gegevensraadpleger of gegevenszender. Allereerst authenticeert het GBZ zelf de eindgebruiker als deze aanlogt bij het GBZ. Ook verstrekt het GBZ in berichten aan de ZIM verifieerbare identiteitsinformatie van de eindgebruiker. Het GBZ legt de basis voor de identificatie van de patiënt, door het burgerservicenummer van de patiënt vast te leggen; hierbij registreert het GBZ ook of de identiteit van de patiënt is geverifieerd door de controle van een wettelijk identiteitsdocument (WID) als genoemd in de Wbsn-z.

- In het GBZ wordt, indien het GBZ dient als bronsysteem van patiëntgegevens, vastgelegd of de patiënt heeft ingestemd (opt-in) met het beschikbaar maken van gegevens via AORTA. Het is mogelijk om deze opt-in in plaats van in het bronsysteem te laten vastleggen in Mitz.

- In het GBZ wordt het bestaan van een behandelrelatie tussen zorgverlener en patiënt vastgelegd; aangezien de behandelrelatie in het contact tussen zorgverlener en patiënt tot stand komt, is het zorgsysteem van de zorgverlener de aangewezen plaats om de behandelrelatie te bevestigen.

- In het GBZ wordt bijgehouden op basis van welke autorisatieregels een zorgverlener gebruik kan maken van een mandaat.

[^1]: Het voldoen aan de implementatie- en exploitatie-eisen wordt getoetst door een eigen verklaring van de beheerorganisatie en uitvoering van steekproefsgewijze schouwingen.

[^2]: Deze lijst van verantwoordelijkheden is niet limitatief. Hier worden enkele kernverantwoordelijkheden genoemd die bij het GBZ worden belegd in tegenstelling tot de ZIM.
