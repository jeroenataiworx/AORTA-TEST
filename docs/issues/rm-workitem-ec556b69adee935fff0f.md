# Mogelijke overeenkomst: gbx.opv.e4514 (AORTA REQ) ↔ gbx.opv.e4514.1 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 8dca4308-6fd1-5303-bdf7-b18988e395da

## Bevinding

Eis gbx.opv.e4514 uit AORTA REQ komt vermoedelijk overeen met eis gbx.opv.e4514.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 13.13%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Afhandelen bouwstenen door een bronsysteem

**Requirement-ID:** `4ae5d9c6-8fa1-5dfe-9760-bf6a00f6039c`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.OPV.e4514"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

> \"\; Een XIS dat bouwsteentypen oplevert\, moet van die bouwsteentypen alle mogelijke bouwsteeninstantiaties kunnen opleveren\. \;\"  

### Afhandelen bouwstenen door een bronsysteem

**Requirement-ID:** `e368c202-aded-5e69-99ae-bc30f8158e51`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.OPV.e4514.1"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

> \"\"\"\<b\>Eis\: \<\/b\>  
> Een XIS dat bouwsteentypen oplevert\, moet van die bouwsteentypen alle mogelijke bouwsteeninstantiaties kunnen opleveren\.  
> 
> \<b\>Toelichting bij eis\: \<\/b\>  
> Een zorgtoepassing beschrijft welke bouwstenen en met welke filter\- en queryparameters dienen te worden opgevraagd binnen een specifieke context voor een bepaalde rolcode\. De filter\- en queryparameters perken de op te leveren bouwstenen in m\.b\.t\. de opgenomen informatie\. Denk hierbij bijvoorbeeld aan een tijdsinperking \(queryparameter\) of een inperking o\.b\.v\. een codetabel zoals de NHG \(filterparameters\)\. Het bouwsteenresulaat als gevolg van de inperkingen worden bouwsteeninstantiaties genoemd\.   
> Een bronsysteem dient altijd geaccepteerd te worden voor het opleveren van de bouwstenen zonder de verschillende beperkingen\. Dit is van belang om eventuele compatibiliteit met andere zorgtoepassingen te kunnen garanderen\. Daarnaast leiden eventuele aanpassingen in de SDS tabellen \(waarin de verschillende filter\- en queryparameters zijn opgenomen\) niet noodzakelijk tot wijzigingen bij het bronsysteem\.   
> Deze eis garandeert snellere doorlooptijden aan de kant van een XIS met betrekking tot de implementatie van nieuwe zorgtoepassingen en\/of wijzigingen aan de SDS\.\"\"\"  

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "5bb83d68-b378-5bb8-9eb3-b6201bb0fcb2",
    "evidenceIds": [
      "2ff7dc29-b3c9-5297-bb60-0dbe42a07d84"
    ],
    "connectionId": "240ed967-1934-581f-9bc5-10a8ac6f957e",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "8dca4308-6fd1-5303-bdf7-b18988e395da",
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
  "entityId": "8dca4308-6fd1-5303-bdf7-b18988e395da",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.opv.e4514 (AORTA REQ) ↔ gbx.opv.e4514.1 (AORTA AS REQ)",
  "description": "Eis gbx.opv.e4514 uit AORTA REQ komt vermoedelijk overeen met eis gbx.opv.e4514.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 13.13%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:8dca4308-6fd1-5303-bdf7-b18988e395da"
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
      "4ae5d9c6-8fa1-5dfe-9760-bf6a00f6039c"
    ],
    "requirementB": [
      "e368c202-aded-5e69-99ae-bc30f8158e51"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.opv.e4514"
    ],
    "requirementNumberB": [
      "gbx.opv.e4514.1"
    ],
    "requirementTitleA": [
      "Afhandelen bouwstenen door een bronsysteem"
    ],
    "requirementTitleB": [
      "Afhandelen bouwstenen door een bronsysteem"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      13.13
    ],
    "conclusion": [
      "Eis gbx.opv.e4514 uit AORTA REQ komt vermoedelijk overeen met eis gbx.opv.e4514.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 13.13%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

