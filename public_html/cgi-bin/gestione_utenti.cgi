#!/usr/bin/perl
use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use utf8;

my $file= '../data/utenti.xml';

require('customHtmlFunction.pl');
require('sessionHelper.pl');

if (!checkAuthLevel(2)){
	print redirect("noauth.cgi");
} 


my $page = CGI->new; #Variabile locale scalare
print $page->header('text/html'); #header HTTP

printStartPage();
printAdminHtmlHead("Gestione Utenti");
print '<body>';
printHeader();
printAdminNavbar(1); #Stampa la navbar corretta

print '<div id="content">
		<div id="breadcrumbs">
			<p>Ti trovi in: <span class="currentPage">Gestione Utenti</span></p>
		</div>';
printSessionData();

my $parser= XML::LibXML->new();
my $doc = $parser->parse_file($file) || die("parsificazione non riuscita");
my $radice= $doc->getDocumentElement || die("Non riesco ad accedere alla radice");
my @nodi= $radice->getElementsByTagName("utente")->get_nodelist();


print '<h1>Gestione Utenti</h1>';


print '<a href="utente_inserisci.cgi">Inserisci nuovo utente</a>';

print '<ul class="listaUtenti">';

foreach $nodo(@nodi) {
	my $email = $nodo->getElementsByTagName('email')->to_literal();
	my $nome = $nodo->getElementsByTagName("nome")->to_literal();
	my $cognome = $nodo->getElementsByTagName("cognome")->to_literal();

	my $id = $nodo->getAttribute("id");

	print '<li>';
	print "<p><strong>Email:</strong> $email</p>";
	print "<p><strong>Nome:</strong> $nome</p>";
	print "<p><strong>Cognome:</strong> $cognome</p>";


	print '<form action="utente_modifica.cgi" method="post" class="formGestioneUtenti"> ';
	print '<fieldset>';
	print '<input type="hidden" name="id" value="'.$id.'" />';
	print '<input type= "submit" name= "modifica" value="Modifica" /> ';
	print '</fieldset>';
	print '</form>';
	
	print '<form action="utente_elimina.cgi" method="post" class="formGestioneUtenti"> ';
	print '<fieldset>';
	print '<input type="hidden" name="id" value="'.$id.'" />';
	print '<input type= "submit" name= "elimina" value="Elimina" /> ';
	print '</fieldset>';
	print '</form>';

	print '</li>';
}

print '</ul>';
print "</div>";
printFooter();

print $page->end_html;