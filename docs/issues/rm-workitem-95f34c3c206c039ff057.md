# Mogelijke overeenkomst: gbx.opl.e4170 (AORTA REQ) ↔ gbx.opl.e4170 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: e8ca6d2f-80eb-54d3-8d71-7dd8cedc8dd8

## Bevinding

Eis gbx.opl.e4170 uit AORTA REQ komt vermoedelijk overeen met eis gbx.opl.e4170 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 13.33%. Eisnamen verschillend; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Opleveren contactafspraak

**Requirement-ID:** `f8ec8cce-916e-5307-a3d5-82c436e71093`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.OPL.e4170"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Het XIS moet een opvraag contactafspraak (QUAF_IN990001NL01) kunnen ontvangen en verwerken. Op basis van deze opvraag dient het XIS een antwoord contactafspraak (QUAF_IN990003NL01) te versturen. ;"
```

### Ondersteunen FHIR bevragingen t.b.v. eOverdracht

**Requirement-ID:** `e740606b-66aa-523b-a0ac-f013f296b966`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.OPL.e4170"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis:</b>
Het systeem dient de verschillende FHIR queries te kunnen verwerken en de daarbij behorende resource types te kunnen opleveren zoals beschreven in de gegevensdienst 'eOverdracht'. 
<b>
</b><b>Toelichting bij eis:</b>
De FHIR queries en de in gegevensdienst opgenomen resources zijn beschreven in FHIR-package zoals opgenomen in simplifier. 
"""
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "098f7501-11cf-5612-8db2-f13f23746af4",
    "evidenceIds": [
      "5daaba69-d30d-57dd-9577-ed765eb0e6b2"
    ],
    "connectionId": "8db9a25e-6738-54ef-a5f9-3819109d8b3d",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "e8ca6d2f-80eb-54d3-8d71-7dd8cedc8dd8",
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
  "entityId": "e8ca6d2f-80eb-54d3-8d71-7dd8cedc8dd8",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.opl.e4170 (AORTA REQ) ↔ gbx.opl.e4170 (AORTA AS REQ)",
  "description": "Eis gbx.opl.e4170 uit AORTA REQ komt vermoedelijk overeen met eis gbx.opl.e4170 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 13.33%. Eisnamen verschillend; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:e8ca6d2f-80eb-54d3-8d71-7dd8cedc8dd8"
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
      "f8ec8cce-916e-5307-a3d5-82c436e71093"
    ],
    "requirementB": [
      "e740606b-66aa-523b-a0ac-f013f296b966"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.opl.e4170"
    ],
    "requirementNumberB": [
      "gbx.opl.e4170"
    ],
    "requirementTitleA": [
      "Opleveren contactafspraak"
    ],
    "requirementTitleB": [
      "Ondersteunen FHIR bevragingen t.b.v. eOverdracht"
    ],
    "matchBasis": [
      "NUMBER"
    ],
    "scorePercent": [
      13.33
    ],
    "conclusion": [
      "Eis gbx.opl.e4170 uit AORTA REQ komt vermoedelijk overeen met eis gbx.opl.e4170 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 13.33%. Eisnamen verschillend; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

