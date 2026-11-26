# Mogelijke overeenkomst: gbx.bet.e4020.1 (AORTA REQ) ↔ gbx.bet.e4020.2 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: baf6e11a-3aec-5ac9-bc26-67b7f305e9b9

## Bevinding

Eis gbx.bet.e4020.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.bet.e4020.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 26.44%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Borgen van de betrouwbaarheid bij grote storingen

**Requirement-ID:** `ab2432a7-4308-5235-b4e4-db3aeb3ab71f`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.BET.e4020.1"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Grote storingen in een GBx mogen niet meer dan gemiddeld 2 keer per jaar voorkomen en dienen dan binnen 1 dag te zijn opgelost. ;"
```

### Borgen van de betrouwbaarheid bij grote storingen

**Requirement-ID:** `2b82a167-6e64-5cf3-b5ac-2b958a10de8b`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.BET.e4020.2"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis:</b>
Grote storingen in een GBx mogen niet meer dan gemiddeld 2 keer per jaar voorkomen en dienen dan binnen 1 dag te zijn opgelost.

<b>Toelichting bij eis: </b>
De term 'grote storing' is niet SMART gedefinieerd. Het kan vele soorten storingen betreffen. Het doel van deze eis is om te voorkomen dat een GBx na een grote storing zeer lang onbeschikbaar blijft. Onbeschikbaarheid zou bijvoorbeeld kunnen komen omdat er geen onderhoudscontract is en daardoor de hulp slechts langzaam op gang komt. 

Deze eis betekent voor de zorgaanbieder dat er snel teruggevallen moet kunnen worden op de XIS-leverancier, GZN-leverancier en/of andere ICT-leveranciers. Zo moet bij een grote storing, snel een leverancier beschikbaar zijn om het probleem te verhelpen. Wellicht kunnen zijn ICT-leveranciers hem een 24-uurs onderhoudscontract bieden. """
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "6eff8a87-4b3d-5cfe-99ca-3e5b678762fd",
    "evidenceIds": [
      "58a54f88-c947-52a0-9766-8e81bccab4cc"
    ],
    "connectionId": "bfd5b077-6439-5404-bd0f-14f1e14b1092",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "baf6e11a-3aec-5ac9-bc26-67b7f305e9b9",
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
  "entityId": "baf6e11a-3aec-5ac9-bc26-67b7f305e9b9",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.bet.e4020.1 (AORTA REQ) ↔ gbx.bet.e4020.2 (AORTA AS REQ)",
  "description": "Eis gbx.bet.e4020.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.bet.e4020.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 26.44%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:baf6e11a-3aec-5ac9-bc26-67b7f305e9b9"
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
      "ab2432a7-4308-5235-b4e4-db3aeb3ab71f"
    ],
    "requirementB": [
      "2b82a167-6e64-5cf3-b5ac-2b958a10de8b"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.bet.e4020.1"
    ],
    "requirementNumberB": [
      "gbx.bet.e4020.2"
    ],
    "requirementTitleA": [
      "Borgen van de betrouwbaarheid bij grote storingen"
    ],
    "requirementTitleB": [
      "Borgen van de betrouwbaarheid bij grote storingen"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      26.44
    ],
    "conclusion": [
      "Eis gbx.bet.e4020.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.bet.e4020.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 26.44%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

