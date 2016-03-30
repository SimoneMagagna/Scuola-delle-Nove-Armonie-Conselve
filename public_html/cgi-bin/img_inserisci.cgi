#!/usr/bin/perl
use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use File::Basename;
use utf8;

require ('funzioni.pl');
require('customHtmlFunction.pl');
require('sessionHelper.pl');

if (!checkAuthLevel(1)){
	print redirect("noauth.cgi");
} 

my $file= '../data/immagini.xml';
my $fotoDirecotry = "../Foto/";

my $page = CGI->new; #Variabile locale scalare
print $page->header('text/html'); #header HTTP


my $immagineInserita = 0;



printStartPage();
printAdminHtmlHead("Inserisci Foto - Gestione Foto");
print '<body>';
printHeader();
printAdminNavbar(3); #Stampa la navbar corretta

print '<div id="content">
		<div id="breadcrumbs">
			<p>Ti trovi in: <a href="gestione_img.cgi">Gestione Foto</a> &gt; &gt; <span class="currentPage">Inserisci nuova foto</span></p>
		</div>';
printSessionData();
print '<h1>Inserisci nuova foto</h1>';


if ( ($page->param('invia') ne 0) && ($page->param('invia') eq "Inserisci") )  {
	#Se ci sono i dati di input, inserisco la foto
	$input{srcsmall}= $page->param('src_small');
	$input{src}= $page->param('src');
	$input{alt}= $page->param('alt');

	my $controlloerr= &controllacampiimmagine($input{src});

	if ($controlloerr eq "") { 

		my $parser= XML::LibXML->new();
		my $doc = $parser->parse_file($file) || die("parsificazione non riuscita");
		my $radice= $doc->getDocumentElement || die("Non riesco ad accedere alla radice");
		my $query= "//immagine[src='$fotoDirecotry$input{src}']/src";


		my $xpc = XML::LibXML::XPathContext->new($doc);
		$xpc->registerNs('i', 'http://www.9armonie.com/immagini');

		my $query= "//i:immagine[i:src='$fotoDirecotry$input{src}']/i:src"; #identifico la news che voglio eliminare

		if ($xpc->findnodes($query)->size()>0) {
			print "<p class=\"errore\"><strong>Immagine gi&agrave; presente</strong></p>";
		} else {

			&uploadimmagine($input{src},$page,"src");

			if ($input{srcsmall}) {
				&uploadimmagine($input{srcsmall},$page,"src_small");
			
			} else {
				$input{srcsmall}= $input{src};
			}

			my $frammento= "	<immagine>
		<src>".$fotoDirecotry.$input{src}."</src>
		<src_small>".$fotoDirecotry.$input{srcsmall}."</src_small>
		<alt>".$input{alt}."</alt>
	</immagine>\n";
			if ($radice) {
				my $nodo= $parser->parse_balanced_chunk($frammento) || die ("frammento nodo non riuscito");
				$radice->appendChild($nodo) || die("inserimento non riuscito");
			} else {
				print "<p class=\"errore\"><strong>Non esiste la radice</strong></p>";
			}

			open(OUT, ">$file") || die("impossibile aprire il documento");
			print OUT $doc->toString || die("impossibile scrivere sul documento");
			close(OUT) || die("impossibile chiudere il documento");
			print '<h2 class="okMessage">Immagine inserita correttamente</h2>';
			print '<a href="gestione_img.cgi" class="goBack">Torna indietro</a>';
			$immagineInserita = 1;
		}
	} else {
		print "<p class=\"errore\"><strong>$controlloerr</strong></p>";
	}
}

if (!$immagineInserita){
	print '<div id="errorBox"></div>';
	print '
	<form action="" method="post" enctype="multipart/form-data" class="customForm" id="formImmagini" onsubmit="return validateFormImmagini();">
	<fieldset>
	<label for="alt">Descrizione:</label>
	<input type="text" name="alt" id="alt"/>
	
	<label for="src">Percorso:</label>
	<input type="file" name="src" id="src" />
	
	<label for="src_small">Percorso immagine piccola:</label>
	<input type="file" name="src_small" id="src_small" />
	</fieldset>
	<fieldset class="buttonArea">
	<input id="invia" type="submit" name="invia" value="Inserisci" class="bottone"/>
	</fieldset>
	</form>';
}

print '</div>';
printFooter();
print '<script type="text/javascript" src="../js/validateFormImmagini.js" charset="UTF-8"></script>';
print $page->end_html;
