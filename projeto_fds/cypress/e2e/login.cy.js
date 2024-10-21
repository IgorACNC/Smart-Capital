describe('test suite Cadastro', () => {
    it('Cadastro com sucesso', () => {
        cy.visit('/');
        cy.get('.login').click()
        cy.get('#email_create').type('asdadhjjmktvvsdasde@gmail.com')
        cy.get('#SubmitCreate > span').click()
        cy.get('#id_gender2').click()
        cy.get('#customer_firstname').type('Test')
        cy.get('#customer_lastname').type('User')
        cy.get('#passwd').type('32415')
        cy.get('#submitAccount > span').click()
        cy.get('.alert').invoke('text').should('have.string', "Your account has been created")
    })
    it('Login com sucesso', () => {
        cy.visit('/');
        cy.get('.login').click()
        cy.get('#email').type('ldigbeukge@gmail.com')
        cy.get('#passwd').type('32415')
        cy.get('#SubmitLogin > span').click()
        cy.get('.account > span').invoke('text').should('have.string', "Test User")
    })
  })