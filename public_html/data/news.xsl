<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">

<xsl:for-each select="notizie/news">
    <div>
        <h2><xsl:value-of select="titolo"/></h2>
        <p><xsl:value-of select="data"/> <xsl:value-of select="ora"/></p>
        <p>
            <xsl:value-of select="descrizione"/>
        </p>
    </div>
</xsl:for-each>

</xsl:template>

</xsl:stylesheet>