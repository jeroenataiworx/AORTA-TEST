[AORTA 8.5.2](../../index.md) / [Logische architectuur](../../logische-architectuur.md) / [Berichtafhandeling](../berichtafhandeling.md)

# Afhandelen van berichtversies

De specificaties van de AORTA-infrastructuur en bijbehorende zorgtoepassingen vallen onder versiebeheerprocedures[^1]; met regelmaat worden nieuwe versies gepubliceerd. Door het toevoegen van nieuwe functionaliteit aan AORTA kunnen meerdere versies van een interactietype ontstaan, waarbij verschillen kunnen optreden in de interface-definitie. Omdat aangesloten informatiesystemen een kwalificatietraject moeten doorlopen voor nieuwe AORTA-functies (zie '[Zorginformatiesystemen (XIS) en het Goed beheerd zorgsysteem (GBZ)](https://vzvz.atlassian.net/wiki/x/iQARBQ)'), worden nieuwe berichtversies niet in gelijk tempo door alle aangesloten informatiesystemen geadopteerd.

De ZIM ondersteunt steeds de berichtversies die horen bij twee opeenvolgende versies van een zorgtoepassing. Bij het versturen van patiëntgegevens moet een GBZ rekening houden met de interactieversie die de ontvanger ondersteunt. De interactieversie van de ontvanger kan achterhaald worden door middel van een bevraging van het ZAB.

Details van het omgaan met berichtversies zijn beschreven in het [Ontw OPV], het [Ontw STU] en het [Ontw APR].

[^1]: Een beschrijving van deze versiebeheerprocedures valt buiten de reikwijdte van dit architectuurdocument.
