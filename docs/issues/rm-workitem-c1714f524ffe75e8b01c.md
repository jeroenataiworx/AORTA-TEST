# Mogelijke overeenkomst: gbx.ida.e4050 (AORTA REQ) ↔ gbx.ida.e4050.1 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 21edc39f-70f3-555a-9600-ca1332014470

## Bevinding

Eis gbx.ida.e4050 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4050.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 47.19%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Bijhouden behandelrelatie

**Requirement-ID:** `f7471adf-49f1-5c7f-b4a2-2ce944981cfb`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.IDA.e4050"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Het systeem moet een gebruiker de volgende mogelijkheden bieden in de lokale patiëntadministratie voor een patiënt/cliënt. ; De status van de behandelrelatie inzien, waarbij wordt getoond: ;  of een behandelrelatie bestaat, en zo ja met welke zorgverleners een behandelrelatie bestaat; ;  ten behoeve van welke zorgaanbieder (URA) de behandelrelatie wordt onderhouden. ; Een nieuwe behandelrelatie beginnen, waarbij wordt vastgelegd: ;  begindatum; ;  UZI-nummer van de zorgverlener; ;  de URA van de zorgaanbieder ten behoeve van wie de behandelrelatie onderhouden wordt. ; Een bestaande behandelrelatie beëindigen, waarbij wordt vastgelegd: ;  einddatum; ;  UZI-nummer van de zorgverlener. ;"
```

### Bijhouden behandelrelatie

**Requirement-ID:** `03d942d6-bbb2-51f0-a967-956bc5b0e738`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.IDA.e4050.1"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis:</b>
Het systeem moet een gebruiker de volgende mogelijkheden bieden in de lokale pati&#235;ntadministratie voor een pati&#235;nt/cli&#235;nt.

De status van de behandelrelatie inzien, waarbij wordt getoond:
<ol>
	<li>of een behandelrelatie bestaat, en zo ja met welke zorgverleners (in ieder geval o.b.v. UZI) een behandelrelatie bestaat;</li>
	<li>ten behoeve van welke zorgaanbieder (in ieder geval o.b.v. URA) de behandelrelatie wordt onderhouden.</li>
</ol>

Een nieuwe behandelrelatie beginnen, waarbij wordt vastgelegd:
<ol>
	<li>begindatum;</li>
	<li>UZI-nummer van de zorgverlener;</li>
	<li>de URA van de zorgaanbieder ten behoeve van wie de behandelrelatie onderhouden wordt.</li>
</ol>

Een bestaande behandelrelatie be&#235;indigen, waarbij wordt vastgelegd:
<ol>
	<li>einddatum;</li>
	<li>UZI-nummer van de zorgverlener.</li>
</ol>

<b>Toelichting bij eis:</b>
De zorgverlener onderhoudt de behandelrelatie hetzij ten behoeve van de zorgaanbieder waarvoor hij werkzaam is, hetzij als zorgaanbieder indien het een zelfstandig werkende beroepsbeoefenaar betreft.

Een zorgverlener die de pati&#235;nt/cli&#235;nt niet ziet, bijvoorbeeld in een laboratorium, legt een behandelrelatie vast in de zin van een verklaring dat hij werkt in opdracht van een andere zorgverlener die een behandelrelatie met de pati&#235;nt/cli&#235;nt heeft."""
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "076c3ab0-da54-5dc0-9d9c-04a6b1807be9",
    "evidenceIds": [
      "376e86bb-8d38-5004-86d6-8703348f86d3"
    ],
    "connectionId": "d4f4540e-b481-5f51-a2a3-ef2f4cf6c1f5",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "21edc39f-70f3-555a-9600-ca1332014470",
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
  "entityId": "21edc39f-70f3-555a-9600-ca1332014470",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.ida.e4050 (AORTA REQ) ↔ gbx.ida.e4050.1 (AORTA AS REQ)",
  "description": "Eis gbx.ida.e4050 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4050.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 47.19%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:21edc39f-70f3-555a-9600-ca1332014470"
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
      "f7471adf-49f1-5c7f-b4a2-2ce944981cfb"
    ],
    "requirementB": [
      "03d942d6-bbb2-51f0-a967-956bc5b0e738"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.ida.e4050"
    ],
    "requirementNumberB": [
      "gbx.ida.e4050.1"
    ],
    "requirementTitleA": [
      "Bijhouden behandelrelatie"
    ],
    "requirementTitleB": [
      "Bijhouden behandelrelatie"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      47.19
    ],
    "conclusion": [
      "Eis gbx.ida.e4050 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4050.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 47.19%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

