# Mogelijke overeenkomst: gbx.fbh.e4030 (AORTA REQ) ↔ gbx.fbh.e4030.1 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 61100724-2a7e-5a7c-b815-3a0e715d5230

## Bevinding

Eis gbx.fbh.e4030 uit AORTA REQ komt vermoedelijk overeen met eis gbx.fbh.e4030.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 51.72%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Bijhouden van een gebruikersregistratie

**Requirement-ID:** `ded42d99-9589-51b1-a198-d50c91a24f41`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.FBH.e4030"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Binnen het GBx dient te worden bijgehouden welke UZI-passen worden toegelaten voor gebruik. Deze gebruikersregistratie is uitsluitend toegankelijk voor gebruikers van de gastheerinstelling, na authenticatie op basis van een sterk authenticatiemiddel (2 factorauthenticatie bijvoorbeeld via een UZI-pas) van diezelfde gastheerinstelling. ;"
```

### Bijhouden van een gebruikersregistratie

**Requirement-ID:** `14c31701-e556-5dc6-ac8b-7f6977f10968`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.FBH.e4030.1"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis:</b>

Binnen het GBx dient te worden bijgehouden welke UZI-passen worden toegelaten voor gebruik. Deze gebruikersregistratie is uitsluitend toegankelijk voor de rol van autorisatiebeheerder, na authenticatie op basis van een sterk authenticatiemiddel (tweefactorauthenticatie bijvoorbeeld via een UZI-pas).

<b>Toelichting bij eis:</b>

Dit is nodig om te voorkomen dat een willekeurig persoon de gebruikersregistratie kan aanpassen. 
Dit betekent voor de zorgaanbieder dat hij invulling moet geven aan de rol van autorisatiebeheerder. """
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "57c0d2cf-9ee3-5cd4-941b-1874184f9d5e",
    "evidenceIds": [
      "8382c103-dd70-5cb0-87e5-c34d6fb8dae7"
    ],
    "connectionId": "859407db-f552-5c4f-8c58-1d4661b00bda",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "61100724-2a7e-5a7c-b815-3a0e715d5230",
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
  "entityId": "61100724-2a7e-5a7c-b815-3a0e715d5230",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.fbh.e4030 (AORTA REQ) ↔ gbx.fbh.e4030.1 (AORTA AS REQ)",
  "description": "Eis gbx.fbh.e4030 uit AORTA REQ komt vermoedelijk overeen met eis gbx.fbh.e4030.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 51.72%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:61100724-2a7e-5a7c-b815-3a0e715d5230"
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
      "ded42d99-9589-51b1-a198-d50c91a24f41"
    ],
    "requirementB": [
      "14c31701-e556-5dc6-ac8b-7f6977f10968"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.fbh.e4030"
    ],
    "requirementNumberB": [
      "gbx.fbh.e4030.1"
    ],
    "requirementTitleA": [
      "Bijhouden van een gebruikersregistratie"
    ],
    "requirementTitleB": [
      "Bijhouden van een gebruikersregistratie"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      51.72
    ],
    "conclusion": [
      "Eis gbx.fbh.e4030 uit AORTA REQ komt vermoedelijk overeen met eis gbx.fbh.e4030.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 51.72%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

