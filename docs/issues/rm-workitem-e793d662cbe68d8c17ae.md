# Mogelijke overeenkomst: gbx.con.e4080.4 (AORTA REQ) ↔ gbx.con.e4080.7 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 8c6e1417-0a1c-574c-818e-d709c14e6a4f

## Bevinding

Eis gbx.con.e4080.4 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4080.7 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 47.71%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Opzetten beveiligde verbinding met de ZIM

**Requirement-ID:** `e8ebbfca-d824-5436-8b1a-916dccb023b0`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.CON.e4080.4"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

> \"\; Het GBx dient voor het landelijk uitwisselen van patiëntgegevens een TLS\-sessie met de ZIM met de volgende kenmerken op te zetten\: \;  tweezijdige authenticatie met behulp van het servercertificaat van de ZIM en \;  \(indien tokenauthenticatie\) het servercertificaat van het GBx voor vertrouwensniveau midden \;  het servercertificaat van het GBx voor vertrouwensniveau laag \{GBK\} en midden \;  tijdelijke sleutels die elke applicatie\-max\-sleutel\-duur ververst worden door middel van TLS Secure Renegotiation\; \;  gebruikmakend van Cipher Suites die door het NCSC minimaal worden gekenmerkt als voldoende\; \;  gebruikmakend van de sterkste cipher suite die gedeeld wordt met de ZIM\; \;  gebruikmakend van de hoogste toegestane TLS\-versie die door beide partijen wordt ondersteunt\; \;  een ten hoogste ongebruikte TLS\-sessie van applicatie\-max\-sessie\-onbruik\. \;\"  

### Opzetten beveiligde verbinding met de ZIM

**Requirement-ID:** `e52c798f-97d2-5928-9be1-27167a1cd855`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.CON.e4080.7"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

> \"\"\"\<b\>Eis\:\<\/b\>  
> Het GBx dient voor het landelijk uitwisselen van pati\&\#235\;ntgegevens een TLS\-sessie met de ZIM met de volgende kenmerken op te zetten\:  
> \<ol\>  
> \<li\>tweezijdige authenticatie met behulp van het servercertificaat van de ZIM en het servercertificaat van het GBx\;\<\/li\>  
> \<li\>tijdelijke sleutels die elke 5 minuten ververst worden door middel van TLS Secure Renegotiation\;\<\/li\>  
> \<li\>gebruikmakend van Cipher Suites die door het NCSC minimaal worden gekenmerkt als goed\;\<\/li\>  
> \<li\>gebruikmakend van de sterkste cipher suite die gedeeld wordt met de ZIM\;\<\/li\>  
> \<li\>gebruikmakend van de hoogste toegestane TLS\-versie die door beide partijen wordt ondersteund\;\<\/li\>  
> \<li\>een ongebruikte TLS\-sessie van maximaal 15 minuten\.\<\/li\>  
> \<\/ol\>  
> 
> \<b\>Toelichting bij eis\: \<\/b\>  
> Dit is nodig opdat een GBx een voldoende hoog beveiligingsniveau kan afdwingen bij het opzetten van een TLS\-sessie met de ZIM\.  
> Dit betekent voor de organisatie dat hij of zijn XIS\-leverancier de bovenstaande parameters moet instellen in de TLS\-library in de betrokken applicatie\(s\) en\/of de eventuele communicatieserver\. Hiermee wordt tweezijdige authenticatie bewerkstelligd\.\"\"\"  

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "b1470ded-1847-52ff-8f32-96e481c3725b",
    "evidenceIds": [
      "b09c38ca-4448-5772-ad6a-008458646ecc"
    ],
    "connectionId": "6cfd5e90-c684-54b8-b8b5-50780caab9a3",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "8c6e1417-0a1c-574c-818e-d709c14e6a4f",
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
  "entityId": "8c6e1417-0a1c-574c-818e-d709c14e6a4f",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.con.e4080.4 (AORTA REQ) ↔ gbx.con.e4080.7 (AORTA AS REQ)",
  "description": "Eis gbx.con.e4080.4 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4080.7 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 47.71%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:8c6e1417-0a1c-574c-818e-d709c14e6a4f"
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
      "e8ebbfca-d824-5436-8b1a-916dccb023b0"
    ],
    "requirementB": [
      "e52c798f-97d2-5928-9be1-27167a1cd855"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.con.e4080.4"
    ],
    "requirementNumberB": [
      "gbx.con.e4080.7"
    ],
    "requirementTitleA": [
      "Opzetten beveiligde verbinding met de ZIM"
    ],
    "requirementTitleB": [
      "Opzetten beveiligde verbinding met de ZIM"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      47.71
    ],
    "conclusion": [
      "Eis gbx.con.e4080.4 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4080.7 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 47.71%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

