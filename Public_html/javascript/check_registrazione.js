function check_registrazione() {

var nome = document.getElementById("nome");
var cognome = document.getElementById("cognome");
var giorno = document.getElementById("giorno");
var mese = document.getElementById("mese");
var anno = document.getElementById("anno");
var e_mail = document.getElementById("email");
var check_e_mail = e_mail.search(/^([\w\-\+\.]+)@([\w\-\+\.]+).([\w\-\+\.]+)$/); 
var username = document.getElementById("registrazione");
var password =  document.getElementById("password");
var repeat_password =  document.getElementById("repeat_password");

if((nome == "" ) || (nome == "undefined"){

alert("campo NOME non può essere vuoto");
document.getElementById("nome").focus();

}

if((cognome == "") || (cognome == "undefined"){

alert("campo COGNOME non può essere vuoto");
document.getElementById("cognome").focus();

}

if((anno % 4 == 0)){

  if(mese == "2"){
  	if(giorno > 29){
		alert("Febbraio negli anni bisestili non può avere più di 29 giorni");  	
  		document.getElementById("giorno").focus();
  	}
  }
  else if(mese == "4" || mese == "6" || mese == "9" || mese == "11" ){
  	if(giorno == 31){
		alert("Aprile, Giugno, Settembre e Novembre hanno 30 giorni ");
		document.getElementById("giorno").focus();  	
  	}
  
  }


}
else if(anno % 4 != 0){

 	if(giorno > 28){
		alert("Febbraio negli anni non bisestili non ha più di 28 giorni");  	
  		document.getElementById("giorno").focus();
  	}
  }
  else if(mese == "4" || mese == "6" || mese == "9" || mese == "11" ){
  	if(giorno == 31){
		alert("Aprile, Giugno, Settembre e Novembre hanno 30 giorni ");
		document.getElementById("giorno").focus();  	
  	}


}

if(check_e_mail != 0){

alert("MAIL non valida");
document.getElementById("e_mail").focus();

}

if(username == "" || username == "undefined"){


alert("campo USERNAME non può essere vuoto");
document.getElementById("username").focus();

}


if((password != repeat_password) ){
	alert("PASSWORD e REINSERISCI PASSWORD devono essere uguali");
	document.getElementById("repeat_password").focus();
}
else if(password == "" || password == "undefined"){
	alert("campo PASSWORD non può essere vuoto");
	document.getElementById("password").focus();

}
else if(repeat_password == "" || repeat_password == "undefined"){
	alert("campo REINSERISCI PASSWORD non può essere vuoto")	
	document.getElementById("repeat_password").focus();

}

}