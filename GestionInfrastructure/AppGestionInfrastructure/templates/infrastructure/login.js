// Sélection des éléments du formulaire
const prenom = document.querySelector('#prenom');
const nom = document.querySelector('#nom'); 
const email = document.querySelector('#email'); 
const motdepasse = document.querySelector('#motdepasse'); 
const tel = document.querySelector('#tel'); 

// Fonction pour valider l'email
function isValidEmail(item) {
    const reg = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!reg.test(item.value.trim())) {
        console.log("Le champ ne contient pas un email valide.");
        item.style.borderColor = 'red';
        return [false];
    } else {
        item.style.borderColor = 'green';
        return [true, item.value];
    }
}

// Fonction pour valider les champs
function isValid(item, msg) {
    if (item.value.trim() === "") {
        console.log('Le champ ' + msg + ' est vide.');
        item.style.borderColor = 'red';
        return [false];
    } else {
        item.style.borderColor = 'green';
        return [true, item.value];
    }
}

// Fonction d'inscription
function SignUp(event) {
    event.preventDefault(); 

    const validEmail = isValidEmail(email); 
    const validNom = isValid(nom, 'nom');
    const validPrenom = isValid(prenom, 'prénom');
    const validMotdepasse = isValid(motdepasse, 'mot de passe');
    const validTel = isValid(tel, 'téléphone');

    const inscriptionData = {
        nom: validNom[1],
        prenom: validPrenom[1],
        tel: validTel[1],
        email: validEmail[1],
        password: validMotdepasse[1]
    };

    if (validEmail[0] && validNom[0] && validPrenom[0] && validMotdepasse[0] && validTel[0]) {
        alert("Tout est ok !!!!");

        fetch("http://127.0.0.1:8000/infratructure/SignUp/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ 'data': inscriptionData }),
        })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            alert(data.message);

            // Réinitialiser les champs du formulaire
            tel.value = '';
            motdepasse.value = '';
            email.value = '';
            nom.value = '';
            prenom.value = '';
            window.location.href('./index.html')
        })
        .catch((error) => console.error(error));
    } else {
        alert('Vos informations ne sont pas valides.');
    }

    return true;
}

// Attacher l'écouteur d'événements au bouton de soumission
const btnSubmit = document.querySelector('#btnSubmit');
btnSubmit.addEventListener('click', SignUp); // Passer la référence de la fonction