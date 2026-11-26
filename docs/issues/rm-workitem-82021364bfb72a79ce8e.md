# Mogelijke overeenkomst: sys.bvl.e4010 (AORTA REQ) ↔ sys.bvl.e4010.2 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: ef03d156-8a31-56f6-9499-85189fa5607a

## Bevinding

Eis sys.bvl.e4010 uit AORTA REQ komt vermoedelijk overeen met eis sys.bvl.e4010.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 38.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Beveiligde opslag

**Requirement-ID:** `8da3116f-d85a-57d1-a869-7545ae9f1a5c`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "SYS.BVL.e4010"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Data die persoonsgegevens bevatten dienen versleuteld en beveiligd te worden opgeslagen. Het gaat hierbij om alle opgeslagen data (bv. logging en backups). ;"
```

### Beveiligde opslag

**Requirement-ID:** `082e0f33-3115-5986-b6a4-e9b07ad558f1`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "SYS.BVL.e4010.2"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis:</b>
Data die persoonsgegevens bevatten dienen versleuteld en beveiligd te worden opgeslagen. Het gaat hierbij om alle opgeslagen data (bv. logging en backups).

<b>Toelichting bij eis:</b>
In principe moet alle data met persoonsgegevens worden ge&#235;ncrypt. Dit betreft o.a. gegevens die worden opgeslagen ten behoeve van een autorisatiesessie. Mocht hiervan met het oog op systeemprestaties van afgeweken worden, dan dient dit overlegd te worden met VZVZ. """
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "63a6fd42-4694-5a4c-8be9-f71d6b490376",
    "evidenceIds": [
      "058913c8-14d3-532c-87b0-9de2a72dee1c"
    ],
    "connectionId": "4028dcbf-8219-5b34-bce6-6a4fcb53f9c6",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "ef03d156-8a31-56f6-9499-85189fa5607a",
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
  "entityId": "ef03d156-8a31-56f6-9499-85189fa5607a",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: sys.bvl.e4010 (AORTA REQ) ↔ sys.bvl.e4010.2 (AORTA AS REQ)",
  "description": "Eis sys.bvl.e4010 uit AORTA REQ komt vermoedelijk overeen met eis sys.bvl.e4010.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 38.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:ef03d156-8a31-56f6-9499-85189fa5607a"
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
      "8da3116f-d85a-57d1-a869-7545ae9f1a5c"
    ],
    "requirementB": [
      "082e0f33-3115-5986-b6a4-e9b07ad558f1"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "sys.bvl.e4010"
    ],
    "requirementNumberB": [
      "sys.bvl.e4010.2"
    ],
    "requirementTitleA": [
      "Beveiligde opslag"
    ],
    "requirementTitleB": [
      "Beveiligde opslag"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      38.0
    ],
    "conclusion": [
      "Eis sys.bvl.e4010 uit AORTA REQ komt vermoedelijk overeen met eis sys.bvl.e4010.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 38.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

