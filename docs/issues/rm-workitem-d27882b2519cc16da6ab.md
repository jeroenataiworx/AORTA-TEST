# Mogelijke overeenkomst: gbx.bvl.e4080.1 (AORTA REQ) ↔ gbx.bvl.e4080.1 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 3341ad4a-eb9b-51de-8ff3-5dc2ded01a30

## Bevinding

Eis gbx.bvl.e4080.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.bvl.e4080.1 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 58.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Een GBx beschikt over een geldig UZI/PKIO-servercertificaat

**Requirement-ID:** `a07c9fdc-acf5-51c5-afe8-a2d3ff020f31`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.BVL.e4080.1"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Een GBx dient een {GBx}UZI- of {GBK}{GBP}{GBO} PKIO-servercertificaat te hebben dat op naam staat van de opdrachtgever en is gecertificeerd door een Certificate Authority (CA) onder de root van de Staat der Nederlanden. ;"
```

### Een GBx beschikt over een geldig UZI/PKIO-servercertificaat

**Requirement-ID:** `b44b120a-b9ab-5a7e-b16e-c3ce751d10aa`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.BVL.e4080.1"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis:</b>
Een GBx dient een {GBx}UZI- of {GBK}{GBP}{GBO} PKIO-servercertificaat te hebben dat op naam staat van de zorgaanbieder en is gecertificeerd door een Certificate Authority (CA) onder de root van de Staat der Nederlanden.

<b>Toelichting bij eis:</b>
Deze eis is nodig opdat de authenticiteit van het GBx en de exclusiviteit van getransporteerde gegevens door een Trusted Third Party (TTP) kan worden gewaarborgd."""
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "9b743ede-6254-5fe6-9e39-cc54993125f2",
    "evidenceIds": [
      "ee5edb0e-07ee-58f7-b18b-e195840041e7"
    ],
    "connectionId": "ee8278b5-9b81-52b9-9ee6-adcc2eb82383",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "3341ad4a-eb9b-51de-8ff3-5dc2ded01a30",
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
  "entityId": "3341ad4a-eb9b-51de-8ff3-5dc2ded01a30",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.bvl.e4080.1 (AORTA REQ) ↔ gbx.bvl.e4080.1 (AORTA AS REQ)",
  "description": "Eis gbx.bvl.e4080.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.bvl.e4080.1 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 58.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:3341ad4a-eb9b-51de-8ff3-5dc2ded01a30"
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
      "a07c9fdc-acf5-51c5-afe8-a2d3ff020f31"
    ],
    "requirementB": [
      "b44b120a-b9ab-5a7e-b16e-c3ce751d10aa"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.bvl.e4080.1"
    ],
    "requirementNumberB": [
      "gbx.bvl.e4080.1"
    ],
    "requirementTitleA": [
      "Een GBx beschikt over een geldig UZI/PKIO-servercertificaat"
    ],
    "requirementTitleB": [
      "Een GBx beschikt over een geldig UZI/PKIO-servercertificaat"
    ],
    "matchBasis": [
      "NUMBER"
    ],
    "scorePercent": [
      58.0
    ],
    "conclusion": [
      "Eis gbx.bvl.e4080.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.bvl.e4080.1 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 58.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

