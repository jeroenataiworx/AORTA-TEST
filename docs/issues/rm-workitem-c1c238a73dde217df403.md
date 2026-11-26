# Mogelijke overeenkomst: gbx.ida.e4015 (AORTA REQ) ↔ gbx.ida.e4015.3 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 58778730-009a-5656-bfdb-c08c721a63b5

## Bevinding

Eis gbx.ida.e4015 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4015.3 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 11.57%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Verwerken geboortedatums waarin nullen zijn opgenomen

**Requirement-ID:** `7a26cad5-0809-57b5-b495-08a5ed95df13`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.IDA.e4015"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

> \"\; Een geboortedatum die teruggegeven wordt door de SBV\-Z kan nullen bevatten \(jjjjmm00\, jjjj0000 of 00000000\)\. Het XIS moet in staat zijn hiermee adequaat om te gaan zonder dat de applicatie vastloopt\. \;\"  

### Verwerken geboortedatums waarin nullen zijn opgenomen

**Requirement-ID:** `8aad4511-ed83-508c-92a1-81a50bfc6466`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.IDA.e4015.3"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

> \"\"\"\<b\>Eis\:\<\/b\>  
> Het XIS moet adequaat om kunnen gaan met onvolledige of ontbrekende geboortedatums \(formaten jjjjmm00\, jjjj0000 of 00000000\) zoals geleverd door de SBV\-Z\, zonder dat de applicatie vastloopt of foutmeldingen geeft\.  
> 
> Afgeleide functionele eisen\:  
> \<ul\>  
> \<li\>Het XIS moet het BSN kunnen opvragen en verifi\&\#235\;ren via Zoekpad 1 en Zoekpad 2 conform de SBV\-Z\-specificaties\.\<\/li\>  
> \<li\>Wanneer de door de SBV\-Z geleverde geboortedatum niet direct door de database geaccepteerd wordt\, moet het XIS de gebruiker in staat stellen de geboortedatum handmatig aan te passen naar een geldige datum v\&\#243\;\&\#243\;r opslag\.\<\/li\>  
> \<li\>Het aanpassen van een geboortedatum binnen de vergelijkingsdialoog mag niet leiden tot het verlies van de status \'BSN geverifieerd\'\.\<\/li\>  
> \<li\>Indien een gebruiker de geboortedatum buiten de SBV\-Z\-vergelijkingsdialoog om wijzigt\, moet de status \'BSN geverifieerd\' automatisch vervallen\.\<\/li\>  
> \<li\>Het XIS moet registreren \&\#233\;n tonen wanneer een geboortedatum handmatig is aangepast ten opzichte van het SBV\-Z\-antwoord\.\<\/li\>  
> \<li\>De dienst \'Opvragen persoonsgegevens op BSN\' moet ook uitgevoerd kunnen worden voor reeds bekende pati\&\#235\;nten waarvan de eerdere verificatie is mislukt door een afwijkende of onvolledige geboortedatum\. Het XIS toont in dat geval een dialoogvenster waarin de gegevens uit de SBV\-Z en de lokale database naast elkaar worden vergeleken\.\<\/li\>  
> \<\/ul\>  
> 
> \<b\>Toelichting\:\<\/b\>  
> Er worden\<b\> \<\/b\>twee zoekpaden ondersteund door het SBV\-Z\:  
> \<ul\>  
> \<li\>Zoekpad 1 \(Opvragen op BSN\)\: Het rechtstreeks opvragen of verifi\&\#235\;ren van persoonsgegevens bij de SBV\-Z op basis van het BSN\. Dit zoekpad wordt gebruikt wanneer het BSN van de pati\&\#235\;nt reeds bekend is in het XIS\.\<\/li\>  
> \<li\>Zoekpad 2 \(Zoeken op persoonsgegevens\)\: Het opzoeken van een BSN bij de SBV\-Z op basis van een combinatie van identificerende persoonsgegevens \(zoals geboortedatum\, geslacht\, postcode en huisnummer\)\, voor situaties waarin het BSN nog niet bekend is \(zoals bij niet\-ingezetenen\)\.\<\/li\>  
> \<\/ul\>  
> 
> Veel databasestructuren vereisen een valide datumformaat \(dd\-mm\-jjjj\)\. Omdat SBV\-Z nulwaarden toestaat voor dag en\/of maand bij onbekende geboortedatums\, dient het XIS te zorgen voor een correcte afhandeling \(bijvoorbeeld via conversie naar een geaccepteerd opslagformaat of een gecontroleerde gebruikersinvoer\)\.  
> 
> Om inzichtelijk te houden dat een datum afwijkt van de brongegevens van de SBV\-Z\, dient het systeem dit herkenbaar vast te leggen\. Dit kan bijvoorbeeld worden vormgegeven door\:  
> \<ul\>  
> \<li\>Een visuele indicator in de interface \(bijv\. een label\, icoon of afwijkende tekst\-\/achtergrondkleur\)\.\<\/li\>  
> \<li\>Het opgeslagen houden van de originele SBV\-Z\-waarde in een afzonderlijk audit\- of referentieveld\.\<\/li\>  
> \<\/ul\>  
> 
> De afwijking in de geboortedatum is een bekend issue bij historische\/onvolledige persoonsgegevens\. Door de BSN\-verificatie in stand te houden binnen de dialoog\, wordt voorkomen dat valide burgers opnieuw handmatig gecontroleerd moeten worden\. Aanpassingen achteraf \(buiten het SBV\-proces\) verbreken echter de wettelijke keten van verificatie\, waardoor de geverifieerde status logischerwijs moet vervallen\.\"\"\"  

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "c8255710-80c6-587f-b637-21aa7060f48c",
    "evidenceIds": [
      "974a6346-873f-5592-ae06-ef1f12ea2307"
    ],
    "connectionId": "d08f9606-f0b1-5e7b-b14e-be43072e890c",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "58778730-009a-5656-bfdb-c08c721a63b5",
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
  "entityId": "58778730-009a-5656-bfdb-c08c721a63b5",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.ida.e4015 (AORTA REQ) ↔ gbx.ida.e4015.3 (AORTA AS REQ)",
  "description": "Eis gbx.ida.e4015 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4015.3 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 11.57%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:58778730-009a-5656-bfdb-c08c721a63b5"
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
      "7a26cad5-0809-57b5-b495-08a5ed95df13"
    ],
    "requirementB": [
      "8aad4511-ed83-508c-92a1-81a50bfc6466"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.ida.e4015"
    ],
    "requirementNumberB": [
      "gbx.ida.e4015.3"
    ],
    "requirementTitleA": [
      "Verwerken geboortedatums waarin nullen zijn opgenomen"
    ],
    "requirementTitleB": [
      "Verwerken geboortedatums waarin nullen zijn opgenomen"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      11.57
    ],
    "conclusion": [
      "Eis gbx.ida.e4015 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4015.3 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 11.57%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

