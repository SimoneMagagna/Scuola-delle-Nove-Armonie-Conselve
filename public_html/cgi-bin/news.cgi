#!/usr/bin/perl
use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use utf8;

require('customHtmlFunction.pl');


my $file= '../data/news.xml';

my $page = CGI->new; #Variabile locale scalare

print $page->header('text/html'); #header HTTP

printStartPage();
printHtmlHead("News");
print '<body>';
printHeader();
printNavbar(0);

print '<div id="content">
		<div id="breadcrumbs">
			<p>Ti trovi in: <a href="index.cgi" xml:lang="en">Home</a> &gt;&gt; <span class="currentPage">News</span></p>
		</div>';



my $parser= XML::LibXML->new();
my $doc = $parser->parse_file($file) || die("Parsing non riuscita");
my $radice= $doc->getDocumentElement || die("Non riesco ad accedere alla radice");
my @nodi= $radice->getElementsByTagName("news")->get_nodelist();

print '<h1>News</h1>';
@nodi = reverse(@nodi);

foreach $nodo(@nodi){

	print '<div class="immagineDecorativa lineSeparator"></div>';
	my $titolo = $nodo->getElementsByTagName("titolo")->to_literal();
	my $data = $nodo->getElementsByTagName("data")->to_literal();
	my $ora = $nodo->getElementsByTagName("ora")->to_literal();
	my $contenuto = $nodo->getElementsByTagName("descrizione")->to_literal();
	my $id = $nodo->getAttributeNode("id")->to_literal();
	print '<div class="newsBox">';
	print "<h2><a href=\"dettaglioNews.cgi?id=$id\">$titolo</a></h2>";
	print "<p class=\"newsPubDate\">$data $ora</p>
				<div class=\"newsContent\">$contenuto</div>
				<p><a href=\"#content\" class=\"tornaSu\">Torna su</a></p>
			";
	print '</div>'; #fine newsbox
}


print '</div>'; #fine div content



printFooter();

print $page->end_html;

#print $nodi->toString();