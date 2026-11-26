# Mogelijke overeenkomst: gbx.con.e4100 (AORTA REQ) ↔ gbx.con.e4100 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: b5ef858c-9c3e-5ecf-ad96-f2c6541eafb2

## Bevinding

Eis gbx.con.e4100 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4100 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 41.94%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Kenbaar maken Certificate Authorities

**Requirement-ID:** `6e9a6149-7f30-5b97-ac54-a754c075c5d6`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.CON.e4100"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

> \"\; Het GBx dient alleen de keten van Certificate Authorities \(CA\'s\) van het GBX\-certificaat kenbaar te maken aan de ZIM in het \\\"certificate request\\\" bericht van de TLS\-handshake\, waaronder ook het stamcertificaat \(Root CA\) van de keten\. \;\"  

### Kenbaar maken Certificate Authorities

**Requirement-ID:** `a4d242bd-e576-5d6d-abba-82fd7ee8ff90`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.CON.e4100"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

> \"\"\"\<b\>Eis\:\<\/b\>  
> Het GBx dient alleen de keten van Certificate Authorities \(CA\'s\) van het GBX\-certificaat kenbaar te maken aan de ZIM  in het “certificate request” bericht van de TLS\-handshake\, waaronder ook het stamcertificaat \(Root CA\) van de keten\.  
> 
> \<b\>Toelichting bij eis\:\<\/b\>  
> Dit is nodig opdat een GBx beperkt kenbaar maakt welke CA\'s het vertrouwt\.  
> 
> Dit betekent voor de zorgaanbieder dat hij of zijn XIS\-leverancier selectief om moet gaan met het aantal CA\'s waarmee de betrokken XIS\-applicatie\(s\) en\/of de eventuele communicatieserver worden opgezet\.\"\"\"  

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "8ee627bb-7347-5d8e-9566-f3cd3b9f924e",
    "evidenceIds": [
      "85e34120-f2bb-5b0f-86c7-b971d83a434f"
    ],
    "connectionId": "24c91a9a-6914-5716-b344-d99eebf87269",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "b5ef858c-9c3e-5ecf-ad96-f2c6541eafb2",
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
  "entityId": "b5ef858c-9c3e-5ecf-ad96-f2c6541eafb2",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.con.e4100 (AORTA REQ) ↔ gbx.con.e4100 (AORTA AS REQ)",
  "description": "Eis gbx.con.e4100 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4100 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 41.94%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:b5ef858c-9c3e-5ecf-ad96-f2c6541eafb2"
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
      "6e9a6149-7f30-5b97-ac54-a754c075c5d6"
    ],
    "requirementB": [
      "a4d242bd-e576-5d6d-abba-82fd7ee8ff90"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.con.e4100"
    ],
    "requirementNumberB": [
      "gbx.con.e4100"
    ],
    "requirementTitleA": [
      "Kenbaar maken Certificate Authorities"
    ],
    "requirementTitleB": [
      "Kenbaar maken Certificate Authorities"
    ],
    "matchBasis": [
      "NUMBER"
    ],
    "scorePercent": [
      41.94
    ],
    "conclusion": [
      "Eis gbx.con.e4100 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4100 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 41.94%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

