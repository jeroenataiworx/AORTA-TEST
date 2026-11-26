# Mogelijke overeenkomst: gbx.con.e4090.2 (AORTA REQ) ↔ gbx.con.e4090.3 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: f2c849c3-c5e4-5b6c-9665-995c76a58d37

## Bevinding

Eis gbx.con.e4090.2 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4090.3 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 50.49%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Opzetten beveiligde verbinding vanuit de ZIM met een GBx

**Requirement-ID:** `56970bd0-fa9a-5cd5-a313-53a8d1e5a1f2`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.CON.e4090.2"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Het GBx dient voor het landelijk uitwisselen van patiëntgegevens een TLS-sessie met de ZIM met de volgende kenmerken te accepteren: ;  tweezijdige authenticatie met behulp van het UZI-servercertificaat van het GBZ en het servercertificaat van de ZIM, ;  tijdelijke sleutels die elke systeem-max-sleutel-duur ververst worden, ;  gebruikmakend van Cipher Suites die door het NCSC minimaal worden gekenmerkt als voldoende(goed dus altijd ook) en tevens worden ondersteund door de ZIM.Voor encryptie moet altijd de sterkste vorm als eerste worden geprobeerd, ;  een maximale sessieduur van systeem-max-sessie-duur, ;  een ten hoogste ongebruikte TLS-sessie van systeem-max-sessie-onbruik. ;"
```

### Opzetten beveiligde verbinding vanuit de ZIM met een GBx

**Requirement-ID:** `623581e2-71f4-56e2-b4b7-68cc03fd023b`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.CON.e4090.3"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis:</b>
Het GBx dient voor het landelijk uitwisselen van pati&#235;ntgegevens een TLS-sessie met de ZIM met de volgende kenmerken te accepteren:
<ol>
	<li>tweezijdige authenticatie met behulp van het UZI-servercertificaat van het GBZ en het servercertificaat van de ZIM,</li>
	<li>tijdelijke sleutels die elke 5 minuten ververst worden,</li>
	<li>gebruikmakend van Cipher Suites die door het NCSC minimaal worden gekenmerkt als goed en tevens worden ondersteund door de ZIM. Voor encryptie moet altijd de sterkste vorm als eerste worden geprobeerd,</li>
	<li>een maximale sessieduur van 8 uur,</li>
	<li>een maximale ongebruikte TLS-sessie van 15 minuten.</li>
</ol>

<b>Toelichting bij eis:</b>
Dit is nodig opdat de ZIM een voldoende hoog beveiligingsniveau kan afdwingen bij het opzetten van een TLS-sessie met een GBx.

Dit betekent voor de zorgaanbieder dat hij of zijn XIS-leverancier de bovenstaande parameters moet instellen in de TLS-library in de betrokken XIS-applicatie(s) en/of de eventuele communicatieserver.
"""
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "10228853-e6be-58e2-b4bf-82d90eea20f2",
    "evidenceIds": [
      "aabf86e0-30a7-5afe-90c5-dc26a6a35c5a"
    ],
    "connectionId": "4336cf06-37d7-5de4-8903-49dc0280bbc0",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "f2c849c3-c5e4-5b6c-9665-995c76a58d37",
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
  "entityId": "f2c849c3-c5e4-5b6c-9665-995c76a58d37",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.con.e4090.2 (AORTA REQ) ↔ gbx.con.e4090.3 (AORTA AS REQ)",
  "description": "Eis gbx.con.e4090.2 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4090.3 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 50.49%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:f2c849c3-c5e4-5b6c-9665-995c76a58d37"
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
      "56970bd0-fa9a-5cd5-a313-53a8d1e5a1f2"
    ],
    "requirementB": [
      "623581e2-71f4-56e2-b4b7-68cc03fd023b"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.con.e4090.2"
    ],
    "requirementNumberB": [
      "gbx.con.e4090.3"
    ],
    "requirementTitleA": [
      "Opzetten beveiligde verbinding vanuit de ZIM met een GBx"
    ],
    "requirementTitleB": [
      "Opzetten beveiligde verbinding vanuit de ZIM met een GBx"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      50.49
    ],
    "conclusion": [
      "Eis gbx.con.e4090.2 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4090.3 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 50.49%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

