# Mogelijke overeenkomst: age.log.e4010 (AORTA REQ) ↔ lsp.log.e4017 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 2831b6a8-1b25-5268-a0c2-52d0dfcb2fd9

## Bevinding

Eis age.log.e4010 uit AORTA REQ komt vermoedelijk overeen met eis lsp.log.e4017 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 20.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Bewaartermijn loggegevens

**Requirement-ID:** `8848ca1f-96da-5372-b136-7055888de0cd`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "AGE.LOG.e4010"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

> \"\; De bewaartermijn van de toegangsloggegevens is \*\<toegangslog\_bewaartermijn\>\.\* Voor de overige logs \(technische logs\) geldt een bewaartermijn van \*\<systeemlog\_bewaartermijn\>\.\* \;\"  

### Bewaartermijn loggegevens

**Requirement-ID:** `b6ef3e92-240a-5f29-9e8e-4ff98d066abe`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "LSP.LOG.e4017 "

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

> \"\"\"De bewaartermijn van de toegangloggegevens is \<i\>\&lt\;LSP\_toeganglog\_bewaartermijn\&gt\;\.\<\/i\> Voor de overige logs \(technische logs\) geldt een bewaartermijn van \<i\>\&lt\;LSP\_systeemlog\_bewaartermijn\&gt\;\.\<\/i\>  
> 
> \<b\>Functie\<\/b\>  
> Persisteren loggegevens\.  
> 
> \<b\>Toelichting\<\/b\>  
> Voor de toegangslog \(log met betrekking tot patiëntgegevens\) geldt \(mogelijk\) een andere bewaartermijn dan voor de systeemlog\. Conform NEN 7513\:2018 paragraaf 8\.5 kan een patiënt binnen een bepaalde tijdsperiode nog aanspraak maken op inzage in de loggegevens\. Deze tijdsperiode kan voor de technische log echter onnodig lang zijn en daarmee onnodig veel opslagcapaciteit verbruiken\.\"\"\"  

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "247a2012-329a-55ef-8e2e-53c450629aa7",
    "evidenceIds": [
      "64bf7afd-d989-5af2-8439-95af1d3abfcd"
    ],
    "connectionId": "d02dc278-37f4-538b-95a7-b430fe3694b3",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "2831b6a8-1b25-5268-a0c2-52d0dfcb2fd9",
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
  "entityId": "2831b6a8-1b25-5268-a0c2-52d0dfcb2fd9",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: age.log.e4010 (AORTA REQ) ↔ lsp.log.e4017 (AORTA AS REQ)",
  "description": "Eis age.log.e4010 uit AORTA REQ komt vermoedelijk overeen met eis lsp.log.e4017 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 20.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:2831b6a8-1b25-5268-a0c2-52d0dfcb2fd9"
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
      "8848ca1f-96da-5372-b136-7055888de0cd"
    ],
    "requirementB": [
      "b6ef3e92-240a-5f29-9e8e-4ff98d066abe"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "age.log.e4010"
    ],
    "requirementNumberB": [
      "lsp.log.e4017"
    ],
    "requirementTitleA": [
      "Bewaartermijn loggegevens"
    ],
    "requirementTitleB": [
      "Bewaartermijn loggegevens"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      20.0
    ],
    "conclusion": [
      "Eis age.log.e4010 uit AORTA REQ komt vermoedelijk overeen met eis lsp.log.e4017 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 20.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

