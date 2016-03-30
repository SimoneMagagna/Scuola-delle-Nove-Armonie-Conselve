#!/usr/bin/perl
use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use utf8;

require('customHtmlFunction.pl');

my $page = CGI->new; #Variabile locale scalare

print $page->header('text/html'); #header HTTP

printStartPage();
printHtmlHead("Home");
print '<body>';
printHeader();
printNavbar(0);

print '<div id="content">
		<div id="breadcrumbs">
			<p>Ti trovi in: <span xml:lang="en" class="currentPage">Home</span></p>
		</div>';


#div con i titoli delle news
print '<div id="news"><h1 xml:lang="en">News</h1>';
print '<a class="linkArchivio" href="news.cgi">Archivio</a>'; # Link all'archivio
print '<ul>';

my $file= '../data/news.xml';
my $parser= XML::LibXML->new();
my $doc = $parser->parse_file($file);

my $xpc = XML::LibXML::XPathContext->new($doc);
$xpc->registerNs('news', 'http://www.9armonie.com/news');
#my $query = '/news:notizie/news:news[position() < 4]';
my $query = '/news:notizie/news:news[last()-2] | /news:notizie/news:news[last()-1] | /news:notizie/news:news[last()]';
my @nodi = $xpc->findnodes($query);

@nodi = reverse(@nodi);

foreach $nodo(@nodi){
	my $titolo = $nodo->getElementsByTagName("titolo")->to_literal();
	my $data = $nodo->getElementsByTagName("data")->to_literal();
	my $id = $nodo->getAttributeNode("id")->to_literal();
	print '<li>';
	print "<h2><a href=\"dettaglioNews.cgi?id=$id\">[$data] $titolo</a></h2>\n";
	print '</li>';
}

print '</ul>';
print '</div>'; #fine div news




#div con testo introduttivo
print '<div id="quote">
				<h1>La scuola</h1>
				<p>La Scuola delle 9 Armonie di Kung Fu Tradizionale Cinese e Tibetano e di T\'ai C\'hi Chuan pratica 9 stili sia della Cina settentrionale che meridionale. E\' un\'Associazione Sportiva Dilettantistica senza fini di lucro ed è presente nel territorio dal 2005. 
				Si ispira a principi di non violenza e rispetto delle diversità, ed ha come obiettivo la divulgazione della pratica del Kung Fu nella sua forma più pura e tradizionale, in modo da permettere a chiunque voglia avvicinarsi al Kung Fu di conoscere e praticare questa antichissima arte risalente a più di 4000 anni fa.</p>
			</div>
			<div id="imm1" class="immagineDecorativa"></div>';


print '</div>'; #fine div content

printFooter();

print $page->end_html;

#print $nodi->toString();