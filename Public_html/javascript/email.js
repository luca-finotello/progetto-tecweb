function Email() {
  var email=document.modulo.email.value;
  var oggetto = document.modulo.oggetto.value;
  var messaggio = document.modulo.messaggio.value;
   
  if ((email == "") || (email == "undefined")) {
   alert("Inserire un indirizzo email corretto.");
   document.modulo.email.focus();
}
  else if ((oggetto == "") || (oggetto == "undefined")) {
    alert("Inserire un oggetto.");
    document.modulo.oggetto.focus();
  }
  else if ((messaggio == "") || (messaggio == "undefined")) {
    alert("Inserire un messaggio.");
    document.modulo.messaggio.focus();
  }
  else {
    location.href = "mailto:studioideaweb@gmail.com" + email + "?Subject=" + oggetto + "&Body=" + messaggio; 
  }
  return false
}
