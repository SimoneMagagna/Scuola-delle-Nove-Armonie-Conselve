// JavaScript Document
function validateFormNews() { 
	//leggo i valori dei campi testuali
    var titolo = document.forms["formNews"]["titolo"].value;
	
	var invio = true; // se non si sono verificati errori, invio il form
	var errore = ""; // contiene una descrizione dell'errore
	
    if (titolo == null || titolo == "") {
        errore += "<p class=\"errore\">Il campo Titolo deve avere un valore.</p>";
        invio = false;
    }
	
	document.getElementById("errorBox").innerHTML = errore;
	return invio;
}