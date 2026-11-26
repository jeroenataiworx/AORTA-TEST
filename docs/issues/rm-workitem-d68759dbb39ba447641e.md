# Mogelijke overeenkomst: age.log.e4030 (AORTA REQ) ↔ lsp.log.e4025 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 118bec10-addb-5f40-b65e-7e60b789f104

## Bevinding

Eis age.log.e4030 uit AORTA REQ komt vermoedelijk overeen met eis lsp.log.e4025 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 44.12%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Uitschakelen logging

**Requirement-ID:** `77340042-a70f-5c14-833c-b65097f4535d`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "AGE.LOG.e4030"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Het loggen van de berichtuitwisseling in de toegangslog en het loggen van acties op de toegangslog mogen niet uitgeschakeld kunnen worden. ;"
```

### Uitschakelen logging

**Requirement-ID:** `f8e004c3-b2a4-5728-9029-a95452747a15`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "LSP.LOG.e4025 "

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""Het loggen van de berichtuitwisseling in de toegangslog en het loggen van acties op de toegangslog mogen niet uitgeschakeld kunnen worden.

<b>Functie</b>
Garanderen dat logging te allen tijde actief is.

<b>Toelichting</b>
Conform NEN 7513:2018 Paragraaf 6.4.2"""
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "41d1cda0-2fb9-54c6-adea-b20edd0dcc42",
    "evidenceIds": [
      "811f1b98-71e5-580e-85b5-b08f6b39c171"
    ],
    "connectionId": "9f629e45-c2aa-58b0-9cb1-79db6cca8040",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "118bec10-addb-5f40-b65e-7e60b789f104",
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
  "entityId": "118bec10-addb-5f40-b65e-7e60b789f104",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: age.log.e4030 (AORTA REQ) ↔ lsp.log.e4025 (AORTA AS REQ)",
  "description": "Eis age.log.e4030 uit AORTA REQ komt vermoedelijk overeen met eis lsp.log.e4025 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 44.12%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:118bec10-addb-5f40-b65e-7e60b789f104"
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
      "77340042-a70f-5c14-833c-b65097f4535d"
    ],
    "requirementB": [
      "f8e004c3-b2a4-5728-9029-a95452747a15"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "age.log.e4030"
    ],
    "requirementNumberB": [
      "lsp.log.e4025"
    ],
    "requirementTitleA": [
      "Uitschakelen logging"
    ],
    "requirementTitleB": [
      "Uitschakelen logging"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      44.12
    ],
    "conclusion": [
      "Eis age.log.e4030 uit AORTA REQ komt vermoedelijk overeen met eis lsp.log.e4025 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 44.12%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

