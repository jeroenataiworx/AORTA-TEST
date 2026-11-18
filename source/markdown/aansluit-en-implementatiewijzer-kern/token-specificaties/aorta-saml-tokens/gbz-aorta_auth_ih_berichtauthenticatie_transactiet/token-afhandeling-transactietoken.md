[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBZ AORTA_Auth_IH_Berichtauthenticatie_Transactietoken](../gbz-aorta_auth_ih_berichtauthenticatie_transactiet.md)

# Token afhandeling transactietoken

## Verificatie van het bericht

Het is belangrijk vast te stellen dat de velden in het SAML transactietoken overeenstemmen met die van het bericht voor de gegevensuitwisseling en geldig ondertekend zijn. Wanneer dit niet zou gebeuren, kan een kwaadwillende met een gestolen token nog steeds gegevens opvragen van bv. ieder willekeurig Burgerservicenummer.

De ontvanger controleert of de WS-Security SOAP Header voor hem bestemd is, zie soap attribuut actor.

Het SAML transactietoken wordt door de ontvanger uit de WS-Security SOAP Header gehaald indien de WS-Security SOAP Header voor de ontvanger bestemd is en dat de ontvanger deze moet verwerken. Bij gebruik van het SAML transactietoken moet de ontvanger controleren of:

- Het attribuut ID van het Assertion element een unieke waarde heeft, welke slechts eenmalig gebruikt mag worden, zie [Uniekheid](het-saml-transactietoken.md#uniekheid);

- De aanduiding voor de versie van SAML gedefinieerd is op "2.0", zie [Uniekheid](het-saml-transactietoken.md#uniekheid) ;

- De juiste organisatieID is opgenomen die deze assertion heeft gecreëerd en de gebruiker heeft geauthenticeerd, zie [Afzender](het-saml-transactietoken.md#afzender). Het zorgaanbiederID in het token dient overeen te komen met de zorgaanbiederID in het bericht;

- Indien Conditionele Query (token is ondertekend met een certificaat met certificaattype “S”): de NameID van het Subject is wel aanwezig maar leeg, zie [Onderwerp](het-saml-transactietoken.md#onderwerp); Tevens dient er een mandaattoken en inschrijftoken aanwezig te zijn;

- In overige gevallen: Het UZI-nummer en rolcode van het authenticatie certificaat, gebruikt voor de ondertekening van de Assertion, overeenkomt met de NameID van het Subject en met de authorOrPerformer in het bericht zie [Onderwerp](het-saml-transactietoken.md#onderwerp);

- De Assertion correct is ondertekend door de Signature te valideren met het gerefereerde authenticatie certificaat.

- Het gebruikte certificaat en de relevante certificaatketen te valideren op geldigheid, inclusief revocatie.

- Het bericht ontvangen is binnen de geldigheidsperiode van het token, zie [Geldigheid](het-saml-transactietoken.md#geldigheid) ;

- De afnemer van het SAML transactietoken (audience) de ZIM is, zie [Ontvanger](het-saml-transactietoken.md#ontvanger);

- Indien gebruik gemaakt is van een mandaat, dan dient er een getekend mandaattoken te zijn opgenomen in de SOAP-header (zie [Mandaattoken]). Het attribuut "autorisatieregel/context" dient identiek te zijn aan het overeenkomstige attribuut in het mandaattoken. Daarnaast dient de organisatieID in beide tokens overeen te komen.

- Indien geen Conditionele Query: De zorgverlener/zorgmedewerker is geauthenticeerd via het voorgedefinieerde authenticatiemiddel, de SmartCardPKI, zoals beschreven in [Authenticatie](het-saml-transactietoken.md#authenticatie) ;

- Indien Conditionele Query: Het systeem is geauthenticeerd via het voorgedefinieerde authenticatiemiddel, Het X509 servercertificaat, zoals beschreven in [Authenticatie](het-saml-transactietoken.md#authenticatie) ;

- Alleen die attributen zijn gedefinieerd, die zijn beschreven in [Attributen](het-saml-transactietoken.md#attributen) ;

- De attribuutwaarde van interactionId overeenkomt met *het extension-element* van het HLv3 bericht, zie [Attributen](het-saml-transactietoken.md#attributen) ;

- In het geval van een generieke query dient er een contextcode te zijn opgenomen. De contextcode dient overeen te komen met de contextcode in het bericht, zie [Attributen](het-saml-transactietoken.md#attributen) ;.

- De attribuutwaarden van messageIdRoot en messageIdExt overeenkomt met de gebruikte HL7v3 [message.id](http://message.id), zie [Attributen](het-saml-transactietoken.md#attributen) ;

- Indien de interactie patient-specifiek is: de attribuutwaarde van burgerServiceNummer overeenkomt met het BSN in het HL7v3 bericht ofwel dat de gegevens in het bericht daadwerkelijk betrekking hebben op de persoon, zie [Attributen](het-saml-transactietoken.md#attributen) . De volgende situaties zijn hierbij te onderscheiden:Wel BSN in token en in bericht; er is sprake van een goedsituatie indien BSN overeenkomt. Indien dat niet het geval is, is er sprake van een foutsituatie;Wel BSN in token en niet in het bericht; er is sprake van een foutsituatie;Geen BSN in token en wel in bericht; er is sprake van een foutsituatie;Geen BSN in token en geen BSN in het bericht; er is sprake van een goedsituatie.

- Indien het token gebruikt wordt binnen de AORTA infrastructuur moet de juiste applicatieID zijn vastgelegd die deze assertion heeft gecreëerd en de gebruiker heeft geauthenticeerd. Het applicatieID dient overeen te komen met de Message/sender/device/id in de transmission wrapper van het HL7v3 bericht;

- Indien het inschrijftoken ondertekend is met het authenticiteit certificaat van ZORG-ID Token CA (CA) dienen de volgende extra controles plaats te vinden:Van het gebruikte certificaat moet het extensie bewijs (proofValue) gecontroleerd worden dat dit met een geldige UZI-medewerkerspas op naam is gebeurd ten tijde van de ondertekening.De proofValue extensie heeft de volgende OID: 2.16.840.1.113883.2.4.3.111.20.5 (Custom Extension copied Certificate)De proofValue is een JSON Web Token dat uit drie delen bestaat: `header.payload.signature`Om het bewijs te controleren, moet uit het header element `x5c`, het X.509 certificaat geëxtraheerd worden, met Base64, waar vervolgens de publieke sleutel gehaald wordt.Gebruik de publieke sleutel om de JWT-handtekening te valideren met de algoritme die uit het header element `alg` is vastgelegd.Controleer of het geëxtraheerde certificaat ondertekend is door de vertrouwde CA (Certificate Authority)Decodeer de payload met Base64.Controleer de claims uit de payload, met die van het authenticiteit certificaat van ZORG-ID Token CA:"ura"""uziNumber""roleCode"

Als aan één van de bovenstaande condities niet is voldaan, moet het bericht door de ontvanger geweigerd worden en een SOAP foutmelding aan het verzendende systeem afgegeven worden, zie foutafhandeling in [IH tokens generiek].

Als wel aan alle condities is voldaan, wordt het bericht verder verwerkt.
