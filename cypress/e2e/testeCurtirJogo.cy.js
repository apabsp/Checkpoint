describe('Curtir Jogo', () =>{
    it('Curtir Hades', () => {
        cy.visit('/')

        cy.get('[placeholder="Usuário"]').type("usuarioficticio")
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.get('.poppins-semibold').click()
        
        cy.get('.forms-container > .search > input').type('Hades')
        cy.wait(1500)
        cy.get('.search-button').click()

        cy.get('.game-name').invoke('text').should('have.string', "Hades")
        cy.wait(1500)
        cy.get('.game-name').click()

        cy.wait(1500)
        cy.get('#like').click();
        cy.wait(1500)
    })

    it('Descurtir Hades', () => {
        cy.visit('/')

        cy.get('[placeholder="Usuário"]').type("usuarioficticio")
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.get('.poppins-semibold').click()
        
        cy.get('.forms-container > .search > input').type('Hades')
        cy.wait(1500)
        cy.get('.search-button').click()

        cy.get('.game-name').invoke('text').should('have.string', "Hades")
        cy.wait(1500)
        cy.get('.game-name').click()

        cy.wait(1500)
        cy.get('#like').click();
        cy.wait(1500)
    })

})