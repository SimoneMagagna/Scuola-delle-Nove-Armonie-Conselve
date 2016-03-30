# Funzioni presenti:
# printStartPage
# printHtmlHead
# printAdminHtmlHead
# printHeader
# printNavbar
# printAdminNavbar
# printFooter

require('sessionHelper.pl');

sub printSessionData(){
	$email=getSession();
	if ($email){
		print '<p class="sessionInfo">Sei autenticato come '.$email.', <a href="logout.cgi">Esci</a></p>';
	}
}


# Stampa il tag DOCTYPE e l'apertura del tag html
sub printStartPage{
	print '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it" >';
}


# Stampa il tag DOCTYPE e l'apertura del tag html versione 5
sub printStartPageHTML5{
	print '<!DOCTYPE html> <html lang="it">';
}

# Stampa il tag <head>, primo parametro: titolo della pagina
# Include tutti i vari meta tag e i css.
# Da usare su ogni pagina generata
# Esempio di chiamata: printHtmlHead("Home");
sub printHtmlHead{
	$pageTitle = @_[0];


	print '<head>';
	print "<title>$pageTitle - Scuola delle 9 Armonie Conselve</title>"; # Inserisce il titolo passato per parametro
	print '<link href="../Immagini/favicon_logo.ico" rel="shortcut icon" type="image/x-icon" />
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta name="keywords" content="scuola delle 9 armonie conselve, kung fu, t\'ai-c\'hi-chuan, arti marziali, cina, wing-chun, siu-lam, hung-gar, hop-gar, tang-lang, choy-ley-fut, fut-gar, yang, sun, chen, kao tibetano" />
        <meta name="description" content="Sito dedicato alla Scuola delle 9 armonie Conselve" />
		<meta name="author" content="Simone Magagna" />
        <meta name="language" content="italian it" />
		<link href="../css/main.css" media="screen" rel="stylesheet" type="text/css" />
		<link href="../css/mobile.css" media="handheld, screen and (max-width:1024px), only screen and (max-device-width:1024px)" rel="stylesheet" type="text/css" />
		<link href="../css/print.css" media="print" rel="stylesheet" type="text/css" />';
	print '</head>';
}

# Versione HTML5
# Stampa il tag <head>, primo parametro: titolo della pagina
# Include tutti i vari meta tag e i css.
# Da usare su ogni pagina generata
# Esempio di chiamata: printHtmlHead("Home");
sub printHtml5Head{
	$pageTitle = @_[0];

	print '<head>';
	print "<title>$pageTitle - Scuola delle 9 Armonie Conselve</title>"; # Inserisce il titolo passato per parametro
	print '<link href="../Immagini/favicon_logo.ico" rel="shortcut icon" type="image/x-icon" />
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta name="keywords" content="scuola delle 9 armonie conselve, kung fu, t\'ai-c\'hi-chuan, arti marziali, cina, wing-chun, siu-lam, hung-gar, hop-gar, tang-lang, choy-ley-fut, fut-gar, yang, sun, chen, kao tibetano" />
        <meta name="description" content="Sito dedicato alla Scuola delle 9 armonie Conselve" />
		<meta name="author" content="Simone Magagna" />
		<link href="../css/main.css" media="screen" rel="stylesheet" type="text/css" />
		<link href="../css/mobile.css" media="handheld, screen and (max-width:1024px), only screen and (max-device-width:1024px)" rel="stylesheet" type="text/css" />
		<link href="../css/print.css" media="print" rel="stylesheet" type="text/css" />
		<link href="../css/fresco.css" media="screen" rel="stylesheet" type="text/css" />';
	print '</head>';
}


# Stampa il tag <head>, primo parametro: titolo della pagina
# Include tutti i vari meta tag e i css, compresi quelli per le pagine di amministrazione
# Da usare su ogni pagina generata
# Esempio di chiamata: printHtmlHead("Home");
sub printAdminHtmlHead{
	$pageTitle = @_[0];


	print '<head>';
	print "<title>$pageTitle - Scuola delle 9 Armonie Conselve</title>"; # Inserisce il titolo passato per parametro
	print '<link href="../Immagini/favicon_logo.ico" rel="shortcut icon" type="image/x-icon" />
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta name="keywords" content="scuola delle 9 armonie conselve, kung fu, t\'ai-c\'hi-chuan, arti marziali, cina, wing-chun, siu-lam, hung-gar, hop-gar, tang-lang, choy-ley-fut, fut-gar, yang, sun, chen, kao tibetano" />
        <meta name="description" content="Sito dedicato alla Scuola delle 9 armonie Conselve" />
		<meta name="author" content="Simone Magagna" />
        <meta name="language" content="italian it" />
		<link href="../css/main.css" media="screen" rel="stylesheet" type="text/css" />
		<link href="../css/amministrazione.css" media="screen" rel="stylesheet" type="text/css" />
		<link href="../css/mobile.css" media="handheld, screen and (max-width:1024px), only screen and (max-device-width:1024px)" rel="stylesheet" type="text/css" />
		<link href="../css/print.css" media="print" rel="stylesheet" type="text/css" />';
	print '</head>';
}


# Stampa l'header della pagina, con il logo e il titolo
sub printHeader {
	print '<div class="skipLink">
		<a href="#content" class="skipLink">Vai al contenuto</a>
	</div>
		<div id="header">
			<a href="index.cgi">
				<img class="logo" src="../Immagini/logo.png" alt="Scuola delle 9 Armonie Conselve home page" title="Logo Scuola delle 9 Armonie Conselve" />
			</a>
			<div class="titleArea">
				<h1>Scuola delle 9 Armonie</h1>
				<h2>Conselve</h2>
			</div>
		</div>';
}


# Stampa la Navbar principale, quelle usata nelle varie pagine statiche
# Da usare quando viene generata la lista di foto o le news;
# Parametro: intero da 0 a 7, corrispondete alla pagina attiva
# 0 -> index, 1 -> Chi siamo, 2 -> Sedi e corsi, ecc.
# Esempio: printNavar(0) --> Navbar che ha come pagina corrente la Home
sub printNavbar {
	# body...
	$active = @_[0];
	print '<div id="nav"><ul>';
	print "\n";
	if ($active eq 0){
		print '<li xml:lang="en" class="currentLink">Home</li>';
	}else {
		print '<li xml:lang="en"><a href="index.cgi">Home</a></li>';
	}
	print "\n";
	if ($active eq 1){
		print '<li class="currentLink">Chi siamo</li>';
	}else {
		print '<li><a href="../chi_siamo.html">Chi Siamo</a></li>';
	}
	print "\n";
	if ($active eq 2){
		print '<li class="currentLink">Sedi e Corsi</li>';
	}else {
		print '<li><a href="../sedi_e_corsi.html">Sedi e Corsi</a></li>';
	}
	print "\n";
	if ($active eq 3){
		print '<li class="currentLink"><span title="tai ci ciuan">T\'ai C\'hi Chuan</span></li>';
	}else {
		print '<li><a href="../tai_chi_chuan.html"><span title="tai ci ciuan">T\'ai C\'hi Chuan</span></a></li>';
	}
	print "\n";
	if ($active eq 4){
		print '<li class="currentLink">Kung Fu</li>';
	}else {
		print '<li><a href="../kung_fu.html">Kung Fu</a></li>';
	}
	print "\n";
	if ($active eq 5){
		print '<li class="currentLink">Maestro</li>';
	}else {
		print '<li><a href="../maestro.html">Maestro</a></li>';
	}
	print "\n";
	if ($active eq 6){
		print '<li class="currentLink">Istruttori</li>';
	}else {
		print '<li><a href="../istruttori.html">Istruttori</a></li>';
	}
	print "\n";
	if ($active eq 7){
		print '<li class="currentLink">Foto</li>';
	}else {
		print '<li><a href="foto.cgi">Foto</a></li>';
	}
	print "\n";
	print '</ul>
			</div>';

}


# Stampa la Navbar principale, in versione HTML5 quelle usata nelle varie pagine statiche
# Da usare quando viene generata la lista di foto o le news;
# Parametro: intero da 0 a 7, corrispondete alla pagina attiva
# 0 -> index, 1 -> Chi siamo, 2 -> Sedi e corsi, ecc.
# Esempio: printNavar(0) --> Navbar che ha come pagina corrente la Home
sub printNavbarHTML5 {
	# body...
	$active = @_[0];
	print '<div id="nav"><ul>';
	print "\n";
	if ($active eq 0){
		print '<li lang="en" class="currentLink">Home</li>';
	}else {
		print '<li lang="en"><a href="index.cgi">Home</a></li>';
	}
	print "\n";
	if ($active eq 1){
		print '<li class="currentLink">Chi siamo</li>';
	}else {
		print '<li><a href="../chi_siamo.html">Chi Siamo</a></li>';
	}
	print "\n";
	if ($active eq 2){
		print '<li class="currentLink">Sedi e Corsi</li>';
	}else {
		print '<li><a href="../sedi_e_corsi.html">Sedi e Corsi</a></li>';
	}
	print "\n";
	if ($active eq 3){
		print '<li class="currentLink"><span title="tai ci ciuan">T\'ai C\'hi Chuan</span></li>';
	}else {
		print '<li><a href="../tai_chi_chuan.html"><span title="tai ci ciuan">T\'ai C\'hi Chuan</span></a></li>';
	}
	print "\n";
	if ($active eq 4){
		print '<li class="currentLink">Kung Fu</li>';
	}else {
		print '<li><a href="../kung_fu.html">Kung Fu</a></li>';
	}
	print "\n";
	if ($active eq 5){
		print '<li class="currentLink">Maestro</li>';
	}else {
		print '<li><a href="../maestro.html">Maestro</a></li>';
	}
	print "\n";
	if ($active eq 6){
		print '<li class="currentLink">Istruttori</li>';
	}else {
		print '<li><a href="../istruttori.html">Istruttori</a></li>';
	}
	print "\n";
	if ($active eq 7){
		print '<li class="currentLink">Foto</li>';
	}else {
		print '<li><a href="foto.cgi">Foto</a></li>';
	}
	print "\n";
	print '</ul>
			</div>';

}


# Stampa la barra di navigazione per la zona di amministrazione
# Parametro: intero da 0 a 3, corrispondete alla pagina attiva
# 0 -> Home, 1 -> Utenti, 2 -> News, 3 -> Foto
# Esempio: printNavar(0) --> Navbar che ha come pagina corrente la Home
sub printAdminNavbar {
	# body...
	# @_ è l'array che contiene i parametri
	$active = @_[0]; 
	print '<div id="nav"><ul>';
	if ($active eq 0){
		print '<li xml:lang="en" class="currentLink">Home</li>';
	}else {
		print '<li xml:lang="en"><a href="index.cgi">Home</a></li>';
	}
	print "\n";
	if ($active eq 1){
		print '<li class="currentLink">Utenti</li>';
	}else {
		print '<li><a href="gestione_utenti.cgi">Utenti</a></li>';
	}
	print "\n";
	if ($active eq 2){
		print '<li class="currentLink" xml:lang="en">News</li>';
	}else {
		print '<li><a href="gestione_news.cgi" xml:lang="en">News</a></li>';
	}
	print "\n";
	if ($active eq 3){
		print '<li class="currentLink">Foto</li>';
	}else {
		print '<li><a href="gestione_img.cgi">Foto</a></li>';
	}
	print "\n";
	print '</ul></div>';
}


# Stampa il footer, nessun parametro
sub printFooter {
	print '<div id="footer">
			<p class="address">
				<strong>Scuola delle 9 Armonie Conselve</strong> <br/>
				Via Beggiato, 50 c/o Scuola Tommaseo Conselve (PD) <br/>
				Telefono: 347 8480028
			</p>
			<div class="social">
			<p class="seguici">Seguici su:</p>
				<a href="https://www.facebook.com/pages/ASD-Scuola-Delle-Nove-Armonie-Conselve/421687384603863" tabindex="9">
					<img alt="facebook" src="../Immagini/fb.png" height="45" width="45"/></a>
				<a href="https://plus.google.com/s/scuola%20nove%20armonie%20conselve" tabindex="10">
					<img alt="google plus" src="../Immagini/gplus.png" height="45" width="45"/></a>
			</div>
			<p class="footerLink">
				<a href="../mappa.html" tabindex="11">Mappa del sito</a> |
				<a href="login.cgi" tabindex="12">Area riservata</a>
			</p>
			<div class="skipLink">
				<a href="#nav" class="skipLink">Torna alla barra di navigazione</a>
			</div>
		</div>';
	print '<script src="http://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
        <script src="../jquery/jquery.backstretch.min.js" type="text/javascript"></script>
		<script type="text/javascript">
  			$.backstretch("../Immagini/sfondo2modified.jpg");
		</script>';
}
1;
