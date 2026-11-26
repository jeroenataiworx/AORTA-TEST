# Mogelijke overeenkomst: gbx.opv.e4550.1 (AORTA REQ) ↔ gbx.opv.e4550.2 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 3eb48fcb-64a5-5b56-85e0-83528bc6eb84

## Bevinding

Eis gbx.opv.e4550.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.opv.e4550.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 19.35%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Compatibiliteit bieden met de diverse (zorg)toepassingen

**Requirement-ID:** `e8f75214-3c9c-5a49-9fb2-202d5392218c`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.OPV.e4550.1"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Een bronsysteem moet bevragingen van diverse actoren en vanuit diverse organisaties kunnen verwerken. ;"
```

### Compatibiliteit bieden met de diverse (zorg)toepassingen 

**Requirement-ID:** `8fcc0a56-2259-521c-bedc-aeb8e7762664`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.OPV.e4550.2"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis:</b>
Een bronsysteem moet bevragingen van diverse actoren en vanuit diverse organisaties kunnen verwerken. 

<b>Toelichting bij eis:</b>
De volgende actoren of groep van actoren moeten door het bronsysteem worden ondersteunt als opvrager (of opvraagverantwoordelijke):
<ul>
	<li>Een zorgverlener op basis van UZI;</li>
	<li>Een burger op basis van BSN (alleen indien XIS-leverancier gegevens beschikbaar wil stellen aan MedMij via LSP+).</li>
</ul>

De volgende organisaties moeten door het bronsysteem worden ondersteunt als organisatie vanuit waar opgevraagd wordt: 
<ul>
	<li>Resource Broker VnC;</li>
	<li>Pati&#235;ntenportaal (GBP);</li>
	<li>Goed beheerde organisatie (GBO).</li>
</ul>"""
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "4e9ee02c-2c42-533e-845b-dc53c19dcad2",
    "evidenceIds": [
      "f02a4d09-81b5-5744-bf08-c426185ece9b"
    ],
    "connectionId": "51c75191-b67e-5c26-8cfb-99663c17d6a1",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "3eb48fcb-64a5-5b56-85e0-83528bc6eb84",
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
  "entityId": "3eb48fcb-64a5-5b56-85e0-83528bc6eb84",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.opv.e4550.1 (AORTA REQ) ↔ gbx.opv.e4550.2 (AORTA AS REQ)",
  "description": "Eis gbx.opv.e4550.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.opv.e4550.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 19.35%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:3eb48fcb-64a5-5b56-85e0-83528bc6eb84"
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
      "e8f75214-3c9c-5a49-9fb2-202d5392218c"
    ],
    "requirementB": [
      "8fcc0a56-2259-521c-bedc-aeb8e7762664"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.opv.e4550.1"
    ],
    "requirementNumberB": [
      "gbx.opv.e4550.2"
    ],
    "requirementTitleA": [
      "Compatibiliteit bieden met de diverse (zorg)toepassingen"
    ],
    "requirementTitleB": [
      "Compatibiliteit bieden met de diverse (zorg)toepassingen "
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      19.35
    ],
    "conclusion": [
      "Eis gbx.opv.e4550.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.opv.e4550.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 19.35%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

