

function planifier(id) {
    const datePlanification = prompt('Entrez la date de planification (YYYY-MM-DD) :');
    if (datePlanification) {
        // Déplacer l'infrastructure dans la liste des planifiées
        const infrastructure = infrastructures.find(i => i.id === id);
        infrastructures.splice(infrastructures.indexOf(infrastructure), 1); // Retirer des non planifiées
        
        const tbodyPlanified = document.querySelector('.infrastructuresProgramer');
        const rowPlanified = `
            <tr>
                <td>${infrastructure.id}</td>
                <td>${infrastructure.type}</td>
                <td>${infrastructure.localisation}</td>
                <td>${infrastructure.description}</td>
                <td>${infrastructure.etat}</td>
                <td>${infrastructure.dateEnregistrement}</td>
                <td>${datePlanification}</td>
                <td>${admin.name}</td>
            </tr>
        `;
        tbodyPlanified.insertAdjacentHTML('beforeend', rowPlanified);
        
        //loadInfrastructures(); // Mettre à jour la table des non planifiées
    }
}




const DateNonPlanifie = document.querySelector('#DateNonPlanifie');

DateNonPlanifie.addEventListener('click', function (event){
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
                            <td><button class="btn btn-primary" onclick="planifier(${infrastructure.id})">Planifier</button></td>
                        </tr>
                    `;
                }).join('');
        
                const listsInfrastuctNoNplanifier = document.querySelector('.listsInfrastuctNoNplanifier');
    
                listsInfrastuctNoNplanifier.innerHTML = DatarRender;
            




        })
        .catch(error => console.error('Error:', error));

})





























































const refreshlisplanifier = document.querySelector('#refreshlisplanifier');

refreshlisplanifier.addEventListener('click', function (event){
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

                        let statusCell;
                        
                        alert(item.infrastructure.infratsEtat);

                        if (item.infrastructure.infratsEtat === 'Urgent') {
                            statusCell = `<td style="background-color:red; color:black;">${item.infrastructure.infratsEtat}</td>`;
                        } else if (item.infrastructure.infratsEtat === 'Passable') {
                            statusCell = `<td style="background-color:yellow; color:black;">${item.infrastructure.infratsEtat}</td>`;
                        } else if (item.infrastructure.infratsEtat === 'Non-prioritaire') {
                            statusCell = `<td style="background-color:green; color:black;">${item.infrastructure.infratsEtat}</td>`;
                        }
                        
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
    
                infrastructuresProgramer.innerHTML = DatarRender;
               




        })
        .catch(error => console.error('Error:', error));

})


































//  // Simulate adding non-validated infrastructures
//  const infrastructures = [
//     { id: 1, type: "École Publique", localisation: "Centre ville", description: "Manque de voiture", etat: "Urgent", dateEnregistrement: "2024-05-05" }
// ];

// const admin = { name: "Admin 1" }; // Exemple d'admin connecté

// function loadInfrastructures() {
//     const tbody = document.querySelector('.listsInfrastuctSave');
//     tbody.innerHTML = '';
//     infrastructures.forEach((infrastructure, index) => {
//         const row = `
//             <tr>
//                 <td>${index + 1}</td>
//                 <td>${infrastructure.type}</td>
//                 <td>${infrastructure.localisation}</td>
//                 <td>${infrastructure.description}</td>
//                 <td>${infrastructure.etat}</td>
//                 <td>${infrastructure.dateEnregistrement}</td>
//                 <td><button class="btn btn-primary" onclick="planifier(${infrastructure.id})">Planifier</button></td>
//             </tr>
//         `;
//         tbody.insertAdjacentHTML('beforeend', row);
//     });
// }





// function planifier(id) {
//     const datePlanification = prompt('Entrez la date de planification (YYYY-MM-DD) :');
//     if (datePlanification) {
//         // Déplacer l'infrastructure dans la liste des planifiées
//         const infrastructure = infrastructures.find(i => i.id === id);
//         infrastructures.splice(infrastructures.indexOf(infrastructure), 1); // Retirer des non planifiées
        
//         const tbodyPlanified = document.querySelector('.infrastructuresProgramer');
//         const rowPlanified = `
//             <tr>
//                 <td>${infrastructure.id}</td>
//                 <td>${infrastructure.type}</td>
//                 <td>${infrastructure.localisation}</td>
//                 <td>${infrastructure.description}</td>
//                 <td>${infrastructure.etat}</td>
//                 <td>${infrastructure.dateEnregistrement}</td>
//                 <td>${datePlanification}</td>
//                 <td>${admin.name}</td>
//             </tr>
//         `;
//         tbodyPlanified.insertAdjacentHTML('beforeend', rowPlanified);
        
//         loadInfrastructures(); // Mettre à jour la table des non planifiées
//     }
// }

// //
