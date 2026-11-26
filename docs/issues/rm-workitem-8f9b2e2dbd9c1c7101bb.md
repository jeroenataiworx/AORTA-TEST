# Mogelijke overeenkomst: gbx.ida.e4040 (AORTA REQ) ↔ gbx.ida.e4040.1 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 7193f466-beef-5daa-9995-aef82e4c489c

## Bevinding

Eis gbx.ida.e4040 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4040.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 60.23%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Controleren geldigheid van een WID

**Requirement-ID:** `0fd75867-b142-5a08-8056-be38735e8d31`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.IDA.e4040"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Het systeem moet voor een geselecteerde patiënt/cliënt de gebruiker de mogelijkheid bieden: ;  het 'in omloop mogen zijn' van het WID te controleren door raadplegen van de SBV-Z op basis van aard en nummer van het WID; ;  in de lokale patiëntenindex vast te leggen dat hij 'het in omloop mogen zijn' van het WID heeft gecontroleerd, onder vermelding van: ;  resultaat van de controle, ;  datum en tijd, ;  indien beschikbaar het UZI-nummer of anders een unieke identificatie van de gebruiker, ;  aard en nummer van het WID. ;  de onder 2. vastgelegde informatie op elk gewenst moment te raadplegen. ;"
```

### Controleren geldigheid van een WID

**Requirement-ID:** `296a6553-2c3e-52a4-a4cb-03a4843a0921`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.IDA.e4040.1"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis:</b>
Het systeem moet voor een geselecteerde pati&#235;nt/cli&#235;nt de gebruiker de mogelijkheid bieden:
<ol>
	<li>het 'in omloop mogen zijn' van het WID te controleren door raadplegen van de SBV-Z op basis van aard en nummer van het WID;</li>
	<li>in de lokale pati&#235;ntenindex vast te leggen dat hij 'het in omloop mogen zijn' van het WID heeft gecontroleerd, onder vermelding van:</li>
</ol>
            - resultaat van de controle;
            - datum en tijd;
            - indien beschikbaar het UZI-nummer of anders een unieke               identificatie van de gebruiker;
            - aard en nummer van het WID.
<ol>
	<li>de onder 2. vastgelegde informatie op elk gewenst moment te raadplegen.</li>
</ol>

<b>Toelichting bij eis:</b>
Dit is belangrijk voor een zorgverlener/medewerker die in geval van twijfel over de echtheid of geldigheid van een WID wil nagaan of deze in omloop mag zijn. Hiertoe biedt de SBV-Z een dienst om te kunnen controleren of een bepaald WID in omloop mag zijn."""
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "dbbaa8ae-1e70-5aef-a61b-918138360081",
    "evidenceIds": [
      "0a202dc9-e2a4-5f77-93c7-be685eee830b"
    ],
    "connectionId": "b4b86f21-f19d-5261-a49c-b50b93aa6bc4",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "7193f466-beef-5daa-9995-aef82e4c489c",
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
  "entityId": "7193f466-beef-5daa-9995-aef82e4c489c",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.ida.e4040 (AORTA REQ) ↔ gbx.ida.e4040.1 (AORTA AS REQ)",
  "description": "Eis gbx.ida.e4040 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4040.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 60.23%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:7193f466-beef-5daa-9995-aef82e4c489c"
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
      "0fd75867-b142-5a08-8056-be38735e8d31"
    ],
    "requirementB": [
      "296a6553-2c3e-52a4-a4cb-03a4843a0921"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.ida.e4040"
    ],
    "requirementNumberB": [
      "gbx.ida.e4040.1"
    ],
    "requirementTitleA": [
      "Controleren geldigheid van een WID"
    ],
    "requirementTitleB": [
      "Controleren geldigheid van een WID"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      60.23
    ],
    "conclusion": [
      "Eis gbx.ida.e4040 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4040.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 60.23%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

