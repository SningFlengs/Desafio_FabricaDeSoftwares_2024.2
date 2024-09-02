# Desafio_Fabrica-2024

## Status

**Em Desenvolvimento** 🛠️

## Descrição do Projeto

Este projeto foi desenvolvido como parte do desafio _Fábrica de Softwares_. Ele tem como objetivo permitir que os usuários realizem operações de CRUD (Create, Read, Update, Delete) em imagens utilizando a API do Cloudinary para armazenamento.

## Tecnologias Utilizadas

- **Python**: 3.11.8
- **Django**: 3.2.25
- **Cloudinary**: 1.29.0

## Funcionalidades

- **Autenticação de Usuários**: Criação de contas, login e logout.
- **Upload de Imagens**: Usuários podem fazer upload de imagens, que são armazenadas no Cloudinary.
- **Edição de Imagens**: Usuários podem editar o título e a descrição de suas imagens.
- **Exclusão de Imagens**: Usuários podem deletar imagens.
- **Visualização de Imagens**: As imagens carregadas por um usuário são exibidas em um painel.

## Campos do Modelo de Imagem

- **title**: Título da imagem.
- **description**: Descrição da imagem.
- **image**: Arquivo da imagem enviado.
- **user**: Usuário que enviou a imagem.

## Como Rodar o Projeto

1. **Clone o repositório**: `git clone https://github.com/username/Desafio_Fabrica-2024.git`
2. **Crie e ative um ambiente virtual**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use venv\Scripts\activate
    ```
3. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Configurações**: Crie um arquivo `.env` com as seguintes variáveis:
    ```bash
    SECRET_KEY=your_secret_key
    NAME=nome_do_banco
    USER=usuario_do_banco
    PASSWORD=senha_do_banco
    CLOUD_NAME=cloudinary_cloud_name
    API_KEY=cloudinary_api_key
    API_SECRET=cloudinary_api_secret
    ```
5. **Rodar as Migrações**:
    ```bash
    python manage.py migrate
    ```
6. **Iniciar o Servidor**:
    ```bash
    python manage.py runserver
    ```
7. **Acessar a aplicação**:
    - Vá para `http://127.0.0.1:8000/` e faça o login ou crie uma conta.
    - Após logar, você será redirecionado para o painel onde poderá gerenciar suas imagens.

## Endpoints Principais

- **Dashboard**: `/myapp/dashboard/` - Painel do usuário com suas imagens.
- **Upload**: `/myapp/upload/` - Página para fazer upload de novas imagens.
- **Edição**: `/myapp/edit/<id>/` - Página para editar uma imagem existente.
- **Deleção**: `/myapp/delete/<id>/` - Página para deletar uma imagem existente.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

**Ítalo Oliveira**
- GitHub: [@Italo_Oliveira](https://github.com/SningFlengs)
- LinkedIn: [@Italo_Oliveira](https://www.linkedin.com/in/ítalo-cauã-58b12030b/)
- Email: italocaua19506@gmail.com
