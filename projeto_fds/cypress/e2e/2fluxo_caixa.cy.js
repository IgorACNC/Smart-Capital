describe('test suite 1', () => {
    
    it('cenario1', () => {
        cy.visit('/');
        cy.get('[href="/cadastro/"]').click()
        cy.get('#username').click()
        cy.get('#username').type('igor')
        cy.get('#email').click()
        cy.get('#email').type('igor@cesar.school')
        cy.get('#password1').click()
        cy.get('#password1').type('123')
        cy.get('#password2').click()
        cy.get('#password2').type('123')
        cy.get('#numero_telefone').click()
        cy.get('#numero_telefone').type('81971081092')
        cy.get('#estado').select(['Pernambuco'])
        cy.get('button').click()
        cy.get('#username').click()
        cy.get('#username').type('igor')
        cy.get('#password').type('123')
        cy.get('button').click()
        cy.visit('/');
        cy.get('[href="/login/"]').click()
        cy.get('#username').click()
        cy.get('#username').type('igor')
        cy.get('#password').type('123')
        cy.get('button').click()
        cy.wait(3000)
        cy.get('.menu-icon').click()
        cy.wait(3000)
        cy.get('[href="/fluxo-caixa/calculo/"]').click()
        cy.wait(2000)
        cy.get('[type="text"]').click()
        cy.get('[type="text"]').type('Fevereiro')
        cy.wait(2000)
        cy.get('[name="ebit"]').click()
        cy.get('[name="ebit"]').type('1000')
        cy.wait(2000)
        cy.get('[name="ir"]').click()
        cy.get('[name="ir"]').type('10')
        cy.wait(2000)
        cy.get('[name="depreciacao"]').click()
        cy.get('[name="depreciacao"]').type('50')
        cy.wait(2000)
        cy.get('[name="receita_total"]').click()
        cy.get('[name="receita_total"]').type('1000')
        cy.wait(2000)
        cy.get('[name="despesa_total"]').click()
        cy.get('[name="despesa_total"]').type('3000')
        cy.wait(2000)
        cy.get('button').click()
        cy.wait(5000)
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
        cy.get('[href="/fluxo-caixa/calculo/"]').click()
        cy.wait(2000)
        cy.get('.link-historico > a').click()
        cy.wait(5000)
    })  
})