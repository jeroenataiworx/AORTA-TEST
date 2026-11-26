# Mogelijke overeenkomst: age.log.e4060 (AORTA REQ) ↔ lsp.log.e4030 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: d6c566e9-770a-5f43-bb6a-04930978bdf2

## Bevinding

Eis age.log.e4060 uit AORTA REQ komt vermoedelijk overeen met eis lsp.log.e4030 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 59.52%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Wijzigen logging

**Requirement-ID:** `2643785a-e4ba-5eef-9e9b-0ccb82ca4400`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "AGE.LOG.e4060"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

> \"\; Gegevens in de log mogen niet wijzigbaar of verwijderbaar \(alleen in het kader van eis \*\*AGE\.LOG\.e4050\*\*\) zijn\. Het niet kunnen wijzigen\/verwijderen van loggegevens moet worden afgedwongen door technische maatregelen\. \;\"  

### Wijzigen logging

**Requirement-ID:** `8fb52b47-aac5-5279-9979-dad318e2bdd1`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "LSP.LOG.e4030 "

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

> \"\"\"Gegevens in de log mogen niet wijzigbaar of verwijderbaar \(alleen in het kader van eis \<b\>LSP\.LOG\.e4023\<\/b\>\) zijn\. Het niet kunnen wijzigen\/verwijderen van loggegevens moet worden afgedwongen door technische maatregelen\.   
> 
> \<b\>Functie\<\/b\>  
> Onweerlegbaarheid garanderen van log\.  
> 
> \<b\>Toelichting\<\/b\>  
> Conform NEN 7513\:2018 Paragraaf 6\.4\.3\"\"\"  

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "587157fa-ff1f-5ea9-8110-44def2c5de4f",
    "evidenceIds": [
      "09e14a07-a632-5651-9340-384ba5690f3e"
    ],
    "connectionId": "19ca9b7f-de7d-5fef-a902-29edb16f22f9",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "d6c566e9-770a-5f43-bb6a-04930978bdf2",
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
  "entityId": "d6c566e9-770a-5f43-bb6a-04930978bdf2",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: age.log.e4060 (AORTA REQ) ↔ lsp.log.e4030 (AORTA AS REQ)",
  "description": "Eis age.log.e4060 uit AORTA REQ komt vermoedelijk overeen met eis lsp.log.e4030 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 59.52%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:d6c566e9-770a-5f43-bb6a-04930978bdf2"
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
      "2643785a-e4ba-5eef-9e9b-0ccb82ca4400"
    ],
    "requirementB": [
      "8fb52b47-aac5-5279-9979-dad318e2bdd1"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "age.log.e4060"
    ],
    "requirementNumberB": [
      "lsp.log.e4030"
    ],
    "requirementTitleA": [
      "Wijzigen logging"
    ],
    "requirementTitleB": [
      "Wijzigen logging"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      59.52
    ],
    "conclusion": [
      "Eis age.log.e4060 uit AORTA REQ komt vermoedelijk overeen met eis lsp.log.e4030 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 59.52%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

