[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBZ AORTA_Auth_IH_Berichtauthenticatie_Transactietoken](../gbz-aorta_auth_ih_berichtauthenticatie_transactiet.md)

# Het SAML transactietoken

In dit hoofdstuk wordt de inhoud en het gebruik van het **SAML-transactietoken** besproken, zoals dat wordt toegepast bij berichtauthenticatie met behulp van een gekwalificeerd persoonscertificaat of servercertificaat. Het **SAML-transactietoken** is een XML-gebaseerde **SAML-assertion** die dient als bewijs (assertion) van de authenticatie en identificatie van een zorgverlener, medewerker, of organisatie.

Het token speelt een cruciale rol in het beveiligen van gegevensuitwisselingen tussen zorginformatiesystemen en het Landelijk Schakelpunt (LSP), en ondersteunt de integriteit en betrouwbaarheid van transacties in de zorg. Het is specifiek ontworpen om te voldoen aan de eisen voor gegevensbescherming en privacy, zoals vastgelegd in de NEN7510- en NEN7518-normen.

Alle XML voorbeelden in het document dienen door de betrokken partijen tijdens het bouwen van de uitwisseling getest, en waar nodig, in samenspraak met VZVZ aangepast te worden voor een juiste optimale werking.

De **SAML-transactietoken** wordt gebruikt bij verschillende koppelvlakken, zoals:

- **AORTA/LSP**: Goed Beheerd Zorgsysteem (GBZ) – het Landelijk SchakelPunt (LSP)

- **Mitz**: Toestemmingsbeheer en

- **AoF**: Aorta on FHIR (RESTful API's)

Hierbij worden de volgende transport mechanismes gebruikt:

- **WSS (Web Service Security) SOAP-berichtenprofiel**Dit profiel faciliteert het veiligstellen en uitwisselen van authentieke SOAP-berichten tussen een Goed Beheerd Zorgsysteem (GBZ) en het LSP.Het token wordt gebruikt om de afzender te authentiseren en het bericht te autoriseren.

- **FHIR RESTful-interacties** Voor omgevingen die gebruikmaken van (FHIR) REST-API’s, zoals in **AORTA on FHIR**, wordt de SAML-assertion meegegeven in de HTTP-header, bijvoorbeeld in een `Authorization` header. Hier wordt vaak gebruik gemaakt van een combinatie van **SAML** en **JWT** (JSON Web Token) voor compatibiliteit met moderne infrastructuren.

- **SAML assertion via HTTP-payload**Hier wordt de SAML-assertion in de body van een HTTP-verzoek opgenomen, als onderdeel van een JSON- of XML-structuur, bv in een JSON payload: `"samlAssertion": "<Base64-encoded-SAML-assertion>"`

Voor het verkrijgen van het SAML-transactietoken en het aanbieden van dit token aan systemen worden de volgende profielen gebruikt:

- Het gebruik van het SAML transactietoken (security token) in het kader van het WSS SOAP berichten profiel voor het veilig stellen en uitwisseling van authentieke SOAP berichten.

- Het gebruik van het SAML transactietoken (security token) in het kader AORTA on FHIR berichten profiel voor het veilig stellen en uitwisseling van authentieke FHIR berichten.

De profielen worden in de volgende paragrafen verder uitgewerkt.

### Het gebruik van OID in SAML-assertions.

Een **OID** (Object Identifier) is een unieke identificatie die wordt gebruikt om objecten of entiteiten te identificeren binnen verschillende technische systemen, met name in de wereld van cryptografie, certificaatbeheer, netwerken en softwareontwikkeling. OID's worden vaak gebruikt om standaardconfiguraties, waarden, of zelfs certificaatattributen te identificeren, zoals algoritmen, protocollen en sleutelomgevingen.

Een OID bestaat uit een reeks niet-negatieve gehele getallen, gescheiden door punten (bijv. **2.16.840.1.113883.2.4.3.111**VZVZ service centrum). Volgens de ITU-T X.690-standaard (die ASN.1 BER/DER-codering definieert) en ISO/IEC 9834-1:

Elk getal in de reeks moet zonder voorloopnullen worden weergegeven.  
Bijvoorbeeld, **2.16.84.01** is ongeldig, terwijl **2.16.840.1** correct is.  
Dit voorkomt ambiguïteit en zorgt voor een eenduidige representatie van OIDs in verschillende systemen.

Kenmerken van een OID:

- **Uniciteit**: OID's zijn wereldwijd uniek en worden vaak beheerd door officiële organisaties zoals ISO (International Organization for Standardization), IETF (Internet Engineering Task Force), of specifieke standaarden organisaties.

- **Hiërarchische structuur**: OID's volgen een hiërarchische structuur, waarbij elk segment van het nummer verwijst naar een specifieke subcategorie of entiteit. Dit maakt het mogelijk om complexe structuren van objecten te representeren.

- **Gebruik in certificaten**: OID's worden veel gebruikt in digitale certificaten en cryptografie. Bijvoorbeeld, een OID kan worden gebruikt om het type algoritme te identificeren in een digitale handtekening of om de extensies van een certificaat te definiëren.

- **Gebruik in LDAP en andere protocollen**: In LDAP (Lightweight Directory Access Protocol) en andere netwerksystemen worden OID's gebruikt om attributen of objectklassen te identificeren.

OID’s die worden gebruikt in SAML-assertions moet in het volgende formaat worden opgenomen, ongeacht of het een HL7v3- of FHIR-client is:

- `"urn:IIroot:"<OID voor het betreffende ID-stelsel>":IIext:"<gehanteerde ID binnen dit stelsel>`, bijvoorbeeld `"urn:IIroot:"2.16.528.1.1007.3.3":IIext:"<URA>`

Belangrijk hierbij is dat de <URA> hier een unieke identificatiecode is voor zorgverleners en gekoppeld is aan het **UZI-register**.

**Obsolete OID formaat**

Het volgende OID formaat is **Obsolete**.

"`urn:oid:"<OID voor het betreffende ID-stelsel>"."<gehanteerde ID binnen dit stelsel>`

`bijvoorbeeld`

"urn:2.16.528.1.1007.3.3."<URA>

## Structuur

Het SAML transactietoken is een afgegeven SAML-assertion die gebruikt wordt bij berichtauthenticatie met behulp van een gekwalificeerd persoonscertificaat of servercertificaat. Er wordt gebruik gemaakt van SAML v2.0 [SAML Core].

Het UZI-register en ZORG-ID hebben als doel zorgaanbieders bij elektronische communicatie en toegang tot gegevens uniek te identificeren. Zowel het UZI-register als ZORG-ID koppelt hiertoe op unieke wijze de fysieke identiteit aan een elektronische identiteit en legt deze vast in authenticiteit certificaten. Deze certificaten en de hierbij behorende cryptografische sleutels worden vastgelegd op de **smartcard**.

Bij het UZI-register heet dit de '**UZI-pas**' en bij ZORG-ID heet dit de '**ZORG-ID Smartcard**'.

### SAML-assertion

De SAML-assertion heeft de volgende structuur (de waarden die in het token gebruikt worden zijn fictief):

| **Element/@Attribute** ; | **Cardinaliteit** ; | **Omschrijving** ; | **Vaste waarde** ; |
| --- | --- | --- | --- |
| @ID ; | 1..1 ; | Unieke identificatie van de SAML-assertion. Een ID in XML mag NIET met een cijfer beginnen. Bij het gebruik van een UUID is het aan te raden een prefix te gebruiken, welke met een letter of underscore ('_') begint. ; |  |
| @Version ; | 1..1 ; | Versie van het SAML Protocol. ; | `"2.0"` ; |
| @IssueInstant ; | 1..1 ; | Tijdstip van uitgifte van de SAML-assertion. De tijdswaarde is gecodeerd in UTC (Universal Time Coordinated). UTC wordt gebruikt als referentie voor tijd over de hele wereld, en het vormt de basis voor de tijdzones. De UTC wordt weergegeven in het ISO 8601 formaat. ; |  |
| Issuer ; | 1..1 ; | Bevat het OrganisatieID van de zendende applicatie. Hiervoor wordt de URA (UZI-Register Abonneenummer) gebruikt voor identificatie en authenticatie van zorgaanbieders in elektronische communicatie binnen de zorg. ;  De OrganisatieID wordt uitgedrukt met behulp van een URN (Uniform Resource Name) omdat deze een organisatie formeel identificeert, zonder deze fysiek te lokaliseren. De URN string is opgebouwd uit een IIroot en een IIext. "II" staat voor het HL7v3 datatype Instance Indentifier. Om de namespace in URN uniek te krijgen is II als prefix voor de root en ext geplaatst. ;  `"urn:IIroot:"2.16.528.1.1007.3.3":IIext:"<URA>"` ; |  |
| Issuer.@NameQualifier ; | 0 ; | Niet gebruiken ; |  |
| Issuer.@SPNameQualifier ; | 0 ; | Niet gebruiken ; |  |
| Issuer.@Format ; | 1..1 ; | Geeft aan dat de inhoud van het element de identifier is van een entiteit die SAML-gebaseerde diensten levert (zoals een SAML-autoriteit, een requester of responder) of deelneemt aan SAML-profielen (zoals een serviceprovider die het browser-SSO-profiel ondersteunt). Een dergelijke identifier kan worden gebruikt in het <Issuer>-element om de afzender van een SAML-verzoek, -antwoord of -assertion te identificeren, of in het <NameID>-element om uitspraken te doen over systeementiteiten die SAML-verzoeken, -antwoorden en -assertions kunnen afgeven. Het kan ook worden gebruikt in andere elementen en attributen die bedoeld zijn om een systeementiteit te identificeren in verschillende protocoluitwisselingen. ; | `"urn:oasis:names:tc:SAML:2.0:nameid-format:entity"` ; |
| Issuer.@SPProviderID ; | 0 ; | Niet gebruiken ; |  |
| Signature ; | 1..1 ; | Een XML-handtekening die de responder authenticeert en de integriteit van het bericht garandeert. ;  AORTA/LSP en AoF: Bevat de handtekening over de SAML-assertion zoals gezet met behulp van de smartcard van de zorgverlener (Z) of de smartcard van de medewerker op naam(N). ;  Alleen in het geval van een conditionele query mag de handtekening ook gezet worden met het servercertificaat (S) van de applicatie. ;  MITZ: Bevat de handtekening over de SAML-assertion zoals gezet met behulp van het PKIo- servercertificaat van de Issuer. De handtekening dient geplaatst te zijn met behulp van een ander servercertificaat dan waarmee de TLS-sessie wordt opgezet. ; |  |
| Subject ; | 1..1 ; | AORTA/LSP en AoF: ;  De zorgverlener/medewerker die zich authentiseert. ;  MITZ: ;  Bevat de OrganisatieID van de zendende applicatie (zie Issuer) ; |  |
| Subject.BaseID ; | 0 ; | Niet gebruiken ; |  |
| Subject.NameID ; | 0..1 ; | AORTA/LSP en AoF: ;  Bevat zowel het UZI-nummer van de geauthentiseerde zorgverlener/medewerker alsmede diens rolcode. ; Alleen in het geval van de conditionele query, waarmee de handtekening met een servercertificaat wordt geplaatst, MOET dit veld leeggelaten worden. ;  MITZ: ;  De handtekening wordt gezet met een server certificaat en MOET leeg gelaten worden. ;  WIJZIGINGSVOORSTEL: Is bij het gebruik van een server certificaat, zoals bij MITZ, de URA te plaatsen, zodat de *zorgaanbieder* geïdentificeerd kan worden. ; |  |
| Subject.EncryptedID ; | 0 ; | Niet gebruiken ; |  |
| Subject.SubjectConfirmation ; | 1..1 ; | Moet aanwezig zijn ; |  |
| Subject.SubjectConfirmation@Method ; | 1..1 ; | Het Subject-element is verplicht en bij een naam identificator (NameID) gebruiken we een subjectbevestiging gebaseerd op bewijs van bezit van een sleutel. Ook als er geen naam identificator gebruikt wordt. ; | `"urn:oasis:names:tc:SAML:2.0:cm:holder-of-key"` ; |
| Subject.SubjectConfirmation.SubjectConfirmationData ; | 0 ; | Niet gebruiken ; |  |
| Subject.SubjectConfirmation.SubjectConfirmationData@Recipient ; | 0 ; | Niet gebruiken ; |  |
| Subject.SubjectConfirmation.SubjectConfirmationData@NotOnOrAfter ; | 0 ; | Niet gebruiken ; |  |
| Subject.SubjectConfirmation.SubjectConfirmationData@InResponseTo ; | 0 ; | Niet gebruiken ; |  |
| Subject.SubjectConfirmation.SubjectConfirmationData@NotBefore ; | 0 ; | Niet gebruiken ; |  |
| Subject.SubjectConfirmation.SubjectConfirmationData@Address ; | 0 ; | Niet gebruiken ; |  |
| Subject.SubjectConfirmation.SubjectConfirmationData.ds:KeyInfo.X509Data ; | 1..1 ; | Het element KeyInfo is onderdeel van het XML Signature schema. SAML vereist niet het gebruik van het KeyInfo element en legt geen beperkingen op aan het gebruik ervan. ;  Het element KeyInfo bevat informatie over het certificaat en de daarbij behorende sleutel die is gebruikt voor het zetten van de digitale handtekening over de SAML-assertion. ;  Het element KeyInfo.X509Data bevat certificaatinformatie in X.509-indeling. ;  AORTA/LSP, AoF en MITZ: ;  In dit geval bevat het de X.509 Issuer.Serial Number van de smartcard van de medewerker of het servercertificaat. ;  In alle X.509 versies moet het serienummer uniek zijn voor elk certificaat dat door een specifieke CA wordt uitgegeven (zoals vermeld in RFC 5280). ; |  |
| Conditions ; | 1..1 ; | Moet aanwezig zijn. Dit zijn de voorwaarden die MOETEN worden geëvalueerd bij het beoordelen van de geldigheid van en/of het gebruik van de SAML-assertion. ; |  |
| Conditions@NotBefore ; | 1..1 ; | Moet aanwezig zijn. Geeft het vroegste tijdstip aan waarop de SAML-assertion geldig is. De tijdwaarde wordt gecodeerd in UTC. ; |  |
| Conditions@NotOnOrAfter ; | 1..1 ; | Moet aanwezig zijn. Specificeert het moment waarop de SAML-assertion is verlopen. De tijdwaarde wordt gecodeerd in UTC. ;  AORTA/LSP en AoF: ;  Mag maximaal 90 minuten na @NotBefore liggen. ;  MITZ: ;  Mag maximaal 10 minuten na @NotBefore liggen. ;  WIJZIGINGSVOORSTEL: voor beide koppelvlakken: 90 minuten gebruiken. ; |  |
| Conditions.Condition ; | 0 ; | Niet gebruiken ; |  |
| Conditions.AudienceRestriction ; | 1..1 ; | Moet aanwezig zijn. Geeft aan dat de SAML-assertion gericht is aan een specifiek publiek. ; |  |
| Conditions.AudienceRestriction.Audience ; | 1..1 ; | Bij AORTA/LSP en AoF: ;  `urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:1`(1 is de applicatie-id van de ZIM) ;  Bij MITZ ;  `"urn:oid:2.16.840.1.113883.2.4.3.111.2.1"`(is MITZ) ;  **WIJZIGINGSVOORSTEL**: ;  De verschillende Audience samenvoegen en er ;  `<saml:Audience>urn:generic:audience</saml:Audience>` ;  van maken. ; | `<saml:Audience>` ; `urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:1` ; `</saml:Audience>` ; `<saml:Audience>` ; `urn:oid:2.16.840.1.113883.2.4.3.111.2.1` ; `</saml:Audience>` ; |
| Conditions.ProxyRestriction ; | 0 ; | Niet gebruiken ; |  |
| Conditions.Advice ; | 0 ; | Niet gebruiken ; |  |
| AuthnStatement ; | 1..1 ; | Moet aanwezig zijn. Beschrijft een verklaring van de SAML-autoriteit waarin wordt bevestigd dat het subject van de verklaring op een specifieke manier op een bepaald moment is geauthentiseerd. Verklaringen die `<AuthnStatement>`-elementen bevatten, MOETEN een `<Subject>`-element bevatten. ; |  |
| AuthnStatement@AuthnInstant ; | 1..1 ; | Geeft het tijdstip aan waarop de authenticatie (van de gebruiker of applicatie) heeft plaatsgevonden. De tijdwaarde wordt gecodeerd in UTC. ; |  |
| AuthnStatement@SessionIndex ; | 0 ; | Niet gebruiken ; |  |
| AuthnStatement.AuthnContext ; | 1..1 ; | Moet aanwezig zijn. De context die door de authenticerende autoriteit is gebruikt tot en met het authenticatie-evenement dat tot deze verklaring heeft geleid. Bevat een verwijzing naar een authenticatiecontextklasse, een verklaring van de authenticatiecontext of een verwijzing naar een verklaring, of beide. Raadpleeg de specificatie van de Authentication Context [SAMLAuthnCxt] voor een volledige beschrijving van informatie over de authenticatiecontext. ; |  |
| AuthnStatement.AuthnContext.AuthnContextClassRef ; | 1..1 ; | In het AuthnRequest wordt in het element AuthnContextClassRef het minimaal vereiste *betrouwbaarheidsniveau* meegegeven. Om de betrouwbaarheidsniveaus in de berichten mee te geven bevat het element AuthnContext een van de volgende declarations. ;  **Laag**: "`urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport`" ;  **Midden**: "`urn:oasis:names:tc:SAML:2.0:ac:classes:MobileTwoFactorContract`" ;  **Substantieel**: "`urn:oasis:names:tc:SAML:2.0:ac:classes:Smartcard`" of "`urn:oasis:names:tc:SAML:2.0:ac:classes:X509`" ;  **Hoog**: "`urn:oasis:names:tc:SAML:2.0:ac:classes:SmartcardPKI`" ;  De aanbieder moet controleren of het betrouwbaarheidsniveau in de ontvangen SAML-assertion voldoet aan het minimaal gevraagde betrouwbaarheidsniveau. ; | Ingeval van ondertekening met smartcard: "`urn:oasis:names:tc:SAML:2.0:ac:classes:SmartcardPKI`" ; Ingeval van ondertekening met UZI-server certificaat: "`urn:oasis:names:tc:SAML:2.0:ac:classes:X509`" ; |
| AttributeStatement ; | 1..1 ; | Moet aanwezig zijn. Beschrijft een verklaring van de SAML-autoriteit waarin wordt bevestigd dat het subject van de verklaring is gekoppeld aan de gespecificeerde attributen. ;  Verklaringen die `<AttributeStatement>`-elementen bevatten, MOETEN een `<Subject>`-element bevatten. ; |  |
| AttributeStatement.Attribute ; | 0..1 ; | Moet aanwezig zijn indien bericht aan één patiënt is gerelateerd. ; |  |
| AttributeStatement.Attribute@Name ; | 1..1 ; | Vaste waarde "patientIdentifier" of de oude waarde "burgerServiceNummer" wat door MITZ ondersteund wordt. ; | "patientIdentifier" of "burgerServiceNummer" ; |
| AttributeStatement.Attribute.AttributeValue ; | 0..1 ; | ID van de patiënt (BSN, hash van BSN of COA nummer). ;  Verplicht bij patiëntgebonden interacties. Anders afwezig. ;  Formaat van een patientIdentifier: ;  "urn:IIroot:"2.16.840.1.113883.2.4.6.3":IIext:"<BSN>" ;  Formaat van een hash van een patientIdentifier: ;  "urn:IIroot:"2.16.840.1.113883.2.4.3.111.4":IIext:"<BSN>" ;  Formaat van een COA nummer: ;  `"urn:IIroot:"2.16.840.1.113883.2.4.3.111.6":IIext:"<BSN>"` ;  Let op! Indien “burgerServiceNummer” wordt gebruikt als attribuut, dan zal de root OID niet zijn opgenomen in de attribuutwaarde, maar slechts het BSN. ; |  |
| AttributeStatement.Attribute ; | 0..1 ; | Moet aanwezig zijn bij AORTA/LSP en AoF ; |  |
| AttributeStatement.Attribute@Name ; | 1..1 ; | Vaste waarde: "messageIdRoot" ; | "messageIdRoot" ; |
| AttributeStatement.Attribute.AttributeValue ; | 1..1 ; | De waarde van de messageIdRoot bijvoorbeeld: ;  "`2.16.840.1.113883.2.4.3.111.15.4`" (AORTA RequestID) ; |  |
| AttributeStatement.Attribute ; | 0..1 ; | Moet aanwezig zijn bij AORTA/LSP en AoF ; |  |
| AttributeStatement.Attribute@Name ; | 1..1 ; | Vaste waarde: "messageIdExt" ; | "messageIdExt" ; |
| AttributeStatement.Attribute.AttributeValue ; | 1..1 ; | Het MessageId van het bericht. Dit is de waarde van het requestID dat zal worden meegestuurd in de AORTA-ID HTTP header. ; |  |
| AttributeStatement.Attribute ; | 0..1 ; | Moet aanwezig zijn bij AORTA/LSP en AoF ; |  |
| AttributeStatement.Attribute@Name ; | 1 ; | Vaste waarde: "InteractionId" ; | "InteractionId" ; |
| AttributeStatement.Attribute.AttributeValue ; | 1 ; | Het InteractionId van het Bericht (het extension-element). ; |  |
| AttributeStatement.Attribute ; | 0..1 ; | Moet aanwezig zijn bij de Generieke Query van AORTA/LSP en AoF ; |  |
| AttributeStatement.Attribute@Name ; | 1 ; | Vaste waarde: "contextCodeSystem" ; | "contextCodeSystem" ; |
| AttributeStatement.Attribute.AttributeValue ; | 0..1 ; | "`2.16.840.1.113883.2.4.3.111.15.1`" (AORTA Contextcodes) ; | "2.16.840.1.113883.2.4.3.111.15.1" ; |
| AttributeStatement.Attribute ; | 0..1 ; | Moet aanwezig zijn bij de Generieke Query van AORTA/LSP en AoF ; |  |
| AttributeStatement.Attribute@Name ; | 1..1 ; | Vaste waarde: "contextCode". De contextcode die aanduidt binnen welke (zorg)toepassing de (FHIR)-interactie word geïnitieerd. ; | "contextCode" ; |
| AttributeStatement.Attribute.AttributeValue ; | 0..1 ; | De contextcode uit de Generieke query. bijv. "BGZ", of "MEDGEGTOT". ; |  |
| AttributeStatement.Attribute ; | 0..1 ; | De scope waarop het transactietoken betrekking heeft. Wordt bij AoF gebruikt. ; |  |
| AttributeStatement.Attribute@Name ; | 1..1 ; | "scope" ; | "scope" ; |
| AttributeStatement.Attribute.AttributeValue ; | 1..1 ; | Bijvoorbeeld: ;  patient/Patient.s (verzamelen BGZ) ;  patient/Observation.s (verzamelen meetwaarden) ;  ... ; |  |
| AttributeStatement.Attribute ; | 0..1 ; | Moet aanwezig zijn indien gebruik gemaakt is van een mandaat ; |  |
| AttributeStatement.Attribute@Name ; | 1 ; | Vaste waarde: "autorisatieregel/context" ; | "autorisatieregel/context" ; |
| AttributeStatement.Attribute.AttributeValue ; | 0..1 ; | URI waar de autorisatieregel/context gevonden kan worden waarbinnen het mandaat gegeven wordt. ;  Moet aanwezig zijn indien gebruik gemaakt is van een mandaat. ;  Lokaal is vastgelegd dat een bepaald mandaat daadwerkelijk door een mandaatverlener is toegekend aan een bepaald persoon/systeem. ; |  |
| AttributeStatement.Attribute ; | 0..1 ; | Moet aanwezig zijn indien gebruikt wordt binnen AORTA infrastructuur (AORTA/LSP en AoF) ; |  |
| AttributeStatement.Attribute@Name ; | 1..1 ; | Vaste waarde: "applicationID" ; | "applicationID" ; |
| AttributeStatement.Attribute.AttributeValue ; | 0..1 ; | AORTA ApplicatieID van de (GBx) applicatie ;  Formaat van een applicatie-id: ;  `"urn:IIroot:"2.16.840.1.113883.2.4.6.6":IIext:"<applicatie-id>"` ; |  |
| AttributeStatement.Attribute ; | 0..1 ; | De versie van de tokendefinitie die wordt gehanteerd. Geïntroduceerd bij AoF. Verplicht bij gebruik van deze versie van het token (Feature versie >= 2.1). ; |  |
| AttributeStatement.Attribute@Name ; | 1..1 ; | Vaste waarde: "tokenVersion" ; | "tokenVersion" ; |
| AttributeStatement.Attribute.AttributeValue ; | 1..1 ; | Formaat: “<major versie>.<minor versie>”, conform semver. ; |  |

N.B.: bovenstaande tabel bevat de meest gebruikte elementen van SAML assertions en is derhalve niet volledig. Voor niet genoemde elementen geldt: Niet gebruiken.

## Namespaces

Het SAML transactietoken die gebruikt wordt bij berichtauthenticatie maakt gebruik van de volgende namespaces. De prefixen zijn niet normatief maar worden in dit document als voorbeelden gebruikt.

**Tabel AORTA.STK.t3300 – Namespaces**

| **Prefix** ; | **Namespace URI** ; |
| --- | --- |
| ds ; | http://www.w3.org/2000/09/xmldsig# ; |
| saml ; | urn:oasis:names:tc:SAML:2.0:assertion ; |
| wss ; | http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd ; |

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Bij het gebruik van de namespace-prefixes is het van belang deze na het ondertekenen niet meer te veranderen, dit maakt de digitale handtekening ongeldig. ; |
| --- | --- |

## Inhoud

De volgende paragrafen beschrijven de verschillende kenmerken en beveiliging gerelateerde gegevens die het SAML transactietoken onderscheiden, zoals in [IH tokens generiek] beschreven is.

```
<saml:Assertion ... xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">
```

Het SAML transactietoken begint met het Assertion element en een verwijzing naar de XML SAML namespace voor SAML 2.0 assertions. De attributen behorende bij het Assertion element wordt in [paragraaf 2.3.1](het-saml-transactietoken.md#uniekheid) Uniekheid beschreven.

### Uniekheid

```
ID="token_ dd1c1f96-f0b0-4026-a978-4d724c0a0a4f"

IssueInstant="2009-06-24T11:47:34Z"

Version="2.0">
```

De volgende attributen van het SAML assertion element maken van de SAML assertion een uniek gegeven, uitgegeven door de verzender van het bericht. Het attribuut ID identificeert op een unieke wijze de assertion. De assertion mag slechts eenmalig als token gebruikt worden. De waarde moet *mondiaal uniek* zijn voor AORTA berichten, zodat bij samenvoegen van meerdere XML bestanden (in een HL7v3 batch of anderszins) de waarde uniek blijft.

Het wordt aanbevolen een UUID (Universally Unique Identifier) te gebruiken. Bij het gebruik van andere vormen is er een kans, hoe klein ook, dat een ID samenvalt met een ID gemaakt volgens een andere methode van een andere leverancier).

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Een ID in XML mag niet met een cijfer beginnen. Bij het gebruik van een UUID is het dus aan te raden een prefix te gebruiken, welke met een letter of underscore ('_') begint. ; |
| --- | --- |

Het attribuut IssueInstant is een tijdsmoment van uitgifte van de SAML assertion. De tijdswaarde is gecodeerd in UTC. Het attribuut Version is de gebruikte SAML versie van de SAML assertion. De aanduiding voor de versie van SAML gedefinieerd in deze specificatie is "2.0".

### Afzender

```
<saml:Issuer>

 <!-- De Issuer verwijst naar de organisatie van waaruit het totale bericht verstuurd wordt.-->

     urn:IIroot:2.16.528.1.1007.3.3:IIext:12345678

</saml:Issuer>
```

De URA wordt uitgedrukt met behulp van een URN (Uniform Resource Name). De URN is opgebouwd uit:

"urn:IIroot:"<OID voor UZI organisatieIds>":IIext:"<URA>

De URN string is opgebouwd uit een IIroot en een IIext. "II" staat voor het HL7v3 datatype Instance Indentifier. Om de namespace in URN uniek te krijgen is II als prefix voor de root en ext geplaatst.

URA’s worden uitgedrukt als een id onder het identificatiesysteem “2.16.528.1.1007.3.3”. De URA wordt toegekend door het UZI-register. Stel dat de URA de waarde “12345678” heeft, dan ziet de URN er als volgt uit:

urn:IIroot:**2.16.528.1.1007.3.3**:IIext:**12345678**

### Onderwerp

```
<saml:Subject>

  <saml:NameID>

   123456789:01.015

  </saml:NameID>

  <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:holder-of-key">

     <saml:SubjectConfirmationData>

       <saml:KeyInfo>

         <ds:X509Data>

           <ds:X509IssuerSerial>

             <ds:X509IssuerName>CN=...,...,O=...,C=NL</ds:X509IssuerName>

             <ds:X509SerialNumber>...834756977854956...</ds:X509SerialNumber>

            </ds:X509IssuerSerial>

          </ds:X509Data>

        </saml:KeyInfo>

      </saml:SubjectConfirmationData>

  </saml:SubjectConfirmation>

</saml:Subject>
```

De Subject verwijst naar het UZI-nummer van de zorgverlener/medewerker die de assertion heeft gegenereerd in combinatie met de rolcode van diezelfde zorgverlener/medewerker gescheiden door een dubbele punt (:). Voor de zorgverlener en de medewerker op naam is het UZI-nummer uniek gekoppeld aan de natuurlijk persoon.

Alleen in het geval van een conditionele query (een query die automatisch door het systeem verstuurd wordt) mag het nameID-element leeg gelaten worden.

In het geval van een conditionele query dient tevens een Mandaattoken [Mandaattoken] en een Inschrijftoken [Inschrijftoken] in het bericht opgenomen te zijn.

Vervolgens moet de SubjectConfirmation / SubjectConfirmationData / KeyInfo nog toegevoegd worden. Deze KeyInfo dient te verwijzen naar het certificaat waarmee het token ondertekend is.

Voor een beschrijving van de opbouw van de KeyInfo wordt verwezen naar [hoofdstuk 4.4.3](../gbx-aorta_auth_ih_security_tokens_generiek/digitaal-tekenen.md#certificaatverwijzingen) Certificaatverwijzingen in document [IH tokens generiek].

### Geldigheid

```
saml:Conditions

 NotBefore="2009-06-24T11:47:34Z"

 NotOnOrAfter="2009-06-24T11:52:34Z">
```

Het attribuut *NotBefore* is de tijd waarop de SAML assertion geldig wordt. Dit hoeft niet de tijd te zijn waarop het bericht is aangemaakt. Het is mogelijk *NotBefore* in de toekomst te zetten, en het bericht na deze tijd pas te verzenden.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Wordt een bericht ontvangen voor *NotBefore* is aangevangen, dan **moet** dit bericht geweigerd worden. ; |
| --- | --- |

Het attibuut *NotOnOrAfter* is de tijd waarop de SAML assertion vervalt.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Wordt een bericht ontvangen op of nadat *NotOnOrAfter* is verstreken, dan **moet** dit bericht geweigerd worden. ; |
| --- | --- |

Deze tijd is als bovenstaande tijd geformatteerd. Richtlijn voor het verschil tussen *NotBefore* en *NotOnOrAfter* is 5 minuten. Het maximaal toegestane verschil is 90 minuten. Dit maximum dient voor berichten die niet direct, maar bijvoorbeeld 's nachts verzonden worden, of kort voor de aanvang van een consult, zodat er iets ruimere mogelijkheden voor batchgewijze processen zijn. Het wordt sterk aanbevolen de SAML assertion direct (binnen 5 minuten) te gebruiken voor berichten die verzonden worden (dus terwijl de zorgverlener of medewerker achter diens computer zit). Het gaat immers om het voorkomen van misbruik van onderschepte tokens, en 5 minuten is meer dan voldoende om de hele keten van vraag tot antwoord te doorlopen.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | De geldigheidsduur van een token (*NotOnOrAfter* minus *NotBefore*) mag niet langer dan 90 minuten zijn. Wordt een bericht ontvangen waarin deze geldigheidsduur overschreden is, dan **moet** dat bericht geweigerd worden, ook al is het tijdstip *NotOnOrAfter* nog niet verstreken. ; |
| --- | --- |

Het inperken van bepaalde partijen (AudienceRestriction) waarvoor de assertion bedoeld is wordt beschreven in [paragraaf 2.3.5](het-saml-transactietoken.md#ontvanger) Ontvanger.   
De subelementen OneTimeUse en ProxyRestriction worden niet gebruikt binnen het <Conditions> element bij berichtauthenticatie met behulp van de smartcard, gebaseerd op PKI.

### Ontvanger

```
<saml:AudienceRestriction>

  <!-- Root en extensie van de ZIM -->

  <saml:Audience>urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:1</saml:Audience>

</saml:AudienceRestriction>
```

In de AudienceRestriction wordt beschreven aan wie de SAML assertion is gericht. De waarden in de elementen zijn (voorlopig) vaste waarden. Voor de <Audience> parameter is (ook) gekozen voor URN, zie voor opbouw [paragraaf 2.3.2](https://vzvz.atlassian.net/wiki/spaces/AORTA84/pages/879593488/Het+SAML+transactietoken#HetSAMLtransactietoken-Afzender) Afzender.

### Authenticatie

```
<saml:AuthnStatement

 AuthnInstant="2009-06-24T11:47:34"

 SessionIndex="token_2.16.528.1.1007.3.3.1234567.1_0123456789">
```

Het subject, een zorgverlener of medewerker, in de SAML assertion is geauthenticeerd door middel van een authenticatiemiddel op een gegeven moment.

```
<saml:AuthnContext>

  <saml:AuthnContextClassRef>

      urn:oasis:names:tc:SAML:2.0:ac:classes:SmartcardPKI

  </saml:AuthnContextClassRef>

</saml:AuthnContext>
```

Als het transactietoken ondertekend is met het servercertificaat dan dient de AuthnContextClassRef de waarde urn:oasis:names:tc:SAML:2.0:ac:classes:X509 te krijgen .

Binnen de gebruikte applicatie beveiligingsstandaarden is er sprake van verschillende vertrouwensniveaus.

Binnen de SAML-specificatie geeft men een authenticatie-context (*AuthnContext*) mee die de context van het gebruikte authenticatiemiddel aangeeft. Hiervoor zijn een aantal contexten gespecificeerd, zie [SAMLAuthnContext], die gebruikt worden als referentiekader voor de communicatie tussen de ZIM en andere componenten zoals GBZ applicaties.

```
</saml:AuthnStatement>
```

Afsluiting authentication statement.

### Attributen

```
<saml:AttributeStatement>
```

De volgende attributen zijn gegevens uit het HL7v3 bericht die met de authenticatie meegetekend worden. Dit zijn kopieën van gegevens die elders in hetzelfde HL7v3 bericht voorkomen. De volgorde van de attributen in het AttributeStatement is niet relevant. Er mogen geen andere attributen opgenomen worden in het AttributeStatement dan hier beschreven is.

**InteractionId**

```
<saml:Attribute Name="interactionId">

  <saml:AttributeValue>QURX_IN990011NL</saml:AttributeValue>

</saml:Attribute>
```

Het attribuut interactionId wordt altijd meegetekend. De interactionId geeft een directe relatie met het berichttype. Dit attribuut meesturen verhindert veel soorten aanvallen, bijvoorbeeld het token van een query kapen en proberen deze te hergebruiken voor het afhandelen van verzoeken van patiënten en hun vertegenwoordigers om inzage te verkrijgen in de verwijsindex.

**contextCode**

```
<saml:Attribute Name="contextCodeSystem">

  <saml:AttributeValue>2.16.840.1.113883.2.4.3.111.15.1</saml:AttributeValue>

</saml:Attribute>

<saml:Attribute Name="contextCode">

  <saml:AttributeValue>KZDI</saml:AttributeValue>

</saml:Attribute>
```

In het geval er sprake is van een opvraag op basis van een context dient ook de contextCode meegetekend te worden. Dit is in principe alleen het geval bij de generiekeQueryZorggegevens. Bij deze generieke query is het trigger event niet meer voldoende om de intentie van de verzender aan te geven, aangezien deze altijd gelijk is. Door het toevoegen van de contextCode wordt deze intentie wel weer expliciet gemaakt. De codes zijn te vinden in het vocab bestand 2.16.840.1.113883.2.4.3.111.15.1.xml.

**messageId**

```
<saml:Attribute Name="messageIdRoot">

  <saml:AttributeValue>2.16.528.1.1007.3.3.1234567.1</saml:AttributeValue>

</saml:Attribute>

<saml:Attribute Name="messageIdExt">

  <saml:AttributeValue>0123456789</saml:AttributeValue>

</saml:Attribute>
```

De Attributen messageIdRoot en messageIdExt vormen een uniek gegeven, uitgegeven door de verzender van het HL7v3-bericht. De combinatie van de attribuutwaarden messageIdRoot en messageIdExt moeten gelijk zijn aan het uiteindelijk gebruikte HL7v3 message.Id.

**burgerServiceNummer**

```
<saml:Attribute Name="burgerServiceNummer">

  <saml:AttributeValue>950052413</saml:AttributeValue>

</saml:Attribute>
```

Voor berichten die betrekking hebben op een enkele patiënt, wordt het burgerServiceNummer (BSN) van de patiënt opgenomen. Dit maakt ook weer vele aanvallen onmogelijk, namelijk gegevens van een andere patiënt proberen op te vragen. Dit geldt voor alle berichten die betrekking hebben op één en niet meer dan één patiënt.

Het BSN in het token moet overeenkomen met het BSN in het bericht. In het geval er sprake is van een voorloopnul in het bericht, dan dient deze ook overgenomen te worden in het token.

Voor berichten die geen betrekking hebben op een persoon waarvan het burgerServiceNummer bekend is, wordt het burgerServiceNummer weggelaten. Hierbij zijn twee situaties te onderscheiden:

- Logistieke berichten; het bericht betreft géén informatie gerelateerd tot een specifieke patiënt;

- Medische berichten; het bericht betreft medische informatie gerelateerd tot een specifieke patiënt(en), maar waarvan het BSN niet bekend is. In de implementatiehandleiding van een zorgtoepassing zal bij de betreffende interactie expliciet benoemd staan, dat een patiëntidentificatie niet voorkomt of optioneel is.

**autorisatieregel/context**

Alleen indien gebruik gemaakt wordt van een mandaat dient het volgende attribuut toegevoegd te worden:

```
<saml:Attribute Name="autorisatieregel/context">

  <saml:AttributeValue>https://goedbeheerdziekenhuis/autorisatieregels/medicatiecontext/v2 </saml:AttributeValue>

</saml:Attribute>
```

In het voorbeeld is voor een URL gekozen.

**applicationID**

Indien het transactietoken gebruikt wordt binnen de AORTA infrastructuur is het applicatieID verplicht:

```
<saml:Attribute Name="applicationID">

<!-- Applicatie-id van de GBZ-applicatie, zoals toegekend bij aansluiting.-->

<saml:AttributeValue>urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:? </saml:attributeValue>

</saml:Attribute>
```

Het applicatie-id van de afzender die deze SAML assertion heeft gecreëerd en de gebruiker authenticeert. De Issuer wordt uitgedrukt met behulp van een URN (Uniform Resource Name). De URN is opgebouwd uit:

"urn:IIroot:"<OID voor AORTA Applicatie-id’s>":IIext:"<applicatie-id GBZ>

De URN string is opgebouwd uit een IIroot en een IIext. "II" staat voor het HL7v3 datatype Instance Indentifier. Om de namespace in URN uniek te krijgen is II als prefix voor de root en ext geplaatst.

AORTA Applicatie-id’s worden uitgedrukt als een id onder het identificatiesysteem “2.16.840.1.113883.2.4.6.6”. Het correcte applicatie-id voor de GBZ-applicatie wordt toegekend bij aansluiting op de AORTA. Stel dat dit “300” zou zijn, dan ziet de URN er als volgt uit:

urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:300

**attributeStatement blok**

Het attributen statement blok ziet er dan bijvoorbeeld zo uit (de volgorde van de attributen is niet relevant):

```
<saml:AttributeStatement>

  <saml:Attribute Name="interactionId">

   <saml:AttributeValue>QURX_IN990011NL</saml:AttributeValue>

  </saml:Attribute>

  <saml:Attribute Name="messageIdRoot">

   <saml:AttributeValue>2.16.528.1.1007.3.3.1234567.1</saml:AttributeValue>

  </saml:Attribute>

  <saml:Attribute Name="messageIdExt">

   <saml:AttributeValue>0123456789</saml:AttributeValue>

  </saml:Attribute>

  <saml:Attribute Name="burgerServiceNummer">

   <saml:AttributeValue>950052413</saml:AttributeValue>

  </saml:Attribute>

  <saml:Attribute Name="autorisatieregel/context">    
    
   <saml:AttributeValue>https://goedbeheerdziekenhuis/autorisatieregels/medicatiecontext/v2</saml:AttributeValue>

  </saml:Attribute>

  <saml:Attribute Name="applicationID">

   <saml:AttributeValue>urn:IIroot:2.16.840.1.113883.2.4.6.6:IIext:300

   </saml:AttributeValue>

  </saml:Attribute>

</saml:AttributeStatement>
```

Tenslotte wordt het attributen statement blok afgesloten met

</saml:AttributeStatement>

## Algoritmes

Om de integriteit en onweerlegbaarheid van het SAML transactietoken te waarborgen wordt een XML Signature geplaatst, zoals beschreven in [IH tokens generiek]. Na plaatsen van de XML Signature kan de ontvanger, met gebruikmaking van het persoons- of organisatiegebonden authenticiteit certificaat van de verzender en de CA certificaten gebaseerd op PKI , onomstotelijk vaststellen dat het SAML transactietoken ondertekend is met de privé sleutel behorend bij het gebruikte authenticiteit certificaat van de zorgmedewerker of de organisatie.

De XML Signature van het SAML transactietoken die gebruikt wordt bij berichtauthenticatie met behulp van een authenticiteit certificaat, gebaseerd op PKI, maakt gebruik van de volgende algoritmes, zoals beschreven in [IH tokens generiek]:

- Voor het berekenen van de hashwaarde wordt SHA-256 gebruikt.

- Voor de digitale handtekening in AORTA wordt gebruik gemaakt van een RSA handtekening over een SHA-256 digest.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Omdat de XML Signature onderdeel is van het SAML transactietoken en in het SAML transactietoken geplaatst wordt, moet er een "enveloped-signature" transformatie uitgevoerd worden die de Signature tags uit het SAML transactietoken verwijderd gevolgd door een “exc-c14n transformatie” (zie ook [SAML Core] §5.4.3 en §5.4.4). ; |
| --- | --- |

## Opbouw

### De headers

Eerst wordt het SAML transactietoken – het <saml:Assertion ...> element aangemaakt en gevuld met die elementen, zoals beschreven in [paragraaf 2.3](https://vzvz.atlassian.net/wiki/spaces/AORTA84/pages/879593488/Het+SAML+transactietoken#HetSAMLtransactietoken-Inhoud) Inhoud.

```
<saml:Assertion

   ID="token_2.16.528.1.1007.3.3.1234567.1_0123456789"

   IssueInstant="2009-06-24T11:47:34Z"

   Version="2.0"

   xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">

 ... Zie paragraaf 2.3 Inhoud ...

</saml:Assertion>
```

Het XML Signature blok is onderdeel van het SAML transactietoken. Het XML Signature blok komt na het <saml:Issuer> element. Na de Signature volgt de rest van de inhoud van de assertion.

```
<saml:Assertion

   ID="token_2.16.528.1.1007.3.3.1234567.1_0123456789"

   IssueInstant="2009-06-24T11:47:34Z"

   Version="2.0"

   xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">

  <saml:Issuer Format="urn:oasis:names:tc:SAML:2.0:nameid-format:entity">

   urn:IIroot:?:IIext:?

  </saml:Issuer>

  <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">

    <ds:SignedInfo>

    ...

    </ds:SignedInfo>

    <ds:SignatureValue>Wuwn...5e4=</ds:SignatureValue>

    <ds:KeyInfo>

      <ds:X509Data>

        <X509IssuerSerial>

          <X509IssuerName>CN=De Auteur CA,O=Nictiz,C=NL</X509IssuerName>

          <X509SerialNumber>359724...41160195</X509SerialNumber>        

        </X509IssuerSerial>

       </ds:X509Data>

    </ds:KeyInfo>

  </ds:Signature>  ...

  ... Zie paragraaf 2.3 Inhoud ...

</saml:Assertion>
```

Indien de Signature aangemaakt wordt moet niet meer met de strings (saml:Assertion en SignedInfo) gemanipuleerd worden, maar ze moeten octet-voor-octet overgenomen worden in het bericht. Strikt genomen is het toegestaan wijzigingen aan te brengen die door canonicalisatie bij de ontvanger weer opgeheven worden, maar wanneer de digitale handtekening door middel van strings wordt opgebouwd, is het een foutgevoelige handeling.

Lange Base 64 waarden zijn in het voorbeeld afgekort. Wederom kan dit als strings worden behandeld, waarbij drie waarden vervangen moeten worden.

Deze drie waarden worden ingevuld:

- Neem het SignedInfo blok op.

- Neem de SignatureValue op.

- Neem certificaatgegevens in het KeyInfo blok op, in de vorm van een verwijzing (X509IssuerSerial).

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Wanneer een bericht een SAML assertion bevat, moet dat bericht precies één bijbehorende digitale handtekening bevatten. ; |
| --- | --- |

Het maken van de XML Signature uit strings levert de SAML assertion op met daarin de Signature.

### Plaats van het SAML token en de digitale handtekening

Het SAML transactietoken met daarin de digitale handtekening wordt in het WS-Security SOAP Header gezet. Op het <wss:Security> element **moet** een soap:mustUnderstand="1" vlag opgenomen worden, die aangeeft dat de ontvanger dit security element **moet** verwerken en een soap:actor="[http://www.aortarelease.nl/actor/zim](http://www.aortarelease.nl/actor/zim)" die aangeeft dat de ZIM dit security element verwerkt.

```
<soap:Header xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

  ...

  <wss:Security xmlns:wss=

    "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"

    soap:actor="http://www.aortarelease.nl/actor/zim" soap:mustUnderstand="1">

       <saml:Assertion ... >

       <saml:Issuer>...</saml:Issuer>

       <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">

        <ds:SignedInfo>

        ...

        </ds:SignedInfo>

        <ds:SignatureValue>Wuwn...5e4=</ds:SignatureValue>

        <ds:KeyInfo>

          <ds:X509Data>

          ...

          </ds:X509Data>

        </ds:KeyInfo>

       </ds:Signature>

    ... Zie paragraaf 2.3 Inhoud ...

       </saml:Assertion ... >

  </wss:Security>

</soap:Header>
```
