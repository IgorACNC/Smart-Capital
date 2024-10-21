describe('test suite 1', () => {
    it('cenario1', () => {
        cy.visit('/');
        cy.get('[href="/login/"]').click()
        cy.get('#username').click()
        cy.get('#username').type('iacnc')
        cy.get('#password').type('123')
        cy.get('button').click()
        cy.get('.menu-icon').click()
        cy.get('[href="/imposto_renda/calculo/"]').click()
        cy.get('#nome').type('igor')
        cy.get('#renda_anual').type('25000')
        cy.get('[type="submit"]').click()
    })
})