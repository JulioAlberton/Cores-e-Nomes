import tkinter as tk
from tkinter import ttk
import random


#janela-------- --  -   -   -
janela = tk.Tk()
janela.geometry('300x200')
janela.title('teste botão')


#listaCor
amarelo = "yellow"
vermelho = 'Red'
laranja = 'Orange'
azul = 'Blue'
roxo = 'Purple'
verde = 'Green'
cinza = 'Grey'

#base
def trocar_cores():
    
    lista_cores_da_letra = [
        amarelo,verde,vermelho,laranja,azul,roxo,cinza]
    lista_nomes_botao =[
        'Amarelo','Verde','Vermelho','Laranja','Azul','Roxo','Cinza']
    cor_letra_texto = random.choice(lista_cores_da_letra)
    nome_letra = random.choice(lista_nomes_botao) 
    return  lista_nomes_botao,nome_letra, lista_cores_da_letra, cor_letra_texto

lista_nomes_botao, nome_letra, lista_cores_da_letra, cor_letra_texto = trocar_cores()

    
#labelmsg menor
lblmenor = tk.Label(janela,text='escolha o nome da cor que se refere a cor da palavra')
lblmenor.pack()


#pontuação
lblpontuação = tk.Label(janela,text='0' )
lblpontuação.pack()



#labelmsg da cor
lblcor = ttk.Label(
    janela,
    text=nome_letra,  #cores aleatorias aqui! --------------------
    foreground=cor_letra_texto, #random
    font=('Arial',50),
    anchor='center'
)
lblcor.pack() 

#função contador
x = 0  # ------------------------------------------------------------------------------------------------
def quando_clicar():
    global x
    x = x + 1
    lblpontuação.config(text=x)

#função atualizar
def atualizar_(): #------------------------------------------------------------------------------------------------
    lista_nomes_botao,nome_letra,lista_cores_da_letra,cor_letra_texto = trocar_cores()
    lblcor.config(text=nome_letra,foreground=cor_letra_texto)

    y = lista_cores_da_letra.index(cor_letra_texto)
    lista_botao_aleatorio = [1,2]
    botao_aleatorio = random.choice(lista_botao_aleatorio)

    if botao_aleatorio == 1:
        botao1.config(text=lista_nomes_botao[y],command=lambda:[atualizar_(),quando_clicar()])  #---
        del(lista_nomes_botao[y])
        botao2.config(text=random.choice(lista_nomes_botao),command=atualizar_)

    else:
        botao2.config(text=lista_nomes_botao[y],command=lambda:[atualizar_(),quando_clicar()])    
        del(lista_nomes_botao[y])
        botao1.config(text=random.choice(lista_nomes_botao),command=atualizar_)
        #----


#botões
botao1 = tk.Button(janela,text='comece',command=atualizar_)  #---
botao1.pack()
botao2 = tk.Button(janela,text='comece',command= atualizar_)  #----
botao2.pack()
janela.mainloop()
