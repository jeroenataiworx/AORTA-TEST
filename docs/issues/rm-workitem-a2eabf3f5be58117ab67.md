# Mogelijke overeenkomst: gbx.con.e4070.2 (AORTA REQ) ↔ gbx.con.e4070.3 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 9ef5bd8f-6e19-575b-ac6d-23acf685998e

## Bevinding

Eis gbx.con.e4070.2 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4070.3 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 52.46%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Opzetten en gebruiken van TLS-sessies

**Requirement-ID:** `eb65389c-fafb-5532-9ec4-e1cb779a316b`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.CON.e4070.2"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Het GBx moet na het beschikbaar worden voor de ZIM: ;  verzoeken van de ZIM voor het opzetten van nieuwe TLS-sessies honoreren ten behoeve van berichtuitwisseling voor andere zorgaanbieders, ;  {GBx}{GBK}{GBO} voor gebruikers die landelijk patiëntgegevens willen uitwisselen, een of meer TLS-sessies met de ZIM (her)gebruiken voor berichtuitwisseling als gevolg van gebruikersfuncties. ;"
```

### Opzetten en gebruiken van TLS-sessies

**Requirement-ID:** `5fdcd27b-5d3a-500c-b58e-d119dc442d88`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.CON.e4070.3"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis:</b>
Het GBx moet na het beschikbaar worden voor de ZIM:
<ul>
	<li>verzoeken van de ZIM voor het opzetten van nieuwe TLS-sessies honoreren ten behoeve van berichtuitwisseling voor andere zorgaanbieders,</li>
	<li>voor gebruikers die landelijk pati&#235;ntgegevens willen uitwisselen, een of meer TLS-sessies met de ZIM (her)gebruiken voor berichtuitwisseling.</li>
</ul>

<b>Toelichting bij eis:</b>
Deze eis is nodig opdat een GBx beveiligd kan communiceren met de ZIM volgens bewezen technologie op eigen initiatief en op initiatief van de ZIM."""
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "e1e7363e-7812-5f50-b603-ec632ec42e11",
    "evidenceIds": [
      "8c4d26a0-942f-5c6b-95ff-2b0a34929799"
    ],
    "connectionId": "b68240dc-d54f-5935-bafd-323c3eff7351",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "9ef5bd8f-6e19-575b-ac6d-23acf685998e",
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
  "entityId": "9ef5bd8f-6e19-575b-ac6d-23acf685998e",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.con.e4070.2 (AORTA REQ) ↔ gbx.con.e4070.3 (AORTA AS REQ)",
  "description": "Eis gbx.con.e4070.2 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4070.3 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 52.46%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:9ef5bd8f-6e19-575b-ac6d-23acf685998e"
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
      "eb65389c-fafb-5532-9ec4-e1cb779a316b"
    ],
    "requirementB": [
      "5fdcd27b-5d3a-500c-b58e-d119dc442d88"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.con.e4070.2"
    ],
    "requirementNumberB": [
      "gbx.con.e4070.3"
    ],
    "requirementTitleA": [
      "Opzetten en gebruiken van TLS-sessies"
    ],
    "requirementTitleB": [
      "Opzetten en gebruiken van TLS-sessies"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      52.46
    ],
    "conclusion": [
      "Eis gbx.con.e4070.2 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4070.3 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 52.46%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

