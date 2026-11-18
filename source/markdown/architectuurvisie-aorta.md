[AORTA 8.5.2](index.md)

# Architectuurvisie AORTA

## Ontwikkelingen

- Opkomst/ontwikkeling van meerdere landelijke/regionale/leverancier specifieke zorginfrastructuren in Nederland, naast AORTA. Informatie die uitgewisseld wordt in/binnen de ene zorginfrastructuur kan relevant zijn voor toepassingen die in een andere zorginfrastructuur. Daarom ziet VZVZ de noodzaak om AORTA te kunnen koppelen op andere zorginfrastructuren, bij voorkeur via het Twiin afsprakenstelsel. Een uitdaging hierbij is dat het verschil in (implementatie van het) beveiligings-/vertrouwensniveau met AORTA overbrugt dient te worden.

- Ontwikkelingen in de AORTA-architectuur duren vaak lang omdat de lat voor veilige uitwisseling in het stelsel hoog is gelegd. Naast dit bestaande 'spoor' moet AORTA ook een spoor kunnen bieden waar ontwikkelingen kort cyclisch gedaan kunnen worden en er sneller meerwaarde aan de eindgebruiker geboden kan worden.

- Landelijke normeringen op verschillende aspecten gaan deels dicteren hoe AORTA moet werken en/of geïmplementeerd moet worden:Duurzaam Informatiestelsel in de Zorg Referentie Architectuur (DIZRA). Afsprakenstelsels en andere bouwstenen die onderdeel willen zijn van het duurzame informatiestelsel in de zorg dienen te voldoen aan DIZRA. Vanuit de Wet elektronische gegevensuitwisseling in de zorg (Wegiz) worden er verschillende NEN-normen opgesteld waaraan bepaalde informatie-uitwisselingen in de zorg aan moeten voldoen. Onder andere zal dit gaan gelden voor toestemming, identificatie & authenticatie en lokalisatie van patiëntgegevens.

- Verandering van het IT-landschap van meer monolithische systemen naar een open IT-platform

Om de ontwikkelingen te kunnen volgen dient AORTA het volgende te gaan ondersteunen:

## Hybride (bimodal) besturingsvormen

- Hybride besturingsvormen kunnen elke op hun eigen manier informatie- en technologie-intensieve diensten leveren:Modus 1 is traditioneel en legt de nadruk op veiligheid en nauwkeurigheid​Modus 2 is verkennend en legt de nadruk op wendbaarheid en snelheid

| **Modus 1**​ ; | ​ ; | **Modus 2**​ ; |
| --- | --- | --- |
| Betrouwbaarheid​ ; | **Doel**​ ; | Wendbaarheid​ ; |
| Goede prijs, hoge performance​ ; | **Klantwaarde**​ ; | Optimale klantbeleving, nieuwe features​ ; |
| Waterval, projectmanagement, Lean​ ; | **Aanpak**​ ; | Agile, Lean, Scrum, DevOps​ ; |
| Plan- en mandaat gedreven​ ; | **Governance**​ ; | Empirisch, continue proces georiënteerd​ ; |
| Lange termijn contracten, grote leveranciers, structurele financiering​ ; | **Sourcing**​ ; | Innovatieve leveranciers, nieuwe toetreders, korte termijn contracten, stimuleren met tijdelijke subsidies​ ; |
| Gericht op standaardisatie, project gedreven, zekerheidzoekend​ ; | **Competentie medewerkers**​ ; | Gericht op vernieuwing, kunnen omgaan met onzekerheden​ ; |
| IT centraal, klant op afstand​ ; | **Cultuur kenmerk**​ ; | Klant centraal, gericht op functionaliteit en klantwaarde​ ; |
| Lang, maanden​ ; | **Cyclustijd**​ ; | Kort, dagen, weken​ ; |

- Deze hybride besturing vraagt om een verbindend afsprakenstelsel waarmee beide modi naast elkaar kunnen werken (en samenwerken). Hierin moet komen te staanHoe modus 2 met modus 1 kan communicerenHoe in modus 2 ontwikkelde toepassing naar modus 1 kan worden overgebrachtHoe beide modi tegelijk kunnen werken en ieder een eigen governance hebbenHoe modus 1 zich toch ook toekomstvast kan blijven vernieuwen

- Het koppelen van andere zorginfrastructuren aan AORTA moet via modus 2Dit vraagt om de introductie van zorgservices; generieke functionaliteit die los van het LSP te gebruiken is

## Zorgservices

Een ‘zorgservice’ levert generieke functionaliteit, gerealiseerd door software, die locatie onafhankelijk is (in het XIS of hierbuiten). Voorbeelden van zorgservices zouden bijvoorbeeld kunnen zijn: lokaliseren van patiëntgegevens, autoriseren, het beheren van toestemming of adressering. Het idee is dat wanneer dit soort generiek functionaliteit los gebruikt / aangeboden kan worden, projecten in modus 2 makkelijker bediend en versneld kunnen worden zonder dat men aan alle implementatie-eisen hoeft te voldoen die nu een samenhangend geheel vormen voor de aansluiting op het LSP/de ZIM. Daarnaast biedt het de mogelijkheid om degelijke generieke diensten los(ser) van elkaar verder te ontwikkelen en implementeren of aan te passen op specifieke behoeftes voor een bepaald project. Mogelijke nadelen van losse generieke functies kunnen zijn de algehele beschikbaarheid en een verhoogde complexiteit van het systeem.
