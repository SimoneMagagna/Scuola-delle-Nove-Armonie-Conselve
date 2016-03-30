#!/usr/bin/perl
use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use utf8;

require('customHtmlFunction.pl');
require('sessionHelper.pl');

if (!checkAuthLevel(1)){
	print redirect("noauth.cgi");
} 


my $page = CGI->new; #Variabile locale scalare
print $page->header('text/html'); #header HTTP

printStartPage();
printAdminHtmlHead("Gestione News");
print '<body>';
printHeader();
printAdminNavbar(2); #Stampa la navbar corretta

print '<div id="content">
		<div id="breadcrumbs">
			<p>Ti trovi in: <span class="currentPage">Gestione News</span></p>
		</div>';

printSessionData();




my $file= '../data/news.xml';
my $parser= XML::LibXML->new();
my $doc = $parser->parse_file($file) || die("parsificazione non riuscita");
my $radice= $doc->getDocumentElement || die("Non riesco ad accedere alla radice");
my @nodi= $radice->getElementsByTagName("news")->get_nodelist();

print '<h1>Gestione News</h1>';

print '<a href="news_inserisci.cgi">Inserisci nuova news</a>';

@nodi = reverse(@nodi);

foreach $nodo(@nodi) {

	print '<div class="immagineDecorativa lineSeparator"></div>';
	my $titolo = $nodo->getElementsByTagName("titolo")->to_literal();
	my $data = $nodo->getElementsByTagName("data")->to_literal();
	my $ora = $nodo->getElementsByTagName("ora")->to_literal();
	my $contenuto = $nodo->getElementsByTagName("descrizione")->to_literal();
	my $id = $nodo->getAttributeNode("id")->to_literal();

	print '<div class="newsBox">';
	print "<h2>$titolo</h2>";

	print '<form action="news_modifica.cgi" method="post" class="formGestioneNews"> ';
	print '<fieldset>';
	print '<input type= "hidden" name="id" value="'.$id.'"/>';
	print '<input type= "submit" name= "modifica" value="Modifica" /> ';
	print '</fieldset>';
	print '</form>';
	print '<form action="news_elimina.cgi" method="post" class="formGestioneNews"> ';
	print '<fieldset>';
	print '<input type= "hidden" name="titolo" value="'.$titolo.'" />';
	print '<input type= "submit" name= "elimina" value="Elimina" /> ';
	print '</fieldset>';
	print '</form>';

	print "<p class=\"newsPubDate\">$data $ora</p>
				<div class=\"newsContent\">$contenuto</div>
				<p><a href=\"#content\" class=\"tornaSu\">Torna su</a></p>
			";
	print '</div>'; #fine newsbox






	
}


print "</div>";

printFooter();

print $page->end_html