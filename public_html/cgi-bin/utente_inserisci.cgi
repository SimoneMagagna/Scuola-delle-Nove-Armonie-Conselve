#!/usr/bin/perl
use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use utf8;

my $file='../data/utenti.xml';

require ('funzioni.pl');
require('customHtmlFunction.pl');
require('sessionHelper.pl');
if (!checkAuthLevel(2)){
	print redirect("noauth.cgi");
} 

my $page = CGI->new; #Variabile locale scalare
print $page->header('text/html'); #header HTTP


printStartPage();
printAdminHtmlHead("Inserisci Utente - Gestione Utenti");
print '<body>';
printHeader();
printAdminNavbar(1); #Stampa la navbar corretta

print '<div id="content">
		<div id="breadcrumbs">
			<p>Ti trovi in: <a href="gestione_utenti.cgi">Gestione Utenti</a> &gt; &gt; <span class="currentPage">Inserisci nuovo utente</span></p>
		</div>';
printSessionData();
print '<h1>Inserisci nuovo utente</h1>';


my $utenteInserito = 0;

if ( ($page->param('invia') ne 0) && ($page->param('invia') eq "Registra") )  {

	$input{password}= $page->param('password');
	$input{email}= $page->param('email');
	$input{nome}= $page->param('nome');
	$input{cognome}= $page->param('cognome');
	$input{admin} = $page->param('admin');

	my $controlloerr= &controllacampiutente($input{nome},$input{cognome},$input{email},$input{password});

	if ($controlloerr eq "") { 

		my $parser= XML::LibXML->new();
		my $doc = $parser->parse_file($file) || die("parsificazione non riuscita");
		
		my $xpc = XML::LibXML::XPathContext->new($doc);
		$xpc->registerNs('u', 'http://www.9armonie.com/utenti');
		my $q = "//u:utente[u:email='$input{email}']";
		$email = $xpc->findnodes($q)->get_node(1);
		
		if ($email) {
			print "<p class=\"errore\"><strong>Utente già esistente</strong></p>";

		} else {
			#recupero l'ultimo ID inserito
			#my $xpc = XML::LibXML::XPathContext->new($doc);
			
			my $query = '/u:utenti/@nextid';
			my $newId = $xpc->findnodes($query)->get_node(1)->nodeValue;

			#aggiorno l'attributo nextid della radice
			$query = '/u:utenti';

			my $radice = $xpc->findnodes($query)->get_node(1);
			$radice->removeAttribute("nextid");
			$radice->setAttribute("nextid", $newId+1);

			#$input{admin} -> "true" se il checkbox era checked

			my $adminFlag ="false";
			if ($input{admin}){
				$adminFlag=$input{admin};
			}

			my $frammento= "	
	<utente amministratore=\"$adminFlag\" id=\"$newId\">
		<nome>$input{nome}</nome>
		<cognome>$input{cognome}</cognome>
		<email>$input{email}</email>
		<password>$input{password}</password>
	</utente>\n";
			if ($radice) {
				my $nodo= $parser->parse_balanced_chunk($frammento) || die ("frammento nodo non riuscito");
				$radice->appendChild($nodo) || die("inserimento non riuscito");
			} else {
				print "<p class=\"errore\"><strong>Non esiste la radice</strong></p>";
			}
			open(OUT, ">$file") || die("impossibile aprire il documento");
			print OUT $doc->toString || die("impossibile scrivere sul documento");
			close(OUT) || die("impossibile chiudere il documento");

			print "<h2 class=\"okMessage\">Utente inserito correttamente</h2>";
			print '<a href="gestione_utenti.cgi" class="goBack">Torna indietro</a>';
			$utenteInserito=1;
		}

	} else {
		print "<p class=\"errore\"><strong>$controlloerr</strong></p>";
	}

}

if (!$utenteInserito){

	print '<div id="errorBox"></div>';
	print '
	<form action="utente_inserisci.cgi" method="post" class="customForm smallForm" onsubmit="return validateFormUtente();" id="formUtente">
	<fieldset>
		<label for="nome">Nome:</label>
		<input type="text" name="nome" id="nome"/>
		<label for="cognome">Cognome:</label>
		<input type="text" name="cognome" id="cognome"/> 
	</fieldset>
	<fieldset>
		<label for="admin" class="checkboxLabel">Amministratore:</label>
		<input name="admin" id="admin" type="checkbox" value="true" class="checkbox"/> 
	</fieldset>
	<fieldset>
		<label for= "email">Email:</label>
		<input type="text" name="email" id="email"/> 
		<label for="password">Password:</label>
		<input type="password" name="password" id="password"/>
	</fieldset>
	<fieldset>
	<input id="invia" type="submit" name="invia" value="Registra" class="bottone"/>
	</fieldset>
</form>';
}



print '</div>';
printFooter();
print '<script type="text/javascript" src="../js/validateFormUtente.js" charset="UTF-8"></script>';
print $page->end_html;
