describe('test suite 1', () => {
    
    it('cenario1', () => {
        cy.visit('/');
        cy.get('[href="/login/"]').click()
        cy.get('#username').click()
        cy.get('#username').type('igor')
        cy.get('#password').type('123')
        cy.get('button').click()
        cy.wait(3000)
        cy.get('.menu-icon').click()
        cy.wait(3000)
        cy.get('[href="/controle_gastos/visualizar/"]').click()
        cy.wait(4000)
        cy.get(':nth-child(1) > form > button').click()
        cy.wait(10000)
    })
    
    it('cenario2', () => {
        cy.visit('/');
        cy.get('[href="/login/"]').click()
        cy.get('#username').click()
        cy.get('#username').type('igor')
        cy.get('#password').type('123')
        cy.get('button').click()
        cy.wait(3000)
        cy.get('.menu-icon').click()
        cy.wait(3000)
        cy.get('[href="/controle_gastos/visualizar/"]').click()
        cy.wait(4000)
        cy.get(':nth-child(2) > form > a > .fa-solid').click()
        cy.wait(2000)
        cy.get('.excluir').click()
        cy.wait(5000)
    })
})