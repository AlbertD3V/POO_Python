from tkinter import *
from tkinter import messagebox

def exibir_mensagem():
    nome = coleta1.get()
    curso = coleta2.get()
    apelido = coleta3.get()

    if nome and curso and apelido:
        mensagem = f"Olá {nome}, bem-vindo(a) ao curso de {curso}! Seu apelido {apelido} é bem legal."
        messagebox.showinfo("Mensagem de Boas-Vindas", mensagem)
    else:
        messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")

window = Tk()
window.title("Sistema de Cadastro")


window.geometry("400x200+100+200")

texto1 = Label(text='Digite seu nome:')
texto1.pack()
coleta1 =  Entry(fg='black',
                bg='white',
                width=50
)
coleta1.pack()

texto2 = Label(text='Seu curso:')
texto2.pack()
coleta2 =  Entry(fg='black',
                bg='white',
                width=30
)
coleta2.pack()

texto3 = Label(text='Seu apelido:')
texto3.pack()
coleta3 =  Entry(fg='black',
                bg='white',
                width=15
)
coleta3.pack()

botao = Button(text='Enviar',
               fg='yellow',
               bg='black',
               command=exibir_mensagem
)
botao.pack()

window.mainloop()
