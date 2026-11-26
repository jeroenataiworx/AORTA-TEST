# Mogelijke overeenkomst: gbx.ida.e4090 (AORTA REQ) ↔ gbx.ida.e4090.1 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: afbdffc3-3101-5950-8387-427ae7f1bad9

## Bevinding

Eis gbx.ida.e4090 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4090.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 43.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Afbreken van een gebruikerssessie

**Requirement-ID:** `6d851a82-a080-5fd1-aacf-e7debb0f83c9`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.IDA.e4090"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

> \"\; Het systeem moet een gebruikerssessie voor het landelijk uitwisselen van patiëntgegevens op vertrouwensniveau laag of midden afsluiten\: \;  op commando van de gebruiker \(zoals een muisklik of toetsencombinatie\)\; \;  door uitnemen van het vertrouwensmiddel door de zorgverlener\/medewerker\; \;  wanneer de applicatie gedurende gebruiker\-max\-applicatie\-onbruik niet is gebruikt\; \;  wanneer de se\*ssie gedurende\* open staat\. \;  IP\-adres van gebruiker gedurende een sessie wijzigt\. \; De parameter gebruiker\-max\-applicatie\-onbruik is binnen de applicatie instelbaar\, naar redelijkheid en risico\, en heeft een maximale waarde van 60 minuten\. \;\"  

### Afbreken van een gebruikerssessie

**Requirement-ID:** `715535ef-ceb6-5cf6-b770-7bf61828e60c`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.IDA.e4090.1"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

> \"\"\"\<b\>Eis\:\<\/b\>  
> Het systeem moet een gebruikerssessie voor het landelijk uitwisselen van pati\&\#235\;ntgegevens op vertrouwensniveau laag of midden afsluiten\:  
> \<ol\>  
> \<li\>op commando van de gebruiker \(zoals een muisklik of toetsencombinatie\)\;\<\/li\>  
> \<li\>door uitnemen van het vertrouwensmiddel door de zorgverlener\/medewerker\;\<\/li\>  
> \<li\>wanneer de applicatie gedurende maximaal 60 minuten niet is gebruikt\. Deze tijd dient instelbaar te zijn in het systeem\, maar mag niet de 60 minuten overschrijden\;\<\/li\>  
> \<li\>wanneer de gebruikerssessie\<i\> \<\/i\>gedurende 1 uur open staat\;\<\/li\>  
> \<li\>IP\-adres van gebruiker gedurende een sessie wijzigt\.\<\/li\>  
> \<\/ol\>  
> 
> \<b\>Toelichting bij eis\:\<\/b\>  
> Dit is nodig opdat een gebruiker zelf zijn gebruikerssessie kan uitloggen met de zekerheid dat niemand anders zijn sessie kan voortzetten en vervolgens zijn bevoegdheden kan misbruiken\. Daarnaast is deze eis nodig om tegen te gaan dat een in onbruik geraakte sessie door een onbevoegde kan worden misbruikt\.\"\"\"  

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "a2b0ae8b-b555-51af-ad82-097b68b69453",
    "evidenceIds": [
      "c9981f58-95a9-5d70-84d4-d197eb8958a1"
    ],
    "connectionId": "f1b0ebb8-1db9-572a-b7bf-3ecba9297de9",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "afbdffc3-3101-5950-8387-427ae7f1bad9",
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
  "entityId": "afbdffc3-3101-5950-8387-427ae7f1bad9",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.ida.e4090 (AORTA REQ) ↔ gbx.ida.e4090.1 (AORTA AS REQ)",
  "description": "Eis gbx.ida.e4090 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4090.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 43.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:afbdffc3-3101-5950-8387-427ae7f1bad9"
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
      "6d851a82-a080-5fd1-aacf-e7debb0f83c9"
    ],
    "requirementB": [
      "715535ef-ceb6-5cf6-b770-7bf61828e60c"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.ida.e4090"
    ],
    "requirementNumberB": [
      "gbx.ida.e4090.1"
    ],
    "requirementTitleA": [
      "Afbreken van een gebruikerssessie"
    ],
    "requirementTitleB": [
      "Afbreken van een gebruikerssessie"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      43.0
    ],
    "conclusion": [
      "Eis gbx.ida.e4090 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4090.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 43.00%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

