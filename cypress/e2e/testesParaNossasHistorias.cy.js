//Eu como usuário gostariar de avaliar (0-5 estrelas) os jogos disponíveis. 

describe('Sign up e Sign in', () =>{
    it('Entrou no site com sucesso', () =>{

        cy.visit('/')
    })
    it('Criou uma conta', () =>{
        cy.visit('/')
        cy.get('.link').click()
        cy.get('[placeholder="Usuário"]').type('usuarioficticio')
        cy.get('[placeholder="Email"]').type('emailficticio@email.com')
        cy.get('[placeholder="Senha"]').type('senhaficticia')
        cy.get('[placeholder="Confirme a Senha"]').type('senhaficticia')
        cy.get('.poppins-semibold').click()
        cy.get('h1').should('have.string', "Login")
    })
    

})