describe('Criar uma review de jogo', () => {
    it('Criando uma review', () => {
        cy.visit('/')

        cy.get('[placeholder="Usuário"]').type("usuarioficticio")
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.get('.poppins-semibold').click()
        
        cy.get('.forms-container > .search > input').type('left 4 dead')
        cy.wait(850)
        cy.get('.search-button').click()

        cy.wait(850)
        cy.get('.game-name').click()
        cy.wait(850)
        cy.get('#addReview').click()

        cy.get('#texto').type("Esse jogo é legal!")
        cy.wait(850)
        cy.get('.review-modal > div > form > button').click()

        cy.get('#review-text').invoke('val').should("have.string", "Esse jogo é legal!")
        cy.wait(850)
        cy.get('#delete-review').click()
        cy.wait(850)
    })
})
