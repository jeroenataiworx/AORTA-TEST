[AORTA 8.5.2](../../../index.md) / [Logische architectuur](../../../logische-architectuur.md) / [Informatiesystemen](../../informatiesystemen.md) / [Zorginformatiemakelaar (ZIM)](../zorginformatiemakelaar-zim.md)

# Gebeurtenisverdeler en gebeurtenisafhandelaars

De gebeurtenisverdeler is het centrale meldpunt voor gebeurtenissen voor de overige componenten van de ZIM. De gebeurtenisverdeler zorgt ervoor dat gebeurtenissen worden doorgegeven aan alle gebeurtenisafhandelaren die in een bepaalde gebeurtenis geïnteresseerd zijn. Gebeurtenisafhandelaren zijn technische componenten die specifieke acties kunnen ondernemen, zoals het sturen van signaleringen. Concrete gebeurtenisafhandelaren zijn de Signaleringsafhandelaar en de Afhandelaar Bezwaar Patiënt.

De Signaleringsafhandelaar is een gebeurtenisafhandelaar die signalen stuurt naar een op de ZIM aangesloten informatiesysteem als een gebeurtenis plaatsvindt waarvoor het aangesloten systeem een abonnement heeft geregistreerd. De signaleringsafhandelaar gebruikt hierbij het [abonnementenregister](https://vzvz.atlassian.net/wiki/x/QwERBQ)om te controleren welke systemen een abonnement hebben voor een bepaalde gebeurtenis.
