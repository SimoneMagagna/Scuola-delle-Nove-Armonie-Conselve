<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">

        <ul>
            <xsl:for-each select="immagini/immagine">
                <xsl:variable name="img_src">
                    <xsl:value-of select="/src_small"/>
                </xsl:variable>
                <xsl:variable name="img_alt">
                    <xsl:value-of select="/alt"/>
                </xsl:variable>
                <li>
                    <img src="{$img_src}" alt="{$img_alt}"/>
                </li>
            </xsl:for-each>
        </ul>
    </xsl:template>

</xsl:stylesheet>