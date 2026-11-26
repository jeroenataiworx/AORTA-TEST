# Mogelijke overeenkomst: gbx.pst.e4015 (AORTA REQ) ↔ gbx.pst.e4015 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: e9e18cc0-e167-565d-8624-d152db15cff7

## Bevinding

Eis gbx.pst.e4015 uit AORTA REQ komt vermoedelijk overeen met eis gbx.pst.e4015 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 23.15%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Tijdige verwerking van berichten

**Requirement-ID:** `93c3ab8c-7945-5969-a85b-a9a02c2e4bc8`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.PST.e4015"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Een GBx dient voor gebruikersinteracties, na het commando van een gebruiker of een daaropvolgende ontvangst van een bericht van de ZIM, binnen 0,3 seconden het aangegeven resultaat te hebben bereikt. ;"
```

### Tijdige verwerking van berichten

**Requirement-ID:** `4967dae2-6f41-5ebd-bc80-ffec0846c3d1`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.PST.e4015"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis:</b>
Een GBx dient voor gebruikersinteracties, na het commando van een gebruiker of een daaropvolgende ontvangst van een bericht van de ZIM, binnen 0,3 seconden het aangegeven resultaat te hebben bereikt.

<b>Toelichting bij eis:</b>
Deze eis is nodig om te voorkomen dat een zorgaanbieder bij zijn GZN of het LSP gaat klagen over te lange responstijden terwijl de oorzaak misschien ligt bij bijv. een eigen computer die in beslag wordt genomen door andere toepassingen of een lokaal netwerk met onvoldoende bandbreedte. 

Deze eis betekent voor de zorgaanbieder dat hij zijn XIS-applicatie moet installeren op ICT-voorzieningen met voldoende prestaties. Zonodig moeten bijv. de computers worden ingeregeld op de behoefte van deze XIS-applicatie, bijv. als ze ook worden gebruikt voor andere toepassingen. Wellicht kan zijn XIS-leverancier helpen bij het selecteren en inregelen van ICT-voorzieningen. Indien de zorgaanbieder een ASP-leverancier (Application Service Provider) heeft geselecteerd voor zijn XIS, kan hij dit voor de centrale ICT-voorzieningen wellicht overlaten aan die ASP-leverancier, maar moeten de lokale werkplekken niet vergeten worden."""
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "88c27404-75a6-585d-837d-9419053624ef",
    "evidenceIds": [
      "57dd66e4-568b-53db-b5f6-a5a3b992ab08"
    ],
    "connectionId": "c0d324d6-83a1-5cb6-b83a-37ae6cb1c7d0",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "e9e18cc0-e167-565d-8624-d152db15cff7",
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
  "entityId": "e9e18cc0-e167-565d-8624-d152db15cff7",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.pst.e4015 (AORTA REQ) ↔ gbx.pst.e4015 (AORTA AS REQ)",
  "description": "Eis gbx.pst.e4015 uit AORTA REQ komt vermoedelijk overeen met eis gbx.pst.e4015 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 23.15%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:e9e18cc0-e167-565d-8624-d152db15cff7"
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
      "93c3ab8c-7945-5969-a85b-a9a02c2e4bc8"
    ],
    "requirementB": [
      "4967dae2-6f41-5ebd-bc80-ffec0846c3d1"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.pst.e4015"
    ],
    "requirementNumberB": [
      "gbx.pst.e4015"
    ],
    "requirementTitleA": [
      "Tijdige verwerking van berichten"
    ],
    "requirementTitleB": [
      "Tijdige verwerking van berichten"
    ],
    "matchBasis": [
      "NUMBER"
    ],
    "scorePercent": [
      23.15
    ],
    "conclusion": [
      "Eis gbx.pst.e4015 uit AORTA REQ komt vermoedelijk overeen met eis gbx.pst.e4015 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 23.15%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

