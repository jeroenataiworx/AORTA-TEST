[AORTA 8.5.2](../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../aansluit-en-implementatiewijzer-kern.md) / [Berichttransport](../../berichttransport.md) / [AORTA_Trp_IH_Berichttransport](../aorta_trp_ih_berichttransport.md)

# Diakritische tekens

Het is van belang te verifiëren of diakritische en andere tekens goed gecodeerd zijn. Dat kan bijvoorbeeld met de volgende tekst:

![Diagram](../../../../assets/4520f6ae325e61288b949be493d7d08e1f7f5dff3a4238b50ca34ec39ad4ef37.png)

Noot: afhankelijk van de instellingen van de PC kunnen diakritische tekens anders overkomen. Daarom is deze tekst grafisch opgenomen. Wanneer deze tekens hieronder er anders uitzien, gebruik de tekens uit het plaatje.

Deze tekst dient exact zo in het bronsysteem van de zender ingevoerd te worden in een veld dat vrije tekst toestaat. Bij de ontvanger dient de tekst in het doelsysteem weer zo leesbaar te zijn. Wanneer het doelsysteem één of meer van deze tekens niet ondersteunt, dient de ontvangende partij in de XML te verifiëren dat de tekst ongeschonden is overgekomen. De tekst is zo gekozen omdat ze de verschillen tussen de meest gebruikte tekstcoderingen, UTF-8, ISO-8859-1, ISO8859-15 en Windows-1252 blootlegt.

| **Hexadecimale representatie van enkele diakritische tekens** ; |  |  |  |
| --- | --- | --- | --- |
| **Encoding** ; | **Euroteken (€)** ; | **Kleine letter o met forward slash (ø)** ; | **Kleine a met trema (ä)** ; |
| UTF-8 ; | E2 82 AC ; | C3 B8 ; | C3 A4 ; |
| ISO-8859-1 ; | bestaat niet ; | F8 ; | E4 ; |
| ISO-8859-15 ; | A4 ; | F8 ; | E4 ; |
| Windows-1252 ; | 80 ; | F8 ; | E4 ; |

Een geschikte plaats voor deze tekst is (alleen in testomgevingen) het optionele element <softwareName> in de Transmission Wrapper. Dit komt in alle berichten voor, maar wordt veelal niet gebruikt in testen.

| CODE  `<?xml version="1.0" encoding="utf-8"?> ... <sender> <device> <id extension="01234567" root="2.16.840.1.113883.2.4.6.6"/> <softwareName>€ of døllär</softwareName> </device> </sender> ...` |
| --- |
