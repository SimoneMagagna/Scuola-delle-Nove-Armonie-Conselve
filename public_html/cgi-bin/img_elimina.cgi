#!/usr/bin/perl
use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use utf8;

my $file= '../data/immagini.xml';
my $fotoDirecotry = "../Foto/";

require('customHtmlFunction.pl');
require('sessionHelper.pl');

if (!checkAuthLevel(1)){
	print redirect("noauth.cgi");
} 


my $page = CGI->new; #Variabile locale scalare


$input{srcsmall}= $page->param('srcsmall');
$input{src}= $page->param('src');
$input{alt}= $page->param('alt');

print $page->header('text/html'); #header HTTP
printStartPage();
printAdminHtmlHead("Elimina Foto - Gestione Foto");
print '<body>';
printHeader();
printAdminNavbar(3); #Stampa la navbar corretta

print '<div id="content">
		<div id="breadcrumbs">
			<p>Ti trovi in: <a href="gestione_img.cgi">Gestione Foto</a> &gt; &gt;<span class="currentPage">Elimina foto</span></p>
		</div>';
printSessionData();




my $parser= XML::LibXML->new();
my $doc = $parser->parse_file($file) || die("parsificazione non riuscita");

my $xpc = XML::LibXML::XPathContext->new($doc);
$xpc->registerNs('i', 'http://www.9armonie.com/immagini');

my $query= "//i:immagine[i:src='$input{src}']"; #identifico la news che voglio eliminare
my $img= $xpc->findnodes($query)->get_node(1);


my $padre = $img->parentNode;
$padre->removeChild($img);
#$input{src} e $input{srcsmall} contengono il percorso completo
if ($input{src} ne $input{srcsmall}) {
	unlink "$input{srcsmall}";
}
unlink "$input{src}";
open(OUT, ">$file") || die("impossibile aprire il documento");
print OUT $doc->toString || die("impossibile scrivere sul documento");
close(OUT) || die("impossibile chiudere il documento");

print '<h2 class="okMessage">Foto eliminata</h2>';
print '<a href="gestione_img.cgi" class="goBack">Torna indietro</a>';


print '</div>';
printFooter();

print $page->end_html;