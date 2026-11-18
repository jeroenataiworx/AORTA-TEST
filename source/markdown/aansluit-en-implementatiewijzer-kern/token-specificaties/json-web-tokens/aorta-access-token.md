[AORTA 8.5.2](../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../token-specificaties.md) / [JSON Web tokens](../json-web-tokens.md)

# AORTA Access token

## Inhoud en formaat van het AORTA access_token

**AOF.TS.AAT.100.v1**

Het JWT-based AORTA access_token bestaat uit een header, een payload en een signature, waarbij gebruik wordt gemaakt van [JWS Compact Serialization](https://tools.ietf.org/html/rfc7515#section-3.1).

**AOF.TS.AAT.200.v2**

De header van het token bevat de volgende attributen:

| **Claim** ; | **Vaste waarde** ; | **Toelichting** ; |
| --- | --- | --- |
| alg ; | RS256 ; |  |
| typ ; | aorta-at+JWT ; | "aorta-at" is een afkorting voor AORTA access_token. ; |
| kid ; | - ; | The identifier of the key-pair used to sign this JWT ; |

**AOF.TS.AAT.300.v1**

Het token wordt op basis van RS256 (RSA Signature met SHA-256), digitaal ondertekend met de private key van de Autorisatie Server. De signature wordt geplaatst over de header en de payload.

**AOF.TS.AAT.400.v2**

De payload van het token is omschreven in onderstaande tabel.

| **Claim** ; | **Cardinaliteit** ; | **Vaste waarde** ; | **Toelichting** ; |
| --- | --- | --- | --- |
| jti ; | 1..1 ; | - ; | jti bevat een globaal uniek ID van het betreffende token. Aanbevolen wordt om een UUID te gebruiken. ; |
| iat ; | 1..1 ; | - ; | iat bevat het tijdstip van uitgifte van dit token (aantal seconden sinds 1970-01-01T0:0:0Z gemeten in UTC). ; |
| iss ; | 1..1 ; | - ; | iss bevat de HTTPS-URL van de autorisatieserver die het token heeft uitgegeven. Op deze manier kan automatisch de juiste metadata, met daarin de juiste endpoints, worden opgehaald. ; |
| sub ; | 1..1 ; | - ; | Formaat: "<id-systeem>\|<id>" ;  Het ID van de gebruiker, of van een systeem, die uitgifte van dit access_token legitimeert. De claim kan bevatten: ;  Het BSN van de persoon die een interactie initieert m.b.t. haar eigen gegevens, of die een ander persoon hiertoe heeft gemachtigd - sub bevat dan de string "[http://fhir.nl/fhir/NamingSystem/bsn\|<bsn](aorta-access-token.md)>" ;  Het UZI-nummer van een zorgverlener - sub bevat dan de string "[http://fhir.nl/fhir/NamingSystem/uzi-nr-pers](http://fhir.nl/fhir/NamingSystem/uzi-nr-pers)\|<UZI-nummer>" ;  Het appID van het systeem (indien het request zonder tussenkomst van een gebruiker is ingestuurd) - sub bevat dan de string "[http://fhir.nl/fhir/NamingSystem/uzi-nr-sys\|<app-id](aorta-access-token.md)>" ; |
| role ; | 0..1 ; | - ; | Formaat: "<codesysteem>\|<rolcode>" ;  De rolcode van de gebruiker die uitgifte van dit access_token legitimeert. De claim kan bevatten: ;  De rolcode die hoort bij een persoon, ofwel "[http://fhir.nl/fhir/NamingSystem/aorta-rolcode](http://fhir.nl/fhir/NamingSystem/aorta-rolcode)\|P" ;  De UZI-rolcode van een zorgverlener, ofwel "[http://fhir.nl/fhir/NamingSystem/uzi-rolcode](http://fhir.nl/fhir/NamingSystem/uzi-rolcode)\|<UZI-rolcode>" ;  Verplicht indien de sub claim is gevuld met een ID van een persoon. ; |
| act ; | 0..1 ; | - ; | De act claim bevat een aantal subclaims en wordt opgenomen wanneer iets of iemand handelt namens een ander persoon. Zie ook [RFC 8693](https://datatracker.ietf.org/doc/html/rfc8693#section-4.1) voor voorbeelden. ; |
| act.sub ; | 1..1 ; | - ; | Formaat: "<id-systeem>\|<id>" ;  Het ID van de gebruiker of van het systeem die handelt namens de persoon, die is opgenomen in de sub claim. De claim kan bevatten: ;  Het BSN van een gemachtigd persoon die gegevens van een ander persoon opvraagt - sub bevat dan de string "[http://fhir.nl/fhir/NamingSystem/bsn\|<bsn](aorta-access-token.md)>" ;  Het UZI-nummer van een zorgverlener of van een medewerker van een zorginstelling - sub bevat dan de string "[http://fhir.nl/fhir/NamingSystem/uzi-nr-pers](http://fhir.nl/fhir/NamingSystem/uzi-nr-pers)\|<UZI-nummer>" ;  Het appID van het systeem (indien het request zonder tussenkomst van een gebruiker is ingestuurd) - sub bevat dan de string "[http://fhir.nl/fhir/NamingSystem/aorta-app-id\|<app-id](aorta-access-token.md)>" ; |
| acr ; | 1..1 ; | - ; | De Authentication Context Class Reference. Geeft informatie over het niveau waarop de sub, of indien aanwezig, de act.sub van het token is geauthenticeerd. Mogelijke waarden, zoals [gespecificeerd binnen SAML](http://docs.oasis-open.org/security/saml/v2.0/saml-authn-context-2.0-os.pdf) zijn: ;  "urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport" (bijvoorbeeld DigiD-basis) ;  "urn:oasis:names:tc:SAML:2.0:ac:classes:MobileTwoFactorContract" (bijvoorbeeld DigiD-midden) ;  "urn:oasis:names:tc:SAML:2.0:ac:classes:Smartcard" (bijvoorbeeld DigiD-substantieel) ;  "urn:oasis:names:tc:SAML:2.0:ac:classes:SmartcardPKI" (bijvoorbeeld UZI-pas of DigiD-hoog) ;  "urn:oasis:names:tc:SAML:2.0:ac:classes:X509" (servercertificaat) ; |
| attest ; | 1..1 ; | - ; | Informatie over op welke grondslag of grondslagen dit token is gebaseerd. Het betreft een door spatie gescheiden set van strings. Mogelijk waarden: ;  "MAP" - het Medisch Autorisatie Protocol is toegepast. ;  "TR"- toestemming van patiënt is vastgelegd in een toegelaten toestemmingsregister. ;  "MedMij" - het token is uitgeven n.a.v. een conform MedMij afgegeven toestemmingsverklaring. ;  "BRON" - toestemming is, door de patiënt of diens vertegenwoordiger, vastgelegd bij de bronhoudende zorgaanbieder zelf, en is daarom nog niet getoetst. ;  "CNST" - toestemming mag door de bronhoudende zorgaanbieder worden verondersteld te zijn verkregen, bijvoorbeeld t.b.v. een verwijzing van de patiënt - deze is vastgelegd in een consent_token, en het juiste gebruik van dit token voor het ontvangen request is reeds getoetst. ;  "LOG" - specifieke autorisatieregels m.b.t. de toegangslog zijn toegepast. ;  "ACT/VWI" - specifieke autorisatieregels m.b.t. toegang tot ACT/VWI-entries zijn toegepast. ;  Een voorbeeld van een attest claim is "MAP TR", waarmee dan wordt aangeduid dat het MAP is getoetst en dat toestemming is vastgelegd en getoetst in een toegelaten toestemmingsregister. ; |
| nbf ; | 1..1 ; | - ; | nbf bevat het tijdstip van uitgifte van dit token (aantal seconden sinds 1970-01-01T0:0:0Z gemeten in UTC). ; |
| exp ; | 1..1 ; | - ; | Wordt gevuld met de expiration time van het MedMij access_token of met de expiration time van het AORTA transactietoken naar aanleiding waarvan dit AORTA access_token wordt uitgegeven. ; |
| aud ; | 1..1 ; | - ; | Formaat: ["<appID>", "<appID>"] ;  De aud van het token bevat de set van appID's van alle GBx-applicaties, die deze interactie gaan ontvangen. Deze GBZ-applicaties vallen altijd onder één organisatie. ;  Een appID heeft het formaat: "urn:oid:2.16.840.1.113883.2.4.6.6.<applicatie-id>". Aan iedere GBx-applicatie die is aangesloten op AORTA wordt een eigen <applicatie-id> toegekend. ; |
| scope ; | 1..1 ; | - ; | Voor de juiste vulling zie tekst onder deze tabel. ; |
| patient ; | 0..1 ; | - ; | Formaat: "<id-systeem>\|<id>" ;  Het BSN van de patiënt, d.w.z. de persoon waarop de gegevens, die worden uitgewisseld, betrekking hebben. ;  patient bevat de string "[http://fhir.nl/fhir/NamingSystem/bsn\|](http://fhir.nl/fhir/NamingSystem/bsn%7C)<bsn>". De verwachting is weliswaar dat hier altijd BSN's gecommuniceerd gaan worden. Het id-systeem is hier toegevoegd om consistent te blijven met de sub claim en om eventueel ook eigen patient-ID's van een zorgaanbieder te kunnen ondersteunen. ;  Verplicht gevuld bij patiëntgebonden interacties. ; |
| client_id ; | 1..1 ; | - ; | Formaat: "urn:oid:2.16.840.1.113883.2.4.6.6.<applicatie-id>" ;  Dit attribuut bevat informatie over de partij die als resource client mag optreden en daarvoor dit token mag gebruiken. ;  Wanneer een interactie door RB VnC wordt geïnitieerd bij een resource server, dan bevat de client_id claim het appID van de Resource Broker VnC component. ;  Wanneer een interactie door RB ZA-in wordt geïnitieerd bij een andere Resource Broker component (bijv. RB ACT) dan bevat de client_id claim het appID van de Resource Broker ZA-in component. ; |
| _vrb ; | 0..1 ; | - ; | De _vrb claim bevat, in een aantal subclaims, VZVZ Resource Broker specifieke informatie over de afhandeling van interacties. Een resource server (GBZ-applicatie) mag deze claim desgewenst negeren. ;  Deze claim is slechts aanwezig wanneer een interactie, via RB VnC, wordt geïnitieerd bij een resource server. ; |
| _vrb. _vrb_aud ; | 1..1 ; | - ; | Het appID van de Resource Broker VnC component. Formaat: "urn:oid:2.16.840.1.113883.2.4.6.6.<applicatie-id>". ; |
| _vrb. _vrb_client_id ; | 1..1 ; | - ; | Het appID van de Resource Broker MedMij-in component of van de Resource Broker ZA-in component, die jegens de Resource Broker VnC component optreedt als resource client. Formaat: "urn:oid:2.16.840.1.113883.2.4.6.6.<applicatie-id>". ; |
| _vrb. _vrb_ion ; | 1..1 ; | - ; | Een kenmerk van de organisatie die die het request heeft geïniteerd (de "initiating organisation name"). In de MedMij use case gaat het om de OAuthclientOrganisatienaam (naam van het PGO), zoals opgenomen in de MedMij OCL. In de ZA-ZA use case gaat het om de URA (formaat: "urn:oid:2.16.528.1.1007.3.3.<URA>"). ; |
| ver ; | 1..1 ; | 2.0 ; | De versie van de tokendefinitie die wordt gehanteerd. ; |

**AOF.TS.AAT.500.v2**

De scope claim van het token wordt als volgt gevuld, waarbij verschillende scope-onderdelen door een spatie van elkaar worden gescheiden:

| **Gegevensdienst / Interactie** ; | **Vulling van scope** ; | **Toevoeging op scope bij interactie vanuit MedMij** ; | **Toevoeging op scope bij interactie vanuit AORTA** ; |
| --- | --- | --- | --- |
| **Gegevensdienst / Interactie** ; | **Vulling van scope** ; | **Toevoeging op scope bij interactie vanuit MedMij** ; | **Toevoeging op scope bij interactie vanuit AORTA** ; |
| Verzamelen Afspraken 2.0 ; | patient/Appointment.read ; | medmij.gegevensdienst.47 ; | nog niet beschikbaar ; |
| Verzamelen Basisgegevens zorg 3.0 ; | patient/Patient.read patient/Coverage.read patient/Consent.read patient/Condition.read patient/Observation.read patient/NutritionOrder.read patient/Flag.read patient/AllergyIntolerance.read patient/MedicationStatement.read patient/MedicationRequest.read patient/MedicationDispense.read patient/DeviceUseStatement.read patient/Immunization.read patient/Procedure.read patient/Encounter.read patient/ProcedureRequest.read patient/ImmunizationRecommendation.read patient/DeviceRequest.read patient/Appointment.read ; | medmij.gegevensdienst.48 ; | aorta.contextcode.BGZOPV ; |
| Verzamelen Basisgegevens GGZ 2.0 ; | patient/Patient.read patient/Coverage.read patient/Consent.read patient/Condition.read patient/Observation.read patient/CarePlan.read patient/Procedure.read patient/DiagnosticReport.read patient/CareTeam.read ; | medmij.gegevensdienst.50 ; | nog niet beschikbaar ; |
| Verzamelen Documenten 3.0 ; | patient/DocumentManifest.read patient/DocumentReference.read patient/Binary.read ; | medmij.gegevensdienst.51 ; | nog niet beschikbaar ; |
| Delen Meetwaarden vitale functies 2.0 ; | patient/Observation.write ; | medmij.gegevensdienst.53 ; | nog niet beschikbaar ; |
| Verzamelen Meetwaarden vitale functies 2.0 ; | patient/Observation.read ; | medmij.gegevensdienst.52 ; | nog niet beschikbaar ; |
| Verzamelen verwijzingen naar vragenlijsten 2.0 ; | patient/Task.read ; | medmij.gegevensdienst.59 ; | nog niet beschikbaar ; |
| Delen antwoorden op vragenlijsten 2.0 ; | patient/Task.write patient/QuestionnaireResponse.write ; | medmij.gegevensdienst.60 ; | nog niet beschikbaar ; |
| $is-allowed ; | patient$is-allowed ; | - ; | n.v.t. ; |
| Interacties m.b.t. het actualiteitsregister en de verwijsindex ; | patient/DocumentManifest.write ;  of ;  patient/DocumentManifest.read ;  of ;  patient$delete-dossier ; | n.v.t. ; | - ; |
| Interacties m.b.t. de toegangslog (RB-logging) ; | patient/AuditEvent.read ; | n.v.t. ; | - ; |
| Patiëntgebonden workflow interacties ; | patient/Task.write ;  of ;  patient/Task.read ; | - ; | - ; |
| Niet-patiëntgebonden workflow interacties ; | user/Task.write ;  of ;  user/Task.read ; | n.v.t. ; | - ; |

Met een access_token wordt aan de ontvanger bewezen dat aan een gegeven subject bepaalde toegangsrechten zijn verstrekt.
