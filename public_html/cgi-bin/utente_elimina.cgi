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

my $page = CGI->new; 
$input{id}= $page->param('id');


print $page->header('text/html'); #header HTTP
printStartPage();
printAdminHtmlHead("Elimina Utente - Gestione News");
print '<body>';
printHeader();
printAdminNavbar(1); #Stampa la navbar corretta

print '<div id="content">
		<div id="breadcrumbs">
			<p>Ti trovi in: <a href="gestione_news.cgi">Gestione Utenti</a> &gt; &gt; <span class="currentPage">Elimina Utenti</span></p>
		</div>';
printSessionData();
my $parser= XML::LibXML->new();
my $doc = $parser->parse_file($file) || die("parsificazione non riuscita");

my $xpc = XML::LibXML::XPathContext->new($doc);
$xpc->registerNs('u', 'http://www.9armonie.com/utenti');

my $query = "//u:utente[\@id='$input{id}']";

$utente= $xpc->findnodes($query)->get_node(1);

my $padre= $utente->parentNode;
$padre->removeChild($utente) || die("Impossibile eliminare l'utente");

open(OUT, ">$file") || die("Impossibile aprire il documento");
print OUT $doc->toString || die("Impossibile scrivere sul documento");
close(OUT) || die("Impossibile chiudere il documento");

print "<h2 class=\"okMessage\">Utente eliminato</h2>";
print '<a href="gestione_utenti.cgi" class="goBack">Torna indietro</a>';

print '</div>';
printFooter();

print $page->end_html;