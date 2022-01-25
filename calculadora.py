from tkinter import *

# cores
co1 = '#feffff'  # (white) - Branco
co2 = '#e26165'  # (red) - Vermelho
co2_s = '#fa8f92'   # red
co3 = '#757f7f'  # (grey) - Cinza
co3_s = '#bebebe'   # grey
co4 = '#3ea5e0'  # (blue) - Azul
co4_s = '#71c8fa'  # blue
co5 = '#3cd878'  # (green) - Verde
co5_s = '#75faa8'  # green
fundo = '#3b3b3b'  # (black grey) - Cinza escuro

# para armazenar todas as expressões que serão avaliadas
todos_valores = ''

################# Funções ####################
def pegar_valor(event):
    global todos_valores

    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)


def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    resultado = str(int(resultado)) if resultado - \
        int(resultado) == 0 else str(round(resultado, 4))
    valor_texto.set(resultado)
    todos_valores = resultado


def limpar():
    global todos_valores
    valor_texto.set('0')
    todos_valores = ''


# para entrada de valor único
root = Tk()

icone  = PhotoImage(file='img/icon.png')
root.iconphoto(0, icone)

root.title('Calculadora')
root.geometry('265x365')
root.resizable(0, 0)
root.configure(bg=fundo)

valor_texto = StringVar()
valor_texto.set('0')

################# Label ####################
app_tela = Label(root, textvariable=valor_texto, relief='flat',
                 bd=0, anchor=E, font=('Ivy 16 bold'), background='#b9ce98', foreground='#3b3b3b', padx=8)
app_tela.pack(ipady=15, fill='both')

################# Buttongs ####################
b_1 = Button(root, text='C', height=2, bg=co2, highlightbackground=co2_s, activebackground=co2_s, command=limpar,
             fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_1.place(x=0, y=61, width=131)
b_2 = Button(root, text='%', width=3, height=2, bg=co4, highlightbackground=co4_s, activebackground=co4_s, command=lambda: pegar_valor('%'),
             fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_2.place(x=134, y=61)
b_3 = Button(root, text='/', width=3, height=2, bg=co4, highlightbackground=co4_s, activebackground=co4_s, command=lambda: pegar_valor('/'),
             fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_3.place(x=201, y=61)

b_4 = Button(root, text='7', width=3, height=2, bg=co3, highlightbackground=co3_s, activebackground=co3_s, command=lambda: pegar_valor('7'),
             fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_4.place(x=0, y=122)
b_5 = Button(root, text='8', width=3, height=2, bg=co3, highlightbackground=co3_s, activebackground=co3_s, command=lambda: pegar_valor('8'),
             fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_5.place(x=67, y=122)
b_6 = Button(root, text='9', width=3, height=2, bg=co3, highlightbackground=co3_s, activebackground=co3_s, command=lambda: pegar_valor('9'),
             fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_6.place(x=134, y=122)
b_7 = Button(root, text='*', width=3, height=2, bg=co4, highlightbackground=co4_s, activebackground=co4_s, command=lambda: pegar_valor('*'),
             fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_7.place(x=201, y=122)

b_8 = Button(root, text='4', width=3, height=2, bg=co3, highlightbackground=co3_s, activebackground=co3_s, command=lambda: pegar_valor('4'),
             fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_8.place(x=0, y=183)
b_9 = Button(root, text='5', width=3, height=2, bg=co3, highlightbackground=co3_s, activebackground=co3_s, command=lambda: pegar_valor('5'),
             fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
             overrelief=RIDGE)
b_9.place(x=67, y=183)
b_10 = Button(root, text='6', width=3, height=2, bg=co3, highlightbackground=co3_s, activebackground=co3_s, command=lambda: pegar_valor('6'),
              fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
              overrelief=RIDGE)
b_10.place(x=134, y=183)
b_11 = Button(root, text='-', width=3, height=2, bg=co4, highlightbackground=co4_s, activebackground=co4_s, command=lambda: pegar_valor('-'),
              fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
              overrelief=RIDGE)
b_11.place(x=201, y=183)

b_12 = Button(root, text='1', width=3, height=2, bg=co3, highlightbackground=co3_s, activebackground=co3_s, command=lambda: pegar_valor('1'),
              fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
              overrelief=RIDGE)
b_12.place(x=0, y=244)
b_13 = Button(root, text='2', width=3, height=2, bg=co3, highlightbackground=co3_s, activebackground=co3_s, command=lambda: pegar_valor('2'),
              fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
              overrelief=RIDGE)
b_13.place(x=67, y=244)
b_14 = Button(root, text='3', width=3, height=2, bg=co3, highlightbackground=co3_s, activebackground=co3_s, command=lambda: pegar_valor('3'),
              fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
              overrelief=RIDGE)
b_14.place(x=134, y=244)
b_15 = Button(root, text='+', width=3, height=2, bg=co4, highlightbackground=co4_s, activebackground=co4_s, command=lambda: pegar_valor('+'),
              fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
              overrelief=RIDGE)
b_15.place(x=201, y=244)

b_16 = Button(root, text='0', width=3, height=2, bg=co3, highlightbackground=co3_s, activebackground=co3_s, command=lambda: pegar_valor('0'),
              fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
              overrelief=RIDGE)
b_16.place(x=0, y=305)
b_17 = Button(root, text='.', width=3, height=2, bg=co3, highlightbackground=co3_s, activebackground=co3_s, command=lambda: pegar_valor('.'),
              fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
              overrelief=RIDGE)
b_17.place(x=67, y=305)
b_18 = Button(root, text='=', height=2, bg=co5, highlightbackground=co5_s, activebackground=co5_s, command=calcular,
              fg=co1, activeforeground=co1, font=('Ivy 13 bold'), relief=RAISED,
              overrelief=RIDGE)
b_18.place(x=134, y=305, width=131)

root.mainloop()
