#!/usr/bin/perl
use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use utf8;

my $file='../data/news.xml';
require ('funzioni.pl');
require('customHtmlFunction.pl');
require('sessionHelper.pl');


if (!checkAuthLevel(1)){
	print redirect("noauth.cgi");
} 

my $page = CGI->new; #Variabile locale scalare
print $page->header('text/html'); #header HTTP

my $modificaEffettuata = 0;

printStartPage();
printAdminHtmlHead("Modifica News - Gestione News");
print '<body>';
printHeader();
printAdminNavbar(2); #Stampa la navbar corretta

print '<div id="content">
		<div id="breadcrumbs">
			<p>Ti trovi in: <a href="gestione_news.cgi">Gestione News</a> &gt; &gt; <span class="currentPage">Modifica news</span></p>
		</div>';
printSessionData();
print '<h1>Modifica news</h1>';

$input{id}= $page->param('id');
$input{titolo}= $page->param('titolo');
$input{descrizione}= $page->param('descrizione');
my $postBack = $page->param('postBack');

if ( $postBack && ($page->param('modifica') eq "Modifica") )  {
	# Devo modificare la news. Preparo i parametri
	
	my $controlloerr = &controllacampinews($input{titolo});

	if ($controlloerr eq "") { 
		# I parametri vanno bene, attuo le modifiche
		my $parser= XML::LibXML->new();
		my $doc = $parser->parse_file($file) || die("parsificazione non riuscita");
		my $xpc = XML::LibXML::XPathContext->new($doc);
		
		$xpc->registerNs('news', 'http://www.9armonie.com/news');
		
		my $query = '/news:notizie/news:news[@id="'.$input{id}.'"]';
		my $oldnews = $xpc->findnodes($query)->get_node(1);

		#prearo le ore
		my $ore =(localtime)[2]."";
		if (length($ore) eq 1){
			$ore = "0".$ore;
		}
		my $minuti =(localtime)[1]."";
		if (length($minuti) eq 1){
			$minuti = "0".$minuti;
		}
		my $secondi =(localtime)[0]."";
		if (length($secondi) eq 1){
			$secondi = "0".$secondi;
		}

		$input{ora}= $ore.":".$minuti.":".$secondi;


		# preparo la data
		my $anno = 1900+(localtime)[5];
		my $mese = ((localtime)[4]+1)."";
		if (length($mese) eq 1){
			$mese = "0".$mese;
		}
		my $giorno = (localtime)[3]."";
		if (length($giorno) eq 1){
			$giorno = "0".$giorno;
		}
		$input{data}= $anno."-".$mese."-".$giorno;

		
		$newnode= "
	<news id=\"$input{id}\">
		<data>$input{data}</data>
		<ora>$input{ora}</ora>
		<titolo>$input{titolo}</titolo>
		<descrizione>$input{descrizione}</descrizione>
	</news>\n";


		my $padre= $oldnews->parentNode;
		$padre->removeChild($oldnews) || die("modifica non riuscita");
		my $nodo= $parser->parse_balanced_chunk($newnode) || die ("parser non riuscito");

		$padre->appendChild($nodo) || die("modifica non riuscita");


		open(OUT, ">$file") || die("impossibile aprire il documento");
		print OUT $doc->toString || die("impossibile scrivere sul documento");
		close(OUT) || die("impossibile chiudere il documento");

		print "<h2 class=\"okMessage\">Modifica news effetuata</h2>";
		print '<a href="gestione_news.cgi" class="goBack">Torna indietro</a>';
		$modificaEffettuata =1;

	} else {
		print '<p class="errore"><strong>'.$controlloerr.'</strong></p>';
	}
}

if (!$modificaEffettuata) {
	# Devo mostrare il form per la modifica
	my $parser= XML::LibXML->new();
	my $doc = $parser->parse_file($file) || die("parsificazione non riuscita");
	my $xpc = XML::LibXML::XPathContext->new($doc);
	
	$xpc->registerNs('news', 'http://www.9armonie.com/news');
	my $query = '/news:notizie/news:news[@id="'.$input{id}.'"]';
	my $nodo = $xpc->findnodes($query)->get_node(1);

	my $titolo = $nodo->getElementsByTagName("titolo")->to_literal();
	my $contenuto = $nodo->getElementsByTagName("descrizione")->to_literal();
	print '<div id="errorBox"></div>';
	print '<form action="news_modifica.cgi" method="post" class="customForm" onsubmit="return validateFormNews();" id="formNews">
	<fieldset>
	<label for="titolo">Titolo:</label>
	<input type="text" name="titolo" id="titolo" value="'.$titolo.'" />
	<label for="descrizione">Descrizione:</label>
	<textarea name="descrizione" id="descrizione" cols="40" rows="6">'.$contenuto.'</textarea> 
	</fieldset>
	<fieldset>
		<input id="modifica" type="submit" name="modifica" value="Modifica" class="bottone"/>
		<input id="postBack" type="hidden" name="postBack" value="1" />
		<input id="id" type="hidden" name="id" value="'.$input{id}.'" />
	</fieldset>
	</form>';
}

print '</div>';
printFooter();

print '<script type="text/javascript" src="../js/validateFormNews.js" charset="UTF-8"></script>';

print $page->end_html;
