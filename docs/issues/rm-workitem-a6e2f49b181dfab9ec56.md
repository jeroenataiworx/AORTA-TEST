# Mogelijke overeenkomst: gbx.opv.e4660 (AORTA REQ) ↔ gbx.opv.e4660 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 5c9933d3-8649-5e65-b174-198b842f4f32

## Bevinding

Eis gbx.opv.e4660 uit AORTA REQ komt vermoedelijk overeen met eis gbx.opv.e4660 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 31.91%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Opnemen BSN in opleverbericht

**Requirement-ID:** `66231b96-5fb9-5804-81c9-8f04c5d17336`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.OPV.e4660"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; In FHIR-responses dient er altijd een BSN opgenomen te worden conform de technische specificaties. ;"
```

### Opnemen BSN in opleverbericht

**Requirement-ID:** `2505eb59-9c47-5d4d-a94a-9b20b08136bd`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.OPV.e4660"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis</b>:
In FHIR-responses dient er altijd een BSN opgenomen te worden conform de technische specificaties. <b> </b>

<b>Toelichting bij eis:</b>
Een bronsysteem moet agnostisch zijn voor de infrastructuur ten behoeve waarvan opgeleverd wordt. Indien nodig, zal de resource broker het BSN verwijderen uit de FHIR-response. In de AORTA-communicatie tussen zorgaanbieders dient er altijd een BSN doorgestuurd te worden naar de uiteindelijke bevrager.  """
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "0f706d72-ca31-534c-93af-54d6a4fc5cd9",
    "evidenceIds": [
      "06902496-e844-52a9-a940-c7df4841eabe"
    ],
    "connectionId": "437da501-17b1-5c40-8a48-d4230b68aa7b",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "5c9933d3-8649-5e65-b174-198b842f4f32",
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
  "entityId": "5c9933d3-8649-5e65-b174-198b842f4f32",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.opv.e4660 (AORTA REQ) ↔ gbx.opv.e4660 (AORTA AS REQ)",
  "description": "Eis gbx.opv.e4660 uit AORTA REQ komt vermoedelijk overeen met eis gbx.opv.e4660 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 31.91%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:5c9933d3-8649-5e65-b174-198b842f4f32"
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
      "66231b96-5fb9-5804-81c9-8f04c5d17336"
    ],
    "requirementB": [
      "2505eb59-9c47-5d4d-a94a-9b20b08136bd"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.opv.e4660"
    ],
    "requirementNumberB": [
      "gbx.opv.e4660"
    ],
    "requirementTitleA": [
      "Opnemen BSN in opleverbericht"
    ],
    "requirementTitleB": [
      "Opnemen BSN in opleverbericht"
    ],
    "matchBasis": [
      "NUMBER"
    ],
    "scorePercent": [
      31.91
    ],
    "conclusion": [
      "Eis gbx.opv.e4660 uit AORTA REQ komt vermoedelijk overeen met eis gbx.opv.e4660 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 31.91%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

