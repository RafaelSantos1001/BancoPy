Documentação do Programa de Agência Bancária - Dektos Bank
Este é um programa de agência bancária simples chamado "Dektos Bank" desenvolvido em Python. O programa permite a criação de contas de clientes, bem como a realização de saques, depósitos e transferências.

Estrutura do Projeto
O projeto é dividido em três arquivos principais: banco.py, cliente.py e conta.py. Cada arquivo contém classes e funções específicas para a implementação das funcionalidades da agência bancária.

banco.py
Este arquivo contém a lógica principal do programa. Ele define um menu interativo que permite ao usuário escolher várias opções, como criar uma nova conta, efetuar saques, depósitos e transferências, listar contas existentes e sair do sistema.

cliente.py
O arquivo cliente.py define a classe Cliente, que representa os dados de um cliente do banco. A classe possui propriedades para armazenar informações como código, nome, e-mail, CPF, data de nascimento e data de cadastro do cliente.

conta.py
O arquivo conta.py define a classe Conta, que representa uma conta bancária associada a um cliente. A classe possui propriedades para armazenar informações como número da conta, cliente, saldo, limite e saldo total (considerando saldo e limite). Também possui métodos para realizar depósitos, saques e transferências.

Como Executar
Certifique-se de ter o Python instalado em seu sistema.
Faça o download dos arquivos do projeto.
Abra o terminal e navegue até o diretório onde os arquivos estão localizados.
Execute o seguinte comando para iniciar o programa:
bash
Copy code
python banco.py
Funcionalidades
O programa oferece as seguintes funcionalidades:

Criar Conta: Permite a criação de uma nova conta associada a um cliente. São solicitadas informações como nome, e-mail, CPF e data de nascimento do cliente.

Efetuar Saque: Permite realizar saques de uma conta especificada. (A ser implementado)

Efetuar Depósito: Permite realizar depósitos em uma conta especificada. (A ser implementado)

Efetuar Transferência: Permite realizar transferências entre contas. (A ser implementado)

Listar Contas: Exibe uma lista das contas existentes. (A ser implementado)

Como Contribuir
Se você deseja contribuir para este projeto, siga as etapas abaixo:

Faça um fork deste repositório.
Crie um branch para sua nova funcionalidade (git checkout -b nova-funcionalidade).
Implemente suas alterações.
Commit suas mudanças (git commit -m 'Adicionada nova funcionalidade').
Push para o branch (git push origin nova-funcionalidade).
Abra um pull request descrevendo suas alterações.
Autor
Seu Nome

Licença
Este projeto é licenciado sob a Licença XYZ.

Este é um projeto simples desenvolvido para fins de aprendizado e prática em programação. Fique à vontade para explorar, modificar e contribuir para o projeto! Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato.
