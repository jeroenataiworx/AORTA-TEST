# Mogelijke overeenkomst: sys.bvl.e4010.1 (AORTA REQ) ↔ sys.bvl.e4010.2 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: de5d5b36-1e22-5381-a44b-c40652d791b8

## Bevinding

Eis sys.bvl.e4010.1 uit AORTA REQ komt vermoedelijk overeen met eis sys.bvl.e4010.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 38.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Beveiligde opslag

**Requirement-ID:** `83a41ab8-4fb6-5c33-b0dd-27a96548e250`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "SYS.BVL.e4010.1"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

> \"\; Data die persoonsgegevens bevatten dienen versleuteld en beveiligd te worden opgeslagen\. Het gaat hierbij om alle opgeslagen data \(bv\. logging en backups\)\. \;\"  

### Beveiligde opslag

**Requirement-ID:** `082e0f33-3115-5986-b6a4-e9b07ad558f1`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "SYS.BVL.e4010.2"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

> \"\"\"\<b\>Eis\:\<\/b\>  
> Data die persoonsgegevens bevatten dienen versleuteld en beveiligd te worden opgeslagen\. Het gaat hierbij om alle opgeslagen data \(bv\. logging en backups\)\.  
> 
> \<b\>Toelichting bij eis\:\<\/b\>  
> In principe moet alle data met persoonsgegevens worden ge\&\#235\;ncrypt\. Dit betreft o\.a\. gegevens die worden opgeslagen ten behoeve van een autorisatiesessie\. Mocht hiervan met het oog op systeemprestaties van afgeweken worden\, dan dient dit overlegd te worden met VZVZ\. \"\"\"  

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "5d4ca25b-2afa-5302-a9ba-77cb9e6cb4aa",
    "evidenceIds": [
      "e9f4b2cd-16c0-50cc-91a9-e7593cce9b40"
    ],
    "connectionId": "b0d60c42-e1fe-5320-85a8-939eb603dd53",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "de5d5b36-1e22-5381-a44b-c40652d791b8",
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
  "entityId": "de5d5b36-1e22-5381-a44b-c40652d791b8",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: sys.bvl.e4010.1 (AORTA REQ) ↔ sys.bvl.e4010.2 (AORTA AS REQ)",
  "description": "Eis sys.bvl.e4010.1 uit AORTA REQ komt vermoedelijk overeen met eis sys.bvl.e4010.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 38.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:de5d5b36-1e22-5381-a44b-c40652d791b8"
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
      "83a41ab8-4fb6-5c33-b0dd-27a96548e250"
    ],
    "requirementB": [
      "082e0f33-3115-5986-b6a4-e9b07ad558f1"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "sys.bvl.e4010.1"
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
      "Eis sys.bvl.e4010.1 uit AORTA REQ komt vermoedelijk overeen met eis sys.bvl.e4010.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 38.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

