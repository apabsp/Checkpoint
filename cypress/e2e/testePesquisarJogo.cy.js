describe('Pesquisar por um jogo', () => {
    it('Pesquisando por left 4 dead', () => {
        cy.visit('/')

        cy.get('[placeholder="Usuário"]').type("usuarioficticio")
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.get('.poppins-semibold').click()
        
        cy.get('.forms-container > .search > input').type('left 4 dead')
        cy.wait(1500)
        cy.get('.search-button').click()

        cy.get('.game-name').invoke('text').should('have.string', "Left 4 Dead 2")
        cy.wait(1500)
        cy.get('.game-name').click()
        cy.wait(1500)
    })
})