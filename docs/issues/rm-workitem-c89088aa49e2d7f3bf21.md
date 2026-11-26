# Mogelijke overeenkomst: gbx.log.e4016 (AORTA REQ) ↔ gbx.log.e4016.3 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 80e96bef-a4c1-534a-9cba-a8e3f8b18dde

## Bevinding

Eis gbx.log.e4016 uit AORTA REQ komt vermoedelijk overeen met eis gbx.log.e4016.3 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 62.59%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Toegangslog bijhouden (FHIR)

**Requirement-ID:** `58045abd-6e10-5cda-b766-e692b8e527a3`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.LOG.e4016"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Het systeem moet alle binnenkomende en uitgaande berichten loggen in de toegangslog. Hierbij dienen onderstaande gegevens gelogd te worden, indien aanwezig in het bericht: ;  de identiteit van de patiënt/cliënt/burger (BSN) waar het bericht betrekking op heeft; ;  de identiteit van de organisatie waar het bericht vandaan komt of naar toe wordt gestuurd; ;  de functie en identiteit van de zorgverlener, medewerker of patiënt zoals opgenomen in het verstuurde en/of ontvangen bericht. De functie is de aorta-rolcode zoals opgenomen in het claim-element van het transactietoken. ;  de gebruikersinteractieID. Dit is een combinatie van HTTP-operatie, de URL inclusief de ontvangen zoekparameters en de contentVersion uit de AORTA-Version header; ;  het tijdstip en tijdzone (ten opzichte van UTC) van het moment dat het bericht ontvangen/verstuurd is; ;  de bericht-id van het ontvangen/verstuurde bericht. Dit is het messageID in de HTTP header; ;  het initiële bericht-id van het ontvangen/verstuurde bericht. Dit is het initialMessageID in de HTTP header; ;  de aan het bericht gekoppelde gegevensdienst. Dit is de waarde zoals opgenomen in de scope van het transactietoken; ;  een indicatie van eventueel opgetreden foutsituaties met betrekking tot het ontvangen en verzenden van de berichten. Hierbij dient de HTTP-foutcode, alle informatie in de eventueel aanwezige operationOutcome en de enventuele WWW-Authenticate HTTP response header gelogd te worden. ;"
```

### Toegangslog bijhouden (FHIR)

**Requirement-ID:** `6d909be3-ab37-5af7-ba92-073cab07fce2`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.LOG.e4016.3"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis:</b>
Het systeem moet alle binnenkomende en uitgaande berichten loggen in de toegangslog. Hierbij dienen onderstaande gegevens gelogd te worden, indien aanwezig in het bericht:
<ol>
	<li>de identiteit van de pati&#235;nt/cli&#235;nt/burger (BSN) waar het bericht betrekking op heeft;</li>
	<li>de identiteit van de organisatie waar het bericht vandaan komt of naar toe wordt gestuurd;</li>
	<li>de functie en identiteit van de  zorgverlener, medewerker of pati&#235;nt zoals opgenomen in het verstuurde en/of ontvangen bericht. De functie is de AORTA-rolcode zoals opgenomen in het claim-element van het transactietoken.</li>
	<li>de gebruikersinteractie-id. Dit is een combinatie van HTTP-operatie, de URL  inclusief de ontvangen zoekparameters en de contentVersion uit de AORTA-Version header;</li>
	<li>het tijdstip en tijdzone (ten opzichte van UTC) van het moment dat het bericht ontvangen/verstuurd is;</li>
	<li>het bericht-id van het ontvangen/verstuurde bericht. Dit is het requestID in de HTTP header;</li>
	<li>het initi&#235;le bericht-id van het ontvangen/verstuurde bericht. Dit is het initialRequestID in de HTTP header;</li>
	<li>de aan het bericht gekoppelde gegevensdienst. Dit is de waarde zoals opgenomen in de scope van het transactietoken;</li>
	<li>een indicatie van eventueel opgetreden foutsituaties met betrekking tot het ontvangen en verzenden van de berichten. Hierbij dient de HTTP-foutcode, alle informatie in de eventueel aanwezige OperationOutcome en de eventuele WWW-Authenticate HTTP response header gelogd te worden.</li>
</ol>

<b>Toelichting bij eis: </b>
Het doel van de logging is het inzichtelijk kunnen maken van de datastroom door de gehele keten. Het inzichtelijk maken van de loggegevens kan van belang zijn voor auditredenen of beheerwerkzaamheden zoals het oplossen van fouten in de keten.
Deze eis is conform de vereisten zoals beschreven in de NEN7513. 
Voor de invulling van de velden zoals genoemd in de eis, gelden de standaardnotaties zoals opgenomen in de NEN713, tenzij anders is vermeld in de eis. 

"""
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "76627a97-fdbb-55a2-bbd4-3b028241cef2",
    "evidenceIds": [
      "2817bac0-5497-5f8a-a25a-2c8388cfaaa1"
    ],
    "connectionId": "cbd123d2-d094-5050-9db7-45f57e742cbc",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "80e96bef-a4c1-534a-9cba-a8e3f8b18dde",
    "predicateCode": "has_work_item",
    "direction": "directed",
    "statement": "WorkItem behoort tot WorkItemCatalog",
    "status": "asserted"
  }
]
```

### Evidence

```json
[]
```

### EvidenceObjects en uitsneden

```json
[]
```

## WorkItem (oorspronkelijke gegevens)

```json
{
  "entityId": "80e96bef-a4c1-534a-9cba-a8e3f8b18dde",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.log.e4016 (AORTA REQ) ↔ gbx.log.e4016.3 (AORTA AS REQ)",
  "description": "Eis gbx.log.e4016 uit AORTA REQ komt vermoedelijk overeen met eis gbx.log.e4016.3 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 62.59%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:80e96bef-a4c1-534a-9cba-a8e3f8b18dde"
    }
  ],
  "properties": {
    "classification": [
      "Finding"
    ],
    "issueType": [
      "TEXT_DIFFERENCE_REVIEW"
    ],
    "status": [
      "OPEN"
    ],
    "requirementA": [
      "58045abd-6e10-5cda-b766-e692b8e527a3"
    ],
    "requirementB": [
      "6d909be3-ab37-5af7-ba92-073cab07fce2"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.log.e4016"
    ],
    "requirementNumberB": [
      "gbx.log.e4016.3"
    ],
    "requirementTitleA": [
      "Toegangslog bijhouden (FHIR)"
    ],
    "requirementTitleB": [
      "Toegangslog bijhouden (FHIR)"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      62.59
    ],
    "conclusion": [
      "Eis gbx.log.e4016 uit AORTA REQ komt vermoedelijk overeen met eis gbx.log.e4016.3 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 62.59%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

