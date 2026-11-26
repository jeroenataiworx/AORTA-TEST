# Mogelijke overeenkomst: gbx.bvl.e4050.1 (AORTA REQ) ↔ gbx.bvl.e4050.1 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 6b1f2c35-4852-51eb-97f4-860e5b7d8569

## Bevinding

Eis gbx.bvl.e4050.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.bvl.e4050.1 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 86.02%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Borgen betrouwbare koppeling tussen pas en applicatie

**Requirement-ID:** `468c0758-04ed-5b2d-9fb0-df6b5c9bea00`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.BVL.e4050.1"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Een GBx moet zodanig zijn ingericht dat: ;  passen met SHA-256-certificaten gelezen en gebruikt kunnen worden; ;  paslezers gekoppeld zijn aan werkplekken van gebruikers; ;  de PIN-code die ten behoeve van een authenticatiemiddel wordt ingetoetst op een werkplek, exclusief wordt aangeboden aan de gekoppelde paslezer, ;  {GBx} alle gegevens in berichten die ten behoeve van een gebruiker worden ontvangen exclusief aan die gebruiker worden gepresenteerd; ;  {GBK} alle gegevens in HL7-berichten die ten behoeve van een patiëntopdracht worden ontvangen exclusief gekoppeld worden aan de betreffende patiëntopdracht. ;  geborgd wordt dat: ;  {GBx} het in het bericht vermelde UZI-nummer en de rolcode van de auteur overeenkomen met de UZI-pashouder die het bericht heeft geïnitieerd; ;  {GBK} het in het bericht vermelde certificaatnummer en CA van de auteur overeenkomen met de PKIO-pashouder die het bericht heeft geïnitieerd; ;  {GBx} de auteur inderdaad is gemandateerd door de in het bericht vermelde (eind)verantwoordelijke, of dezelfde persoon is; ;  {GBx} de in het bericht vermelde URA van auteur, (eind)verantwoordelijke en zorginstelling aan elkaar gelijk zijn; ;  {GBK} de in het bericht vermelde instellingsindicatie van de auteur het klantenloket is; ;  {GBK} de instelling van de verantwoordelijke niet ingevuld is. ;"
```

### Borgen betrouwbare koppeling tussen pas en applicatie

**Requirement-ID:** `6dcd3f5b-ebc2-5a8c-a07f-f4bf9cb259ab`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.BVL.e4050.1"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis:</b>
Een GBx moet zodanig zijn ingericht dat:
<ol>
	<li>passen met SHA-256-certificaten gelezen en gebruikt kunnen worden;</li>
	<li>paslezers gekoppeld zijn aan werkplekken van gebruikers;</li>
	<li>de PIN-code die ten behoeve van een authenticatiemiddel wordt ingetoetst op een werkplek, exclusief wordt aangeboden aan de gekoppelde paslezer,</li>
	<li>{GBx} alle gegevens in berichten die ten behoeve van een gebruiker worden ontvangen exclusief aan die gebruiker worden gepresenteerd;</li>
	<li>{GBK} alle gegevens in HL7-berichten die ten behoeve van een pati&#235;ntopdracht worden ontvangen exclusief gekoppeld worden aan de betreffende pati&#235;ntopdracht.</li>
	<li>geborgd wordt dat:</li>
</ol>
<ul>
	<li>{GBx} het in het bericht vermelde UZI-nummer en de rolcode van de auteur overeenkomen met de UZI-pashouder die het bericht heeft ge&#239;nitieerd;</li>
	<li>{GBK} het in het bericht vermelde certificaatnummer en CA van de auteur overeenkomen met de PKIO-pashouder die het bericht heeft ge&#239;nitieerd;</li>
	<li>{GBx} de auteur inderdaad is gemandateerd door de in het bericht vermelde (eind)verantwoordelijke, of dezelfde persoon is;</li>
	<li>{GBx} de in het bericht vermelde URA van auteur, (eind)verantwoordelijke en zorginstelling aan elkaar gelijk zijn;</li>
	<li>{GBK} de in het bericht vermelde instellingsindicatie van de auteur het klantenloket is;</li>
	<li>{GBK} de instelling van de verantwoordelijke niet ingevuld is.</li>
</ul>"""
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "52a5a451-3918-59db-8c9a-f34867ddaf5b",
    "evidenceIds": [
      "30519697-a6a8-515f-972c-d9ddd3894fde"
    ],
    "connectionId": "b8b0c768-05d8-552a-af56-aeda0120fa52",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "6b1f2c35-4852-51eb-97f4-860e5b7d8569",
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
  "entityId": "6b1f2c35-4852-51eb-97f4-860e5b7d8569",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.bvl.e4050.1 (AORTA REQ) ↔ gbx.bvl.e4050.1 (AORTA AS REQ)",
  "description": "Eis gbx.bvl.e4050.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.bvl.e4050.1 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 86.02%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:6b1f2c35-4852-51eb-97f4-860e5b7d8569"
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
      "468c0758-04ed-5b2d-9fb0-df6b5c9bea00"
    ],
    "requirementB": [
      "6dcd3f5b-ebc2-5a8c-a07f-f4bf9cb259ab"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.bvl.e4050.1"
    ],
    "requirementNumberB": [
      "gbx.bvl.e4050.1"
    ],
    "requirementTitleA": [
      "Borgen betrouwbare koppeling tussen pas en applicatie"
    ],
    "requirementTitleB": [
      "Borgen betrouwbare koppeling tussen pas en applicatie"
    ],
    "matchBasis": [
      "NUMBER"
    ],
    "scorePercent": [
      86.02
    ],
    "conclusion": [
      "Eis gbx.bvl.e4050.1 uit AORTA REQ komt vermoedelijk overeen met eis gbx.bvl.e4050.1 uit AORTA AS REQ. Selectie op eisnummer; tekstuele overeenkomst 86.02%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

