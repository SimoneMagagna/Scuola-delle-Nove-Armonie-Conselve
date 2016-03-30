#!/usr/bin/perl
use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use utf8;

require('customHtmlFunction.pl');

my $page = CGI->new; #Variabile locale scalare

print $page->header('text/html'); #header HTTP

printStartPageHTML5();
printHtml5Head("Foto");
print '<body>';
printHeader();
printNavbarHTML5(7);


#print '<div id="fullscreenDiv" onclick="hideFullScreen();" class="hidden"><img id="fullscreenImg" src="" alt=""/></div>';

print '<div id="content">
		<div id="breadcrumbs">
			<p>Ti trovi in: <a href="index.cgi" lang="en">Home</a> &gt;&gt; <span class="currentPage">Foto</span></p>
		</div>';


my $file= '../data/immagini.xml';
my $parser= XML::LibXML->new();
my $doc = $parser->parse_file($file) || die("Parsing non riuscita");
my $radice= $doc->getDocumentElement || die("Non riesco ad accedere alla radice");
my @nodi= $radice->getElementsByTagName("immagine")->get_nodelist();


print '<ul class="listaFoto">';

foreach $nodo(@nodi){
	my $src = $nodo->getElementsByTagName("src_small")->to_literal();
	my $bigSrc = $nodo->getElementsByTagName("src")->to_literal();
	my $alt = $nodo->getElementsByTagName("alt")->to_literal();
	print "<li>\n";
	print "<a href=\"$bigSrc\" class=\"fresco\" data-fresco-group=\"main-photo-gallery\">\n";	
	print "<img src=\"$src\" alt=\"$alt\" width=\"350\" height=\"200\" class=\"foto\"/>\n";
	print "</a>\n</li>\n";
}


print '</ul>';#fine lista
print '</div>'; #fine div content


printFooter();

print '<script src="http://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>';
print '<script type="text/javascript" src="../js/fresco.js"></script>';

print $page->end_html;

#print $nodi->toString();
