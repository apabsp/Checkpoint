# Plataforma de Review de Jogos
![image](https://github.com/lariisantos/Projeto-FDS/assets/142417937/f018c00d-9b12-4d22-a83e-7bba8b0d4c38)

Esse projeto foi desenvolvido como parte da disciplina de Fundamentos de Desenvolvimento de Software. 

O **CheckPoint** tem como objetivo fornecer uma plataforma para que os usuários possam compartilhar, salvar, descobrir e escrever avaliações de jogos.

**Seu guia completo para avaliar e descobrir jogos!**

## O que é?

* Avalie e comente jogos
* Organize sua biblioteca
* Descubra novos jogos
* Conecte-se com a comunidade

## Histórias:

1. Eu, como usuário típico gostaria de editar meu perfil.
2. Eu como usuário típico gostariar de avaliar (0-5 estrelas) os jogos disponíveis.
3. Eu como usuário típico gostaria de favoritar jogos para que apareçam em meu perfil.
4. Eu como usuário típico gostariar de fazer uma review (comentada).
5. Eu como usuário típico gostariar de apagar uma review já criada.
6. Eu como usuário típico gostariar de editar uma review já criada.
7. Eu como usuário típico gostaria de poder visualizar a review de outro usuário.
8. Eu como usuário típico gostaria de poder curtir a review de outro usuário.
9. Eu como usuário típico gostaria de poder comentar a review de outro usuário.
10. Eu como usuário típico gostaria de adicionar jogos a minha “lista de desejos” ou “wishlist”, para demonstrar meu interesse por aquele jogo.
11. Eu como usuário típico gostaria de visualizar a wishlist de outros usuários.
12. Eu como usuário típico gostaria de pesquisar por usuários.
13. Eu como usuário típico gostaria visualizar o perfil de outros usuários.
14. Eu como usuário típico gostaria de seguir outros usuários.
15. Eu como usuário típico gostaria de ver uma aba com reviews recentes de pessoas seguidas.
16. Eu como usuário típico gostaria de pesquisar por jogos específicos.
17. Eu como usuário típico gostaria de curtir um jogo.

## Sobre:

**GGuardians** é um grupo de jogadores, e alunos da faculdade CesarSchool, apaixonados por criar ferramentas que aprimoram a experiência de jogar.

## Missão:

Criar um sistema de review de jogos que seja útil, engajador e inovador.

## Membros da Equipe

Este projeto foi desenvolvido por:

    Antonio Paulo Barros
    Clara Machado
    João Pedro Fontes Ferreira
    João Pedro Maranhão
    Larissa Sobrinho
    Heloísa Tanaka
    
## Processo: 

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

## Entrega 2:

** ![ScreenCast](https://drive.google.com/file/d/15iqvXWf42R92JOHdvqo80P4fT0S81CXy/view?usp=sharing)**

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

