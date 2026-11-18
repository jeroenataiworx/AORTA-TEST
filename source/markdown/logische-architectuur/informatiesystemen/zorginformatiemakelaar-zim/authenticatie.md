[AORTA 8.5.2](../../../index.md) / [Logische architectuur](../../../logische-architectuur.md) / [Informatiesystemen](../../informatiesystemen.md) / [Zorginformatiemakelaar (ZIM)](../zorginformatiemakelaar-zim.md)

# Authenticatie

Dit component is betrokken bij de afhandeling van elk bericht dat bij de ZIM binnenkomt vanuit een op de ZIM aangesloten informatiesysteem, zoals bij het opvragen en versturen van patiëntgegevens. De component identificeert en authentiseert hierbij de initiator van het bericht, aan de hand van informatie die in het bericht is meegegeven waarbij de authenticiteit met voldoende waarborg moet worden vastgesteld.

Hiertoe heeft de gebruiker een vertrouwensmiddel aan de hand waarvan de gebruiker kan worden geauthentiseerd (zie pagina '[Basisregistraties en vertrouwensmiddelen](https://vzvz.atlassian.net/wiki/x/MoWObg)').

- Een zorgverlener maakt hiertoe gebruik van een UZI-pas.

- Een klantenloketmedewerker maakt gebruik van een PKI-overheidspas.

- De patiënt kan zich authentiseren door middel van DigiD.

A.d.h.v. een vertrouwensmiddel wordt een authenticatie token aangemaakt die via een beveiligde verbinding tussen de GBx en ZIM wordt uitgewisseld, op basis van het servercertificaat van het GBx en het servercertificaat van de ZIM. Op basis van het servercertificaat van het GBx wordt vastgesteld vanuit welke organisatie de berichtuitwisseling is geïnitieerd.

Het doel van de authenticatietoken is:

- de gebruiker te identificeren en authentiseren

- de authenticiteit van het verstuurde bericht (deels) te borgen. Hierbij worden elementen uit het verstuurde bericht in het authenticatietoken geplaatst.

- de gebruiker onweerlegbaar aan het verstuurde bericht te koppelen.

Daarnaast kan t.b.v. authenticatie van de gebruiker in het bericht meerdere tokens opgenomen zijn:

- Transactietoken (T); een token dat gekoppeld is aan een uniek bericht; Dit token is getekend door een servercertificaat van het versturende systeem of door het persoonlijke UZI- certificaat van de gebruiker. Zie IH Berichtauthenticatie Transactietoken voor een complete afhandeling en beschrijving van het transactietoken;

- PKIO-token (P); een token dat gekoppeld is aan een uniek bericht; Dit token is getekend door het persoonlijke PKIO-certificaat van de gebruiker. Zie IH Berichtauthenticatie PKIO voor een complete afhandeling en beschrijving van het PKIO-token;

- Mandaattoken (M); een token dat AORTA-autorisaties overdraagt van de mandaterende naar een gemandateerde. Zie IH Mandaattoken voor een complete afhandeling en beschrijving van het mandaattoken;

- Inschrijftoken (I); een token dat de koppeling legt tussen een patiënt en de behandelende organisatie. Zie IH Inschrijftoken voor een complete afhandeling en beschrijving van het Inschrijftoken.

Het voorkomen van een token is afhankelijk van het vertrouwensniveau waarop een bericht wordt verstuurd, of er sprake is van een mandaat en welk specifiek uitwisselingsmechanisme wordt gebruikt.

### SAML2 tokens

Alle XIS-systemen hebben nu voor de authenticatietoken de SAML2 standaard gebruikt. Voor de authenticatie van burgers (patiënten) zijn we afhankelijk van DigiD, die ook op SAML2 is gebaseerd. Voor de FHIR REST interfaces worden SAML2 (authenticatie) ook ondersteund. Het SAML2 (authenticatie) token wordt in XML-vorm opgenomen in de SOAP header van het bericht. De hele SOAP envelop verdwijnt bij het gebruik van een (FHIR) REST service, omdat dit op HTTP gebaseerd is. Hierbij zullen de SAML2 (authenticatie) tokens verplaats worden naar de HTTP "authorization" header in Base64 gecodeerd. Dit heeft de volgende praktische beperkingen:

- de ontvanger van het bericht moet de HTTP "authorization" header eerst decoderen. Het LSP doet de SAML2 (authenticatie) token validatie en controleert of elementen uit het token corresponderen met elementen uit het bericht.

- in de HTTP standaard is er geen beperking aan de grootte van headers, maar in de praktijk hebben verschillende webservers helaas wel een limiet op de de grootte van headers.

- Het SAML2 token verwijst naar bepaalde HL7v3 elementen (zoals triggerEventID). Niet al deze elementen uit HL7v3 hebben een gelijksoortig element in FHIR. De specificaties/implementatiehandleiding van de tokens zal voor FHIR/REST uitwisseling daarom sowieso aangepast moeten worden.

In de huidige opzet zou het meesturen van 1 of meerdere SAML2 "assertions" (beweringen) tokens in de HTTP header van het FHIR verzoek mogelijk zijn. HTTP-headers kennen een beperkte grootte. Bij grotere en meerdere tokens zullen we moeten overgaan op een ander protocol. Webservers kunnen bij een te grootte datavolume de informatie in de HTTP headers niet verwerken. De combinatie van SAML2 en REST is voor de XIS-leveranciers mogelijk ook een blokkerend punt, omdat SAML2 gezien kan worden als een legacy-protocol.
