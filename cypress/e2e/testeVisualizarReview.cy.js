describe('Visualizar Review', () => {
    it('Visualizando Review de outro usuário', () => {
        cy.visit('/')

        cy.get('[placeholder="Usuário"]').type("usuarioficticio2")
        cy.get('[placeholder="Senha"]').type('senhaficticia2')
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
        
        cy.wait(1500)
        cy.get('.actions > .logout').click()

        cy.get('[placeholder="Usuário"]').type("usuarioficticio")
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.wait(1500)
        cy.get('.poppins-semibold').click()

        cy.get('.forms-container > .search > input').type('minecraft')
        cy.wait(1500)
        cy.get('.search-button').click()
        cy.wait(1500)
        cy.get('.game-name').click()
        cy.wait(1500)

        cy.get('.user-review-link').click()

        cy.get('.review').invoke('text').should("have.string", "Esse jogo é legal!")

        cy.wait(1500)
        cy.get('.actions > .logout').click()

    
        cy.get('[placeholder="Usuário"]').type("usuarioficticio2")
        cy.get('[placeholder="Senha"]').type('senhaficticia2')
        cy.wait(1500)
        cy.get('.poppins-semibold').click()

        cy.wait(1500)
        cy.get('.forms-container > .search > input').type('minecraft')
        cy.wait(1500)
        cy.get('.search-button').click()
        cy.wait(1500)
        cy.get('.game-name').click()
        cy.wait(1500)
        cy.get('#view-my-review').click()
        cy.wait(1500)
        cy.get('#delete-review').click()
        cy.wait(1500)
    })

    

})



