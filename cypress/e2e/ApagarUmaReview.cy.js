describe('Apagar uma review de jogo', () => {
    it('Apagando uma review', () => {
        cy.visit('/')

        cy.get('[placeholder="Usuário"]').type("usuarioficticio")
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.wait(850)
        cy.get('.poppins-semibold').click()
        
        cy.get('.forms-container > .search > input').type('minecraft')
        cy.wait(850)
        cy.get('.search-button').click()

        cy.wait(850)
        cy.get('.game-name').click()
        cy.wait(850)
        cy.get('#addReview').click()
        cy.get('#texto').type("Esse jogo é legal!")
        cy.wait(850)
        cy.get('.review-modal > div > form > button').click()
        
        cy.wait(850)
        cy.get('#delete-review').click()

        cy.get('#addReview')
        cy.wait(850)
    })
})
