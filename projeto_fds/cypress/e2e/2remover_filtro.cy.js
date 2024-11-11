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
        cy.get('[href="/controle_gastos/visualizar/"]').click()
        cy.wait(4000)
        cy.get('[href="/controle_gastos/adicionar/"]').click()
        cy.get('#descricao').click()
        cy.get('#descricao').type('Iphone')
        cy.get('#valor').click()
        cy.get('#valor').type('20000')
        cy.get('#data').invoke('val', '2024-10-21').trigger('change')
        cy.get('button').click()
        cy.wait(5000)
        cy.get('.select_filter').select(['Eletrônico'])
        cy.wait(4000)
        cy.get('.filter_button').click()
        cy.wait(5000)
        cy.wait(3000)
        cy.get('[href="/controle_gastos/adicionar/"]').click()
        cy.get('#descricao').click()
        cy.get('#descricao').type('Carregador')
        cy.get('#valor').click()
        cy.get('#valor').type('50')
        cy.get('#data').invoke('val', '2024-11-09').trigger('change')
        cy.get('button').click()
        cy.wait(5000)
        cy.get('.select_filter').select(['Eletrônico'])
        cy.wait(4000)
        cy.get('.filter_button').click()
        cy.wait(5000)
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
        cy.visit('/admin');
        cy.get('#id_username').click()
        cy.get('#id_username').type('iacnc')
        cy.get('#id_password').click()
        cy.get('#id_password').type('123')
        cy.get('.submit-row > input').click()
        cy.get('#auth-user > a').click()
        cy.get(':nth-child(2) > .field-username > a').click()
        cy.get('.deletelink').click()
        cy.get('div > [type="submit"]').click()
    })
})