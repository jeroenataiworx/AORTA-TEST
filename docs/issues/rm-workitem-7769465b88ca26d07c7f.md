# Mogelijke overeenkomst: gbx.ida.e4060.1 (AORTA REQ) ↔ gbx.ida.e4060.2 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 5cd36c65-d1c9-55d6-b1ed-be9c21557ce6

## Bevinding

Eis gbx.ida.e4060.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4060.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 17.14%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Gebruik van geverifieerde BSN's

**Requirement-ID:** `97ba4545-8fe0-5764-aacf-bdb75134031c`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.IDA.e4060.1"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

> \"\; Het systeem moet aan \[Opzoeken en tonen patiënteninformatie\]\(pve\-bronsysteem\-tbv\-medmij\.md\#PvEBronsysteemtbvMedMij\-BK\_1292305474\)\, \[Voorlopig koppelen van patiëntgegevens aan een BSN\]\(pve\-bronsysteem\-tbv\-medmij\.md\#PvEBronsysteemtbvMedMij\-BK\_874324176\)\, \[Controleren geldigheid van een WID\]\(pve\-bronsysteem\-tbv\-medmij\.md\#PvEBronsysteemtbvMedMij\-BK\_64071816\)\, en \[Bijhouden behandelrelatie\]\(pve\-bronsysteem\-tbv\-medmij\.md\#PvEBronsysteemtbvMedMij\-BK\_591027313\) voldoen of \(bij implementatie in een GBZ\) een koppeling kunnen leggen met een derde systeem dat aan die eisen voldoet\. \; Een systeem die gebruik maakt van een extern patiëntadministrerend systeem is verplicht om te controleren of een BSN daadwerkelijk aan alle AORTA eisen voldoet m\.b\.t\. het BSN\. \;\"  

### Gebruik van geverifieerde BSN's

**Requirement-ID:** `c4a17219-8d38-52ef-80f3-ab1a2fd9603a`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.IDA.e4060.2"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

> \"\"\"\<b\>Eis\:\<\/b\>  
> 
> Het XIS moet borgstellen dat alle verwerkte en uitgewisselde BSN’s voldoen aan de AORTA\-eisen \(conform GBX\.IDA\.e4010\, e4020\, e4040 en e4050\)\. Het XIS mag deze functionaliteit zelf ondersteunen \&\#243\;f gebruikmaken van een veilige technische koppeling met een extern\, voor deze eisen geaccepteerd pati\&\#235\;ntadministrerend systeem\. Bij gebruik van een extern systeem moet het XIS de BSN\-status controleren\. Indien een BSN niet aan de eisen voldoet\, mag het bericht niet worden verstuurd en moet de gebruiker hierover actief worden ge\&\#239\;nformeerd\.  
> 
> \<b\>Toelichting\:\<\/b\>  
> 
> Het XIS hoeft geen eigen pati\&\#235\;ntadministratie te bevatten\, zolang het via een veilige technische koppeling \(conform de geldende beveiligingsstandaarden\) kan aansluiten op een reeds gekwalificeerd extern systeem binnen de zorgomgeving \(het GBZ\)\.  
> 
> De wijze waarop het XIS de BSN\-status van het externe systeem ontvangt \(actief opvragen of passief ontvangen\) is vrij\.  
> 
> Voorbeeld\: Een arts verstuurt vanuit de XIS\-interface een recept of overdrachtsbericht\. Het XIS doet op de achtergrond een razendsnelle API\-call \(bijv\. via FHIR of HL7\) naar het externe pati\&\#235\;ntadministratiesysteem om de BSN\-status te verifi\&\#235\;ren\. Als het externe systeem de vlag BSN\_GEVERIFIEERD \= False of Status\: Voorlopig teruggeeft\, onderbreekt het XIS de verzending direct\, blokkeert het AORTA\-bericht en toont een melding aan de arts\: \"Bericht kan niet worden verzonden\: BSN van pati\&\#235\;nt \[X\] is nog niet definitief geverifieerd in de pati\&\#235\;ntadministratie\.\"  
> 
> Belangrijkste uitgangspunt is dat er nooit niet\-gevalideerde BSN’s via AORTA\-berichten worden uitgewisseld\; blokkering van het bericht en een duidelijke foutmelding aan de gebruiker borgen deze ketenveiligheid\.  
> 
> \<b\>Condities\:\<\/b\>  
> Deze eis is verplicht indien het XIS gebruik maakt van een extern pati\&\#235\;ntadministrerend syteem bevat\.\"\"\"  

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "e742ce1b-2fb1-5c2b-bf35-ecbe549195ad",
    "evidenceIds": [
      "af6ebe4e-87c1-58a5-b379-5641bfdf291c"
    ],
    "connectionId": "40c99cf1-c50f-54f4-88f5-7dda1ad2124a",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "5cd36c65-d1c9-55d6-b1ed-be9c21557ce6",
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
  "entityId": "5cd36c65-d1c9-55d6-b1ed-be9c21557ce6",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.ida.e4060.1 (AORTA REQ) ↔ gbx.ida.e4060.2 (AORTA AS REQ)",
  "description": "Eis gbx.ida.e4060.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4060.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 17.14%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:5cd36c65-d1c9-55d6-b1ed-be9c21557ce6"
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
      "97ba4545-8fe0-5764-aacf-bdb75134031c"
    ],
    "requirementB": [
      "c4a17219-8d38-52ef-80f3-ab1a2fd9603a"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.ida.e4060.1"
    ],
    "requirementNumberB": [
      "gbx.ida.e4060.2"
    ],
    "requirementTitleA": [
      "Gebruik van geverifieerde BSN's"
    ],
    "requirementTitleB": [
      "Gebruik van geverifieerde BSN's"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      17.14
    ],
    "conclusion": [
      "Eis gbx.ida.e4060.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4060.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 17.14%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

