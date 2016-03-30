// JavaScript Document

function validateFormImmagini() {

	var src = document.forms["formImmagini"]["src"].value;

	var invio = true; // se non si sono verificati errori, invio il form
	var errore = "<ul class=\"listaErrori\">"; // contiene una descrizione dell'errore

	if (src == null || src == "") {
        errore += "<li>Nessun immagine selezionata</li>";
        invio = false;
    }
	errore += "</ul>";

	if (!invio){
		document.getElementById("errorBox").innerHTML = errore;
	}

	return invio;
}
