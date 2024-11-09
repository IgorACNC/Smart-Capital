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
        cy.wait(4000)
        cy.get('[href="/controle_gastos/visualizar/"]').click()
        cy.wait(3000)
        cy.get(':nth-child(1) > form > a > .fa-solid').click()
        cy.get('button').click()
        cy.wait(5000)
        cy.get('.fa-solid').click()
        cy.get('button').click()
        cy.wait(5000)
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
        cy.wait(4000)
        cy.get('[href="/controle_gastos/visualizar/"]').click()
        cy.wait(3000)
        cy.get('[href="/controle_gastos/adicionar/"]').click()
        cy.get('#descricao').click()
        cy.get('#descricao').type('Hamburguer')
        cy.get('#valor').click()
        cy.get('#valor').type('20')
        cy.get('#data').invoke('val', '2024-09-20').trigger('change')
        cy.get('button').click()
        cy.wait(4000)
        cy.get('[href="/controle_gastos/adicionar/"]').click()
        cy.get('#descricao').click()
        cy.get('#descricao').type('Hamburguer')
        cy.get('#valor').click()
        cy.get('#valor').type('20')
        cy.get('#data').invoke('val', '2024-09-20').trigger('change')
        cy.get('button').click()
        cy.wait(4000)
        cy.get(':nth-child(1) > form > a > .fa-solid').click()
        cy.get('button').click()
        cy.wait(5000)
    })
})