describe('Curtir Review', () => {
    it('Curtir uma review', () => {
        cy.visit('/')

        cy.get('[placeholder="Usuário"]').type("usuarioficticio2")
        cy.get('[placeholder="Senha"]').type('senhaficticia2')
        cy.get('.poppins-semibold').click()


        cy.get('.forms-container > .search > input').type('Valorant')
        cy.wait(1500)
        cy.get('.search-button').click()

        cy.wait(1500)
        cy.get('.game-name').click()
        cy.wait(1500)
        cy.get('#addReview').click()
        
        cy.get('#texto').type("Jogo bacana")
        cy.wait(1500)
        cy.get('.review-modal > div > form > button').click()
        
        cy.wait(1500)
        cy.get('.actions > .logout').click()

        ///////////////////////////////////////////////////////////////////////////////////
        cy.get('[placeholder="Usuário"]').type("usuarioficticio")
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.wait(1500)
        cy.get('.poppins-semibold').click()

        cy.get('.forms-container > .search > input').type('Valorant')
        cy.wait(1500)
        cy.get('.search-button').click()
        cy.wait(1500)
        cy.get('.game-name').click()
        cy.wait(1500)

        cy.get('.user-review-link').click()

        cy.get('#like-review').click()

        cy.wait(1500)
        cy.get('.actions > .logout').click()

    })

    it('Descurtir uma review', () => {
        cy.visit('/')

        cy.get('[placeholder="Usuário"]').type("usuarioficticio")
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.wait(1500)
        cy.get('.poppins-semibold').click()

        cy.get('.forms-container > .search > input').type('Valorant')
        cy.wait(1500)
        cy.get('.search-button').click()
        cy.wait(1500)
        cy.get('.game-name').click()
        cy.wait(1500)

        cy.get('.user-review-link').click()

        cy.get('#like-review').click()

        cy.wait(1500)
        cy.get('.actions > .logout').click()

    })
})



