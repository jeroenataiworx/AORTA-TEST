[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [AORTA_Auth_IH_Berichtauthenticatie_PKIO](../aorta_auth_ih_berichtauthenticatie_pkio.md)

# Token afhandeling Berichtauthenticatie PKIO

## Verificatie van het bericht

Het is belangrijk vast te stellen dat de velden in het SAML authenticatietoken overeenstemmen met die in het HL7v3 bericht en geldig ondertekend zijn. Wanneer dit niet zou gebeuren, kan een kwaadwillende met een gestolen token nog steeds gegevens opvragen van bv. ieder willekeurig burgerservicenummer.

De ontvanger controleert of de WS-Security SOAP Header voor hem bestemd is, zie soap attribuut actor.

Het SAML authenticatietoken wordt door de ontvanger uit de WS-Security SOAP Header gehaald indien de WS-Security SOAP Header voor de ontvanger bestemd is en dat de ontvanger deze moet verwerken. Bij gebruik van het SAML authenticatietoken moet de ontvanger controleren of:

- Het attribuut ID van het Assertion element op een unieke wijze het uiteindelijk gebruikte HL7v3 message.Id identificeert, zie [Uniekheid](het-saml-authenticatietoken-berichtauthenticatie-p.md#uniekheid) ;

- De aanduiding voor de versie van SAML gedefinieerd is op "2.0", zie [Uniekheid](het-saml-authenticatietoken-berichtauthenticatie-p.md#uniekheid) ;

- Het bericht ontvangen is binnen de geldigheidsperiode van het token, zie [Geldigheid](het-saml-authenticatietoken-berichtauthenticatie-p.md#geldigheid) ;

- Het serienummer van het authenticatie certificaat overeenkomt met de NameID van het Subject, zie [paragraaf 2.3.2](https://vzvz.atlassian.net/wiki/pages/createpage.action?spaceKey=A8&title=v) ;

- De juiste afzender is vastgelegd die deze assertion heeft gecreëerd en de gebruiker heeft geauthenticeerd, zie [Afzender](het-saml-authenticatietoken-berichtauthenticatie-p.md#afzender) ;

- De afnemer van het SAML authenticatietoken (audience) het LSP is, zie [Ontvanger](het-saml-authenticatietoken-berichtauthenticatie-p.md#ontvanger) ;

- De klantenloketmedewerker is geauthenticeerd via het voorgedefinieerde authenticatiemiddel, de SmartCardPKI, zoals beschreven in [Authenticatie](het-saml-authenticatietoken-berichtauthenticatie-p.md#authenticatie) ;

- Alleen die attributen zijn gedefinieerd, die zijn beschreven in [Attributen](het-saml-authenticatietoken-berichtauthenticatie-p.md#attributen) ;

- De attribuutwaarde van TriggerEventId overeenkomt met het berichttype van het HLv3 bericht, zie [Attributen](het-saml-authenticatietoken-berichtauthenticatie-p.md#attributen) ;

- De attribuutwaarden van messageIdRoot en messageIdExt overeenkomt met de gebruikte HL7v3 [message.id](http://message.id), zie [Attributen](het-saml-authenticatietoken-berichtauthenticatie-p.md#attributen) ;

- De attribuutwaarde van burgerServiceNummer overeenkomt met het BSN in het HL7v3 bericht ofwel doordat de gegevens in het bericht daadwerkelijk betrekking hebben op de persoon, zie [Attributen](het-saml-authenticatietoken-berichtauthenticatie-p.md#attributen);

Als aan één van de bovenstaande condities niet is voldaan, moet het bericht door de ontvanger geweigerd worden en een SOAP foutmelding aan het verzendende systeem afgegeven worden, zie foutafhandeling in [IH tokens generiek].

Als wel aan alle condities is voldaan, wordt het HL7v3 bericht verder verwerkt.
