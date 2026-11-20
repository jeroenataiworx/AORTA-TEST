# OUT_OF_SCOPE_CONNECTION — Registreren abonnement

**Issue-ID:** `0b6eb7a4cb62eb31c5b2`  
**Bronbestand:** `issues.json`  
**Bronrecord:** `19`  
**Type:** `OUT_OF_SCOPE_CONNECTION`  
**Status op exportmoment:** `REVIEW_REQUIRED`  

## Bronverwijzingen

[Bekijk bron in het statische model](../processen/abonnement-en-signaalfunctie.html)

[Bekijk oorspronkelijke Markdown in het pakket](../../source/markdown/processen/abonnement-en-signaalfunctie.md)

**Bronpad:** `markdown/processen/abonnement-en-signaalfunctie.md`

## Gecontroleerde bronuitsnede

```markdown
- Rolcode

De precieze invulling van het ‘Registreren abonnement’-bericht is opgenomen in DECOR informatie voor project: [DECOR informatie voor project: AORTA (aorta-vzvz-) (nictiz.nl)](https://decor.nictiz.nl/pub/vzvz/index.php?prefix=aorta-vzvz-). Hierbij is in ieder geval de geldigheidsduur van het abonnement verplicht. Een abonnement mag niet langer geldig zijn dan 1,5 jaar. Indien dit wel het geval is, wordt dit abonnement afgewezen en wordt een foutmelding geretourneerd.  
Daarnaast dient het abonnement lokaal in het systeem geregistreerd te worden, zodat functionaliteiten als verlengen en beëindigen van het abonnement mogelijk worden.

#### Registreren abonnement o.b.v. VGU-functionaliteit
```

## Volledige oorspronkelijke bevinding

```json
{
  "type": "OUT_OF_SCOPE_CONNECTION",
  "status": "REVIEW_REQUIRED",
  "source_url": "https://aorta.public.vzvz.nl/documentatie/latest/abonnement-en-signaalfunctie",
  "source_markdown": "markdown/processen/abonnement-en-signaalfunctie.md",
  "heading": "Registreren abonnement",
  "block_index": 16,
  "link_text": "DECOR informatie voor project: AORTA (aorta-vzvz-) (nictiz.nl)",
  "original_url": "https://decor.nictiz.nl/pub/vzvz/index.php?prefix=aorta-vzvz-",
  "target_url": "https://decor.nictiz.nl/pub/vzvz/index.php",
  "fragment": null,
  "http_status": null,
  "detail": "Externe HTTP-controle mislukt: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))"
}
```
