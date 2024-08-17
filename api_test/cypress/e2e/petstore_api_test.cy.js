describe('PetStore API Testing', () => {
    
    const baseUrl = 'https://petstore.swagger.io/v2';
    let petIdRandomGenerated = Math.floor(Math.random() * 1000);
    let petId;
    let report = '';  // Variable para almacenar el reporte
    const reportPath = 'cypress/reports/test-report.txt';  // Ruta del archivo de reporte

    /*
    Genero un número aleatorio restringido porque en la API hay números 
    extremadamente grandes que generan una NumberFormatException por parte
    de la API realizada en Java.
    */

    it('Añadir una mascota a la tienda', () => {
        cy.request({
            method: 'POST',
            url: `${baseUrl}/pet`,
            body: {
                id: petIdRandomGenerated,
                category: { id: 0, name: 'string' },
                name: 'Fiona',
                photoUrls: ['string'],
                tags: [{ id: 0, name: 'string' }],
                status: 'available'
            },
            failOnStatusCode: false
        }).then((response) => {
            if (response.status === 200) {
                petId = response.body.id;
                report += `Test: Añadir una mascota a la tienda - PASSED\n`;
                report += `ID de la mascota creada: ${petId}\n\n`;
            } else {
                expect(response.status == 200)
                report += `Test: Añadir una mascota a la tienda - FAILED\n`;
                report += `Response Status: ${response.status}\n\n`;
            }
        });
    });

    it('Consultar la mascota ingresada previamente (Búsqueda por ID)', () => {
        cy.request({
            method: 'GET',
            url: `${baseUrl}/pet/${petId}`,
            failOnStatusCode: false
        }).then((response) => {
            if (response.status === 200 && response.body.id == petId && response.body.name == 'Fiona') {
                report += `Test: Consultar la mascota ingresada previamente - PASSED\n\n`;
            } else {
                expect(response.status == 200)
                expect(response.body.id).to.eq(petId);
                expect(response.body.name).to.eq('Fiona');
                report += `Test: Consultar la mascota ingresada previamente - FAILED\n`;
                report += `Response Status: ${response.status}\n\n`;
            }
        });
    });

    it('Actualizar el nombre de la mascota y el estatus de la mascota a “sold”', () => {
        cy.request({
            method: 'PUT',
            url: `${baseUrl}/pet`,
            body: {
                id: petId,
                category: { id: 0, name: 'string' },
                name: 'Fiona1',
                photoUrls: ['string'],
                tags: [{ id: 0, name: 'string' }],
                status: 'sold'
            },
            failOnStatusCode: false
        }).then((response) => {
            if (response.status === 200 && response.body.name == 'Fiona1' && response.body.status == 'sold') {
                report += `Test: Actualizar el nombre y estatus de la mascota - PASSED\n\n`;
            } else {
                expect(response.status == 200)
                expect(response.body.name).to.eq('Fiona1');
                expect(response.body.status).to.eq('sold');
                report += `Test: Actualizar el nombre y estatus de la mascota - FAILED\n`;
                report += `Response Status: ${response.status}\n\n`;
            }
        });
    });

    it('Consultar la mascota modificada por estatus (Búsqueda por estatus)', () => {
        cy.request({
            method: 'GET',
            url: `${baseUrl}/pet/findByStatus?status=sold`,
            failOnStatusCode: false
        }).then((response) => {
            const pets = response.body;
            const foundPet = pets.find(pet => pet.id === petId && pet.name === 'Fiona1');
            if (response.status === 200) {
                report += `Test: Consultar la mascota modificada por estatus - PASSED\n`;
            } else {
                expect(response.status == 200)
                expect(foundPet.id).to.eq('petID');
                expect(foundPet.name).to.eq('Fiona1');
                report += `Test: Consultar la mascota modificada por estatus - FAILED\n`;
                report += `Response Status: ${response.status}\n\n`;
            }
        });
    });

    after(() => {
        cy.request({
            method: 'DELETE',
            url: `${baseUrl}/pet/${petId}`,
            failOnStatusCode: false
        }).then((response) => {
            if (response.status === 200) {
                report += `Mascota con ID: ${petId} eliminada.\n`;
            } else {
                report += `Error al eliminar la mascota con ID: ${petId}. Response Status: ${response.status}\n\n`;
            }

            cy.writeFile(reportPath, report);
        });
    });
});
