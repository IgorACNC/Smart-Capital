describe('test suite 1', () => {
    
    it('cenario1', () => {
        cy.visit('/');
        cy.get('[href="/login/"]').click()
        cy.get('#username').click()
        cy.get('#username').type('igor')
        cy.get('#password').type('123')
        cy.wait(1000)
        cy.get('button').click()
        cy.get('.menu-icon').click()
        cy.wait(2000)
        cy.get('[href="/simulacao/adicionar/"]').click()
        cy.get('#valor_investimento').click()
        cy.get('#valor_investimento').type('1000')
        cy.get('#periodo_investimento').click()
        cy.get('#periodo_investimento').type('12')
        cy.get('#perfil_risco').select(['Baixo'])
        cy.wait(2000)
        cy.get('button').click()
        cy.wait(2000)
        cy.get('.button-link').click()

    })

    it('cenario2', () => {
        cy.visit('/');
        cy.get('[href="/login/"]').click()
        cy.get('#username').click()
        cy.get('#username').type('igor')
        cy.get('#password').type('123')
        cy.wait(1000)
        cy.get('button').click()
        cy.get('.menu-icon').click()
        cy.wait(2000)
        cy.get('[href="/simulacao/adicionar/"]').click()
        cy.get('#valor_investimento').click()
        cy.get('#valor_investimento').type('1000')
        cy.get('#periodo_investimento').click()
        cy.get('#periodo_investimento').type('12')
        cy.get('#perfil_risco').select(['Baixo'])
        cy.wait(2000)
        cy.get('button').click()
        cy.wait(2000)
        cy.get('.button-link').click()

    })
})