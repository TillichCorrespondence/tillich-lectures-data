<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  version="3.0">
  
  <!-- Output settings -->
  <xsl:output method="xml" indent="yes"/>
  
  <!-- Process all XML files in the editions folder -->
  <xsl:template name="xsl:initial-template">
    <xsl:for-each select="collection('?select=*.xml')">
      <xsl:result-document href="{document-uri(.)}" method="xml" indent="yes">
        <xsl:apply-templates select="."/>
      </xsl:result-document>
    </xsl:for-each>
  </xsl:template>
  
  <!-- Identity template: copy everything as-is -->
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>
  
  <!-- Special handling for emph with rend="allcaps" -->
  <!-- OPTION 1: Convert to lowercase -->
  <xsl:template match="emph[@rend='allcaps']">
    <xsl:copy>
      <xsl:apply-templates select="@*"/>
      <xsl:value-of select="lower-case(.)"/>
    </xsl:copy>
  </xsl:template>
  
  <!-- OPTION 2: Convert to title case (first letter caps, rest lower) -->
  <!--
    <xsl:template match="emph[@rend='allcaps']">
        <xsl:copy>
            <xsl:apply-templates select="@*"/>
            <xsl:value-of select="concat(upper-case(substring(., 1, 1)), lower-case(substring(., 2)))"/>
        </xsl:copy>
    </xsl:template>
    -->
  
</xsl:stylesheet>