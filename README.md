# Plataforma de Review de Jogos
![image](https://github.com/lariisantos/Projeto-FDS/assets/142417937/f018c00d-9b12-4d22-a83e-7bba8b0d4c38)

Esse projeto foi desenvolvido como parte da disciplina de Fundamentos de Desenvolvimento de Hardware. 

O "CheckPoint" tem como objetivo fornecer uma plataforma para que os usuários possam compartilhar, salvar, descobrir e escrever avaliações de jogos.

**Seu guia completo para avaliar e descobrir jogos!**

## O que é?

* Avalie e comente jogos
* Organize sua biblioteca
* Descubra novos jogos
* Conecte-se com a comunidade

## Histórias:

* Eu, como usuário típico, gostaria de editar meu perfil
* Eu como usuário gostariar de avaliar (0-5 estrelas) os jogos disponíveis. 
* Eu como usuário típico gostaria de favoritar jogos para que apareçam em meu perfil.
* Eu como usuário típico gostaria de poder, ao visualizar a review de um usuário, poder comentar sobre sua review e o respectivo usuário poder visualizar os comentários na sua review.
* Eu como usuário gostariar de fazer review (comentada)
* Eu como usuário típico gostaria de selecionar jogos e colocar uma marcação de “na lista de desejos” ou “wishlist”, para demonstrar jogos que são desejados por mim, além de poder visualizar a wishlist de outros usuários.
* Eu como usuário gostariar de apagar review  já criada 
* Eu como usuário gostariar de editar review já criada 
* Eu como usuário típico gostaria de pesquisar o nome de usuários, visualizar o respectivo perfil e seguir esta pessoa, a fim de poder acompanhar suas atividades recentes.
* Eu como usuário típico gostaria de ver uma aba com reviews recentes de pessoas seguidas, além de poder ter o acesso a review.
* Eu como usuário típico, gostaria de poder colocar 2 jogos com a marcação de “favorito” para que apareça na página do meu perfil.
* Eu como usuário típico, eu gostaria de visualizar os jogos categorizados em “tendência”, os mais visualizados e jogados pelos usuários.
* Eu, como usuário típico, gostaria de comentar em um perfil

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

## ENTREGAS

Entrega 1

- [Link Screencast protótipo lo-fi](https://www.youtube.com/watch?v=2ysd68vxMM0)

- Progresso no Jira
![image](https://github.com/lariisantos/Checkpoint/assets/95260401/ae638d6a-6047-46fa-9e5b-50e84b9fc8e3)

![image](https://github.com/lariisantos/Checkpoint/assets/95260401/cdecf9de-1608-45d8-a514-408709154997)


