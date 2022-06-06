# Teste de Admissão Bluestorm

Este código é parte do processo de admissão da empresa Bluestorm. A base dos requirementos era criar uma simples API
capaz de disponibilizar os dados de pacientes, farmácias e transações obtidos de um banco de dados pré existente.
Os endpoints deveriam estar protegidos por alguma forma de autencação.

## Implementação

 - Para criação da API foi utilizado o framework FastAPI devido a facilidade e velocidade em se criar APIs.
 - Todos os endpoints possuem validação dos tipos de dados a serem recebidos através do validação 
da biblioteca Pydantic.
 - Toda interação com banco de dados é feita através da ORM SQLAlchemy.
 - Como forma de autentiação protegendo todos os endpoints foi escolhido o método OAuth2, há um usuário já previamente
armazenado no banco de dados de senha e usuário dados respectivamente por: "admin" e "Aa!!1111".
 - Os enpoints que retornam dados dos bancos de dados podem se utilizar de query strings para filtrar de diferentes
formas o resultado. Mais detalhes na documentação OpenAPI.
 - Os padrões e estilos de código são garantidos através da ferramentas ativadas antes dos commits do Git. Entre elas há
processo de formatação, checagem de erros, checagem de tipagem adequada etc, otimização de dockerfiles etc.
 - Para a instalação de dependências foi utilizado o Poetry devido a ser mais vantajoso e simples de usar que o Pip.
 - O código utilza tipagem em todos os lugares.
 - Há comandos customizados utilizando o Makefile para facilitar acionamento de testes automáticos e utilização local
do serviço.
 - Docker e docker-compose são utilizados para execução local do projeto e consistência no deploy.
 - O código possui testes automatizados de aceitação. Testes de aceitação são testes de ponta a ponta que testam o 
comportamento esperado da aplicação.

## Design

A aplicação possui 4 camadas que são a principío independentes, porém são conectadas através do sistema de
dependências do FastAPI. Este modelo de camda é bem famoso e usado em outros frameworks como NestJS:
- Modules: São ocmponentes macroscópicos do sistema que tentam mapear os domínios da regra de negócio. Eles separam as
funcionalidades de diferentes partes do sistema para aumentar a organização.
 - Controllers: São os Gateways da aplicação e tem a responsabilidade de validar a entrada e saída ou lidar com alguma
lógica específica desses dois momentos. Eles podem interagir com os Services.
 - Services: Estes são os acionadores de fatos das lógicas da aplicação, responsáveis por abstrair dos controllers os 
detalhes de implementação da lógica de cada endpoint. Eles são chamados pelos controllers, podem se utilizar de outros
services e também interagem com Repositories.
 - Repositories é a camada de interação com a persistência de dados da aplicação. No caso, é responsável por abstrair
dos Services as resposabilidades de interação com banco de dados, assim os detalhes de implementação das ORM's ficam 
nesta camada onde podem ser reaproveitados de diferentes formas pelos services.

As camadas de Services exigem Repositories que implementem interfaces específicas para cada Service, facilitando no futuro 
modificações na solução utilizada para persistência de dados.

Caso não seja evidente as vantagens desse Design note que é devido ao fato do escopo da aplicação ser bem pequeno. Em uma
aplicação onde há diversos endpoints com funcionalidades que se sobrepõe e interagem com diversos componentes do sistema
esse design é bem adequado, um cenário onde modulos distintos interagem, possuem várias controllers, 
services e repositories. Neste caso específico as coisas ficaram meio isoladas afinal há pouca sobreposição de
funcionalidades.

A camada de testes tb é criada em 4 camadas para aumentar reaproveitamento de código. É bem fácil em grandes aplicações
que possuem códigos de testes ainda mais bagunçados e mal escritos que as próprias aplicações. Portanto o código de
testes deve ser tratado com cuidado. A estratégia de 4 camadas aqui é proposta pelo engenheiro de Software Dave Farley.
- Scenarios: Este é o nivel onde os testes são declarados, eles estão escritas na linguagem mais próxima possível do
domínio. Os cenários criados são cenários reais de onde algum usuário da aplicação interagiria com ela.
- DSL: Acrônimo de Domain Specific Language, é a única camada que interage com o cenário, justamente pois o cenário só
fala a linguagem do domínio, esta é a camada que traduz a linguagem do domínio em açoes de fato para os testes.
- Drivers: Apesar da tradução ser feita pela camada de DSL, quem de fato executa a interação do sistema é a camada de
drivers. É uma camada que interage externamente com o sistema, permitindo que o sistema funcione sem 
intervenções e assegurando que o comportamento esperado está de fato sendo testado.
- Application: A aplicação em si a ser testada é quem compõe a ultima camada.


## Instalação

Foi feito deploy do projeto pelo Heroku através do proprio docker file. Acesse: 
[Bluestorm-Admission-Test](https://bluestorm-admission-test.herokuapp.com/docs)

### Docker
Para execução da aplicação da forma mais simples possível utilize é necessário Docker e Docker Compose instalados. 
Caso opte por essa opção apenas execute em sequência os seguintes comandos:
```
> make docker-setup
> make docker-run
```
Caso não deseje instalar o docker, é necessário possuir python 3.10, e se utilizar do poetry para instalação de
dependências. E necessário uma .env file com o seguinte a seguinte variável de ambiente:
TOKEN_SECRET="um token qualquer". Após as dependências devidamente instaladas pode-se usar 
```make run``` para executar a aplicação.

Use ```make help``` para outros comandos.
