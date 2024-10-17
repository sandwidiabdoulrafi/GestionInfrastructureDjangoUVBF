// recuperation des saisie
// pour ajouter un nouveau signalement
const  nameInfrast = document.querySelector('#name');
const position = document.querySelector('#location');
const description = document.querySelector('#description');
const state = document.querySelector('#etat');
const dateSave = document.querySelector('#DateEnrg');
const btnSubmit = document.querySelector('#addNew');
const numList = document.querySelector('.numList');
const listsInfrastuctSave = document.querySelector('.listsInfrastuctSave');


const email = document.querySelector('#email');
const password = document.querySelector('#password');
const btnConnection = document.querySelector('#connexion');



function isValid( item, msg){
    if(item.value.trim() === ""){
        console.log('le champs '+msg+' est vide.')
        item.style.borderColor = 'red';
        return [false];
    }else{
        item.style.borderColor = 'green';
        return [true,item.value];
    }

}

function isValidEmail(item){

    const reg = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if(!reg.test(item.value.trim())){
        console.log("le champs du ne contient pas mail valid .")
        item.style.borderColor = 'red';
        return [false];

    }else{
        item.style.borderColor = 'green';
        return [true,item.value];
    }
}


function Send(item,items, itm,its, itms){
    if(item[0]&&itms[0]&&items[0]&&itm[0]&&its[0]){

        const newTr = document.createElement('tr');
        
        const positionTD = document.createElement('td');
        const descriptionTD = document.createElement('td');
        const stateTD = document.createElement('td');
        const nameInfrastTD = document.createElement('td');
        const dateSaveTD = document.createElement('td');
        const stateNuberListe = document.createElement('td');


                
        const endpoint = "http://127.0.0.1:8000/infratructure/CitizenSaveInfrastruct/";

        const infrasData = {
            'infrats': item[1],
            'localisation': items[1],
            'desciprtion': itm[1],
            'etat': its[1],
            'DateEnrg': itms[1]
        };
        
        
        fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'data':infrasData})
        })
        .then(response => {
            
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            

            alert(data.message);

            nameInfrastTD.textContent = item[1];
            positionTD.textContent = items[1];
            descriptionTD.textContent = itm[1];
            stateTD.textContent = its[1];
            dateSaveTD.textContent = itms[1];
    
            if(its[1] === 'Urgent'){
                stateTD.style.backgroundColor = 'red';
                stateTD.style.color = 'white';
    
            }else if(its[1] === 'Passable'){
                stateTD.style.backgroundColor = 'yellow';
                stateTD.style.color = 'black';
                
            }else if(its[1].trim() === 'Non-prioritaire'){
                stateTD.style.backgroundColor = 'green';
                stateTD.style.color = 'black';
            }
    
            stateNuberListe.textContent = parseInt(numList.textContent) + 1;
    
            newTr.appendChild(stateNuberListe)
            newTr.appendChild(nameInfrastTD);
            newTr.appendChild(positionTD);
            newTr.appendChild(descriptionTD);
            newTr.appendChild(stateTD);
            newTr.appendChild(dateSaveTD);
    
            listsInfrastuctSave.appendChild(newTr);
        })
        .catch(error => {
            console.error("Erreur lors de la requête :", error);
        });



    }else{
        alert("Les informations sont incorrect vérifier vos champs de saisie.");
    }
}


btnSubmit.addEventListener('click',function (event){
    event.preventDefault();
     alert(' sa marche')

    const validNameInfras = isValid(nameInfrast," nom de l'infrastructure");
    const validLocation = isValid(position, "de la localisation");
    const validDescription = isValid(description,"de description");
    const validState  = isValid(state, "de status ");
    const ValidDateSave = isValid(dateSave," de date" );
    
    Send(validNameInfras, validLocation, validDescription, validState, ValidDateSave);
    
    nameInfrast.value= '';
    position.value= '';
    description.value= '';
    state.value= '';
    dateSave.value= '';


    
})



















//recuperation de toute les infrastructure de date et leur intervensions



const infrastructuresProgramer = document.querySelector('.infrastructuresProgramer');
const addIntervention = document.querySelector('.addIntervention');




addIntervention.addEventListener('click', function (event){
    event.preventDefault();


        fetch('http://127.0.0.1:8000/infratructure/InfrastructuresWithIntervensoinDate/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify()
        })

        .then(response => response.json())

        .then(data =>{
            
            console.log(data.Data)

            const brutData = data.Data;

            console.log('API Response:',brutData );

            
                const DatarRender = brutData.map((item, index) => {

                        let statusCell;alert(item.infrastructure.infratsEtat);
                        if (item.infrastructure.infratsEtat === 'Urgent') {
                            statusCell = `<td style="background-color:red; color:black;">${item.infrastructure.infratsEtat}</td>`;
                        } else if (item.infrastructure.infratsEtat === 'Passable') {
                            statusCell = `<td style="background-color:yellow; color:black;">${item.infrastructure.infratsEtat}</td>`;
                        } else if (item.infrastructure.infratsEtat === 'Non-prioritaire') {
                            statusCell = `<td style="background-color:green; color:black;">${item.infrastructure.infratsEtat}</td>`;
                        }
                        //  else {
                            
                        //     statusCell = `<td>${item.infrastructure.infratsEtat}</td>`;
                        // }
                    return `
                        <tr>
                            <td>${index + 1}</td>
                            <td>${item.infrastructure.infratsNom}</td>
                            <td>${item.infrastructure.infratsLocalition}</td>
                            <td>${item.infrastructure.infratsDescrip}</td>
                            ${statusCell}
                            <td>${item.infrastructure.infratsDateEnrg}</td>
                            <td>${item.intertnsDate}</td>
                        </tr>
                    `;
                }).join('');
        
                const infrastructuresProgramer = document.querySelector('.infrastructuresProgramer');
        
                if (infrastructuresProgramer) {
                    infrastructuresProgramer.innerHTML = DatarRender;
                } else {
                    console.error('Element with class infrastructuresProgramer not found.');
                }




        })
        .catch(error => console.error('Error:', error));

})






btnConnection.addEventListener('click', function (event){
    event.preventDefault();

    const validEmail = isValidEmail(email," du mail ");
    const ValidePassword = isValid(password, "du mot de passe ");
    const dateSave = document.querySelector('#DateEnrg');
    
    
    
    if(validEmail[0] && ValidePassword[0]){

        alert("Toute les informations de connection sont correct .");


        const connexionData ={email: validEmail[1] ,password: ValidePassword[1]}
        fetch('http://127.0.0.1:8000/infratructure/Login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                data: connexionData 
            })
        })
        .then(response => response.json())
        .then(data =>{
            alert(data.message);
            
            localStorage.setItem('isLoggedIn', 'true');

            window.location.href = 'main.html';


            email.value= '';
            password.value= '';

        })
        .catch(error => console.error('Error:', error));



    }else{
        alert("Les information pour la connexion sont incorrect vérifier vos champs de saisie.");
    }

    
})