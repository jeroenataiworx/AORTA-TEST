[AORTA 8.5.2](../../index.md) / [Logische architectuur](../../logische-architectuur.md) / [Ondersteunende interacties](../ondersteunende-interacties.md)

# Selecteren van zorgaanbieders, zorgverleners en zorgaanbiederapplicaties

Bij het versturen van gegevens moet de gegevenszender patiëntgegevens kunnen adresseren aan een gegevensontvanger.

Aangezien ook bij het versturen van gegevens het LSP als intermediair optreedt, biedt het LSP aan de gegevenszender de mogelijkheid om voorafgaand aan het sturen van gegevens de gewenste ontvanger op te zoeken in een zorgadresboek (ZORG-AB). De zorgverlener die het zorgadresboek raadpleegt neemt de rol aan van ‘raadpleger zorgveldgegevens’.

Aangezien de beoogde ontvanger van de te versturen patiëntgegevens zowel een zorgaanbieder als een individuele zorgverlener kan zijn (zie pagina '[Sturen van patiëntgegevens](../primaire-interacties/rollen-toekennen-aan-actoren.md#sturen-van-patientgegevens)') zijn zowel zorgaanbieders als zorgverleners opgenomen in dit adresboek. De laatsten moeten wel door de werkgever (zorgaanbieder) met toestemming van het individu worden opgenomen.

De gegevenszender moet ook de zorgaanbiederapplicatie (het informatiesysteem[^1] van een zorgaanbieder) waarnaar de gegevens daadwerkelijk worden gestuurd kunnen opzoeken.

[^1]: De termen ‘informatiesysteem’ en ‘applicatie’ worden in dit document beide gebruikt voor het aanduiden van een systeem voor gegevensverwerking.
