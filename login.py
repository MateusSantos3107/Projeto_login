import customtkinter as ctk

#configuração aparencia
ctk.set_appearance_mode("dark")

#criação das funções de Funcionalidades

def validar_login():
   usuario = campo_usuario.get()
   senha = campo_senha.get()

   #verificar se o usuario é Mateus e a senha for 123456
   if usuario == "Mateus" and senha == "123456":
      resultado_login.configure(text="login feito com sucesso",text_color="green")
   else:
      resultado_login.configure(text="Login incorreto",text_color="red")
   



#criação da janela principal
app = ctk.CTk()
app.title("Sistema de login")
app.geometry("300x300")
#criação dos campos
#label
label_usuario = ctk.CTkLabel(app,text="Usuario")
label_usuario.pack(pady=10)
#Entry
campo_usuario = ctk.CTkEntry(app,placeholder_text="Digite seu usuario")
campo_usuario.pack(pady=10)
#label
label_senha = ctk.CTkLabel(app,text="Senha")
label_senha.pack(pady=10)
#Entry
campo_senha = ctk.CTkEntry(app,placeholder_text="Digite sua senha" , show=("*"))
campo_senha.pack(pady=10)
#button
botao_login = ctk.CTkButton(app,text="Login",command=validar_login)
botao_login.pack(pady=10)
#campo feedback de login
resultado_login = ctk.CTkLabel(app,text="")
resultado_login.pack(pady=10)






#iniciar aplicação
app.mainloop()