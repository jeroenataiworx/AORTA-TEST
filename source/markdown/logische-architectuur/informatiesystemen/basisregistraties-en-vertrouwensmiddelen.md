[AORTA 8.5.2](../../index.md) / [Logische architectuur](../../logische-architectuur.md) / [Informatiesystemen](../informatiesystemen.md)

# Basisregistraties en vertrouwensmiddelen

### UZI-register

Het Unieke Zorgverlener Identificatie register (kortweg UZI-register) is het door de Minister van VWS aangewezen register van zorgaanbieders zoals vermeld in artikel 14 van de Wbsn-z. Het UZI-register wordt beheerd door het CIBG, een uitvoeringsorganisatie van het ministerie van VWS.  
Het UZI-register is de certificatiedienstverlener (ook wel Certificate Service Provider of CSP) die certificaten uitgeeft voor de unieke identificatie en authenticatie van zorgaanbieders en indicatieorganen in de zorg.

Tevens geeft het UZI-register certificaten uit voor de unieke identificatie en authenticatie van zorgverleners. Het UZI-register koppelt hiertoe uniek de fysieke identiteit aan een elektronische identiteit en legt deze vast in certificaten. De certificaten en de hierbij behorende cryptografische sleutels bevinden zich op een smartcard, de UZI-pas.

Het UZI-register geeft UZI-passen uit voor door de minister van VWS bij wet en regelgeving aangewezen partijen. Zorgverleners en medewerkers worden door het UZI-register voorzien van een UZI-pas, informatiesystemen van een UZI-servercertificaat. De UZI-pas is binnen AORTA nodig voor authenticatie van zorgverleners en medewerkers van zorgaanbieders, het UZI-servercertificaat is nodig voor authenticatie van GBZ’en.

Een UZI-pas is een vertrouwensmiddel op basis van PKIO-certificaten (Private Key Infrastructure Overheid, zie [PKIO]). Er zijn aparte passen voor zorgverleners, medewerkers en medewerkers-niet-op-naam. De pas faciliteert bij elektronisch verkeer authenticatie, versleuteling en het plaatsen van een elektronische handtekening (dit laatste alleen met passen op naam). De pas bevat een apart certificaat voor elk van deze drie functies.  
Een UZI-pas bevat o.a. het UZI-nummer, beroep en specialisatie van de pashouder. Ook bevat de pas het nummer van de zorgaanbieder die de pas heeft aangevraagd, het UZI-register abonneenummer (URA).  
Een UZI-servercertificaat is eveneens een vertrouwensmiddel op basis van de PKIO. Het is nodig voor het identificeren van een informatiesysteem en het opzetten van een beveiligde elektronische verbinding. Het servercertificaat bevat eveneens het URA van de zorgaanbieder.

### PKIO

De Public Key Infrastructure Overheid (PKIO) is een infrastructuur voor het uitgeven en beheren van digitale certificaten. PKIoverheid heeft een hiërarchische structuur van certificaten. Het ankerpunt van vertrouwen binnen PKIoverheid, het stamcertificaat Staat der Nederlanden, valt onder verantwoordelijkheid van de Nederlandse overheid.  
PKIO verstrekt zowel persoonlijke vertrouwensmiddelen op naam (PKIO-passen), als systeemvertrouwensmiddelen (servercertificaten).  
PKIO-passen worden gebruikt voor de identificatie van medewerkers van het klantenloket.  
PKIO-servercertificaten worden gebruikt door de ZIM, door het GBK,door GBP’en en door niet UZI-abonnees (GBO). Ze zijn nodig voor het identificeren van het informatiesysteem en het opzetten van een beveiligde elektronische verbinding.

### ZORG-ID

ZORG-ID is een door VZVZ beheerde voorziening voor identificatie en authenticatie van zorgprofessionals en ondersteunend personeel binnen AORTA.

Het fungeert als een modern vertrouwensmiddel in aanvulling op de al bestaande middelen (zoals UZI, PKIoverheid en DigiD) en sluit aan bij de wettelijke kaders en beveiligingsstandaarden die gelden in de zorg.

ZORG-ID voorziet zorgverleners en medewerkers van een elektronische identiteit die gebruikt kan worden voor:

- **Authenticatie** – sterke en multifactor authenticatie op basis van moderne standaarden.

- **Identificatie** – koppeling van de elektronische identiteit aan een fysieke identiteit door middel van een betrouwbaar registratieproces (RA-proces).

- **Digitale handtekening** – ondersteuning van geavanceerde of gekwalificeerde elektronische handtekeningen, afhankelijk van het gebruikte middel.

Het ZORG-ID platform ondersteunt zowel bestaande middelen (zoals de UZI-pas) als nieuwe vormen van identificatie en authenticatie die aansluiten bij de digitalisering van de zorg. Voorbeelden hiervan zijn:

- **ZORG-ID Mobile App** – een mobiele oplossing die fungeert als toegangsmiddel tot de ZORG-ID wallet, met ondersteuning voor twee-factorauthenticatie, digitale ondertekening en het scannen van een WID-document.

- **ZORG-ID Smartcard** – een fysieke kaart die toegang biedt tot de wallet en inlogfunctionaliteit ondersteunt.

Deze middelen faciliteren de drie rollen binnen het verifiable-credentials-model:

- **Issuer** – de partij die vertrouwelijke gegevens of attributen uitgeeft (bijvoorbeeld een UZI-register).

- **Holder** – de zorgprofessional die deze gegevens in de wallet beheert.

- **Verifier** – de partij die de gegevens en authenticatie controleert (bijvoorbeeld het LSP).

ZORG-ID zelf geeft X.509-certificaten uit en functioneert daarmee als zelfstandige Certificate Authority (CA).

### DigiD

Het DigiD-register (zie [DigiD]) is een ICT-voorziening onder beheer van ‘Logius’, de dienst digitale overheid van het ministerie van Binnenlandse Zaken en Koninkrijksrelaties. In het DigiD-register worden personen geregistreerd die door het DigiD-register zijn voorzien van een vertrouwensmiddel.  
Personen die vervolgens hun DigiD gebruiken om zich te identificeren, kunnen door het DigiD-register worden geauthenticeerd. Hierbij geeft het DigiD-register een elektronisch ondertekende bewering af over de mate waarin het de authenticiteit van de gebruiker waarborgt. DigiD treedt hierbij dus op als ‘identity provider’.

Authenticatie met behulp van DigiD is van toepassing voor patiënten die gebruikmaken van een GBP (zie ook ['Berichtafhandeling door de ZIM: Authenticatie van de gebruiker / pashouder'](../berichtafhandeling/berichtafhandeling-door-de-zim.md#authenticatie-van-de-gebruiker-pashouder)).

### SBV-Z

De SBV-Z biedt toegang tot de volgende BSN-diensten die voor AORTA relevant zijn:

- het opvragen en verifiëren van het BSN;

- het opvragen van persoonsgegevens op basis van het BSN;

- het verifiëren van de geldigheid van het Nederlands identiteitsdocument.

Deze diensten kunnen worden aangeroepen vanuit een GBZ wanneer de zorgverlener de identiteit van de patiënt verifieert (zie ook [Zorginformatiesystemen (XIS) en het Goed beheerd zorgsysteem (GBZ)](zorginformatiesystemen-xis-en-het-goed-beheerd-zor.md)).

### Mitz

- Mitz is een centrale toestemmingsregistratie en biedt de volgende services: Locatieservice; welke zorgaanbieder heeft welke gegevens van welke patiënt waarvoor tevens toestemming is gegeven voor gegevensdeling?

- Toestemmingsservice; welke toestemmingen heeft een patiënt vastgelegd voor een zorgaanbieder?
