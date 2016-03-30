#!/usr/bin/perl
use XML::LibXML;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use utf8;

require('customHtmlFunction.pl');
require('sessionHelper.pl');

my $page = CGI->new; #Variabile locale scalare

destroySession();


print $page->header('text/html'); #header HTTP

printStartPage();
printAdminHtmlHead("Logout");
print '<body>';
printHeader();
printNavbar();


print '<div id="content">
		<div id="breadcrumbs">
			<p>Ti trovi in: <span class="currentPage">Logout</span></p>
		</div>';


print '<h2 class="okMessage">Logout effettuato con successo</h2>';



print '</div>'; #fine div content


printFooter();


print $page->end_html;
