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

my $newsInserita = 0;

printStartPage();
printAdminHtmlHead("Inserisci News - Gestione News");
print '<body>';
printHeader();
printAdminNavbar(2); #Stampa la navbar corretta

print '<div id="content">
		<div id="breadcrumbs">
			<p>Ti trovi in: <a href="gestione_news.cgi">Gestione News</a> &gt; &gt; <span class="currentPage">Inserisci nuova news</span></p>
		</div>';
printSessionData();
print '<h1>Inserisci nuova news</h1>';

if ( ($page->param('invia') ne 0) && ($page->param('invia') eq "Inserisci") )  {

	$input{titolo}= $page->param('titolo');
	$input{descrizione}= $page->param('descrizione');
	
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

	my $controlloerr= &controllacampinews($input{titolo});

	if ($controlloerr eq "") { 

		my $parser= XML::LibXML->new();
		my $doc = $parser->parse_file($file) || die("parsificazione non riuscita");
		my $radice= $doc->getDocumentElement || die("Non riesco ad accedere alla radice");

		my $query= "//news[titolo='$input{titolo}']";
		my $node= $doc->findnodes($query);

		if ($node) {
			print "<p class=\"errore\"><strong>News già presente</strong></p>";
		} else {
			#devo inserire una news
			#recupero l'ultimo ID inserito
			my $xpc = XML::LibXML::XPathContext->new($doc);
			$xpc->registerNs('news', 'http://www.9armonie.com/news');
			my $query = '/news:notizie/@nextid';
			my $newId = $xpc->findnodes($query)->get_node(1)->nodeValue;


			#aggiorno l'attributo nextid della radice
			$query = '/news:notizie';
			$radice = $xpc->findnodes($query)->get_node(1);
			$radice->removeAttribute("nextid");
			$radice->setAttribute("nextid", $newId+1);


			#preparo il frammento
			my $frammento= "
	<news id=\"$newId\">
		<data>".$input{data}."</data>
		<ora>".$input{ora}."</ora>
		<titolo>".$input{titolo}."</titolo>
		<descrizione>".$input{descrizione}."</descrizione>
	</news>\n";

			if ($radice) {
				#creo un nodo a partire dal frammento
				my $nuovaNews= $parser->parse_balanced_chunk($frammento) || die ("frammento nodo non riuscito");
				#inseirisco il nuovo nodo in fondo
				$radice->appendChild($nuovaNews) || die("inserimento non riuscito");
			} else {
				print "<p class=\"errore\"><strong>Non esiste la radice</strong></p>";
			}

			open(OUT, ">$file") || die("impossibile aprire il documento");
			print OUT $doc->toString || die("impossibile scrivere sul documento");
			close(OUT) || die("impossibile chiudere il documento");
			print '<h2 class="okMessage">Nuova news inserita</h2>';
			print '<a href="gestione_news.cgi" class="goBack">Torna indietro</a>';
			$newsInserita = 1;
		}
	} else {
		print '<p class="errore"><strong>'.$controlloerr.'</strong></p>';
	}
}



if (!$newsInserita){
	print '<div id="errorBox"></div>';
	print '<form action="news_inserisci.cgi" method="post" class="customForm" onsubmit="return validateFormNews();" id="formNews">
	<fieldset>
	<label for="titolo">Titolo:</label>
	<input type="text" name="titolo" id="titolo"/>

	<label for="descrizione">Descrizione:</label>
	<textarea name="descrizione" id="descrizione" cols="40" rows="6"></textarea>
	
	</fieldset>
	<fieldset>
		<input id="invia" type="submit" name="invia" value="Inserisci" class="bottone" />
	</fieldset>
</form>';
}

print '</div>';
printFooter();
print '<script type="text/javascript" src="../js/validateFormNews.js" charset="UTF-8"></script>';
print $page->end_html;
