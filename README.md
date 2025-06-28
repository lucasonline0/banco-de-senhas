# Cofre de Senhas Desktop

<p align="center">
  <img src="https://img.shields.io/github/stars/lucasonline0/banco-de-senhas?style=social" alt="GitHub Stars"/>
  <img src="https://img.shields.io/github/forks/lucasonline0/banco-de-senhas?style=social" alt="GitHub Forks"/>
  <img src="https://img.shields.io/github/license/lucasonline0/banco-de-senhas" alt="Licença"/>
  <img src="https://img.shields.io/github/last-commit/lucasonline0/banco-de-senhas" alt="Último Commit"/>
</p>

> Um gerenciador de senhas de desktop seguro, com suporte a múltiplos usuários, construído com Python e CustomTkinter. Todos os dados são criptografados e armazenados localmente no seu computador.



## 🎯 Sobre

O **Cofre de Senhas Desktop** é uma aplicação de código aberto criada para oferecer uma solução segura e offline para o gerenciamento de senhas. A principal motivação é dar ao usuário controle total sobre seus dados, sem depender de serviços em nuvem de terceiros.

O projeto utiliza **Python** como base, com uma interface gráfica desenvolvida com a biblioteca **CustomTkinter**. A segurança é o pilar central, implementada com a biblioteca **Cryptography**, que garante que todas as informações sejam armazenadas de forma segura através de derivação de chave (PBKDF2HMAC) e criptografia simétrica (Fernet).

---

## 🖼️ Screenshots

<p align="center">
  <img src="https://github.com/user-attachments/assets/fda38f51-2e99-42db-b205-da934dcb569f" alt="Tela de Login" width="400"/>
  <img src="https://github.com/user-attachments/assets/1fbbc2be-b1c2-4ea3-9e50-efefd4ab9cbf" alt="Tela Principal" width="400"/>
</p>
<p align="center">
  <em>Tela de Login e Tela Principal do Cofre</em>
</p>


---

## ✨ Features

-   ✅ **Criptografia Forte:** Utiliza salt individual por usuário, PBKDF2HMAC para derivar uma chave segura da senha mestre e Fernet (AES 128 bits em modo CBC) para criptografar os dados.
-   ✅ **Suporte a Múltiplos Usuários:** Permite que diferentes usuários criem seus próprios perfis protegidos por senha na mesma aplicação, com cofres de senhas totalmente separados.
-   ✅ **Armazenamento 100% Local:** Todos os perfis e dados criptografados são salvos diretamente na sua máquina. Nenhuma informação é enviada para a internet.
-   ✅ **Interface Gráfica Moderna:** Interface amigável e intuitiva construída com a biblioteca CustomTkinter.
-   ✅ **Gerenciamento Simples:** Adicione novas credenciais (site, usuário e senha), liste todas as senhas salvas e copie-as para a área de transferência com um único clique.

---

## 📋 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

-   [Git](https://git-scm.com)
-   [Python 3.8+](https://www.python.org/downloads/)
-   É recomendado ter um editor de código como o [VSCode](https://code.visualstudio.com/) para trabalhar no projeto.

---

## 🚀 Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

```bash
# 1. Clone este repositório
$ git clone [https://github.com/lucasonline0/banco-de-senhas.git](https://github.com/lucasonline0/banco-de-senhas.git)

# 2. Acesse a pasta do projeto no terminal/cmd
$ cd banco-de-senhas

# 3. (Recomendado) Crie e ative um ambiente virtual
# Em Windows
$python -m venv venv$ .\venv\Scripts\activate
# Em macOS/Linux
$python3 -m venv venv$ source venv/bin/activate

# 4. Instale as dependências listadas no requirements.txt
$ pip install -r requirements.txt

# 5. Execute a aplicação
$ python main.py