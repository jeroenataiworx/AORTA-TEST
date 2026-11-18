[AORTA 8.5.2](../../index.md) / [Logische architectuur](../../logische-architectuur.md) / [Primaire interacties](../primaire-interacties.md)

# Identificatie en authenticatie

Alle actoren die betrokken zijn bij het opvragen en sturen van gegevens moeten geïdentificeerd kunnen worden om de volgende redenen:

- Om fouten te voorkomen, moet onomstotelijk vaststaan over welke patiëntgegevens worden uitgewisseld.

- Om autorisatieregels te kunnen controleren, moet onomstotelijk vaststaan welke zorgverleners en zorgaanbieders (en in het geval van patiënttoegang welke patiënten en eventuele vertegenwoordigers) optreden als gegevensraadpleger of gegevenszender.

- Om het uitwisselen van gegevens traceerbaar te maken, moet onomstotelijk vaststaan welke zorgverleners en zorgaanbieders (en in het geval van patiënttoegang welke patiënten en eventuele vertegenwoordigers) optreden als gegevensraadpleger of gegevenszender.

De betrokken actoren kunnen op de volgende wijze kunnen worden geïdentificeerd:

- Patiënten worden geïdentificeerd aan de hand van hun Burgerservicenummer (BSN). Het BSN is een uniek persoonsnummer. Iedereen die zich inschrijft bij een Nederlandse gemeente krijgt een BSN. Het BSN is bedoeld om persoonsverwisselingen te voorkomen. Er is wettelijk geregeld welke instanties of organisaties het BSN mogen gebruiken. De Wet Aanvullende Bepalingen Verwerking Persoonsgegevens in de Zorg (Wabvpz) regelt het gebruik van het BSN in de zorg.

- Zorgverleners worden geïdentificeerd aan de hand van hun ‘unieke zorgverlener identificatie (UZI)’. Het Unieke Zorgverlener Identificatie-register (UZI-register) is een overheidsregister onder beheer van het Ministerie van VWS waarin iedere zorgverlener zich kan laten registreren, waarbij tevens een koppeling wordt gelegd met het beroep van de zorgverlener zoals vastgelegd in het BIG-register. Zorgverleners krijgen een UZI-pas om hun identiteit mee aan te tonen. Overigens is het mogelijk dat een zorgverlener die werkzaam is bij meerdere zorgaanbieders slechts één UZI-pas heeft die bij meerdere zorgaanbieders kan worden gebruikt; dit wordt ‘gastgebruik’ genoemd (zie ook pagina '[Authenticatie van de gebruiker / pashouder](../berichtafhandeling/berichtafhandeling-door-de-zim.md#authenticatie-van-de-gebruiker-pashouder)').

- Zorgverleners kunnen ook geïdentificeerd worden met de ZORG-ID Smartcard. De ZORG-ID Smartcard wordt beheerd door zorgaanbieders en uitgegeven op basis van een actieve UZI-pas op naam van de zorgmedewerker. Het Landelijk Schakelpunt (LSP) zal deze smartcards accepteren voor de ondertekening van inschrijftokens en transactietokens.

- Medewerkers van zorgaanbieders (niet-zorgverleners) worden eveneens geïdentificeerd aan de hand van hun ‘Unieke Zorgverlener Identificatie’ (UZI). Ze krijgen een door het UZI-register uitgegeven medewerker pas op naam om hun identiteit mee aan te tonen.

- Systemen worden geïdentificeerd aan de hand van hun unieke applicatieID. Ze krijgen een door het LSP-organisatie uitgegeven applicatieID om hun identiteit mee aan te tonen.

- Zorgaanbieders worden geïdentificeerd aan de hand van hun UZI-registerabonneenummer (URA). Dit is een identificatie die wordt verstrekt aan de zorgaanbieder of zorgverlener die UZI-passen heeft aangevraagd. Als een zorgaanbieder UZI-passen aanvraagt voor haar zorgverleners en medewerkers, krijgt de organisatie een unieke URA en worden de zorgverleners en medewerkers van de zorgaanbieder aan dit URA gekoppeld. Daardoor kunnen zorgverleners worden gerelateerd aan zorgaanbieders. Aangezien de organisatie die UZI-passen aanvraagt een grote organisatie kan zijn (bv. een zorggroep met meerdere huisartsenpraktijken) is de organisatienaam die gerelateerd is aan de URA niet noodzakelijk herleidbaar tot één vestiging locatie of organisatieonderdeel van die zorgaanbieder.

- Niet UZI-abonnees (GBO) worden geïdentificeerd aan de hand van hun PKIoverheid servercertificaatnummer.
