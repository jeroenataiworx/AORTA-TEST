[AORTA 8.5.2](../index.md) / [Logische architectuur](../logische-architectuur.md)

# Beveiliging

Vanwege het vertrouwelijke karakter van patiëntgegevens is beveiliging een centraal aspect van de AORTA-architectuur dat verweven is met andere aspecten van de architectuur. Diverse aspecten van beveiliging zijn dan ook al in voorgaande hoofdstukken aangestipt. Dit hoofdstuk heeft dan ook het karakter van een overzicht.

De [AVG] vereist bij de verwerking van persoonsgegevens een passend beveiligingsniveau gelet op de risico’s die de verwerking en de aard van de te

beschermen gegevens met zich meebrengen. In [AV23] worden vier risicoklassen voor persoonsgegevens opgevoerd (publiek niveau, basisniveau, verhoogd risico en hoog risico). Volgens de in [AV23] gestelde criteria valt de verwerking van persoonsgegevens in AORTA onder risicoklasse III (hoog risico) omdat sprake is van:

- bijzondere persoonsgegevens, namelijk gezondheidsgegevens;

- veel persoonsgegevens, namelijk in principe van alle patiënten van zorgaanbieders in Nederland.

De beveiligingsmaatregelen van AORTA moeten daarom zijn afgestemd op een hoog risico.

De beveiliging van AORTA is gebaseerd op een [Vertrouwensmodel]. Dit model is het geheel van technische, organisatorische en juridische waarborgen voor het vertrouwen in de landelijke elektronische uitwisseling van medische gegevens.

In dit hoofdstuk wordt vooral ingegaan op de technische waarborgen. Details van diverse beveiligingsaspecten worden daarnaast verder uitgewerkt in de ontwerpdocumenten van deelcomponenten van de ZIM [Ontw Authenticatie], [Ontw APT] en [Ontw APR].

Er is sprake van technische beveiligingswaarborgen in drie fasen van het gebruik van de AORTA infrastructuur:

- vooraf, bij het aansluiten op de infrastructuur;

- tijdens het gebruik van de infrastructuur, bij gegevensuitwisseling;

- achteraf, na uitwisseling van gegevens.

Voorafgaand aan het aansluiten op de infrastructuur moet voor een XIS een XIS-typekwalificatie worden behaald. Hiervoor moet worden voldaan aan een programma van eisen, waarvan beveiligingseisen een onderdeel zijn. Voordat een specifieke implementatie van een XIS bij een zorgaanbieder daadwerkelijk kan worden aangesloten, moet voldaan worden aan de implementatie-eisen voor een GBZ. Ook voor GBP en GBK gelden dergelijke eisen.

Een GBx moet bij aansluiting worden geregistreerd in het applicatieregister van de ZIM. Binnen dit register krijgt het systeem een status toegekend en wordt per interactietype vastgelegd of het systeem dit type interactie mag uitvoeren. Een GBx dat niet de status actief heeft en dat niet geregistreerd is voor het deelnemen aan de juiste interactietypen zal geen gegevens kunnen uitwisselen.

Het GBx zelf moet van de juiste servercertificaten worden voorzien. Deze zijn afkomstig van het UZI-register. In het geval van GBP’s, GBK’s en niet-UZI-abonnees zijn deze afkomstig van PKIoverheid. De gebruikers van een GBZ moeten beschikken over een UZI-pas, ZORG-ID Smartcard of ZORG-ID Mobile App. Voor het GBK moeten gebruikers beschikken over een PKIO-pas. Voorafgaand aan de verstrekking van dergelijke passen worden controles uitgevoerd om vast te stellen of de gebruiker voor de pas in aanmerking komt. Passen kunnen centraal worden gedeactiveerd in geval van vermissing. Het gebruik van de pas vereist de kennis van een beveiligingscode.

Bij het uitwisselen van gegevens met de ZIM wordt de vertrouwelijkheid gegarandeerd doordat het GBx een beveiligde verbinding opbouwt op basis van TLS, waarbij het GBx en de ZIM wederzijdse authenticatie uitvoeren op basis van certificaten.

Bij het uitwisselen van patiëntgegevens worden aan het GBZ onder meer eisen gesteld ten aanzien van (zie [paragraaf 6.4](informatiesystemen/zorginformatiesystemen-xis-en-het-goed-beheerd-zor.md)):

- het inloggen van de gebruiker met een vertrouwensmiddel;

- het vastleggen van en controleren op de toestemming (opt-in) van de patiënt voor het beschikbaar maken van gegevens via AORTA;

- het verifiëren van de identiteit en het Burgerservicenummer van de patiënt;

- het vastleggen van de behandelrelatie tussen zorgverlener en patiënt;

- het bijhouden van de autorisatieregels met betrekking tot mandaten.

Bij elke berichtuitwisseling tussen GBx en de ZIM geldt een vaste reeks van controles:

- de geldigheid van de berichtsyntax wordt gecontroleerd;

- het applicatieregister wordt geraadpleegd om vast te stellen of het GBx de onderhavige interactie mag uitvoeren;

- er vindt authenticatie plaats van de gebruiker op basis van het gebruikte vertrouwensmiddel;

- de integriteit van een aantal kerngegevens in het bericht wordt gecontroleerd (deze is geborgd door versleuteling van deze gegevens in het authenticatietoken);

- er wordt gecontroleerd of de gebruiker voldoet aan de voorwaarden in het autorisatieprotocol; dit houdt onder meer in dat de toegang tot specifieke gegevenssoorten en bouwstenen is voorbehouden aan zorgverleners met de juiste beroepscode.

Niet alleen voor de implementatie en exploitatie van GBx’en, maar ook op de implementatie en exploitatie van de ZIM is een programma van eisen van toepassing, waarvan beveiligingseisen een onderdeel zijn. Onder meer wordt van de beheerorganisatie van de ZIM verlangd dat deze voldoet aan de [NEN 7510].

Als wordt geconstateerd dat een GBx afwijkt van het programma van eisen, kan in het uiterste geval door de ZIM-beheerder worden overgegaan tot het tijdelijk uitsluiten van gegevensuitwisseling via de ZIM – en uiteindelijk zelfs tot definitieve afsluiting. Daarbij wordt het belang van continuïteit van de zorgcommunicatie nadrukkelijk meegewogen.

In de ZIM bevinden zich geen inhoudelijke patiëntgegevens. De ZIM houdt uitsluitend bij welke aangesloten informatiesystemen gegevens bevatten over patiënten. De GBZ-gebruiker kan op elk gewenst moment de beschikbaarheid van gegevens aanmelden, in geval er sprake is van opt-in van de betreffende patiënt, of afmelden.

Na afloop van elke interactie die verloopt via de ZIM wordt de interactie geregistreerd in een toegangslog, zodat achteraf exact kan worden nagegaan welke toegangsgebeurtenissen hebben plaatsgevonden. Er zijn maatregelen getroffen om ongebruikelijke interactiepatronen te signaleren.
