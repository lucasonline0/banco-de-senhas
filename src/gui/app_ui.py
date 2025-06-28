import customtkinter as ctk
import pyperclip
import json
from cryptography.fernet import InvalidToken

from src.storage import data_manager
from src.security import crypto_utils

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cofre de Senhas Multiusuário")
        self.root.geometry("800x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.key = None
        self.passwords = {}
        self.current_user = None

        self.create_welcome_screen()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_columnconfigure(0, weight=0)
    
    def show_feedback(self, message, color="green", duration=2000):
        feedback_label = ctk.CTkLabel(self.root, text=message, text_color=color, fg_color=("gray75", "gray25"), corner_radius=8)
        feedback_label.place(relx=0.5, rely=0.95, anchor="center")
        feedback_label.after(duration, feedback_label.destroy)

    def create_welcome_screen(self):
        self.clear_frame()
        self.current_user = None
        
        frame = ctk.CTkFrame(self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        label = ctk.CTkLabel(frame, text="Selecione um Usuário ou Crie um Novo", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=20)

        users = data_manager.load_users()
        
        if not users:
            ctk.CTkLabel(frame, text="Nenhum usuário encontrado.").pack(pady=10)
        else:
            users_list_frame = ctk.CTkFrame(frame, fg_color="transparent")
            users_list_frame.pack(pady=10, padx=50, fill="x", expand=True)
            for user in users:
                user_frame = ctk.CTkFrame(users_list_frame)
                user_frame.pack(fill="x", pady=4)
                user_frame.grid_columnconfigure(0, weight=1)
                ctk.CTkButton(user_frame, text=user, command=lambda u=user: self.create_login_screen_for_user(u)).grid(row=0, column=0, sticky="ew", padx=(0, 5), pady=5)
                ctk.CTkButton(user_frame, text="Excluir", width=100, fg_color="red", hover_color="#C00000", command=lambda u=user: self.create_delete_user_confirmation_screen(u)).grid(row=0, column=1, sticky="e", padx=(5, 0), pady=5)

        ctk.CTkButton(frame, text="Criar Novo Usuário", command=self.create_new_user_screen, fg_color="green", hover_color="darkgreen").pack(pady=30)
    
    def create_login_screen_for_user(self, username):
        self.clear_frame()
        self.current_user = username
        center_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        center_frame.pack(fill="both", expand=True)
        login_frame = ctk.CTkFrame(center_frame, corner_radius=15, border_width=1)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")
        ctk.CTkLabel(login_frame, text="Bem-vindo de volta!", font=ctk.CTkFont(size=28, weight="bold")).pack(pady=(30, 10), padx=80)
        ctk.CTkLabel(login_frame, text=username, font=ctk.CTkFont(size=20), text_color=("gray30", "gray70")).pack(pady=(0, 30))
        self.password_entry = ctk.CTkEntry(login_frame, placeholder_text="Sua Senha", show="*", width=300, height=40, corner_radius=8)
        self.password_entry.pack(pady=10, padx=40)
        self.password_entry.focus()
        self.password_entry.bind("<Return>", self.login)
        ctk.CTkButton(login_frame, text="Entrar", command=self.login, width=300, height=40, corner_radius=8).pack(pady=10, padx=40)
        self.status_label = ctk.CTkLabel(login_frame, text="", text_color="red")
        self.status_label.pack(pady=(5, 20))
        ctk.CTkButton(self.root, text="« Voltar", command=self.create_welcome_screen, fg_color="transparent", text_color=("gray10", "gray90"), hover=False).place(relx=0.02, rely=0.03, anchor="nw")

    def create_new_user_screen(self):
        self.clear_frame()
        frame = ctk.CTkFrame(self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        ctk.CTkLabel(frame, text="Criar Novo Perfil", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=40)
        self.new_user_entry = ctk.CTkEntry(frame, placeholder_text="Nome de Usuário", width=300)
        self.new_user_entry.pack(pady=10); self.new_user_entry.focus()
        self.new_password_entry = ctk.CTkEntry(frame, placeholder_text="Defina uma Senha", show="*", width=300)
        self.new_password_entry.pack(pady=10)
        self.confirm_password_entry = ctk.CTkEntry(frame, placeholder_text="Confirme a Senha", show="*", width=300)
        self.confirm_password_entry.pack(pady=10)
        ctk.CTkButton(frame, text="Criar Perfil", command=self.handle_user_creation).pack(pady=20)
        ctk.CTkButton(frame, text="Voltar", command=self.create_welcome_screen, fg_color="gray", hover_color="darkgray").pack(pady=5)
        self.status_label = ctk.CTkLabel(frame, text="", text_color="red")
        self.status_label.pack(pady=10)
    
    def create_delete_user_confirmation_screen(self, username):
        self.clear_frame()
        frame = ctk.CTkFrame(self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        ctk.CTkLabel(frame, text=f"Excluir Usuário: {username}", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)
        ctk.CTkLabel(frame, text="Esta ação é irreversível.\nPara confirmar, digite sua senha.", text_color="orange").pack(pady=10)
        self.delete_password_entry = ctk.CTkEntry(frame, placeholder_text="Sua Senha", show="*", width=300)
        self.delete_password_entry.pack(pady=10); self.delete_password_entry.focus()
        self.delete_password_entry.bind("<Return>", lambda event, u=username: self.handle_user_deletion(u))
        ctk.CTkButton(frame, text="Confirmar Exclusão", command=lambda u=username: self.handle_user_deletion(u), fg_color="red", hover_color="darkred").pack(pady=20)
        ctk.CTkButton(frame, text="Cancelar", command=self.create_welcome_screen, fg_color="gray", hover_color="darkgray").pack(pady=5)
        self.status_label = ctk.CTkLabel(frame, text="", text_color="red")
        self.status_label.pack(pady=10)

    def create_main_ui(self):
        self.clear_frame()
        self.root.grid_rowconfigure(0, weight=1); self.root.grid_columnconfigure(0, weight=1)
        main_frame = ctk.CTkFrame(self.root, fg_color="transparent"); main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        main_frame.grid_rowconfigure(1, weight=1); main_frame.grid_columnconfigure(1, weight=1)
        nav_frame = ctk.CTkFrame(main_frame); nav_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10)); nav_frame.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(nav_frame, text=f"Cofre de: {self.current_user}", font=ctk.CTkFont(size=16)).grid(row=0, column=0, sticky="w", padx=20, pady=10)
        ctk.CTkButton(nav_frame, text="Sair (Logout)", command=self.create_welcome_screen).grid(row=0, column=1, sticky="e", padx=20, pady=10)
        left_frame = ctk.CTkFrame(main_frame, width=250); left_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 10)); left_frame.grid_propagate(False)
        ctk.CTkLabel(left_frame, text="Adicionar Nova Senha", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10, padx=10)
        self.site_entry = ctk.CTkEntry(left_frame, placeholder_text="Site/Serviço"); self.site_entry.pack(pady=5, padx=10, fill="x")
        self.username_entry = ctk.CTkEntry(left_frame, placeholder_text="Usuário/Email"); self.username_entry.pack(pady=5, padx=10, fill="x")
        self.password_entry = ctk.CTkEntry(left_frame, placeholder_text="Senha"); self.password_entry.pack(pady=5, padx=10, fill="x")
        ctk.CTkButton(left_frame, text="Adicionar", command=self.add_password).pack(pady=20, padx=10)
        right_frame = ctk.CTkFrame(main_frame); right_frame.grid(row=1, column=1, sticky="nsew"); right_frame.grid_rowconfigure(1, weight=1); right_frame.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(right_frame, text="Senhas Salvas", font=ctk.CTkFont(size=16, weight="bold")).grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.scrollable_frame = ctk.CTkScrollableFrame(right_frame, label_text=""); self.scrollable_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=(0,5))
        self.populate_password_list()

    def handle_user_creation(self):
        username = self.new_user_entry.get().strip()
        password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not username or not password:
            self.status_label.configure(text="Usuário e senha não podem estar vazios.")
            return
        if password != confirm_password:
            self.status_label.configure(text="As senhas não coincidem.")
            return
        
        users = data_manager.load_users()
        if username in users:
            self.status_label.configure(text="Este nome de usuário já existe.")
            return

        salt = crypto_utils.generate_salt()
        self.key = crypto_utils.derive_key(password, salt)
        data_to_save = json.dumps({})
        encrypted_data = crypto_utils.encrypt_data(data_to_save, self.key)

        data_manager.save_salt(username, salt)
        data_manager.save_encrypted_data(username, encrypted_data)
        
        users.append(username)
        data_manager.save_users(users)
        
        self.current_user = username
        self.passwords = {}
        self.show_feedback(f"Perfil '{username}' criado com sucesso!", color="green")
        self.create_main_ui()

    def handle_user_deletion(self, username, event=None):
        password = self.delete_password_entry.get()
        if not password:
            self.status_label.configure(text="Por favor, insira sua senha para confirmar.")
            return

        salt = data_manager.load_salt(username)
        if not salt:
            self.status_label.configure(text="Erro: Arquivos do usuário não encontrados.")
            return

        key_to_test = crypto_utils.derive_key(password, salt)
        encrypted_data = data_manager.load_encrypted_data(username)

        try:
            crypto_utils.decrypt_data(encrypted_data, key_to_test)
            data_manager.delete_user_files(username)
            users = data_manager.load_users()
            if username in users:
                users.remove(username)
                data_manager.save_users(users)
            
            self.show_feedback(f"Usuário '{username}' e seus dados foram excluídos.", color="white")
            self.create_welcome_screen()

        except InvalidToken:
            self.status_label.configure(text="Senha incorreta. Exclusão cancelada.")
        except Exception as e:
            self.show_feedback(f"Erro ao excluir arquivos: {e}", color="red")
            self.create_welcome_screen()

    def login(self, event=None):
        password = self.password_entry.get()
        if not self.current_user or not password:
            self.status_label.configure(text="Ocorreu um erro. Tente novamente.")
            return

        salt = data_manager.load_salt(self.current_user)
        self.key = crypto_utils.derive_key(password, salt)
        encrypted_data = data_manager.load_encrypted_data(self.current_user)

        if encrypted_data:
            try:
                decrypted_json = crypto_utils.decrypt_data(encrypted_data, self.key)
                self.passwords = json.loads(decrypted_json)
                self.create_main_ui()
            except InvalidToken:
                self.status_label.configure(text="Senha incorreta!")
        else:
             self.status_label.configure(text="Senha incorreta!")


    def add_password(self):
        site = self.site_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if site and username and password:
            self.passwords[site] = {"username": username, "password": password}
            
            passwords_json = json.dumps(self.passwords)
            encrypted_data = crypto_utils.encrypt_data(passwords_json, self.key)
            data_manager.save_encrypted_data(self.current_user, encrypted_data)

            self.populate_password_list()
            self.site_entry.delete(0, 'end')
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')
            self.show_feedback(f"Senha para '{site}' adicionada.", "white")

    def populate_password_list(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        if not self.passwords:
            ctk.CTkLabel(self.scrollable_frame, text="Nenhuma senha salva ainda.").pack(pady=20)
            return
        for site, data in sorted(self.passwords.items()):
            entry_frame = ctk.CTkFrame(self.scrollable_frame)
            entry_frame.pack(fill="x", padx=5, pady=3)
            ctk.CTkLabel(entry_frame, text=f"{site} ({data['username']})", anchor="w").pack(side="left", padx=10, pady=5)
            ctk.CTkButton(entry_frame, text="Copiar Senha", width=120, command=lambda p=data['password']: self.copy_to_clipboard(p)).pack(side="right", padx=10, pady=5)
    
    def copy_to_clipboard(self, password):
        pyperclip.copy(password)
        self.show_feedback("Senha copiada para a área de transferência!", "white")