[AORTA 8.5.2](../../index.md) / [Logische architectuur](../../logische-architectuur.md) / [Informatiesystemen](../informatiesystemen.md)

# Goed beheerd patiëntportaal (GBP)

Een Goed Beheerd Patiëntportaal (GBP) is een (web)portaal voor patiënten die voldoet aan software-specifieke eisen om berichten uit te wisselen met de ZIM én aan implementatie- en exploitatie-eisen die voorwaardelijk zijn voor aansluiting op de ZIM.

Zoals besproken in ['Rollen toekennen aan actoren'](../primaire-interacties/rollen-toekennen-aan-actoren.md#opvragen-van-patientgegevens) kan de patiënt optreden als gegevensraadpleger en heeft de patiënt hierbij toegang tot de eigen gegevens zoals die bij AORTA door zorgverleners zijn aangemeld. De patiënt krijgt toegang via een GBP.

Een inhoudelijke uitwerking van de architectuur van een GBP valt buiten de scope van AORTA. Wel is voor AORTA van belang dat voor een GBP verschillende implementatievormen mogelijk zijn:[^1]

- Een GBP kan als zelfstandig systeem worden geïmplementeerd met een eigen aansluiting op de ZIM.

- Daarnaast kan een XIS-leverancier een patiëntportaalmodule implementeren als aanvullend onderdeel van een XIS. Als een dergelijk XIS wordt ingezet als GBZ, dan mag de patiëntportaalmodule echter niet via het GBZ gegevens ophalen uit AORTA. Om als GBP te worden toegepast moet de patiëntportaalmodule van het XIS worden geïmplementeerd met een eigen aansluiting op de ZIM en mag alleen via deze route communiceren met AORTA. De patiënt kan verder pas via een dergelijke patiëntportaalmodule gegevens uitwisselen via de ZIM indien de module voldoet aan een aantal GBP-eisen, onder meer op het punt van patiëntauthenticatie. De patiëntportaalmodule krijgt een eigen vermelding als GBP in het applicatieregister.

Op dit moment biedt de ZIM nog geen ondersteuning voor vertegenwoordiging van patiënten door andere personen (zie [Toegangsmodel](../primaire-interacties/toegangsmodel.md#vertegenwoordiging)). Eventuele vertegenwoordigers zijn daarom aangewezen op het klantenloket.

### Volgjezorg

Volgjezorg (VZVZ-portaal) is een specifieke invulling van een GBP onder verantwoordelijkheid van VZVZ. Binnen Volgjezorg is het mogelijk om te bevragen welke zorgverleners er gegevens beschikbaar stellen van een specifieke patiënt. Daarnaast is het mogelijk om de logging te bevragen met betrekking tot de gegevensuitwisseling (gegevens over zijn eigen persoon) over de AORTA infrastructuur. Hierbij wordt getoond welke soort informatie is uitgewisseld en welke organisaties bij die uitwisseling betrokken zijn geweest. Er wordt explicliet niet getoond welke zorgverleners er betrokken zijn geweest bij het bevragen of het versturen van gegevens (deze gegevens worden uiteraard wel conform de NEN7513 gelogd). Indien een patiënt wil weten welke zorgverlener verantwoordelijk was voor initiatie van de berichtuitwisseling, dan dient de patiënt deze informatie te verkrijgen bij de verantwoordelijke zorgaanbieder. VZVZ verstrekt deze informatie niet aan de patiënt.

[^1]: Op het moment van publicatie bestaan nog geen concrete GBP-implementaties.
