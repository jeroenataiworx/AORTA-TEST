# Mogelijke overeenkomst: gbx.ida.e4020 (AORTA REQ) ↔ gbx.ida.e4020.1 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: d99cfc22-696f-573a-ab58-71abc12cbe21

## Bevinding

Eis gbx.ida.e4020 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4020.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 47.13%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Voorlopig koppelen van patiëntgegevens aan een BSN

**Requirement-ID:** `96fa43bb-22cb-5fac-93a0-a28675d56ade`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.IDA.e4020"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

> \"\; Het systeem moet een gebruiker de mogelijkheid bieden het door een burgerregister geretourneerde BSN te koppelen aan de identificerende gegevens in de lokale patiëntenindex waarbij bij het overgenomen BSN automatisch wordt vastgelegd\: \;  de bron van het BSN\; \;  datum en tijd van koppelen\; \;  UZI\-nummer of andere identificatie van de gebruiker\. \; Er is dan sprake van een voorlopige koppeling tussen BSN en patiëntgegevens\. \;\"  

### Voorlopig koppelen van patiëntgegevens aan een BSN

**Requirement-ID:** `0668b068-dbb9-57b0-b383-0aa2b88959a5`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.IDA.e4020.1"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

> \"\"\"\<b\>Eis\:\<\/b\>  
> Het systeem moet een gebruiker de mogelijkheid bieden het door een burgerregister geretourneerde BSN te koppelen aan de identificerende gegevens in de gebruikte pati\&\#235\;ntadministratie waarbij bij het overgenomen BSN automatisch wordt vastgelegd\:  
> \<ol\>  
> \<li\>de bron van het BSN\;\<\/li\>  
> \<li\>datum en tijd van koppelen\;\<\/li\>  
> \<li\>UZI\-nummer of andere identificatie van de systeemgebruiker\.\<\/li\>  
> \<\/ol\>  
> 
> Er is dan sprake van een voorlopige koppeling tussen BSN en pati\&\#235\;ntgegevens\.  
> 
> \<b\>Toelichting bij eis\:\<\/b\>  
> Dit is nodig opdat een zorgverlener\/medewerker kan voldoen aan de wettelijke verplichting van de zorgaanbieder om het BSN op te nemen in zijn administratie\, zie de ‘Wet aanvullende bepalingen verwerking persoonsgegevens in de zorg’ \(Wabvpz\)\. Voor het landelijk uitwisselen van medische pati\&\#235\;ntgegevens moet de SBV\-Z of de GBA\/BRP zijn geraadpleegd\.\"\"\"  

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "dcd5afd6-62a4-5435-8604-3c9598e47607",
    "evidenceIds": [
      "d28bac7f-c733-5d4e-aef4-b31f6502706c"
    ],
    "connectionId": "0dff567b-c6af-542b-b4da-56e77ee0be4a",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "d99cfc22-696f-573a-ab58-71abc12cbe21",
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
  "entityId": "d99cfc22-696f-573a-ab58-71abc12cbe21",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.ida.e4020 (AORTA REQ) ↔ gbx.ida.e4020.1 (AORTA AS REQ)",
  "description": "Eis gbx.ida.e4020 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4020.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 47.13%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:d99cfc22-696f-573a-ab58-71abc12cbe21"
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
      "96fa43bb-22cb-5fac-93a0-a28675d56ade"
    ],
    "requirementB": [
      "0668b068-dbb9-57b0-b383-0aa2b88959a5"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.ida.e4020"
    ],
    "requirementNumberB": [
      "gbx.ida.e4020.1"
    ],
    "requirementTitleA": [
      "Voorlopig koppelen van patiëntgegevens aan een BSN"
    ],
    "requirementTitleB": [
      "Voorlopig koppelen van patiëntgegevens aan een BSN"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      47.13
    ],
    "conclusion": [
      "Eis gbx.ida.e4020 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4020.1 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 47.13%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

