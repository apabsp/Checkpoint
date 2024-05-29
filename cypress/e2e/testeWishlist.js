describe('Wishlist', () =>{
    it('Adicionar Gris a wishlist', () => {
        cy.visit('/')

        cy.get('[placeholder="Usuário"]').type("usuarioficticio")
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.get('.poppins-semibold').click()
        
        cy.get('.forms-container > .search > input').type('Gris')
        cy.wait(1500)
        cy.get('.search-button').click()

        cy.wait(1500)
        cy.get('.add-wishlist').click();
        cy.wait(1500)
    })

    it('Remover Gris da wishlist', () => {
        cy.visit('/')

        cy.get('[placeholder="Usuário"]').type("usuarioficticio")
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.get('.poppins-semibold').click()
        
        cy.get('.forms-container > .search > input').type('Gris')
        cy.wait(1500)
        cy.get('.search-button').click()

        cy.get('.game-name').invoke('text').should('have.string', "Gris")
        cy.wait(1500)
        cy.get('.game-name').click()

        cy.wait(1500)
        cy.get('.remove-wishlist').click();
        cy.wait(1500)
    })

})