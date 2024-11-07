# Guia de Contribuição

Bem-vindo ao **Smart Capital**! Estamos entusiasmados em tê-lo como colaborador e ansiosos para trabalhar juntos para melhorar este projeto.

## Índice

- [Código de Conduta](#código-de-conduta)
- [Como Posso Contribuir?](#como-posso-contribuir)
  - [Relatando Bugs](#relatando-bugs)
  - [Corrigindo Bugs](#corrigindo-bugs)
  - [Sugerindo Melhorias](#sugerindo-melhorias)
- [Fluxo de Trabalho de Desenvolvimento](#fluxo-de-trabalho-de-desenvolvimento)
  - [Configurando o Ambiente](#configurando-o-ambiente)
  - [Padrões de Código e Guia de Estilo](#padrões-de-código-e-guia-de-estilo)
  - [Testes](#testes)
- [Submetendo Alterações](#submetendo-alterações)
  - [Pull Requests](#pull-requests)
- [Recursos Úteis](#recursos-úteis)
- [Agradecimentos](#agradecimentos)
- [Contato e Ajuda](#contato-e-ajuda)

## Código de Conduta

Por favor, leia o nosso [Código de Conduta](./CODE_OF_CONDUCT.md) para entender as expectativas em termos de comportamento ao participar deste projeto.

## Como Posso Contribuir?

### Relatando Bugs

Encontrou um bug? Ajude-nos a melhorá-lo:

- **Verifique** se o bug já foi relatado [aqui](https://github.com/IgorACNC/Smart-Capital/issues).
- **Abra** uma nova *issue* com o título **"Bug: [Descrição do Bug]"**.
- **Inclua**:
  - Passos para reproduzir o problema.
  - Comportamento esperado versus o atual.
  - Capturas de tela ou logs relevantes.

Modelo de relatório de bug: [Bug Report Template](./.github/ISSUE_TEMPLATE/bug_report.md)

### Corrigindo Bugs

Quer ajudar a corrigir um bug?

- **Comente** na *issue* do bug que você está trabalhando nele.
- **Siga** as [Padrões de Código e Guia de Estilo](#padrões-de-código-e-guia-de-estilo).
- **Envie** um *pull request* vinculado à *issue* correspondente.

### Sugerindo Melhorias

Tem uma ideia para melhorar o projeto?

- **Verifique** se a sugestão já foi feita [aqui](https://github.com/IgorACNC/Smart-Capital/issues).
- **Abra** uma nova *issue* com o título **"Sugestão: [Descrição da Sugestão]"**.
- **Descreva** detalhadamente a sua ideia e os benefícios esperados.

Modelo de sugestão de melhoria: [Feature Request Template](./.github/ISSUE_TEMPLATE/feature_request.md)

## Fluxo de Trabalho de Desenvolvimento

### Configurando o Ambiente

1. **Faça um fork** do repositório.
2. **Clone** o seu fork:

   ```bash
   git clone https://github.com/seu-usuario/Smart-Capital.git
   ```

3. **Instale** as dependências:

   ```bash
   npm install
   ```

4. **Configure** as variáveis de ambiente necessárias.

### Padrões de Código e Guia de Estilo

- **Linting**: Utilize o [ESLint](https://eslint.org/) com as configurações do projeto.
- **Indentação**: 2 espaços.
- **Nomenclatura**: Use nomes claros e descritivos para variáveis e funções.
- **Comentários**: Adicione comentários para explicar funcionalidades complexas.
- **Commits**:
  - Use o tempo presente (ex.: "Adiciona função de login").
  - Limite a primeira linha a 72 caracteres.
  - Referencie *issues* e *pull requests* quando aplicável.
  - Emojis são bem-vindos! 🎉

Exemplos de commits:

- `feat: Adiciona funcionalidade de cadastro de usuários`
- `fix: Corrige erro na validação de email`

### Testes

- **Escreva** testes unitários para novas funcionalidades usando [Jest](https://jestjs.io/).
- **Execute** os testes antes de submeter:

  ```bash
  npm test
  ```

## Submetendo Alterações

### Pull Requests

1. **Atualize** o seu fork com a branch principal:

   ```bash
   git checkout main
   git pull upstream main
   ```

2. **Crie** uma nova branch:

   ```bash
   git checkout -b minha-nova-funcionalidade
   ```

3. **Faça commit** das suas alterações seguindo o [Guia de Estilo](#padrões-de-código-e-guia-de-estilo).

4. **Envie** a branch para o seu fork:

   ```bash
   git push origin minha-nova-funcionalidade
   ```

5. **Abra** um *pull request*:

   - Descreva as mudanças propostas.
   - Referencie *issues* relacionadas.
   - Aguarde por feedback; respondemos em até **3 dias úteis**.

## Recursos Úteis

- **Issues**: [Lista de Issues](https://github.com/IgorACNC/Smart-Capital/issues)
- **Modelos**:
  - [Relatório de Bug](./.github/ISSUE_TEMPLATE/bug_report.md)
  - [Solicitação de Funcionalidade](./.github/ISSUE_TEMPLATE/feature_request.md)

## Agradecimentos

Obrigado por dedicar seu tempo para contribuir para o **Smart Capital**. Suas contribuições são valiosas e ajudam a melhorar o projeto para todos os usuários.

## Contato e Ajuda

- **E-mail**: [iacnc@gmail.com](mailto:iacnc@gmail.com)
- **GitHub**: [@IgorACNC](https://github.com/IgorACNC)

---

Estamos aqui para ajudar. Se você tiver dúvidas ou precisar de assistência, não hesite em entrar em contato!
