#!/usr/bin/perl

sub elaboraData() {
	$data = @_[0];
	$data = $data->toString;
}

sub controllacampiutente() {

my @controlloerrori;
$controlloerrori[0]= "";
$controlloerrori[1]= "";
$controlloerrori[2]= "";
$controlloerrori[3]= "";
my $i= 0;

if ($_[0] !~ /[a-z0-9A-z]+/) { #controllo nome
	$controlloerrori[0]= "nome troppo corto";
	if ($i != 0) {			
		$controlloerrori[0]= ", " . $controlloerrori[0];
	}
	$i++;
}
if ($_[1] !~ /[a-z0-9A-z]+/) { #controllo cognome
	$controlloerrori[1]= "cognome troppo corto";
	if ($i != 0) {			
		$controlloerrori[1]= ", " . $controlloerrori[1];
	}
	$i++;	
}
if ($_[2] !~ /^([\w\.\-_]+)?\w+@[\w-_]+(\.\w+){1,}$/) { #controllo email
	$controlloerrori[2]= "email non valida";	
	if ($i != 0) {			
		$controlloerrori[2]= ", " . $controlloerrori[2];
	}
	$i++;
}
if ($_[3] !~ /([a-z0-9A-z][a-z0-9A-Z][a-z0-9A-Z][a-z0-9A-Z])+/) { #controllo password
	$controlloerrori[3]= "password troppo corta";
	if ($i != 0) {			
		$controlloerrori[3]= ", " . $controlloerrori[3];
	}
	$i++;
}

my $stringaerrori= "";

for (my $j=0;$j<@controlloerrori;$j++) {
	$stringaerrori= $stringaerrori.$controlloerrori[$j];
}
	return $stringaerrori;
}

sub controllacampinews() {

	my $controlloerrori= "";
	if ($_[0] !~ /[a-z0-9A-z]+/) { #controllo titolo
		$controlloerrori= $controlloerrori."titolo troppo corto";
	}
	return $controlloerrori;
}

sub controllacampiimmagine() {

my $controlloerrori= "";

if (!$_[0]) {
	$controlloerrori= "percorso immagine non valido";
}
	return $controlloerrori;
}

sub uploadimmagine() {
	my $paramName = $_[2];
	my $page= $_[1];
	# "../public_html/Foto" --> per server tecweb
	# "../Foto" --> per funzionamento in locale
	my $upload_dir = "../public_html/Foto";
	my $filename= $_[0];
	my $upload_filehandle = $page->upload($paramName);

open ( UPLOADFILE, ">$upload_dir/$filename" ) or die "$!";
binmode UPLOADFILE;


while ( <$upload_filehandle> )
{
print UPLOADFILE;
}

close UPLOADFILE;

}


1;
