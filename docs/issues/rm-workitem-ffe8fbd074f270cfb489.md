# Mogelijke overeenkomst: gbx.log.e4015.1 (AORTA REQ) ↔ gbx.log.e4015.1 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: c53cdb68-d329-5793-a351-4391c5f0e0f5

## Bevinding

Eis gbx.log.e4015.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.log.e4015.1 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 48.33%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Toegangslog bijhouden

**Requirement-ID:** `95ba57f3-8579-5b3e-82d8-c1299c002b12`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.LOG.e4015.1"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

> \"\; Het systeem moet de volgende berichtuitwisselingen loggen\: \;  Ontvangen opvraagberichten en de daarop verzonden antwoorden\; \;  Verzonden opvraagberichten en daarop verkregen antwoorden\; \;  Verzonden opdrachtberichten en kennisgevingberichten\. \; De log bevat per berichtuitwisseling tenminste\: \;  de identiteit van de patiënt\/cliënt \(BSN\) \;  identiteit van de opvragende\/versturende en bestemde organisatie \;  de functie en identiteit van de opvragende of versturende zorgverlener of medewerker of patiënt\. \;  type van de uitgevoerde gebruikersinteractie \;  het tijdstip en tijdzone \(ten opzichte van UTC\) van de gebruikersinteractie \;  de bericht\-id van het ontvangen \(opvraag\- of bevestig\-\) bericht \;  de bericht\-id van het verzonden \(oplever\- of opdracht\-\) bericht \;  de gegevenssoorten of contextcodes van de verzonden en ontvangen patiëntstukken\; \;  een indicatie van eventueel opgetreden foutsituaties met betrekking tot het ontvangen en verzenden van de berichten\. \;\"  

### Toegangslog bijhouden

**Requirement-ID:** `6c45cab0-cdfb-59f5-9a15-b542aadd5f34`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.LOG.e4015.1"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

> \"\"\"\<b\>Eis\:\<\/b\>  
> Het systeem moet de volgende berichtuitwisselingen loggen\:  
> \<ol\>  
> \<li\>Ontvangen opvraagberichten en de daarop verzonden antwoorden\;\<\/li\>  
> \<li\>Verzonden opvraagberichten en daarop verkregen antwoorden\;\<\/li\>  
> \<li\>Verzonden opdrachtberichten en kennisgevingberichten\.\<\/li\>  
> \<\/ol\>  
> 
> De log bevat per berichtuitwisseling tenminste\:  
> \<ol\>  
> \<li\>de identiteit van de pati\&\#235\;nt\/cli\&\#235\;nt \(BSN\)\<\/li\>  
> \<li\>identiteit van de opvragende\/versturende en bestemde organisatie\<\/li\>  
> \<li\>de functie en identiteit van de opvragende of versturende zorgverlener of medewerker of pati\&\#235\;nt\.\<\/li\>  
> \<li\>type van de uitgevoerde gebruikersinteractie\<\/li\>  
> \<li\>het tijdstip en tijdzone \(ten opzichte van UTC\) van de gebruikersinteractie\<\/li\>  
> \<li\>de bericht\-id van het ontvangen \(opvraag\- of bevestig\-\) bericht\<\/li\>  
> \<li\>de bericht\-id van het verzonden \(oplever\- of opdracht\-\) bericht\<\/li\>  
> \<li\>de gegevenssoorten of contextcodes van de verzonden en ontvangen pati\&\#235\;ntstukken\;\<\/li\>  
> \<li\>een indicatie van eventueel opgetreden foutsituaties met betrekking tot het ontvangen en verzenden van de berichten\.\<\/li\>  
> \<\/ol\>  
> 
> \<b\>Toelichting bij eis\: \<\/b\>  
> Dit is nodig opdat aan de hand van de berichtuitwisseling precies achterhaald kan worden\:  
> \<ul\>  
> \<li\>\{GBx\}wat voor soort pati\&\#235\;ntstukken wanneer zijn opgevraagd door welke zorgverlener\/medewerker van welke andere zorgaanbieder\;\<\/li\>  
> \<li\>\{GBK\} wat voor soort opvragingen\, opdrachten en kennisgevingen wanneer zijn verzonden resp\. ontvangen door welke klantenloketmedewerker\;\<\/li\>  
> \<li\>wat voor soort pati\&\#235\;ntstukken wanneer zijn toegestuurd aan welke andere zorgaanbieder of ZIM\;\<\/li\>  
> \<li\>welke gegevensklasse die pati\&\#235\;ntstukken precies hadden\;\<\/li\>  
> \<li\>wat voor soort pati\&\#235\;ntstukken wanneer zijn opgevraagd door welke pati\&\#235\;nt vanuit welke organisatie\.\<\/li\>  
> \<\/ul\>  
> 
> Dit betekent voor de zorgaanbieder dat hij of zijn XIS\-leverancier deze berichtenlogfunctie moet inbouwen in de betrokken XIS\-applicatie\(s\) of de eventuele communicatieserver\.\"\"\"  

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "c3f36861-fcdb-5c8c-9272-8f85f7b2cc95",
    "evidenceIds": [
      "32b500ce-e420-52de-93ee-be64e4889b4a"
    ],
    "connectionId": "506247e2-7656-5a2e-9756-98c1c5e6422f",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "c53cdb68-d329-5793-a351-4391c5f0e0f5",
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
  "entityId": "c53cdb68-d329-5793-a351-4391c5f0e0f5",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.log.e4015.1 (AORTA REQ) ↔ gbx.log.e4015.1 (AORTA AS REQ)",
  "description": "Eis gbx.log.e4015.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.log.e4015.1 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 48.33%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:c53cdb68-d329-5793-a351-4391c5f0e0f5"
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
      "95ba57f3-8579-5b3e-82d8-c1299c002b12"
    ],
    "requirementB": [
      "6c45cab0-cdfb-59f5-9a15-b542aadd5f34"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.log.e4015.1"
    ],
    "requirementNumberB": [
      "gbx.log.e4015.1"
    ],
    "requirementTitleA": [
      "Toegangslog bijhouden"
    ],
    "requirementTitleB": [
      "Toegangslog bijhouden"
    ],
    "matchBasis": [
      "NUMBER"
    ],
    "scorePercent": [
      48.33
    ],
    "conclusion": [
      "Eis gbx.log.e4015.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.log.e4015.1 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 48.33%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

