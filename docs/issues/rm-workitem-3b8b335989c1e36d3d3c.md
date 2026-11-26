# Mogelijke overeenkomst: gbx.ida.e4080.3 (AORTA REQ) ↔ gbx.ida.e4080.5 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: de59b047-e81b-58b3-985a-c5cfce9001ff

## Bevinding

Eis gbx.ida.e4080.3 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4080.5 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 69.52%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Inloggen op vertrouwensniveau midden

**Requirement-ID:** `5cd7d55f-0f7e-5a42-bbc7-410be7bea0aa`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.IDA.e4080.3"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

> \"\; Het systeem moet een gebruiker de mogelijkheid bieden een gebruikerssessie op vertrouwensniveau midden te starten door\: \;  \{GBx\}\{GBK\}het invoeren van zijn vertrouwensmiddel op de werkplek en het invoeren van de bijbehorende toegangscode\; \;  \{GBP\} zich op niveau DigiD\-midden te authenticeren\. \; \{GBx\} Een GBx dient hierbij een UZI\-pas toe te laten indien\: \;  de UZI\-pas is vastgelegd in de gebruikerstabel \(zie ook eis GBX\.FBH\.e4030\)\; \;  het passen betreft die zijn uitgegeven onder de op dat moment geldende certificaatboom of –bomen\. \(SHA\-256\)\. \; Hierbij dient de applicatie te controleren of het certificaat op de pas niet op de CRL staat\. \; \{GBK\} Een GBK dient hierbij een PKIO\-pas toe te laten indien de betreffende medewerker geautoriseerd is voor toegang tot de GBK\-applicatie en te weigeren in de overige gevallen\. \;\"  

### Inloggen op vertrouwensniveau midden

**Requirement-ID:** `b6527454-c217-504e-bbd4-2cd21dec7d12`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.IDA.e4080.5"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

> \"\"\"\<b\>Eis\:\<\/b\>  
> Het systeem moet een gebruiker de mogelijkheid bieden een gebruikerssessie op vertrouwensniveau midden te starten door\:  
> \<ol\>  
> \<li\>\{GBx\}\{GBK\}het invoeren van zijn vertrouwensmiddel op de werkplek en het invoeren van de bijbehorende toegangscode\;\<\/li\>  
> \<li\>\{GBP\} zich op niveau DigiD\-midden te authentiseren\.\<\/li\>  
> \<\/ol\>  
> 
> \{GBx\} Een GBx dient hierbij een UZI\-pas toe te laten indien\:  
> \<ol\>  
> \<li\>de UZI\-pas is geregistreerd in de gebruikerstabel \(zie ook eis GBX\.FBH\.e4030\)\;\<\/li\>  
> \<li\>de UZI\-pas nog geldig is\;\<\/li\>  
> \<li\>het passen betreft die zijn uitgegeven onder de op dat moment geldende certificaatboom of –bomen\. \(SHA\-256\)\.\<\/li\>  
> \<\/ol\>  
> 
> Hierbij dient de applicatie te controleren of het certificaat op de pas niet op de CRL staat\.  
> 
> \{GBK\} Een GBK dient hierbij een PKIO\-pas toe te laten indien de betreffende medewerker geautoriseerd is voor toegang tot de GBK\-applicatie en te weigeren in de overige gevallen\.  
> 
> \<b\>Toelichting bij eis\:\<\/b\>  
> Dit is nodig opdat gebruikers in staat worden gesteld tot het landelijk uitwisselen van gegevens op vertrouwensniveau midden\.  
> 
> VZVZ biedt gratis generieke tooling in de vorm van ZORG\-ID om de implementatie van het authentiseren met de UZI\-pas te ondersteunen\.\"\"\"  

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "8e085f43-7f3a-5b8e-94f6-647abe8e1bd2",
    "evidenceIds": [
      "c959b88c-873a-5711-b545-448fb9c36b8e"
    ],
    "connectionId": "4bc5b46b-6884-5e55-a912-827464dd30f3",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "de59b047-e81b-58b3-985a-c5cfce9001ff",
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
  "entityId": "de59b047-e81b-58b3-985a-c5cfce9001ff",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.ida.e4080.3 (AORTA REQ) ↔ gbx.ida.e4080.5 (AORTA AS REQ)",
  "description": "Eis gbx.ida.e4080.3 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4080.5 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 69.52%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:de59b047-e81b-58b3-985a-c5cfce9001ff"
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
      "5cd7d55f-0f7e-5a42-bbc7-410be7bea0aa"
    ],
    "requirementB": [
      "b6527454-c217-504e-bbd4-2cd21dec7d12"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.ida.e4080.3"
    ],
    "requirementNumberB": [
      "gbx.ida.e4080.5"
    ],
    "requirementTitleA": [
      "Inloggen op vertrouwensniveau midden"
    ],
    "requirementTitleB": [
      "Inloggen op vertrouwensniveau midden"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      69.52
    ],
    "conclusion": [
      "Eis gbx.ida.e4080.3 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4080.5 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 69.52%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

