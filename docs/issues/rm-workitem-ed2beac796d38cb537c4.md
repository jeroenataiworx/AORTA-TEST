# Mogelijke overeenkomst: gbx.con.e4030.1 (AORTA REQ) ↔ gbx.con.e4030.2 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 6a43c1cd-927b-5eae-9972-80b161d26fc6

## Bevinding

Eis gbx.con.e4030.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4030.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 20.41%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Tijdsynchronisatie GBx en ZIM

**Requirement-ID:** `22c8ccea-4737-535b-afd1-e5ba15b1f5ee`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.CON.e4030.1"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

> \"\; Een GBx dient NTP te gebruiken voor tijdsynchronisatie met de ZIM\. De tijdklok van een GBx mag niet meer dan een halve seconde afwijken van de tijdklok van de ZIM\. \;\"  

### Tijdsynchronisatie GBx en ZIM

**Requirement-ID:** `fbf4359f-8d05-504e-a4bc-d34e8753c344`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.CON.e4030.2"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

> \"\"\"\<b\>Eis\:\<\/b\>  
> Een GBx dient NTP te gebruiken voor tijdsynchronisatie met de ZIM\. De tijdklok van een GBx mag niet meer dan een halve seconde afwijken van de tijdklok van de ZIM\.  
> 
> \<b\>Toelichting bij eis\:\<\/b\>  
> Deze eis is nodig om te voorkomen dat de tijdklok van het GBx gaat afwijken van de tijdklok van de ZIM\. Voor eenzelfde interactie tussen een GBx en de ZIM moeten beide systemen immers dezelfde tijdstempels loggen\. Dit is belangrijk wanneer de toezichthouder of pati\&\#235\;nt een geval van vermeend onrechtmatige uitwisseling van pati\&\#235\;ntgegevens wil onderzoeken en daartoe zowel de lokale toegangslog van het GBx als de centrale toegangslog van het LSP wil raadplegen\.  
> 
> Deze eis betekent voor de organisatie dat er binnen het GBx een NTP\-client is ge\&\#239\;nstalleerd en dat deze is afgestemd op de NTP\-server van de ZIM\. Ook is het mogelijk dat de GZN een gezamenlijke NTP\-client beheert voor alle aangesloten zorgaanbieders en op een andere wijze klaarspeelt dat de tijdklok van hun GBx’en gelijk lopen met die van de ZIM\.   
> 
> Deze eis betekent voor de organisatie dat het GBx periodiek moet synchroniseren tegen een NTP\-server om synchroon te blijven met de ZIM\.\"\"\"  

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "fd61969b-8f11-5f33-a584-9be6419ef240",
    "evidenceIds": [
      "6b42320d-b19e-50f7-a68f-2053b6254a18"
    ],
    "connectionId": "9103708b-ef5f-5949-82e1-d9c13e5ca952",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "6a43c1cd-927b-5eae-9972-80b161d26fc6",
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
  "entityId": "6a43c1cd-927b-5eae-9972-80b161d26fc6",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.con.e4030.1 (AORTA REQ) ↔ gbx.con.e4030.2 (AORTA AS REQ)",
  "description": "Eis gbx.con.e4030.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4030.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 20.41%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:6a43c1cd-927b-5eae-9972-80b161d26fc6"
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
      "22c8ccea-4737-535b-afd1-e5ba15b1f5ee"
    ],
    "requirementB": [
      "fbf4359f-8d05-504e-a4bc-d34e8753c344"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.con.e4030.1"
    ],
    "requirementNumberB": [
      "gbx.con.e4030.2"
    ],
    "requirementTitleA": [
      "Tijdsynchronisatie GBx en ZIM"
    ],
    "requirementTitleB": [
      "Tijdsynchronisatie GBx en ZIM"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      20.41
    ],
    "conclusion": [
      "Eis gbx.con.e4030.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4030.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 20.41%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

