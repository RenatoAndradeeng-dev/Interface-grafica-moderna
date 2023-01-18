import customtkinter as ctk

janela = ctk.CTk()# Janela criada com customtkinter

janela._set_appearance_mode('dark')
#Configurando a janela principal

janela.title('Teste')
janela.geometry('700x400')
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)
janela.resizable(width=True, height=False)
#janela.iconify()#abre e fecha janela
#janela.deiconify()#deixa a janela aberta

#Criando nova janela

def nova_tela():
    nova_tela = ctk.CTkToplevel(janela,fg_color='teal')
    nova_tela.geometry('200x200')
        
   
btn_novatela = ctk.CTkButton(master=janela, text='Abrir nova Janela', command=nova_tela).place(x=300, y=100)





janela.mainloop()