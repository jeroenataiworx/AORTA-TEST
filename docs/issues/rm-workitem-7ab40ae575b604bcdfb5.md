# Mogelijke overeenkomst: age.log.e4070 (AORTA REQ) ↔ lsp.log.e4045 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 7037484b-503f-529f-a216-25b3c4e38194

## Bevinding

Eis age.log.e4070 uit AORTA REQ komt vermoedelijk overeen met eis lsp.log.e4045 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 62.86%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Loggen toegangsregeling

**Requirement-ID:** `8271b9f4-ba2d-5bf7-84bf-ab1f7dac6e48`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "AGE.LOG.e4070"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

> \"\; Elke wijziging in de toegangsregeling dient te worden gelogd\. Hierbij moet onweerlegbaar kunnen worden vastgesteld welke persoon met welke rol welke specifieke aanpassing heeft doorgevoerd\. \;\"  

### Loggen toegangsregeling

**Requirement-ID:** `755ad690-85e1-5be4-b8c6-434f8353460e`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "LSP.LOG.e4045 "

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

> \"\"\"Elke wijziging in de toegangsregeling dient te worden gelogd\. Hierbij moet onweerlegbaar kunnen worden vastgesteld welke persoon met welke rol welke specifieke aanpassing heeft doorgevoerd\.   
> 
> \<b\>Functie\<\/b\>  
> Traceerbaarheid van aanpassingen in de toegangsregeling\.  
> 
> \<b\>Toelichting\<\/b\>  
> Conform NEN 7513\:2018 Paragraaf 6\.3 \"\"\"  

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "6ca59efc-fef4-5edd-bf84-ccf81ab8aa11",
    "evidenceIds": [
      "c617f944-ff1f-5054-a66f-98d4e835f59a"
    ],
    "connectionId": "3eb8c817-b02a-59c0-bf48-fe34365647d3",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "7037484b-503f-529f-a216-25b3c4e38194",
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
  "entityId": "7037484b-503f-529f-a216-25b3c4e38194",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: age.log.e4070 (AORTA REQ) ↔ lsp.log.e4045 (AORTA AS REQ)",
  "description": "Eis age.log.e4070 uit AORTA REQ komt vermoedelijk overeen met eis lsp.log.e4045 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 62.86%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:7037484b-503f-529f-a216-25b3c4e38194"
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
      "8271b9f4-ba2d-5bf7-84bf-ab1f7dac6e48"
    ],
    "requirementB": [
      "755ad690-85e1-5be4-b8c6-434f8353460e"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "age.log.e4070"
    ],
    "requirementNumberB": [
      "lsp.log.e4045"
    ],
    "requirementTitleA": [
      "Loggen toegangsregeling"
    ],
    "requirementTitleB": [
      "Loggen toegangsregeling"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      62.86
    ],
    "conclusion": [
      "Eis age.log.e4070 uit AORTA REQ komt vermoedelijk overeen met eis lsp.log.e4045 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 62.86%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

