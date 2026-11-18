[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [AORTA_Auth_IH_Berichtauthenticatie_UZI](../aorta_auth_ih_berichtauthenticatie_uzi.md)

# Token afhandeling Berichtauthenticatie UZI

## Verificatie met het bericht

Bij ontvangst van een bericht met authenticatietoken moet het *ontvangende systeem* het token en de digitale handtekening daarover controleren (zie [IH tokens generiek]) en controleren of het token overeenstemt met het bericht. Deze twee onderwerpen van controle worden hieronder beschreven.

Bij ontvangst van een bericht haalt het ontvangende systeem het token uit de SOAP header. Het ontvangende systeem controleert of:

- Het gebruikte certificaat geldig is, zie [Certificaten](certificaten-berichtauthenticatie-uzi.md#te-gebruiken-certificaat-en-attributen) ;

- De messageId in het token overeen komt met de gebruikte HL7v3 message.Id in het bericht, zie [Uniekheid](het-saml-authenticatietoken-berichtauthenticatie-u.md#uniekheid) ;

- Het bericht ontvangen is binnen de geldigheidsperiode van het token, zie [Geldigheid](het-saml-authenticatietoken-berichtauthenticatie-u.md#geldigheid) ;

- Het token bestemd is voor het geadresseerde zorgsysteem, zie [Ontvanger](het-saml-authenticatietoken-berichtauthenticatie-u.md#ontvanger) ;

- In het token het patientId staat, en dit patientId overeenkomt met het gebruikte HL7v3 patientId (indien in bericht aanwezig), zie [Attributen](het-saml-authenticatietoken-berichtauthenticatie-u.md#attributen) ;

- In het token het triggerEventId staat, zie [Attributen](het-saml-authenticatietoken-berichtauthenticatie-u.md#attributen)

Als aan één van bovenstaande condities niet is voldaan, wordt het bericht geweigerd en wordt een SOAP foutmelding aan het verzendende systeem gegeven, zie foutafhandeling in [IH tokens generiek]. Als wel aan alle condities is voldaan, wordt het HL7v3 bericht verder verwerkt.

| ![Diagram](../../../../../assets/677bb5f34c4bca6dcec4366d42081f6683a22c0710d147f0b84700677667e213.png) | Als er geen authenticatietoken in de SOAP header is aangetroffen *kan* het HL7v3 bericht wel verder worden verwerkt, op voorwaarde dat voor de betreffende interactie het vertrouwensniveau "laag" is toegestaan. ; |
| --- | --- |

Naast de controle van het token moeten bij het bericht een aantal gegevens worden vastgehouden die verderop worden gebruikt voor inhoudelijke controle van het bericht:

- Authenticatietoken aanwezig (ja/nee);

- UZI-nummer van de afzender van het bericht (afkomstig uit het certificaat van de afzender);

- URA-nummer van het systeem dat het bericht heeft verstuurd (afkomstig uit het servercertificaat van dat systeem, die onderdeel is van gegevens van de TLS sessie).
