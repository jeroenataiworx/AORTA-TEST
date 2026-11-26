# Mogelijke overeenkomst: gbx.stu.e4520 (AORTA REQ) ↔ gbx.stu.e4520.2 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 202032f5-3696-53c3-b14d-85a7f768fdbe

## Bevinding

Eis gbx.stu.e4520 uit AORTA REQ komt vermoedelijk overeen met eis gbx.stu.e4520.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 28.05%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Opslaan ontvangen patiëntgegevens

**Requirement-ID:** `db93aa70-7993-5aac-9285-a9780c9c54cf`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.STU.e4520"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Wanneer patiëntgegevens, die conform [Ontvangen en verwerken van opgestuurde patiëntgegevens](pve-his-tbv-open.md#PvEHIStbvOPEN-BK_282514849) zijn ontvangen, ongewijzigd in de eigen patiëntadministratie worden opgenomen en de patiëntgegevens niet ontvangen zijn in het kader van een dossieroverdracht, dan moet worden vastgelegd dat het een kopie betreft. ;"
```

### Opslaan ontvangen patiëntgegevens

**Requirement-ID:** `c17af446-3c63-592d-80c3-6f6cbe1a97b1`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.STU.e4520.2"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis:</b>
Wanneer ontvangen pati&#235;ntgegevens ongewijzigd in de eigen pati&#235;ntadministratie worden opgenomen en de pati&#235;ntgegevens zijn niet ontvangen in het kader van een dossieroverdracht, dan moet worden vastgelegd dat het een kopie betreft.

<b>Toelichting bij eis: </b>
Gewoonlijk zullen pati&#235;ntgegevens die via het LSP worden ontvangen in de eigen pati&#235;ntadministratie worden opgenomen. Wanneer dit automatisch gebeurt is het raadzaam om de geadresseerde gebruiker van de verwerkte berichten op de hoogte te stellen.
In het verlengde hiervan kan de zorgverlener eigen aantekeningen toevoegen, of de ontvangen gegevens wijzigen. Gewijzigd overgenomen gegevens worden beschouwd als eigen dossiergegevens.
Wanneer een gebruiker, als kopie aangemerkte, gegevens raadpleegt is het raadzaam om aan te geven dat het een kopie betreft, en dat de gegevens mogelijk zijn verouderd."""
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "8ffa6967-605b-5350-a259-dbfc79a984ea",
    "evidenceIds": [
      "87e5e64d-6ab8-55d1-8fab-0ed513812a78"
    ],
    "connectionId": "f0de0310-7ae5-5b6e-a7c9-60c2b93fbd3f",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "202032f5-3696-53c3-b14d-85a7f768fdbe",
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
  "entityId": "202032f5-3696-53c3-b14d-85a7f768fdbe",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.stu.e4520 (AORTA REQ) ↔ gbx.stu.e4520.2 (AORTA AS REQ)",
  "description": "Eis gbx.stu.e4520 uit AORTA REQ komt vermoedelijk overeen met eis gbx.stu.e4520.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 28.05%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:202032f5-3696-53c3-b14d-85a7f768fdbe"
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
      "db93aa70-7993-5aac-9285-a9780c9c54cf"
    ],
    "requirementB": [
      "c17af446-3c63-592d-80c3-6f6cbe1a97b1"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.stu.e4520"
    ],
    "requirementNumberB": [
      "gbx.stu.e4520.2"
    ],
    "requirementTitleA": [
      "Opslaan ontvangen patiëntgegevens"
    ],
    "requirementTitleB": [
      "Opslaan ontvangen patiëntgegevens"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      28.05
    ],
    "conclusion": [
      "Eis gbx.stu.e4520 uit AORTA REQ komt vermoedelijk overeen met eis gbx.stu.e4520.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 28.05%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

