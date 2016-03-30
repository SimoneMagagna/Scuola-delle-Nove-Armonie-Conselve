#!/usr/bin/perl
use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use utf8;

require('customHtmlFunction.pl');

my $page = CGI->new; #Variabile locale scalare

print $page->header('text/html'); #header HTTP

printStartPage();
printAdminHtmlHead("News");
print '<body>';
printHeader();
printNavbar(0);

print '<div id="content">
		<div id="breadcrumbs">
			<p>Ti trovi in: <span class="currentPage">Accesso negato</span></p>
		</div>';

printSessionData();

print '<h1>Accesso negato</h1>';

print '<p class="errore">Non sei loggato o non disponi dei privilegi necessari per visualizzare questa pagina</p>';

print '</div>'; #fine div content



printFooter();

print $page->end_html;

#print $nodi->toString();