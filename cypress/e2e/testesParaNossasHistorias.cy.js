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


//Eu como usuário gostaria de pesquisar por um jogo
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

//Eu como usuário típico gostariar de apagar uma review já criada.
describe('Criar uma review de jogo', () => {
    it('Criando uma review', () => {
        cy.visit('/')

        cy.get('[placeholder="Usuário"]').type("usuarioficticio")
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.get('.poppins-semibold').click()
        
        cy.get('.forms-container > .search > input').type('left 4 dead')
        cy.wait(1500)
        cy.get('.search-button').click()

        cy.wait(1500)
        cy.get('.game-name').click()
        cy.wait(1500)
        cy.get('#addReview').click()

        cy.get('#texto').type("Esse jogo é legal!")
        cy.wait(1500)
        cy.get('.review-modal > div > form > button').click()

        cy.get('#review-text').invoke('val').should("have.string", "Esse jogo é legal!")
        cy.wait(1500)
        cy.get('#delete-review').click()
        cy.wait(1500)
    })
})

describe('Apagar uma review de jogo', () => {
    it('Apagando uma review', () => {
        cy.visit('/')

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
        cy.get('#addReview').click()
        cy.get('#texto').type("Esse jogo é legal!")
        cy.wait(1500)
        cy.get('.review-modal > div > form > button').click()
        
        cy.wait(1500)
        cy.get('#delete-review').click()

        cy.get('#addReview')
        cy.wait(1500)
    })
})

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
        cy.get('#review-text').type("my new review")
        cy.wait(1500)
        cy.get('#edit-review').click()

        cy.get('#review-text').invoke('val').should("have.string", "my new review")
        
        cy.wait(1500)
        cy.get('#delete-review').click()

        cy.get('#addReview')
        cy.wait(1500)
        
    })
})

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

        cy.get('#review-text').invoke('val').should("have.string", "Esse jogo é legal!")

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



