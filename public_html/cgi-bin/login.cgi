#!/usr/bin/perl
use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use utf8;

require('sessionHelper.pl');
require('customHtmlFunction.pl');

#prende i parametri email e password.
# se sono corretti crea una sessione

my $page = CGI->new; 


$input{password}= $page->param('password'); #leggo i valori di input
$input{email}= $page->param('email');

#print redirect('gestione_news.cgi');

my $logged = "";
if (getSession()){
	print redirect('gestione_news.cgi');
} else { 
	if ($input{email}){
		#provo a loggare
		my $file='../data/utenti.xml';
		my $parser= XML::LibXML->new();
		my $doc = $parser->parse_file($file) || die("parsificazione non riuscita");
		my $xpc = XML::LibXML::XPathContext->new($doc);

		$xpc->registerNs('u', 'http://www.9armonie.com/utenti');

		my $query = '//u:utente[u:email="'.$input{email}.'"]';
		my $utente = $xpc->findnodes($query)->get_node(1);

		if ($utente){
			my $password= $utente->getElementsByTagName("password")->to_literal();
			my $admin = $utente->getAttribute("amministratore");
			if ($password eq $input{password}){
				my $auth = 1;
				if ($admin eq "true"){
					$auth = 2;
				}
				$cookie = createSession($input{email},$auth,$page);
				print redirect(-uri => 'gestione_news.cgi', -cookie => $ cookie);
			}else{
				$logged="Email o password errati";
			}
		} else {
			$logged = "Mail non presente nel sistema";
		}
	}

	if (!$input{email} || logged ne ""){

		print $page->header('text/html'); #header HTTP

		printStartPage();
		printAdminHtmlHead("Login");
		print '<body>';
		printHeader();
		printNavbar();


		print '<div id="content">
				<div id="breadcrumbs">
					<p>Ti trovi in: <span class="currentPage">Area riservata</span></p>
				</div>';

		if ($logged){
			#Stampa gli errori rilevati dal server
			print '<p class="errore"><strong>'.$logged.'</strong></p>';
		}
		print '<div id="errorBox"></div>'; #necessario per la stampa degli errore rilevati da JavaScript
		print '<form method="post" action="login.cgi" class="smallForm customForm" id="formLogin" onsubmit="return validateFormLogin();">
				<fieldset>
					<label for="email">E-mail: </label>
					<input type="text" name="email" id="email"/>
				</fieldset>
				<fieldset>
					<label for="password">Password: </label>
					<input type="password" name="password" id="password"/>
				</fieldset>

				<fieldset class="buttonArea">
					<button type="submit" id="submit">Entra</button>
					<button type="reset" id="reset">Reset</button>
				</fieldset>

			</form>';



		print '</div>'; #fine div content


		printFooter();
		print '<script type="text/javascript" src="../js/validateFormUtente.js" charset="UTF-8"></script>';
		print $page->end_html;
	}
}



