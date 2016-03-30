#!/usr/bin/perl
use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use utf8;

my $file='../data/immagini.xml';
require('customHtmlFunction.pl');
require('sessionHelper.pl');

if (!checkAuthLevel(1)){
	print redirect("noauth.cgi");
} 


my $page = CGI->new; #Variabile locale scalare
print $page->header('text/html'); #header HTTP

printStartPage();
printAdminHtmlHead("Gestione Foto");
print '<body>';
printHeader();
printAdminNavbar(3); #Stampa la navbar corretta

print '<div id="content">
		<div id="breadcrumbs">
			<p>Ti trovi in: <span class="currentPage">Gestione Foto</span></p>
		</div>';

printSessionData();


my $parser= XML::LibXML->new();
my $doc = $parser->parse_file($file) || die("parsificazione non riuscita");
my $radice= $doc->getDocumentElement || die("Non riesco ad accedere alla radice");

my @nodi= $radice->getElementsByTagName("immagine")->get_nodelist();

print '<h1>Gestione Foto</h1>';


print '<a href="img_inserisci.cgi">Inserisci nuova foto</a>';


print '<ul class="listaImmagini">';
foreach $nodo(@nodi) {
	print '<li>';
	my $src = $nodo->getElementsByTagName('src')->to_literal();
	my $srcsmall = $nodo->getElementsByTagName('src_small')->to_literal();
	my $alt = $nodo->getElementsByTagName('alt')->to_literal();


	print '<img src="'.$srcsmall.'" alt="" width="175" height="100" />';
	print '<p><strong>Descrizione</strong><br />'.$alt.'</p>';
	

	print '<form action="img_elimina.cgi" method="post" class="formGestioneImmagini">';
	print '<fieldset class="buttonArea">';
	print '<input type="hidden" name="src" value="'.$src.'"/>';
	print '<input type="hidden" name="srcsmall" value="'.$srcsmall.'"/>';
	print '<input type= "submit" name= "elimina" value="Elimina" /> ';
	print '</fieldset>';
	print '</form>';

	print '</li>';
}


print '</ul>';

print "</div>";

printFooter();

print $page->end_html;