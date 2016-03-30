#!/usr/bin/perl
use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use utf8;

my $file= '../data/news.xml';

require('customHtmlFunction.pl');
require('sessionHelper.pl');

if (!checkAuthLevel(1)){
	print redirect("noauth.cgi");
} 


my $page = CGI->new; 
my $titolo = $page->param('titolo');


print $page->header('text/html'); #header HTTP
printStartPage();
printAdminHtmlHead("Elimina News - Gestione News");
print '<body>';
printHeader();
printAdminNavbar(2); #Stampa la navbar corretta

print '<div id="content">
		<div id="breadcrumbs">
			<p>Ti trovi in: <a href="gestione_news.cgi">Gestione News</a> &gt; &gt; <span class="currentPage">Elimina News</span></p>
		</div>';
printSessionData();


my $parser= XML::LibXML->new();
my $doc = $parser->parse_file($file);

my $xpc = XML::LibXML::XPathContext->new($doc);
$xpc->registerNs('news', 'http://www.9armonie.com/news');


my $query= "//news:news[news:titolo='$titolo']"; #identifico la news che voglio eliminare
my $news= $xpc->findnodes($query)->get_node(1);

my $padre= $news->parentNode; #prendo il padre
$padre->removeChild($news) || die("impossibile eliminare la news"); #tolgo il nodo

open(OUT, ">$file"); 
print OUT $doc->toString; 
close(OUT);

print "<h2 class=\"okMessage\">News eliminata</h2>";
print '<a href="gestione_news.cgi" class="goBack">Torna indietro</a>';

print '</div>';
printFooter();

print $page->end_html;