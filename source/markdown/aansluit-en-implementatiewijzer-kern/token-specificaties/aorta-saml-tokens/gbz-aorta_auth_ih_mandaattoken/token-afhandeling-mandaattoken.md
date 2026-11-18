[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBZ AORTA_Auth_IH_Mandaattoken](../gbz-aorta_auth_ih_mandaattoken.md)

# Token afhandeling mandaattoken

## Verificatie van het mandaattoken

Het is belangrijk vast te stellen dat de velden in het SAML mandaattoken overeenstemmen met die in het transactietoken en geldig ondertekend zijn. Wanneer dit niet zou gebeuren, kan een kwaadwillende met een gestolen mandaattoken nog steeds gegevens opvragen.

Het SAML mandaattoken wordt door de ontvanger uit het transactietoken gehaald indien aanwezig. Bij gebruik van het SAML mandaattoken moet de ontvanger controleren of:

- De aanduiding voor de versie van SAML gedefinieerd is op "2.0", zie [Uniekheid](het-saml-mandaattoken.md#uniekheid) ;

- De URA, weergegeven door de NameID van het Subject, moet overeenkomen met de URA binnen het transactietoken en de URA uit het servercertificaat waarmee de TLS-verbinding is opgezet, zie [Onderwerp](het-saml-mandaattoken.md#onderwerp) ;

- Het bericht ontvangen is binnen de geldigheidsperiode van het token, zie [Geldigheid](het-saml-mandaattoken.md#geldigheid) ;

- De Assertion correct is ondertekend door de Signature te valideren met het gerefereerde handtekening certificaat.

- Het certificaat waarmee de ondertekening heeft plaatsgevonden geldig was ten tijde van de ondertekening.

- De juiste afzender (issuer) is vastgelegd die deze assertion heeft gecreëerd en ondertekend, zie [Afzender](het-saml-mandaattoken.md#afzender). De UZI en rolcode dienen overeen te komen met de bijbehorende waarden uit het UZI-certificaat van de mandaatgever. Die waarden dienen tevens overeen te komen met de Overseer in het HL7v3 bericht;

- De afnemers van het SAML mandaattoken (audience) de ZIM en de verzendende applicatie zijn, zie [Ontvanger](het-saml-mandaattoken.md#ontvanger) ;

- De als audience opgenomen applicatie moet geregistreerd zijn bij de URA uit het Subject.

- Alleen die attributen zijn gedefinieerd, die zijn beschreven in [Attributen](het-saml-mandaattoken.md#attributen);

- Indien Conditionele Query: de overseer in het HL7-bericht moet gelijk zijn aan het eerste gedeelte van de issuer (UZI) in het mandaattoken. Tevens dient het tweede gedeelte van de issuer (de rolcode) in het mandaattoken vergeleken te worden met de rolcode van de overseer in het HL7 bericht;

Het mandaattoken mag meerdere malen gebruikt worden. Het attribuut ‘autorisatieregel/context’ kan niet door de ZIM gecontroleerd worden maar dient wel in de log van de ZIM opgenomen te worden.

Als aan één van de bovenstaande condities niet is voldaan, moet het bericht door de ontvanger geweigerd worden en een SOAP foutmelding aan het verzendende systeem afgegeven worden, zie foutafhandeling in [IH tokens generiek].

Als wel aan alle condities is voldaan, wordt het HL7v3 bericht verder verwerkt.
