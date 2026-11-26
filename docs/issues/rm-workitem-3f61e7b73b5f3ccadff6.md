# Mogelijke overeenkomst: age.log.e4050 (AORTA REQ) ↔ lsp.log.e4023 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: b47a86f4-40c8-5ba4-9621-3914beeaa245

## Bevinding

Eis age.log.e4050 uit AORTA REQ komt vermoedelijk overeen met eis lsp.log.e4023 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 63.77%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Vernietigen loggegevens

**Requirement-ID:** `24313a31-868a-5042-b9ea-f73389ae8c77`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "AGE.LOG.e4050"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Loggegevens moeten bij het verstrijken van <*log_bewaartermijn>* automatisch worden verwijderd uit de actieve log en uit het archief. De logregels moeten op een zodanige wijze vernietigd worden dat de data niet te reconstrueren is. Dit betekent ook dat eventueel reservekopieen verwijderd/vernietigd/volledig overschreven zijn. ; **Toestemming** ; Conform NEN 7513:2018 paragraaf 8.5. ; Elke afsprakenstelsel/architectuur dient expliciet invulling te geven aan de waarde voor <*log_bewaartermijn>.* Indien deze waarde ontbreekt dan geldt de standaard waarde van 5 jaar. ;"
```

### Vernietigen loggegevens

**Requirement-ID:** `c0a4176f-28ca-5833-a818-20bb1fca5368`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "LSP.LOG.e4023 "

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""Loggegevens moeten bij het verstrijken van &lt;<i>LSP_log_bewaartermijn&gt; </i>automatisch worden verwijderd uit de actieve log en uit het archief. De logregels moeten op een zodanige wijze vernietigd worden dat de data niet te reconstrueren is. Dit betekent ook dat eventueel reservekopieen verwijderd/vernietigd/volledig overschreven zijn.

<b>Functie</b>
Automatisch verwijderen loggegevens na verstrijken bewaartermijn<b>.</b>
<b>
</b><b>Toestemming</b>
Conform NEN 7513:2018 paragraaf 8.5"""
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "ced1e40f-093b-524e-b3ba-b8bc5fa269b3",
    "evidenceIds": [
      "de934220-cf76-5074-8a5d-6df357365efd"
    ],
    "connectionId": "647fb7bb-b6dc-5dc7-b6ed-bbae01c619b8",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "b47a86f4-40c8-5ba4-9621-3914beeaa245",
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
  "entityId": "b47a86f4-40c8-5ba4-9621-3914beeaa245",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: age.log.e4050 (AORTA REQ) ↔ lsp.log.e4023 (AORTA AS REQ)",
  "description": "Eis age.log.e4050 uit AORTA REQ komt vermoedelijk overeen met eis lsp.log.e4023 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 63.77%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:b47a86f4-40c8-5ba4-9621-3914beeaa245"
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
      "24313a31-868a-5042-b9ea-f73389ae8c77"
    ],
    "requirementB": [
      "c0a4176f-28ca-5833-a818-20bb1fca5368"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "age.log.e4050"
    ],
    "requirementNumberB": [
      "lsp.log.e4023"
    ],
    "requirementTitleA": [
      "Vernietigen loggegevens"
    ],
    "requirementTitleB": [
      "Vernietigen loggegevens"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      63.77
    ],
    "conclusion": [
      "Eis age.log.e4050 uit AORTA REQ komt vermoedelijk overeen met eis lsp.log.e4023 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 63.77%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

