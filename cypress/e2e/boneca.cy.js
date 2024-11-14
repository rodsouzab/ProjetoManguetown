describe('Cadastro, alocação e Remoção de Boneca', () => {
    const cpf = '88099122199';  // CPF para verificar e excluir
    
    beforeEach(() => {
        // Realiza o login uma vez para economizar tempo nos testes
        cy.visit('/');
        cy.get('#username').type('admin');
        cy.get('#password').type('123123');
        cy.get('.login_btn').click();
    });
    
    it('Deve cadastrar um novo colaborador e cadastrar uma nova boneca alocada a ele', () => {
  
      // Acessa a página de gestão de colaboradores
      cy.visit('/gestao_colaboradores');
    
        // Verifica a presença do CPF no corpo da página
        cy.get('body').then((body) => {
        if (body.text().includes(cpf)) {
        // Se o CPF existir, realiza a exclusão
        cy.contains(cpf)
            .parents('tr') // Encontra a linha da tabela
            .find('.action-select') // Encontra o dropdown de ações
            .select('excluir'); // Seleciona a ação "Excluir"
        
        // Confirma o alerta de exclusão
        cy.on('window:confirm', (text) => {
            expect(text).to.contains('Tem certeza de que deseja excluir este colaborador?');
            return true; // Confirma a exclusão
        });
        
        // Verifica se o CPF foi excluído
        cy.contains(cpf).should('not.exist');
    }
    });
  
      // Clica no botão "Cadastrar novo Colaborador"
      cy.contains('Cadastrar novo Colaborador').click();
  
      // Verifica se a página de cadastro foi carregada
      cy.url().should('include', '/cadastrar_colaborador');
    
      // Preenche o formulário com dados fictícios
      cy.get('#nome').type('Colaborador Boneca');
      cy.get('#cpf').type(cpf); // Usa o novo CPF
      cy.get('#data_nascimento').type('1980-05-27');
      cy.get('#lugar_onde_mora').type('Casa Amarela');
      cy.get('#renda').type('1500.00');
      cy.get('#situacoes_de_vulnerabilidade').type('Nenhuma');
      cy.get('#quantos_filhos').type('2');
      cy.get('#quantas_pessoas_moram_com_voce').type('4');
      cy.get('#habilidades').type('Costura Intermediária');
    
      // Envia o formulário
      cy.get('button[type="submit"]').click();
    
      // Verifica se o redirecionamento ocorreu e voltou para a página de gestão
      cy.url().should('include', '/gestao_colaboradores');
    
      // Verifica se o colaborador está na lista de colaboradores com o novo CPF
      cy.contains('Colaborador Boneca').should('be.visible');
      cy.contains(cpf).should('be.visible');
      cy.contains('27 de Maio de 1980').should('be.visible');
      cy.contains('Casa Amarela').should('be.visible');
      cy.contains('1500,00').should('be.visible');
      cy.contains('Nenhuma').should('be.visible');
      cy.contains('2').should('be.visible');
      cy.contains('4').should('be.visible');
      cy.contains('Costura Intermediária').should('be.visible');

      // Acessa a página de gestão de bonecas
      cy.visit('/gestao_bonecas');

      // Verifica a presença do nome da boneca no corpo da página
      cy.get('body').then((body) => {
        if (body.text().includes('Boneca Cypress de Pano')) {
        // Se o nome
        cy.contains('Boneca Cypress de Pano')
            .parents('tr') // Encontra a linha da tabela
            .find('button[type="submit"]') // Encontra o dropdown de ações
            .click(); // Seleciona a ação "Excluir"
        
        // Confirma o alerta de exclusão
        cy.on('window:confirm', (text) => {
            expect(text).to.contains('Tem certeza de que deseja excluir esta boneca?');
            return true; // Confirma a exclusão
        });
        
        // Verifica se o CPF foi excluído
        cy.contains('Boneca Cypress de Pano').should('not.exist');
    }
    });
      
      // Clica no botão "Cadastrar nova Boneca"
      cy.contains('Cadastrar nova Boneca').click();
  
      // Verifica se a página de cadastro foi carregada
      cy.url().should('include', '/cadastrar_boneca');

      cy.get('#nome_boneca').type('Boneca Cypress de Pano');

      cy.get('#nivel_dificuldade').type('Muito Difícil');
      cy.get('#colaborador_id').select('Colaborador Boneca');

      // Envia o formulário
      cy.get('button[type="submit"]').click();

      // Verifica se o redirecionamento ocorreu e voltou para a página de gestão
      cy.url().should('include', '/gestao_bonecas');

      // Verifica se o colaborador está na lista de colaboradores com o novo CPF
      cy.contains('Boneca Cypress de Pano').should('be.visible');
      cy.contains('Muito Difícil').should('be.visible');
      cy.contains('Colaborador Boneca').should('be.visible');
    });

    it('Deve cadastrar e excluir uma nova boneca', () => {
        // Acessa a página de gestão de bonecas
      cy.visit('/gestao_bonecas');

      // Verifica a presença do nome da boneca no corpo da página
      cy.get('body').then((body) => {
        if (body.text().includes('Boneca Cypress de Pano 2')) {
        // Se o nome
        cy.contains('Boneca Cypress de Pano 2')
            .parents('tr') // Encontra a linha da tabela
            .find('button[type="submit"]') // Encontra o dropdown de ações
            .click(); // Seleciona a ação "Excluir"
        
        // Confirma o alerta de exclusão
        cy.on('window:confirm', (text) => {
            expect(text).to.contains('Tem certeza de que deseja excluir esta boneca?');
            return true; // Confirma a exclusão
        });
        
        // Verifica se o CPF foi excluído
        cy.contains('Boneca Cypress de Pano 2').should('not.exist');
    }
    });
      
      // Clica no botão "Cadastrar nova Boneca"
      cy.contains('Cadastrar nova Boneca').click();
  
      // Verifica se a página de cadastro foi carregada
      cy.url().should('include', '/cadastrar_boneca');

      cy.get('#nome_boneca').type('Boneca Cypress de Pano 2');
      cy.get('#nivel_dificuldade').type('Fácil');
      cy.get('#colaborador_id').select('Colaborador Boneca');

      // Envia o formulário
      cy.get('button[type="submit"]').click();

      // Verifica se o redirecionamento ocorreu e voltou para a página de gestão
      cy.url().should('include', '/gestao_bonecas');

      // Verifica se o colaborador está na lista de colaboradores com o novo CPF
      cy.contains('Boneca Cypress de Pano 2').should('be.visible');
      cy.contains('Fácil').should('be.visible');
      cy.contains('Colaborador Boneca').should('be.visible');

      // Verifica a presença do CPF no corpo da página
      cy.get('body').then((body) => {
        if (body.text().includes('Boneca Cypress de Pano 2')) {
        // Se o CPF existir, realiza a edição
        cy.contains('Boneca Cypress de Pano 2')
            .parents('tr') // Encontra a linha da tabela
            .find('button[type="submit"]') // Encontra o botão de excluir
            .click(); // Seleciona a ação "Excluir"

        }

        cy.contains('Boneca Cypress de Pano 2').should('not.exist');

        // Verifica se o sistema exibe uma mensagem de confirmacao
        cy.contains('Boneca excluída com sucesso!').should('be.visible');
      });
    });

    it('Deve remover uma boneca ao remover seu respectivo colaborador', () => {
      // Recarrega a página de gestão de colaboradores antes de tentar novo cadastro
      cy.visit('/gestao_colaboradores');

      // Verifica a presença do CPF no corpo da página
      cy.get('body').then((body) => {
        if (body.text().includes(cpf)) {
        // Se o CPF existir, realiza a edição
        cy.contains(cpf)
            .parents('tr') // Encontra a linha da tabela
            .find('.action-select') // Encontra o dropdown de ações
            .select('excluir'); // Seleciona a ação "Excluir"

        }
      });

      // Confirma o alerta de exclusão
      cy.on('window:confirm', (text) => {
        expect(text).to.contains('Tem certeza de que deseja excluir este colaborador?');
        return true; // Confirma a exclusão
      });
    
      // Verifica se o CPF foi excluído
      cy.contains(cpf).should('not.exist');

    // Verifica se o sistema exibe uma mensagem de confirmacao
    cy.contains('Colaborador excluído com sucesso!').should('be.visible'); // Ajuste a mensagem conforme o retorno do seu sistema

    // Acessa a página de gestão de bonecas
    cy.visit('/gestao_bonecas');

    //Confere se a boneca de pano respectiva foi excluída
    cy.contains('Boneca Cypress de Pano 2').should('not.exist');
  
  });
  });
  