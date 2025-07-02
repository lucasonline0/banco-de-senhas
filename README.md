# Desktop Password Vault

<p align="center">
  <img src="https://img.shields.io/github/stars/lucasonline0/banco-de-senhas?style=social" alt="GitHub Stars"/>
  <img src="https://img.shields.io/github/forks/lucasonline0/banco-de-senhas?style=social" alt="GitHub Forks"/>
  <img src="https://img.shields.io/github/license/lucasonline0/banco-de-senhas" alt="License"/>
  <img src="https://img.shields.io/github/last-commit/lucasonline0/banco-de-senhas" alt="Last Commit"/>
</p>

> A secure desktop password manager with multi-user support, built with Python and CustomTkinter. All data is encrypted and stored locally on your computer.

## 🎯 About

The **Desktop Password Vault** is an open-source application created to offer a secure and offline solution for password management. The main motivation is to give the user full control over their data, without depending on third-party cloud services.

The project uses **Python** as its foundation, with a graphical user interface developed using the **CustomTkinter** library. Security is the central pillar, implemented with the **Cryptography** library, which ensures that all information is stored securely through key derivation (PBKDF2HMAC) and symmetric encryption (Fernet).

---

## 🖼️ Screenshots

<p align="center">
  <img src="https://github.com/user-attachments/assets/fda38f51-2e99-42db-b205-da934dcb569f" alt="Login Screen" width="400"/>
  <img src="https://github.com/user-attachments/assets/1fbbc2be-b1c2-4ea3-9e50-efefd4ab9cbf" alt="Main Screen" width="400"/>
</p>
<p align="center">
  <em>Login Screen and Main Vault Screen</em>
</p>

---

## ✨ Features

-   ✅ **Strong Encryption:** Uses a unique salt per user, PBKDF2HMAC to derive a secure key from the master password, and Fernet (128-bit AES in CBC mode) to encrypt the data.
-   ✅ **Multi-User Support:** Allows different users to create their own password-protected profiles in the same application, with completely separate password vaults.
-   ✅ **100% Local Storage:** All profiles and encrypted data are saved directly on your machine. No information is sent over the internet.
-   ✅ **Modern GUI:** A user-friendly and intuitive interface built with the CustomTkinter library.
-   ✅ **Simple Management:** Add new credentials (website, username, and password), list all saved passwords, and copy them to the clipboard with a single click.

---

## 📋 Prerequisites

Before you begin, you will need to have the following tools installed on your machine:

-   [Git](https://git-scm.com)
-   [Python 3.8+](https://www.python.org/downloads/)
-   Having a code editor like [VSCode](https://code.visualstudio.com/) is recommended for working on the project.

---

## 🚀 Installation

Follow the steps below to set up the development environment:

```bash
# 1. Clone this repository
$ git clone [https://github.com/lucasonline0/banco-de-senhas.git](https://github.com/lucasonline0/banco-de-senhas.git)

# 2. Navigate to the project folder in your terminal/cmd
$ cd banco-de-senhas

# 3. (Recommended) Create and activate a virtual environment
# On Windows
$python -m venv venv$ .\venv\Scripts\activate
# On macOS/Linux
$python3 -m venv venv$ source venv/bin/activate

# 4. Install the dependencies listed in requirements.txt
$ pip install -r requirements.txt

# 5. Run the application
$ python main.py
