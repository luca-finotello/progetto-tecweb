 #!/usr/bin/perl

use warnings;
use strict;
use CGI;
use CGI::Carp qw(fatalsToBrowser); 
use CGI::Session;

print "Content-type: text/html\n\n";

print<<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
	<title>Home - Libronline</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<meta name="title" content="" />
	<meta name="description" content="Home page del sito del progetto" />
	<meta name="keywords" content="libraria Padova" />
	<meta name="language" content="italian it" />
	<meta name="author" content="" />
	<link href="style.css" rel="stylesheet" type="text/css" media="screen"/>
	<link rel="stylesheet" href="printstyle.css" type="text/css" media="print"/>	
	<link rel="stylesheet" href="mobilestyle.css" type="text/css" media="handheld, screen and (max-width:480px), only screen and (max-device-width:480px)"/>
	<link href="https://fonts.googleapis.com/css?family=Montserrat%7cMontserrat+Subrayada%7cIndie+Flower" rel="stylesheet" type="text/css" />
	<link href="https://fonts.googleapis.com/css?family=Fredoka+One%7cShadows+Into+Light+Two%7cCherry+Cream+Soda%7cCinzel+Decorative" rel="stylesheet" type="text/css" />
</head>
<body>
	<div id="header">
		<span id="logo"></span>
		<h1> Libronline</h1>
		<h2> il tuo libro a portata di mano ovunque sei</h2>
	</div>
	
	<div id="main">	

		<div id="menu">
			<ul>
				<li><span class="selected" xml:lang="en">Home</span></li>
				<li><a href="libri.html" tabindex="1">Libri</a></li>
				<li><a href="contatti.html" tabindex="2">Contatti</a></li>	
				<li><a href="registrazione.html" tabindex="3">Registrati</a></li>
				<li><a href="login.html" tabindex="4">Entra</a></li>
			</ul>
		</div>

		<div id="contenuto">
		
			<span id="path">Ti trovi in: Home </span>
			EOF

sub createSession() {
		$session = new CGI::Session();
		$session->param('pwd', $password);
}


sub getPwd() {
	$session = CGI::Session->load() or die $!;
	if ($session->is_expired || $session->is_empty ) {
		return undef;
		}	
 	else {
		my $pwd = $session->param('pwd');
		return $pwd;
		}
}

sub destroySession() {
$session = CGI::Session->load() or die $!;
$SID = $session->id();
$session->close();
$session->delete();
$session->flush();
}		

# modifica

$page = new CGI;
createSession();
$password=getPwd();

if(!$password){

	my $submit=$page->param('submit');  
	if($submit){
	
		$password=$page->param('pwd'); 
		if($password eq "admin"){
			print "<h1>BENVENUTO</h1>";
			}
		else
			{print "<h1>ERRORE</h1>";}
		}
		
	else{
	
print<<EOF;
			<h3> Libri consigliati della settimana:</h3>

			<div class="contenitore-img">
				<div class="immagine">
					<img src="immagini/Divergent.jpg" alt="Copertina Divergent"/>
					<a href="#" class="bottone">Scopri di pi&ugrave;</a>
				</div>
				<div class="immagine">
					<img src="immagini/insurgent.jpg" alt="Copertina Insurgent"/>
					<a href="#" class="bottone">Scopri di pi&ugrave;</a>
				</div>
				<div class="immagine">
					<img src="immagini/allegiant.jpg" alt="Copertina Allegiant"/>
					<a href="#" class="bottone">Scopri di pi&ugrave;</a>
				</div>
				<div class="immagine">
					<img src="immagini/vale.jpeg" alt="Copertina Valentino"/>
					<a href="#" class="bottone">Scopri di pi&ugrave;</a>
				</div>
				<div class="immagine">
					<img src="immagini/anna_karenina.jpg" alt="Copertina Anna Karenina"/>
					<a href="#" class="bottone">Scopri di pi&ugrave;</a>
				</div>
			</div>

			<h3>Le ultime novit&agrave; da non perdere!</h3>

			<div class="contenitore-img">
				<div class="immagine">
					<img src="immagini/delitto-e-castigo-dostoevskij.jpg" alt="Copertina Delitto e castigo"/>
				</div>
				<div class="immagine">
					<img src="immagini/il-lungo-addio.jpg" alt="Copertina Il lungo addio"/>
				</div>
				<div class="immagine">
					<img src="immagini/lovecraft_antologia.jpg" alt="Copertina Lovecraft"/>
				</div>
				<div class="immagine">
					<img src="immagini/neve_di_primavera_mishima.png" alt="Copertina Neve di primavera"/>
				</div>
				<div class="immagine">
					<img src="immagini/norwegian_wood.jpg" alt="Copertina Norwegian wood"/>
				</div>
			</div>			
			EOF
	
	}
}

else{

	print "<h1>LOGGED</h1>";

}

print<<EOF;


		</div>
	</div>

	<div id="footer">
		via ugo bassi libreria libronline
	</div>
</body>
</html>
EOF
