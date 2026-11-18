[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBP AORTA_Auth_IH_Berichtauthenticatie_DigiD](../gbp-aorta_auth_ih_berichtauthenticatie_digid.md)

# Token afhandeling berichtauthenticatie DigiD

## Verificatie met het bericht

Het is belangrijk vast te stellen dat velden in het SAML authenticatietoken overeenstemmen met die in het HL7v3 bericht. Wanneer dit niet zou gebeuren, kan een kwaadwillende met een gestolen token nog steeds gegevens opvragen van bv. ieder willekeurig burgerservicenummer.

Voordat het GBP de berichten met de daarbij behorende SAML authenticatietoken doorstuurt naar de ZIM, voert het patiëntenportaal een aantal controles uit op de afgegeven SAML assertion. De controles die het GBP uitvoert staan beschreven in SSO verificatie, omdat deze controles buiten de scope van deze implementatie handleiding vallen.

Na controle door het GBP wordt de SAML assertion door het GBP in de WS-Security SOAP Header geplaatst voor verzending naar de ZIM.

De ontvanger controleert of de WS-Security SOAP Header voor hem bestemd is, zie soap attribuut actor.

Het SAML authenticatietoken wordt door de ontvanger uit de WS-Security SOAP Header gehaald indien de WS-Security SOAP Header voor de ontvanger bestemd is en dat de ontvanger deze moet verwerken. Bij gebruik van het SAML authenticatietoken moet de ontvanger controleren of de digitale handtekening over het SAML authenticatietoken geldig is:

- De aanduiding voor de versie van SAML gedefinieerd is op "2.0", zie [paragraaf 2.3.1](het-saml-authenticatietoken-digid.md#uniekheid) Uniekheid;

- De verschillende attributen die bij de bevestiging van het onderwerp horen voldoen aan de daarvoor gestelde eisen, zie [paragraaf 2.3.2](het-saml-authenticatietoken-digid.md#onderwerp) Onderwerp;

- Het sectoraal nummer een BSN aanduidt en dat het bijbehorende BSN identiek is aan het BSN in de payload van het HL7v3 bericht zie [paragraaf 2.3.2](het-saml-authenticatietoken-digid.md#onderwerp) Onderwerp;

- Het bericht ontvangen is binnen de geldigheidsperiode van het token, zie [paragraaf 2.3.3](het-saml-authenticatietoken-digid.md#geldigheid) Geldigheid;

- De juiste afzender is vastgelegd, die deze assertion heeft gecreëerd en de patiënt heeft geauthenticeerd, zie [paragraaf 2.3.4](het-saml-authenticatietoken-digid.md#afzender) Afzender;

- De verschillende afnemers van de assertion (audience) benoemd zijn die dit token mogen ontvangen en verwerken, zie [paragraaf 2.3.5](het-saml-authenticatietoken-digid.md#ontvanger) Ontvanger;

- De patiënt geauthenticeerd is door de authenticatie autoriteit (DigiD) op minimaal het voorgedefinieerde betrouwbaarheidsniveau ([paragraaf 2.3.6](het-saml-authenticatietoken-digid.md#authenticatie)) voor het bijbehorende bericht;

- Controle of binnen het KeyInfo element de keyName en X509data zijn opgenomen;

- Alleen die attributen zijn gedefinieerd, die zijn beschreven in [paragraaf 2.3.7](het-saml-authenticatietoken-digid.md#Attributen) Attributen

Als aan één van de bovenstaande condities niet is voldaan, moet het bericht door de ontvanger geweigerd worden en een SOAP foutmelding aan het verzendende systeem afgegeven worden, zie foutafhandeling in [IH tokens generiek].

Als wel aan alle condities is voldaan, wordt het HL7v3 bericht verder verwerkt.
