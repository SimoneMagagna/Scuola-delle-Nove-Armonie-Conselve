// JavaScript Document
function isMail(mail) {  
	var formato = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;  
	
	if(formato.test(mail)){
		return true;  
	}else{  
		return false;  
	}  
}  


function validateFormLogin() {

	var mail = document.forms["formLogin"]["email"].value;
	var psw = document.forms["formLogin"]["password"].value;

	var invio = true; // se non si sono verificati errori, invio il form
	var errore = "<ul class=\"listaErrori\">"; // contiene una descrizione dell'errore


	if (mail == null || mail == "") {
        errore += "<li>Il campo e-Mail deve avere un valore.</li>";
        invio = false;
    }else{ // e' stata inserita una mail
	    if(! isMail(mail)){
			errore += "<li>Il campo e-Mail non è un indirizzo valido.</li>";
        	invio = false;
		}
	}
	if (psw == null || psw == "") {
        errore += "<li>Il campo Password deve avere un valore.</li>";
        invio = false;
    }
	errore += "</ul>";

	if (!invio){
		document.getElementById("errorBox").innerHTML = errore;
	}

	return invio;
}

function validateFormUtente() { 
	//leggo i valori dei campi testuali
    var nome = document.forms["formUtente"]["nome"].value;
	var cognome = document.forms["formUtente"]["cognome"].value;
	var mail = document.forms["formUtente"]["email"].value;
	var psw = document.forms["formUtente"]["password"].value;
	
	var invio = true; // se non si sono verificati errori, invio il form
	var errore = "<ul class=\"listaErrori\">"; // contiene una descrizione dell'errore
	
    if (nome == null || nome == "") {
        errore += "<li>Il campo Nome deve avere un valore.</li>";
        invio = false;
    }
	
	if (cognome == null || cognome == "") {
        errore += "<li>Il campo Cognome deve avere un valore.</li>";
        invio = false;
    }
	
	if (mail == null || mail == "") {
        errore += "<li>Il campo e-Mail deve avere un valore.</li>";
        invio = false;
    }else{ // e' stata inserita una mail
	    if(! isMail(mail)){
			errore += "<li>Il campo e-Mail non è un indirizzo valido.</li>";
        	invio = false;
		}
	}
	
	if (psw == null || psw == "") {
        errore += "<li>Il campo Password deve avere un valore.</li>";
        invio = false;
    }else{ // e' stata inserita una password
		var pswL = psw.length;
		if(pswL<4){
			errore += "<li>La password deve contenere almeno 4 caratteri.</li>";
        	invio = false;
		}
	}
	errore += "</ul>";
	
	if (!invio){
		document.getElementById("errorBox").innerHTML = errore;
	}
	return invio;
}