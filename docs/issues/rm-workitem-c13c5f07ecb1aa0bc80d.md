# Mogelijke overeenkomst: gbx.opl.e4130 (AORTA REQ) ↔ gbx.opl.e4130 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 771271c5-af32-5cb9-b11f-d9bc73007dd4

## Bevinding

Eis gbx.opl.e4130 uit AORTA REQ komt vermoedelijk overeen met eis gbx.opl.e4130 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 32.31%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Opleveren correspondentie

**Requirement-ID:** `2fad7c18-f5eb-5776-aa8e-81992526c21e`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.OPL.e4130"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Het XIS moet een opvraag correspondentie (QUCO_IN990001NL01) kunnen ontvangen en verwerken. Op basis van deze opvraag dient het XIS een antwoord correspondentie (QUCO_IN990003NL01) te versturen. ;"
```

### Opleveren correspondentie

**Requirement-ID:** `66422109-2a43-5149-93f0-188abf1c84c6`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.OPL.e4130"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis: </b>
<b>
</b>Het XIS moet een opvraag correspondentie (QUCO_IN990001NL01) kunnen ontvangen en verwerken. Op basis van deze opvraag dient het XIS een antwoord correspondentie (QUCO_IN990003NL01) te versturen. 
<b>
</b><b>Toelichting bij eis:</b>
<b>
</b>Het is mogelijk dat de opvraag specifieke parameters bevat. Het XIS moet op basis van het ontvangen bericht met de daarin opgenomen parameters een antwoord samenstellen. Zowel het binnenkomende opvraagbericht als het uitgaande antwoordbericht staan uitgewerkt in [Art-Decor].

Indien bij het verwerken van het binnenkomende opvraagbericht een fout optreedt of een andere reden waarom het opvraagbericht niet verwerkt kan worden, dan dient er een (fout)melding geretourneerd te worden volgens de [Foutentabel]. """
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "7cfd63c2-126e-57ab-bfa6-f54d9ccf6903",
    "evidenceIds": [
      "a533d809-939d-5110-bb49-7154b4f7fd2e"
    ],
    "connectionId": "0b267485-9d57-5525-9f0b-bf161930313d",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "771271c5-af32-5cb9-b11f-d9bc73007dd4",
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
  "entityId": "771271c5-af32-5cb9-b11f-d9bc73007dd4",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.opl.e4130 (AORTA REQ) ↔ gbx.opl.e4130 (AORTA AS REQ)",
  "description": "Eis gbx.opl.e4130 uit AORTA REQ komt vermoedelijk overeen met eis gbx.opl.e4130 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 32.31%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:771271c5-af32-5cb9-b11f-d9bc73007dd4"
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
      "2fad7c18-f5eb-5776-aa8e-81992526c21e"
    ],
    "requirementB": [
      "66422109-2a43-5149-93f0-188abf1c84c6"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.opl.e4130"
    ],
    "requirementNumberB": [
      "gbx.opl.e4130"
    ],
    "requirementTitleA": [
      "Opleveren correspondentie"
    ],
    "requirementTitleB": [
      "Opleveren correspondentie"
    ],
    "matchBasis": [
      "NUMBER"
    ],
    "scorePercent": [
      32.31
    ],
    "conclusion": [
      "Eis gbx.opl.e4130 uit AORTA REQ komt vermoedelijk overeen met eis gbx.opl.e4130 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 32.31%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

