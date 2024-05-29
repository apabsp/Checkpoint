describe('Modificar uma review de jogo', () => {
    it('Modificando uma review', () => {
        cy.visit('/')

        cy.get('[placeholder="Usuário"]').type("usuarioficticio")
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.get('.poppins-semibold').click()
        
        cy.get('.forms-container > .search > input').type('minecraft')
        cy.wait(1500)
        cy.get('.search-button').click()


        cy.wait(1500)
        cy.get('.game-name').click()
        cy.wait(1500)
        cy.get('#addReview').click()
        cy.get('#texto').type("Esse jogo é legal!")
        cy.wait(1500)
        cy.get('.review-modal > div > form > button').click()

        cy.get('#edit-review').click()
        cy.wait(1500)
        cy.get('#review-text').clear()
        cy.get('#review-text').type("my new review")
        cy.wait(1500)
        cy.get('#save-edited-review').click()

        cy.get('.review').invoke('text').should("have.string", "my new review")
        
        cy.wait(1500)
        cy.get('#delete-review').click()

        cy.get('#addReview')
        cy.wait(1500)
        
    })
})