# Mogelijke overeenkomst: gbx.con.e4130.1 (AORTA REQ) ↔ gbx.con.e4130.1 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 7a81746b-8efe-5851-8848-6dbd6ea5dc4c

## Bevinding

Eis gbx.con.e4130.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4130.1 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 48.94%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Protocolstack voor gegevensuitwisseling o.b.v. FHIR

**Requirement-ID:** `e7f61783-bb35-55e9-9dfd-2ff802fd2b4d`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.CON.e4130.1"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

> \"\; Het GBx dient voor berichtuitwisseling met de ZIM de volgende protocolstack te gebruiken\: \;  HL7 FHIR \;  JWT \;  HTTP v1\.1\/HTTP v2\.0 \;  TLS\-verbindingen met NCSC beveiligingsniveau “goed” \;  TCP \;  IPv4 \;\"  

### Protocolstack voor gegevensuitwisseling o.b.v. FHIR

**Requirement-ID:** `86efb759-1196-584a-a819-8bf9e68c678f`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.CON.e4130.1"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

> \"\"\"\<b\>Eis\:\<\/b\>  
> Het GBx dient voor berichtuitwisseling met de ZIM de volgende protocolstack te gebruiken\:  
> \<ul\>  
> \<li\>HL7 FHIR\<\/li\>  
> \<li\>JWT\<\/li\>  
> \<li\>HTTP v1\.1\/HTTP v2\.0\<\/li\>  
> \<li\>TLS 1\.3\<\/li\>  
> \<li\>TCP\<\/li\>  
> \<li\>IPv4\<\/li\>  
> \<\/ul\>  
> 
> \<b\>Toelichting bij eis\:\<\/b\>  
> Het is niet toegestaan om een lagere protocolversie te hanteren dan die in deze protocolstack vermeld is\.\"\"\"  

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "2c8e3d1f-e1dc-586f-8ece-6782d8dec10d",
    "evidenceIds": [
      "3b59d2a9-7125-5228-8479-9e32b8062145"
    ],
    "connectionId": "cfe25353-e4e3-5eaf-81c9-aef6be786ff5",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "7a81746b-8efe-5851-8848-6dbd6ea5dc4c",
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
  "entityId": "7a81746b-8efe-5851-8848-6dbd6ea5dc4c",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.con.e4130.1 (AORTA REQ) ↔ gbx.con.e4130.1 (AORTA AS REQ)",
  "description": "Eis gbx.con.e4130.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4130.1 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 48.94%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:7a81746b-8efe-5851-8848-6dbd6ea5dc4c"
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
      "e7f61783-bb35-55e9-9dfd-2ff802fd2b4d"
    ],
    "requirementB": [
      "86efb759-1196-584a-a819-8bf9e68c678f"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.con.e4130.1"
    ],
    "requirementNumberB": [
      "gbx.con.e4130.1"
    ],
    "requirementTitleA": [
      "Protocolstack voor gegevensuitwisseling o.b.v. FHIR"
    ],
    "requirementTitleB": [
      "Protocolstack voor gegevensuitwisseling o.b.v. FHIR"
    ],
    "matchBasis": [
      "NUMBER"
    ],
    "scorePercent": [
      48.94
    ],
    "conclusion": [
      "Eis gbx.con.e4130.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4130.1 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 48.94%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

