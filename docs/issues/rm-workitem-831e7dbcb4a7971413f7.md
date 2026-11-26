# Mogelijke overeenkomst: gbx.con.e4110.2 (AORTA REQ) ↔ gbx.con.e4110.2 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 2d6802fd-941b-59e4-9fe0-5b40fec808d9

## Bevinding

Eis gbx.con.e4110.2 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4110.2 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 50.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Ondersteunen servercertificaten en ondertekeningalgoritmen

**Requirement-ID:** `0c633249-10e0-54df-96d5-c8d4fe9b8029`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.CON.e4110.2"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Het GBx dient UZI/PKIo-servercertificaten van de (verschillende) generatie(s) te ondersteunen zoals beschikbaar wordt gesteld door het UZI-Register. ; Er moet gebruik worden gemaakt van het SHA-256 ondertekeningsalgoritme. ;"
```

### Ondersteunen servercertificaten en ondertekeningalgoritmen

**Requirement-ID:** `4bf27a8d-f579-5fa2-950b-d6b2e15033c9`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.CON.e4110.2"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis:</b>
Het GBx dient UZI/PKIo-servercertificaten van de (verschillende) generatie(s) te ondersteunen zoals beschikbaar wordt gesteld door het UZI-Register.

Er moet gebruik worden gemaakt van het SHA-256 ondertekeningsalgoritme.

<b>Toelichting bij eis:</b>
Het UZI-register geeft UZI-servercertificaten uit onder &#233;&#233;n of meerdere certificaatbomen. In het geval er onder diverse certificaatbomen UZI-servercertificaten wordt uitgegeven, is het zaak om alle servercertificaten uitgegeven onder de diverse certificaatbomen te kunnen ondersteunen.

Een GBX-communicatieserver dient te zijn ingericht op het ondertekeningalgoritme SHA-256."""
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "2be4cfa9-b8c4-5a71-9783-5aaf93603bef",
    "evidenceIds": [
      "0571e4dd-082a-5cdb-a78f-50222411980c"
    ],
    "connectionId": "7a31e9b2-4c55-57f0-8d4e-997ad85fd920",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "2d6802fd-941b-59e4-9fe0-5b40fec808d9",
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
  "entityId": "2d6802fd-941b-59e4-9fe0-5b40fec808d9",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.con.e4110.2 (AORTA REQ) ↔ gbx.con.e4110.2 (AORTA AS REQ)",
  "description": "Eis gbx.con.e4110.2 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4110.2 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 50.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:2d6802fd-941b-59e4-9fe0-5b40fec808d9"
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
      "0c633249-10e0-54df-96d5-c8d4fe9b8029"
    ],
    "requirementB": [
      "4bf27a8d-f579-5fa2-950b-d6b2e15033c9"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.con.e4110.2"
    ],
    "requirementNumberB": [
      "gbx.con.e4110.2"
    ],
    "requirementTitleA": [
      "Ondersteunen servercertificaten en ondertekeningalgoritmen"
    ],
    "requirementTitleB": [
      "Ondersteunen servercertificaten en ondertekeningalgoritmen"
    ],
    "matchBasis": [
      "NUMBER"
    ],
    "scorePercent": [
      50.0
    ],
    "conclusion": [
      "Eis gbx.con.e4110.2 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4110.2 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 50.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

