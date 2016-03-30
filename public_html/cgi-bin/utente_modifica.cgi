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

$input{password}= $page->param('password'); #leggo i valori di input
$input{email}= $page->param('email');
$input{nome}= $page->param('nome');
$input{cognome}= $page->param('cognome');
$input{id}= $page->param('id');
$input{admin} = $page->param('admin');
my $postBack = $page->param('postBack');


print $page->header('text/html'); #header HTTP

my $modificaEffettuata = 0;

printStartPage();
printAdminHtmlHead("Modifica Utente - Gestione Utenti");
print '<body>';
printHeader();
printAdminNavbar(1); #Stampa la navbar corretta

print '<div id="content">
		<div id="breadcrumbs">
			<p>Ti trovi in: <a href="gestione_utenti.cgi">Gestione Utenti</a> &gt; &gt; <span class="currentPage">Modifica utente</span></p>
		</div>';
printSessionData();
print '<h1>Modifica utente</h1>';

# PostBack -> la pagina si è inviata dei dati da sola. Il flag vale 1
if ( $postBack && ($page->param('modifica') eq "Modifica") )  {

	my $controlloerr= &controllacampiutente($input{nome},$input{cognome},$input{email},$input{password});

	my $parser= XML::LibXML->new();
	my $doc = $parser->parse_file($file) || die("parsificazione non riuscita");
	my $xpc = XML::LibXML::XPathContext->new($doc);
	
	$xpc->registerNs('u', 'http://www.9armonie.com/utenti');
		
	my $query = "//u:utente[u:email='$input{email}' and u:id!='$input{id}']";
	my $email = $xpc->findnodes($query);


	if ($email){
		# Esiste già un utente con questa mail
		$controlloerr = "Email già in uso";
	}

	if ($controlloerr eq "") {
		
		$query = "//u:utente[\@id='$input{id}']";
		my $oldUser = $xpc->findnodes($query)->get_node(1);

		my $adminFlag ="false";
			if ($input{admin}){
				$adminFlag=$input{admin};
		}
		my $newUser= "<utente amministratore=\"$adminFlag\" id=\"$input{id}\">
		<nome>$input{nome}</nome>
		<cognome>$input{cognome}</cognome>
		<email>$input{email}</email>
		<password>$input{password}</password>
	</utente>\n";

	
		my $padre = $oldUser->parentNode;
		$padre->removeChild($oldUser);
		$padre->appendChild($parser->parse_balanced_chunk($newUser));


		open(OUT, ">$file") || die("impossibile aprire il documento");
		print OUT $doc->toString || die("impossibile scrivere sul documento");
		close(OUT) || die("impossibile chiudere il documento");
		
		print '<h2 class="okMessage">Modifica utente effetuata</h2>';
		print '<a href="gestione_utenti.cgi" class="goBack">Torna indietro</a>';
		$modificaEffettuata = 1; #così non stampa il form di modifica

	} else {
		print '<p class="errore"><strong>'.$controlloerr.'</strong></p>';
	}

} 

if (!$modificaEffettuata) {

	my $parser= XML::LibXML->new();
	my $doc = $parser->parse_file($file) || die("parsificazione non riuscita");


	my $xpc = XML::LibXML::XPathContext->new($doc);
	
	$xpc->registerNs('u', 'http://www.9armonie.com/utenti');
	my $query = '/u:utenti/u:utente[@id="'.$input{id}.'"]';

	my $utente = $xpc->findnodes($query)->get_node(1);


	my $nome = $utente->getElementsByTagName("nome")->to_literal();
	my $cognome = $utente->getElementsByTagName("cognome")->to_literal();
	my $email= $utente->getElementsByTagName("email")->to_literal();
	my $password = $utente->getElementsByTagName("password")->to_literal();

	my $id = $utente->getAttribute("id");
	my $admin = $utente->getAttribute("amministratore");

	my $adminCheck ="";
	if ($admin eq "true"){
		$adminCheck = 'checked="checked"';
	}
	print '<div id="errorBox"></div>';
	print '<form action="utente_modifica.cgi" method="post" class="customForm smallForm" onsubmit="return validateFormUtente();" id="formUtente">
	<fieldset>
		<label for="nome">Nome:</label>
		<input type="text" name="nome" id="nome" value="'.$nome.'" />
		<label for="cognome">Cognome:</label>
		<input type="text" name="cognome" id="cognome" value="'.$cognome.'" /> 

	</fieldset>
	<fieldset>
		<label for="admin" class="checkboxLabel">Amministratore:</label>
		<input name="admin" id="admin" type="checkbox" value="true" class="checkbox" '.$adminCheck.'/> 
	</fieldset>
	<fieldset>
		<label for= "email">Email:</label>
		<input type="text" name="email" id="email" value="'.$email.'" /> 
		<label for="password">Password:</label>
		<input type="password" name="password" id="password" value="'.$password.'" />
	</fieldset>
	<fieldset>
		<input id="modifica" type="submit" name="modifica" value="Modifica" class="bottone"/>
		<input id="postBack" type="hidden" name="postBack" value="1" />
		<input type="hidden" name="id" value="'.$id.'" />
	</fieldset>
	</form>';
}

print '</div>';
printFooter();
print '<script type="text/javascript" src="../js/validateFormUtente.js" charset="UTF-8"></script>';
print $page->end_html;
