describe('test suite Login', () => {
    it('Entrou no site com sucesso', () =>{
        cy.visit('/');
        
    })
    it('Clicou em sign in', () => {
        cy.visit('/');
        cy.get('.login');

    })


})