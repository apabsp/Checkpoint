describe('Avaliar estrelas', () =>{
    it('Avaliar Stardew Valley 3 Estrelas', () => {
        cy.visit('/')

        cy.get('[placeholder="Usuário"]').type("usuarioficticio")
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.get('.poppins-semibold').click()
        
        cy.get('.forms-container > .search > input').type('Stardew Valley')
        cy.wait(1500)
        cy.get('.search-button').click()

        cy.get('.game-name').invoke('text').should('have.string', "Stardew Valley")
        cy.wait(1500)
        cy.get('.game-name').click()

        cy.wait(1500)
        cy.get('label[title="3 stars"]').click();
        cy.wait(1500)
    })

    it('Avaliar Stardew Valley 1 estrela', () => {
        cy.visit('/')

        cy.get('[placeholder="Usuário"]').type("usuarioficticio")
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.get('.poppins-semibold').click()
        
        cy.get('.forms-container > .search > input').type('Stardew Valley')
        cy.wait(1500)
        cy.get('.search-button').click()

        cy.get('.game-name').invoke('text').should('have.string', "Stardew Valley")
        cy.wait(1500)
        cy.get('.game-name').click()

        cy.wait(1500)
        cy.get('label[title="1 star"]').click();
        cy.wait(1500)
    })
})
