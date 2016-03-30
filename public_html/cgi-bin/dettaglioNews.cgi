#!/usr/bin/perl
use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use utf8;

require('customHtmlFunction.pl');

my $page = CGI->new; #Variabile locale scalare
$newsId = $page->param("id");

print $page->header('text/html'); #header HTTP

printStartPage();
printHtmlHead("Dettaglio news");
print '<body>';
printHeader();
printNavbar(0);

my $file= '../data/news.xml';
my $parser= XML::LibXML->new();
my $doc = $parser->parse_file($file);

my $xpc = XML::LibXML::XPathContext->new($doc);
$xpc->registerNs('news', 'http://www.9armonie.com/news');
my $query = '/news:notizie/news:news[@id='.$newsId.']';
my $nodo = $xpc->findnodes($query)->get_node(1);



my $titolo = $nodo->getElementsByTagName("titolo")->to_literal();
my $data = $nodo->getElementsByTagName("data")->to_literal();
my $ora = $nodo->getElementsByTagName("ora")->to_literal();
my $contenuto = $nodo->getElementsByTagName("descrizione")->to_literal();
my $id = $nodo->getAttributeNode("id")->to_literal();

print '<div id="content"><div id="breadcrumbs"><p>Ti trovi in: <a href="index.cgi" xml:lang="en">Home</a> &gt;&gt; <a href="news.cgi" xml:lang="en">News</a> &gt;&gt;';
print "<span class=\"currentpage\">$titolo</span>";
print '</p></div>';

print "<h1>$titolo</h1>";
print "<p class=\"newsPubDate\">Il girono <strong>$data</strong> alle ore <strong>$ora</strong> è stato pubblicato il seguente articolo:</p>";

print "<div class=\"newsContent\">$contenuto</div>";
print '<p><a href="#content" class="tornaSu">Torna su</a></p>';
print '</div>'; #fine div content



printFooter();

print $page->end_html;

#print $nodi->toString();