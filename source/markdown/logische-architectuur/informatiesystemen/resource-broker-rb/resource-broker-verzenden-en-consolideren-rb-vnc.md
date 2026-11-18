[AORTA 8.5.2](../../../index.md) / [Logische architectuur](../../../logische-architectuur.md) / [Informatiesystemen](../../informatiesystemen.md) / [Resource Broker (RB)](../resource-broker-rb.md)

# Resource Broker Verzenden en Consolideren (RB VnC)

De Resource Broker VnC zijn toegankelijk via een geboden interface en worden beschreven in de vorm van use cases. Responses die in een succes- of uitzonderingssituaties moeten worden geretourneerd zijn [voor iedere situatie beschreven](https://aorta-on-fhir.public.vzvz.nl/aorta-on-fhir-specificaties-versie-07x/latest/resource-broker-interfaces-0-7-x). De Resource Broker VnC kan FHIR-search interacties versturen naar meerdere resource servers en de antwoorden *consolideren*in de benodigde response interactie. Het consolidatieproces consolideert ontvangen HL7v3-responses naar FHIR-responses middels een Transformatie Server (BTD).
