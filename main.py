import customtkinter as ctk
from src.gui.app_ui import PasswordManagerApp

if __name__ == "__main__":
    root = ctk.CTk()
    app = PasswordManagerApp(root)
    root.mainloop()