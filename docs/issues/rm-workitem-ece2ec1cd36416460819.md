# Mogelijke overeenkomst: gbx.con.e4020 (AORTA REQ) ↔ gbx.con.e4020.2 (AORTA AS REQ)

ResearchMaster-WorkItem-ID: 38ef7acb-ab45-5af5-9a07-dc57d2971bff

## Bevinding

Eis gbx.con.e4020 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4020.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 60.63%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.

## Betrokken requirements

### Gebruik van IP en DNS

**Requirement-ID:** `0b6e6290-a86f-5fea-8b44-a99ee576e976`

**Broncatalogus:** AORTA AS REQ

**Eisnummer:** "GBX.CON.e4020"

**Bronrecord:** `0f0297a5-3dda-52d0-a795-f7e3f7ad2eaf`

**Eistekst:**

```text
"; Een GBx moet bereikbaar zijn voor de ZIM: ;  {GBx}{GBO} via het IP-adres dat is toegekend aan het GBx en dat is verkregen door DNS-vertaling van de hostnaam van dat GBx; ;  {GBK} via het IP-adres dat door het LSP is toegekend aan het GBK en dat is verkregen door DNS-vertaling van de hostnaam van dat GBK; ;  {GBP} via het IP-adres en de fully qualified domain name (FQDN) die door het LSP zijn toegekend aan het GBP en waarvoor het LSP de DNS-vertaling biedt. ; De ZIM moet bereikbaar zijn vanuit een GBx via het IP-adres van de operationele ZIM, dat is verkregen door DNS-vertaling van de hostnaam van de ZIM. ; Voor de DNS-vertaling geldt dat: ;  de hostnaam een maximale time-to-live (TTL) heeft voor verversing van de cache; ;  het IP-adres van de ZIM zich binnen een vooraf overeengekomen range bevindt die altijd gerouteerd moet worden naar de GZN; ;  een systeem vanuit de applicatie alleen benaderd mag worden op de FQDN. Vertaling naar IP-adres wordt door de DNS uitgevoerd. ; Een GBx mag de volgende IP-adressen niet intern gebruiken: ;  het IP-adres dat door het LSP is uitgegeven voor het GBx als geheel, ;  de IP-adressen die zijn gereserveerd voor de ZIM, ;  de IP-adressen uit het landelijke IP-nummerplan van het LSP. ;"
```

### Gebruik van IP en DNS

**Requirement-ID:** `a254fe5a-9e6a-5d03-9653-ae277be94384`

**Broncatalogus:** AORTA REQ

**Eisnummer:** "GBX.CON.e4020.2"

**Bronrecord:** `002f8c91-3c4e-516b-bb5e-a32ecfc28c02`

**Eistekst:**

```text
"""<b>Eis:</b>
Een GBx moet bereikbaar zijn voor de ZIM:
<ol>
	<li>{GBx}{GBO} via het IP-adres dat is toegekend aan het GBx en dat is verkregen door DNS-vertaling van de hostnaam van dat GBx;</li>
	<li>{GBK} via het IP-adres dat door het LSP is toegekend aan het GBK en dat is verkregen door DNS-vertaling van de hostnaam van dat GBK;</li>
	<li>{GBP} via het IP-adres en de fully qualified domain name (FQDN) die door het LSP zijn toegekend aan het GBP en waarvoor het LSP de DNS-vertaling biedt.</li>
</ol>

De ZIM moet bereikbaar zijn vanuit een GBx via het IP-adres van de operationele ZIM, dat is verkregen door DNS-vertaling van de hostnaam van de ZIM.

Voor de DNS-vertaling geldt dat:
<ol>
	<li>de hostnaam een maximale time-to-live (TTL) heeft voor verversing van de cache;</li>
	<li>het IP-adres van de ZIM zich binnen een vooraf overeengekomen range bevindt die altijd gerouteerd moet worden naar de GZN;</li>
	<li>een systeem vanuit de applicatie alleen benaderd mag worden op de FQDN. Vertaling naar IP-adres wordt door de DNS uitgevoerd.</li>
</ol>

Een GBx mag de volgende IP-adressen niet intern gebruiken:
<ol>
	<li>het IP-adres dat door het LSP is uitgegeven voor het GBx als geheel,</li>
	<li>de IP-adressen die zijn gereserveerd voor de ZIM,</li>
	<li>de IP-adressen uit het landelijke IP-nummerplan van het LSP.</li>
</ol>

<b>Toelichting bij eis:</b>
Deze eis is nodig om ervoor te zorgen dat FQDN en IP-adressen op een juiste wijze worden ingesteld.
Deze eis is ook nodig voor het gebruik van een ZIM op twee operationele locaties en om IP-netwerkconflicten te voorkomen.

Deze eis betekent voor de organisatie dat die voor zijn GBx/GBO een FQDN moet krijgen van zijn GZN en deze laten registreren bij het LSP of bij SIDN. De GZN zal daaraan een IP-adres toekennen. De organisatie moet het toegekende IP-adres tenslotte (laten) configureren in zijn netwerkapparatuur binnen zijn GBx. Deze eis betekent dat een applicatie een ZIM expliciet op naam benadert en dat systemen geconfigureerd moeten worden voor het gebruik van DNS. Door middel van DNS-resolving kan voor het GBx transparant gebruik gemaakt worden van de operationele ZIM op locatie 1 of locatie 2."""
```

## Claims en Evidence

### Claims

```json
[
  {
    "claimId": "ba87d49f-1640-5743-b89a-8ad023f70057",
    "evidenceIds": [
      "542fe564-c60d-520d-904d-0c38b7014c10"
    ],
    "connectionId": "8aa89fe3-d6b8-5b8b-af13-6963074cb52e",
    "subjectEntityId": "8718a582-e755-5be9-b7f4-42617c469f63",
    "objectEntityId": "38ef7acb-ab45-5af5-9a07-dc57d2971bff",
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
  "entityId": "38ef7acb-ab45-5af5-9a07-dc57d2971bff",
  "entityType": "WorkItem",
  "sourceRecordIds": [
    "b02d887a-75c9-5925-ba7f-dbd4798eff9c"
  ],
  "displayName": "Mogelijke overeenkomst: gbx.con.e4020 (AORTA REQ) ↔ gbx.con.e4020.2 (AORTA AS REQ)",
  "description": "Eis gbx.con.e4020 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4020.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 60.63%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld.",
  "externalIdentifiers": [
    {
      "system": "rdf-uri",
      "value": "urn:uuid:38ef7acb-ab45-5af5-9a07-dc57d2971bff"
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
      "0b6e6290-a86f-5fea-8b44-a99ee576e976"
    ],
    "requirementB": [
      "a254fe5a-9e6a-5d03-9653-ae277be94384"
    ],
    "validationExecutionId": [
      "comparison:af886aba-5235-52cf-a7cc-89202836e89e"
    ],
    "requirementNumberA": [
      "gbx.con.e4020"
    ],
    "requirementNumberB": [
      "gbx.con.e4020.2"
    ],
    "requirementTitleA": [
      "Gebruik van IP en DNS"
    ],
    "requirementTitleB": [
      "Gebruik van IP en DNS"
    ],
    "matchBasis": [
      "TITLE"
    ],
    "scorePercent": [
      60.63
    ],
    "conclusion": [
      "Eis gbx.con.e4020 uit AORTA REQ komt vermoedelijk overeen met eis gbx.con.e4020.2 uit AORTA AS REQ. Selectie op gelijke eisnaam; tekstuele overeenkomst 60.63%. Eisnamen gelijk; eisteksten verschillend. Inhoudelijke gelijkwaardigheid is niet vastgesteld."
    ]
  }
}
```

