describe('Editar Perfil', () =>{
    it('Colocar foto de perfil', () => {
        cy.visit('/')

        cy.get('[placeholder="Usuário"]').type("usuarioficticio")
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.get('.poppins-semibold').click()

        cy.get('.profile').click();
        cy.wait(1500)

        cy.get('#image-profile').click();
        cy.wait(1500)        

        cy.get('#url').type('https://i.pinimg.com/564x/a3/0f/bc/a30fbc226ee503d291750a45a4dda359.jpg')
        cy.wait(1500)
        cy.get('.save-button').click()
    })

    it('Remover foto de perfil', () => {
        cy.visit('/')

        cy.get('[placeholder="Usuário"]').type("usuarioficticio")
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.get('.poppins-semibold').click()

        cy.get('.profile').click();
        cy.wait(1500)

        cy.get('#image-profile').click();
        cy.wait(1500)        

        cy.get('.save-button').click()
        cy.wait(1500)    
    })

})