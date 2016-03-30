#!/usr/bin/perl
use CGI;
use CGI::Session;

sub createSession() {
	my $cgi = @_[2];
	my $email = @_[0];
	my $auth = @_[1];

	$session = new CGI::Session("driver:File", undef, {Directory=>"/tmp"});
	$session->param('email', $email);
	$session->param('auth', $auth); 
	$cookie = $cgi->cookie(CGISESSID => $session->id);
    return $cookie;

}

sub getSession() {
	$session = CGI::Session->load();
	if ($session->is_expired || $session->is_empty ) {	

		return undef;
	} else {
		my $email = $session->param('email');
		return $email;	
	}
}

sub getSessionAuth(){
	$session = CGI::Session->load();
	if ($session->is_expired || $session->is_empty ) {	

		return undef;
	} else {
		my $auth = $session->param('auth');
		return $auth;	
	}
}
#0 -> tutti, 1-> logged, 2-> admin
sub checkAuthLevel() {
	$session = CGI::Session->load();
	if ($session->is_expired || $session->is_empty ) {	
	
		return 0;
	} else {
		my $auth = $session->param('auth');

		my $authNeeded = @_[0];
		if ($auth >= $authNeeded){
			return 1;
		}else{
			return 0;
		}
	}
}



sub destroySession() {
	$session = CGI::Session->load() or die $!; 
	$SID = $session->id();
	$session->param('email', "");
	$session->param('auth', 0); 
	$session->close();
	$session->delete();
	$session->flush();
}


1;