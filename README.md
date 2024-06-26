# Plataforma de Review de Jogos

![checkpoint](https://github.com/apabsp/Checkpoint/assets/63313892/83c8a207-6c29-4c70-9a48-e50f3d017cfb)


Esse projeto foi desenvolvido como parte da disciplina de Fundamentos de Desenvolvimento de Software. 

O **CheckPoint** tem como objetivo fornecer uma plataforma para que os usuários possam compartilhar, salvar, descobrir e escrever avaliações de jogos.

**Seu guia completo para avaliar e descobrir jogos!**

## O que é?

* Avalie e comente jogos
* Organize sua biblioteca
* Descubra novos jogos
* Conecte-se com a comunidade

## Histórias:

<ol>
  <li>Eu, como usuário típico gostaria de editar meu perfil.</li>
  <li><b>Eu como usuário típico gostariar de avaliar (0-5 estrelas) os jogos disponíveis.</b></li>
  <li>Eu como usuário típico gostaria de favoritar jogos para que apareçam em meu perfil.</li>
  <li><b>Eu como usuário típico gostariar de fazer uma review (comentada).</b></li>
  <li><b>Eu como usuário típico gostariar de apagar uma review já criada.</b></li>
  <li><b>Eu como usuário típico gostariar de editar uma review já criada.</b></li>
  <li><b>Eu como usuário típico gostaria de poder visualizar a review de outro usuário.</b></li>
  <li>Eu como usuário típico gostaria de poder curtir a review de outro usuário.</li>
  <li>Eu como usuário típico gostaria de poder comentar a review de outro usuário.</li>
  <li><b>Eu como usuário típico gostaria de adicionar jogos a minha “lista de desejos” ou “wishlist”, para demonstrar meu interesse por aquele jogo.</b></li>
  <li>Eu como usuário típico gostaria de visualizar a wishlist de outros usuários.</li>
  <li>Eu como usuário típico gostaria de pesquisar por usuários.</li>
  <li>Eu como usuário típico gostaria visualizar o perfil de outros usuários.</li>
  <li>Eu como usuário típico gostaria de seguir outros usuários.</li>
  <li>Eu como usuário típico gostaria de ver uma aba com reviews recentes de pessoas seguidas.</li>
  <li><b>Eu como usuário típico gostaria de pesquisar por jogos específicos.</b></li>
  <li><b>Eu como usuário típico gostaria de curtir um jogo.</b></li>
</ol>

## Sobre:

**GGuardians** é um grupo de jogadores, e alunos da faculdade CesarSchool, apaixonados por criar ferramentas que aprimoram a experiência de jogar.

## Missão:

Criar um sistema de review de jogos que seja útil, engajador e inovador.

<!-- ## Membros da Equipe

Este projeto foi desenvolvido por:

    Antonio Paulo Barros
    Clara Machado
    João Pedro Fontes Ferreira
    João Pedro Maranhão
    Larissa Sobrinho
    Heloísa Tanaka -->
<details>
 <summary><h2>Processo</h2></summary>

 1. Ideação:
    ![image-6](https://github.com/lariisantos/Projeto-FDS/assets/95260401/b1a8acaa-1282-4aef-a0d3-888df356605e)
    ![Sem título](https://github.com/lariisantos/Projeto-FDS/assets/95260401/f22f9d0f-c468-4ed4-a6e2-ffa4bfa992c2)

    Tudo começa com um brainstorming.
    
    Reunimos a equipe para discutir ideias e soluções.
    
    Exploramos diferentes possibilidades e esboçamos os primeiros conceitos.
    ![Sign In](https://github.com/lariisantos/Checkpoint/assets/95260401/9763776b-e128-4880-91fd-a07e4082a931)
    ![Sign Up](https://github.com/lariisantos/Checkpoint/assets/95260401/4b2d12dc-d25c-4ebb-b571-7ac36beec180)
    ![Home](https://github.com/lariisantos/Checkpoint/assets/95260401/e1215f59-9828-4421-bd63-9c5a962d0e4c)
    ![Search Screen](https://github.com/lariisantos/Checkpoint/assets/95260401/5cad22c5-ae50-43e3-bafe-f092433dd6cc)
    ![Meu Perfil](https://github.com/lariisantos/Checkpoint/assets/95260401/a73badad-15f0-40e7-8663-def7a564b075)
    ![Lista de Amigos](https://github.com/lariisantos/Checkpoint/assets/95260401/ee72c11f-7492-42d5-a680-6cd80d5debb9)
    ![Perfil do Usuário 1](https://github.com/lariisantos/Checkpoint/assets/95260401/0d45c723-2c1e-4943-9290-d805268ee680)
    ![Perfil do Usuário 2](https://github.com/lariisantos/Checkpoint/assets/95260401/b325e362-77b9-45fc-b86c-943d579cf2d4)
    ![Configurações](https://github.com/lariisantos/Checkpoint/assets/95260401/e7abf41b-8e8c-4dfe-896c-4df1ec152639)
    ![Página do Jogo](https://github.com/lariisantos/Checkpoint/assets/95260401/9c0bd66d-9911-45e7-b6dd-d2eba2ce02a6)
    ![Criar Review](https://github.com/lariisantos/Checkpoint/assets/95260401/0c0d0305-7c56-4ddf-9e02-b5e2a6cc0315)
    ![Visualizar Review](https://github.com/lariisantos/Checkpoint/assets/95260401/54d0e6d0-e71c-4b44-b085-fc96d4ea06f0)
    ![Comentar Review](https://github.com/lariisantos/Checkpoint/assets/95260401/ae12878e-d5d1-4ac2-a2a1-5aa0048828fd)
</details>

## Método utilizado - pair programming
O projeto foi feito utilizando o pair-programming, com duplas randomizadas e alternadas a cada semana


## Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias:

    Django
    
## Rodando em ambiente local

Para rodar em ambiente **local**, siga os passos:

1. Crie seu ambiente virtual python executando:

    Para o **Windows**:

    ```bash
    python -m venv venv
    ```

    Para o **Linux**:

    ```bash
    python3 -m venv venv
    ```

2. Ative seu ambiente virtual:

    Para o **Windows**:<br>
    - Antes, no **powershell**:

        ```bash
        Set-ExecutionPolicy Unrestricted -Scope CurrentUser
        ```


    ```bash
    .\venv\Scripts\activate
    ```

    Para o **Linux**:

    ```bash
    source venv/bin/activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r .\requirements.txt
    ```

4. Rode o servidor localmente:

    Para o **Windows**: 

    ```bash
    python manage.py runserver
    ```

    Para o **Linux**: 

    ```bash
    python3 manage.py runserver
    ```

## ENTREGAS

<details>
<summary>Entrega 1:</summary>

## Entrega 1:
- [Link Screencast protótipo lo-fi](https://www.youtube.com/watch?v=2ysd68vxMM0)

- Progresso no Jira
![image](https://github.com/lariisantos/Checkpoint/assets/95260401/ae638d6a-6047-46fa-9e5b-50e84b9fc8e3)

![image](https://github.com/lariisantos/Checkpoint/assets/95260401/cdecf9de-1608-45d8-a514-408709154997)
</details>

<br/>

<details>
<summary>Entrega 2:</summary>

## Entrega 2:

## Instrução de Acesso
Acesso ao Site: https://checkpoint-fds.azurewebsites.net

Ao entrar no site, o usuário será solicitado a fazer login em sua conta (ou registrar-se caso ainda não possua uma). Após concluir este processo, o usuário terá acesso aos serviços da Checkpoint.


**Link do [ScreenCast do Uso do Sistema](https://drive.google.com/file/d/15iqvXWf42R92JOHdvqo80P4fT0S81CXy/view)**

**Relato Programação em Par:**
- **_Clara e Heloísa_**:
    Realizamos pair programming para implementar um novo recurso de avaliação de parâmetro 5 estrelas.
  
    **Resultado:** A implementação, infelizmente, foi falha. Apesar das tentativas de ambas as participantes de implementar a história, acabamos criando mais bugs e issues dentro do código e preferimos não             realizar o commit para não atrapalhar o andamento do projeto como um todo, entretanto, a nossa relação como uma equipe foi fortalecida, é como aquele velho ditado "Os erros são os degraus pelos quais             subimos à sabedoria.".
  
    **Conclusão:** Pair programming fortaleceu nossa colaboração e confiança como equipe.


- **_Larissa e João Pedro Maranhão_**: Realizamos o pair programming na tentativa de realizar a história da criação de uma wishlist.

  **Resultado:** Implementação falha. Depois de muita pesquisa e tentativas, deixamos a respectiva história de lado e, para ainda assim colaborarmos com a equipe, populamos nosso acervo de jogos para o nosso site, fizemos a logo da nossa plataforma e trabalhamos em conjunto
  com Clara para fazer o diagrama de atividades.
  
  **Conclusão:** O Pair Programming aumentou nossa determinação para continuar estudando e tentando, afim de colaborar com o grupo.

- **_João Pedro Fontes e Antonio Paulo Barros_**:
    Realizamos pair programming para implementar a pesquisa por jogos na base de dados, curtir um jogo e fazer a criação de uma nova review para o jogo selecionado.
  
    **Resultado:** Após algumas pesquisas e tentativas iniciais de como poderiamos fazer essas novas features, fazendo os modelos do banco de dados e fazendo alterações no html, conseguimos implementar com sucesso essas histórias, retirando alguns bugs antes do commit como: 
    - **Retorno JSON errado** após a criação da review;

    Além disso, resolvemos algumas issues no github após a criação da historia de curtir um jogo e pesquisa por um jogo, sendo elas:
    - **Bug ao curtir um jogo**: Era mostrado que o jogo não existia se fosse sua primeira ação de curtir um jogo.
    - **Bug ao pesquisar um jogo**: Era mostrado os jogos que batiam exatamente com o que foi pesquisado, pesquisando, inclusive, se o caracter era maiúsculo ou minúsculo.
    - **Bug no redirecionamento de rotas**: Bug que nao redirecionava para a página de login se o usuário não estivesse logado e tentasse acessar a rota privada.

    **Conclusão:** O pair programming serviu para aprendermos mais sobre a implementação das novas features do projeto Checkpoint, além do trabalho em equipe.

<br>

**Print do quadro da sprint 1 no Jira:**

![Sprint 1](https://github.com/apabsp/Checkpoint/assets/63313892/5769e078-b164-4a1e-9164-becbb4fe3281)

![Backblog sprint 1](https://github.com/apabsp/Checkpoint/assets/63313892/a07fe2c3-6e66-445d-b537-5dc183d346e4)

![Backlog](https://github.com/apabsp/Checkpoint/assets/63313892/79b42652-99a6-4441-9dea-453deb478423)
<br>

**Diagrama de Atividades**

![Diagrama Checkpoint drawio(1)](https://github.com/apabsp/Checkpoint/assets/95260401/c34d36db-5808-4531-9385-8856232e87f5)


**Bug Tracker**
![image](https://github.com/apabsp/Checkpoint/assets/130470569/2ede31f6-b9f6-401f-9891-64e581a55d8e)
![image](https://github.com/apabsp/Checkpoint/assets/130470569/765ffa31-1365-4128-a64a-5c93c198a5b2)
</details>

<br/>

<details>
<summary>Entrega 3:</summary>

## Entrega 3:

<details>
 <summary>Screencasts</summary>

**Link do [Screencast do LoFi](https://drive.google.com/file/d/12a0_gtoHXDT2dRK7sGBf7f1rRqEmfe_2/view?usp=sharing)**

**Link do [Screencast do build e deploy com os testes](https://drive.google.com/file/d/18qB9hdLpaBI_lFlOlaB3Zm7JEf0Q-Ni5/view)**


**Link do [Screencast do Sistema](https://drive.google.com/file/d/1g7MePDxJtaA5RkR7Sp5ZHjIKzh6Ctxd1/view?usp=sharing)**


**Link do [Screencast dos testes](https://drive.google.com/file/d/1_FSLtyZh1p8cmYHwtVNLTW8CJ3pCGT_y/view?usp=sharing)**

</details>

<br/>

<details>
 <summary>Jira</summary>

![image](https://github.com/apabsp/Checkpoint/assets/95260401/3e436287-a5a2-461c-8f16-2a9e8bc5d8ee)
![image](https://github.com/apabsp/Checkpoint/assets/95260401/9e9f34f5-d48e-4a22-a12f-be0d102656bc)



</details>

<br/>
<details>
 <summary>Diagrama de Atividades</summary>

![Diagrama Checkpoint drawio](https://github.com/apabsp/Checkpoint/assets/133816986/1bb3d519-efea-4544-a8d4-105d8b26bfa7)
</details>

<br/>

<details>
 <summary>Bug Tracker</summary>
    
![imageCaptura de tela 2024-05-05 201220](https://github.com/apabsp/Checkpoint/assets/142419152/9ff6591b-070e-46c7-a474-eb1247ab01d5)
![imageCaptura de tela 2024-05-05 200951](https://github.com/apabsp/Checkpoint/assets/142419152/ead8f341-da71-40d1-ac9c-6fe6e490def7)

</details>

<br/>

<details>
 <summary>Novas telas do Lo-fi</summary>

![Página do Jogo](https://github.com/apabsp/Checkpoint/assets/130470569/89b1fca5-d22a-4bd0-978e-7767f0185e13)
![Criar Review](https://github.com/apabsp/Checkpoint/assets/130470569/d9b17a4c-c506-41f0-b7bc-4c795b2def2b)
![Review Postada](https://github.com/apabsp/Checkpoint/assets/130470569/373d49d7-06b7-4d3f-b6be-a7bd385d621c)
![Editar Review](https://github.com/apabsp/Checkpoint/assets/130470569/5d537448-a8a7-4226-ab62-419a879f6aa4)
![Visualizar Review](https://github.com/apabsp/Checkpoint/assets/130470569/5d8c3544-9d40-48a4-b948-80120194a955)
![Comentar Review](https://github.com/apabsp/Checkpoint/assets/130470569/dc95710d-d55c-4288-af80-4a0a8aae0444)

</details>

<br/>

<details>
<summary>Relatos de Pair Programming</summary>
<br/>
    
**Antonio e Heloísa**: Durante nossas sessões recentes de pair programming, focamos em três tarefas principais: implementar a história de deletar uma review, realizar melhorias no front-end e implementar testes utilizando Cypress. 

**Resultado**: O desenvolvimento da funcionalidade de deletar reviews foi particularmente ágil, graças ao domínio de Django por ambos. Já as melhorias no front-end foram alcançadas com sucesso, após uma investigação detalhada e algumas iterações de design e usabilidade. Quanto aos testes em Cypress, após de pesquisa para melhor compreensão da ferramenta, conseguimos implementar os testes automatizados.

**Conclusão**: O pair programming serviu para aprendermos mais sobre Front-End em geral e sobre a ferramenta Cypress, além do trabalho em equipe.

**Larissa e Clara**: Durante nossas sessões recentes de pair programming, focamos também em três tarefas principais: pensar na nova atualização do diagrama, pesquisa de bugs e reimaginação do front-end da aplicação.

**Resultado**: Com sucesso, concluímos tudo o que tínhamos pensado. Organização do diagrama, que, antes estava incorreto, procura por bugs a fim de relatá-los no nosso bug tracker e colaboramos com mais ideias e testes de front-end.

**João Pedro Fontes e João Pedro Maranhão**: Durante nossas sessões de pair programming, trabalhamos juntos no desenvolvimento de duas funcionalidades principais para nossa plataforma: a edição de reviews e a implementação de um sistema de avaliação com estrelas para jogos. Nosso foco foi integrar essas funcionalidades de maneira eficaz, tanto no backend quanto no front-end, e garantir seu funcionamento.

**Resultado**: Conseguimos implementar com sucesso a funcionalidade de edição de reviews, permitindo aos usuários modificar suas avaliações de forma segura e intuitiva. O sistema de avaliação com estrelas também foi bem-sucedido, oferecendo uma interface agradável e fácil de usar. Os testes automatizados confirmaram a robustez das novas funcionalidades.

**Conclusão**: As sessões de pair programming foram extremamente benéficas, não só para o desenvolvimento técnico das funcionalidades, mas também para o aprendizado mútuo e aprimoramento das nossas habilidades. A experiência reforçou a importância da colaboração e da comunicação eficaz no sucesso do projeto.

</details>

<br/>

</details>

<br/>

<details>
<summary>Entrega 4:</summary>

## Entrega 4:

<details>
 <summary>Screencasts</summary>

**Link do [Screencast do LoFi](https://drive.google.com/file/d/1_cblsfSAV3-qgVoli3GXO3WtDU_DTQX9/view?usp=sharing)**

**Link do [Screencast do build e deploy com os testes](https://drive.google.com/file/d/1yIxu6EHwEGITw3BFteW7Hqurgfi6u2XI/view?usp=sharing)**


**Link do [Screencast do Sistema](https://drive.google.com/file/d/1B4DZgm0sIZSv7gmu47mBz3T4Mc8vNu-4/view?usp=sharing)**

**Link do [Screencast da Pipeline do Branch de Desenvolvimento com testes](https://drive.google.com/file/d/1tnsCyJ-wQ623gvLTO9Se8SysDNEhqMeM/view?usp=sharing)**


**Link do [Screencast dos testes](https://drive.google.com/file/d/1BX4eyS2HXYqywU8-uIANL2kGyWjfZNV5/view?usp=sharing)**

</details>

<br/>

<details>
 <summary>Jira</summary>
  
![Captura de tela 2024-06-03 173852](https://github.com/apabsp/Checkpoint/assets/142419152/82ddfe6e-97c1-4982-a1f7-d1654cbb6016)
![Captura de tela 2024-06-03 173952](https://github.com/apabsp/Checkpoint/assets/142419152/78250ec9-d9fc-4d14-8216-b6065f5846f6)



</details>

<br/>
<details>
 <summary>Diagrama de Atividades</summary>

![Sem título](https://github.com/apabsp/Checkpoint/assets/95260401/9a7fe9ba-bcea-48e4-8c02-0e235ea81908)




</details>

<br/>

<details>
 <summary>Bug Tracker</summary>

![Captura de tela 2024-06-03 172806](https://github.com/apabsp/Checkpoint/assets/142419152/19bf4f11-3769-4fbc-a945-d37662603bd5)
![Captura de tela 2024-06-03 172830](https://github.com/apabsp/Checkpoint/assets/142419152/bf1ce29d-81c8-40ac-9a00-071ba8b19259)

</details>

<br/>

<details>
 <summary>Novas telas do Lo-fi</summary>

![Editar Perfil](https://github.com/apabsp/Checkpoint/assets/130470569/1be3ec45-19b6-4ec4-9fc3-d0277da0c99a)

</details>

<br/>

<details>
<summary>Relatos de Pair Programming</summary>
<br/>

## João Pedro Fontes e Heloísa Tanaka

Durante nossas sessões recentes de pair programming, focamos em implementar duas histórias importantes: editar perfil e adicionar à wish list, além de desenvolver testes utilizando Cypress.

### Resultado

A implementação das funcionalidades de editar perfil e adicionar à wish list ocorreu de maneira fluida, beneficiando-se da nossa colaboração próxima e da compreensão compartilhada do projeto. Nos testes com Cypress, dedicamos tempo para compreender a ferramenta, resultando em testes automatizados eficazes.

### Conclusão

O pair programming nos proporcionou uma oportunidade valiosa para aprimorar nossas habilidades técnicas, especialmente em relação ao desenvolvimento web e ao uso de ferramentas de teste como o Cypress. Além disso, fortaleceu nossa capacidade de trabalhar em equipe e colaborar de maneira eficaz.

## João Pedro Maranhão e Larissa Sobrinho

Durante nossas sessões recentes de pair programming, concentramo-nos em aprimorar o front-end e realizar melhorias no restante do projeto, incluindo os slides e outras áreas.

### Resultado

O processo de atualização do front-end e das demais partes do projeto foi conduzido de forma colaborativa e eficiente. Através de iterações cuidadosas, conseguimos melhorar a aparência e a usabilidade do projeto de forma significativa.

### Conclusão

O pair programming destacou a importância da comunicação e da colaboração em equipe para alcançar resultados de alta qualidade. Aprendemos muito sobre design de interface e desenvolvimento front-end, o que nos permitirá enfrentar desafios futuros com mais confiança.

## Antônio Paulo e Clara Machado

Durante nossas sessões recentes de pair programming, nos concentramos na implementação da funcionalidade de curtir reviews e na criação de testes automatizados utilizando Cypress.

### Resultado

A implementação da funcionalidade de curtir reviews foi ágil, graças à nossa compreensão sólida da arquitetura do projeto. Além disso, dedicamos tempo para explorar os testes automatizados com Cypress, garantindo a qualidade e confiabilidade do código.

### Conclusão

O pair programming demonstrou ser uma abordagem eficaz para acelerar o desenvolvimento e garantir a qualidade do código. Aprendemos não apenas sobre as funcionalidades específicas do projeto, mas também sobre as melhores práticas de teste, o que beneficiará nosso trabalho futuro.

</details>

<br/>

<details>
  <summary>Apresentação</summary>
  <a href = "https://www.canva.com/design/DAGG5ijomFw/jP5BQBSNdbgOr31hjaF_sA/view?utm_content=DAGG5ijomFw&utm_campaign=designshare&utm_medium=link&utm_source=editor"> Apresentação</a>
</details>

<br/>

</details>

## Contribuidores 👨‍👩‍👧‍👦

<a href="https://github.com/apabsp/Checkpoint/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=apabsp/Checkpoint" />
</a>

<br/>

<ul>
    <li>
        <a href="https://github.com/apabsp">Antonio Paulo Barros</a> - apabsp@cesar.school 📩
    </li>
    <li>
        <a href="https://github.com/helotanaka">Heloisa Tanaka</a> - htf@cesar.school 📩
    </li>
    <li>
        <a href="https://github.com/jotapeans">João Pedro Fontes</a> - jpff2@cesar.school 📩
    </li>
    <li>
        <a href="https://github.com/lariisantos">Larissa Santos</a> - lss2@cesar.school 📩
    </li>
    <li>
        <a href="https://github.com/claramachadoaj">Clara Machado</a> - cma3@cesar.school 📩
    </li>
    <li>
        <a href="https://github.com/Jpmaranhao">João Pedro Maranhão</a> - jpmcf@cesar.school 📩
    </li>
</ul>

## License

[MIT](./LICENSE)
