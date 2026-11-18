[AORTA 8.5.2](../../../../index.md) / [Aansluit- en Implementatiewijzer Kern](../../../../aansluit-en-implementatiewijzer-kern.md) / [Token specificaties](../../../token-specificaties.md) / [AORTA SAML tokens](../../aorta-saml-tokens.md) / [GBZ AORTA_Auth_IH_Mandaattoken](../gbz-aorta_auth_ih_mandaattoken.md)

# Certificaten mandaattoken

## Te gebruiken certificaat en attributen

Voor het tekenen van het Mandaattoken wordt het **handtekening**certificaat van de persoonlijke UZI-pas gebruikt. Dit certificaat bevat een RSA publieke sleutel. Met de privé sleutel wordt de digitale handtekening gegenereerd. Voor de technische context en het feitelijk genereren van de digitale handtekening met een UZI-pas wordt verwezen naar respectievelijk [Bijlage B](../aorta_auth_ih_berichtauthenticatie_uzi/bijlage-b-technische-context-gebruik-uzi-pas.md) en [Bijlage C](../aorta_auth_ih_berichtauthenticatie_uzi/bijlage-c-token-implementatie.md) uit het document IH Berichtauthenticatie met UZI-Pas [UZI berichttoken] met dien verstande dat in het mandaattoken dus het **handtekening**certificaat[^1] wordt gebruikt in plaats van het in de bijlagen vermelde authenticatiecertificaat.

Om de digitale handtekening bij de ZIM te verifiëren, moet de ontvanger over de bijbehorende publieke sleutel beschikken, zie [IH tokens generiek]. Voor verificatie is gekozen door een verwijzing naar het handtekeningcertificaat in het SAML mandaattoken als KeyInfo mee te zenden; de ontvanger moet deze dan met bijvoorbeeld het LDAP protocol ophalen, zie ook [IH tokens generiek].

[^1]: Technisch dus het certificaat met keyUsage non-repudiation (0x40).
