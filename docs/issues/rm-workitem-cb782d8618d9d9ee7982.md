# Mogelijke overeenkomst: gbx.ida.e4010.1 (AORTA REQ) ↔ gbx.ida.e4010.3 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 01c392d1-804d-5cb7-b2f3-0fbabb770b4f

## Bevinding

Eis gbx.ida.e4010.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4010.3 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 27.61%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Opzoeken en tonen patiëntgegevens

**Requirement-ID:** `1dc71690-db4d-5a59-b267-a6edfe3b863e`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.IDA.e4010.1"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

> \"\; Het systeem moet een gebruiker de mogelijkheid bieden een patiënt op te zoeken in de lokale patiëntadministratie van de zorgaanbieder\, door het invoeren van identificerende gegevens\, waarna wordt getoond\: \;  of de patiënt\/cliënt is gevonden\, en zo ja \;  of het BSN wel\/niet is opgevraagd of geverifieerd bij de SBV\-Z \;  de datum en tijd van koppelen \;  de manier van vaststellen van de identiteit\: \;  Controle van echtheid en geldigheidsdatum van WID en de gelijkenis van de in de WID genoemde identificerende gegevens \;  Vergewissen\, \;  indien beschikbaar het UZI\-nummer of anders een unieke identificatie van de gebruiker en het UZI\-nummer van mandaterende zorgverlener indien van toepassing \;  in geval van WID\-controle\: aard en nummer van het WID\. \;\"  

### Opzoeken en tonen patiëntgegevens

**Requirement-ID:** `92ce1df4-2b4a-59f2-90b5-d3d58d2febca`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.IDA.e4010.3"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

> \"\"\"\<b\>Eis\:\<\/b\>  
> Het systeem moet een gebruiker de mogelijkheid bieden een pati\&\#235\;nt op te zoeken in de lokale pati\&\#235\;ntadministratie van de zorgaanbieder op basis van identificerende gegevens\. Indien de pati\&\#235\;nt wordt gevonden\, toont het systeem de volgende gegevens\:  
> \<ul\>  
> \<li\>BSN\-status\: Of het BSN wel of niet is opgevraagd\/geverifieerd bij de SBV\-Z\;\<\/li\>  
> \<li\>Registratiedatum\: Datum en tijdstip van opname van het BSN in de pati\&\#235\;ntadministratie\;\<\/li\>  
> \<li\>Gebruikers\-ID van registrant\: een unieke gebruikers\-ID van de gebruiker die de gegevens heeft vastgelegd\.\<\/li\>  
> \<li\>Identificatiemethode\: De wijze waarop de identiteit is vastgesteld\, zijnde\:\<\/li\>  
> \<\/ul\>  
> \<ol\>  
> \<li\>WID\-controle\: Controle van echtheid en geldigheidsdatum van het WID en overeenkomst van de persoonsgegevens \(inclusief aard en nummer van het WID\)\; \&\#243\;f\<\/li\>  
> \<li\>Vergewissen\: Indien formeel vergewist conform wetgeving\.\<\/li\>  
> \<\/ol\>  
> 
> \<b\>Toelichting\:\<\/b\>  
> Deze eis borgt de naleving van de Wet gebruik BSN in de zorg \(WGBZ\)\. Door de status van de BSN\-verificatie en de wijze van identiteitsvaststelling lokaal inzichtelijk te maken\, kan de zorgverlener direct beoordelen of de identiteit van de pati\&\#235\;nt rechtmatig is vastgesteld en of hernieuwde verificatie nodig is\.  
> Conform de WGBZ betreft \'vergewissen\' het vaststellen dat de pati\&\#235\;nt de persoon is bij wie het BSN hoort\, zonder dat op dat moment een fysiek wettelijk identiteitsdocument \(WID\) wordt gecontroleerd\. Dit is wettelijk uitsluitend toegestaan in specifieke situaties\, zoals\:  
> \<ul\>  
> \<li\>Een al bestaande\, bekende behandelrelatie\;\<\/li\>  
> \<li\>Spoedeisende zorgverlening\;\<\/li\>  
> \<li\>Situaties waarin de pati\&\#235\;nt fysiek of mentaal niet in staat is een WID te tonen\;\<\/li\>  
> \<li\>Identificatie via een goedgekeurd digitaal identificatiemiddel \(zoals DigiD\)\.\<\/li\>  
> \<\/ul\>  
> Het lokaal tonen en vastleggen van deze status voorkomt daarnaast dat de centrale SBV\-Z\-voorziening bij elke interne raadpleging opnieuw hoeft te worden bevraagd\.\"\"\"  

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "bc9fc2b9-c939-510c-b6c6-135353d0b920",
    "evidenceIds": [
      "b0e03b62-1df0-5221-a82b-869588d775a5"
    ],
    "connectionId": "35480526-5863-53dc-be73-ad9c93eaa4e0",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "01c392d1-804d-5cb7-b2f3-0fbabb770b4f",
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
  "entityId": "01c392d1-804d-5cb7-b2f3-0fbabb770b4f",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.ida.e4010.1 (AORTA REQ) ↔ gbx.ida.e4010.3 (AORTA AS REQ)",
  "description": "Eis gbx.ida.e4010.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4010.3 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 27.61%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:01c392d1-804d-5cb7-b2f3-0fbabb770b4f"
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
      "1dc71690-db4d-5a59-b267-a6edfe3b863e"
    ],
    "requirementB": [
      "92ce1df4-2b4a-59f2-90b5-d3d58d2febca"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.ida.e4010.1"
    ],
    "requirementNumberB": [
      "gbx.ida.e4010.3"
    ],
    "requirementTitleA": [
      "Opzoeken en tonen patiëntgegevens"
    ],
    "requirementTitleB": [
      "Opzoeken en tonen patiëntgegevens"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      27.61
    ],
    "conclusion": [
      "Eis gbx.ida.e4010.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.ida.e4010.3 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 27.61%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

