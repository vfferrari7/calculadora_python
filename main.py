#importar tkinter
from tkinter import *
from tkinter import ttk

#cores

black = "#000000"
white = "#ffffff"
blue = "#444f69"
grey = "#6d6d6e"
orange = "#fc7600"

janela =Tk()
janela.title("Calculadora") 
janela.geometry("235x305")
janela.config(bg=black)

#frames

frame_tela = Frame(janela, width=235, height=50,bg=blue)
frame_tela.grid(row=0, column=0)

frame_body = Frame(janela, width=235, height=268,)
frame_body.grid(row=1, column=0)

#variavel valor total

valor_total = ''

#label

valor_text = StringVar()

#lógica da função

def entrada_valores(event):

    global valor_total
    valor_total = valor_total + str(event)

    valor_text.set(valor_total)

#função-calculo
    
def calcular():
    global valor_total
    resultado = eval(valor_total)

    valor_text.set(str(resultado))

#limpar-tela

def limpar_tela():
    global valor_total
    valor_total = ""
    valor_text.set("")




valor_text = StringVar()
app_label = Label(frame_tela, textvariable=valor_text, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=blue, fg=white)
app_label.place(x=0, y=0)

#botões-inicio

b_clean = Button(frame_body, command= limpar_tela, text="C", width=11, height=2, bg=grey, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_clean.place(x=0, y=0)

b_porcentagem = Button(frame_body, command = lambda: entrada_valores('%'), text="%", width=5, height=2 ,bg=grey, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_porcentagem.place(x=118, y=0)

b_divisao = Button(frame_body, command = lambda: entrada_valores('/'), text="/", width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_divisao.place(x=177, y=0)

b_sete = Button(frame_body, command = lambda: entrada_valores('7'), text="7", width=5, height=2 ,bg=grey, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_sete.place(x=0, y=52)

b_oito = Button(frame_body, command = lambda: entrada_valores('8'), text="8", width=5, height=2 ,bg=grey, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_oito.place(x=60, y=52)

b_nove = Button(frame_body, command = lambda: entrada_valores('9'), text="9", width=5, height=2 ,bg=grey, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_nove.place(x=118, y=52)

b_asterisco = Button(frame_body, command = lambda: entrada_valores('*'), text="*", width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_asterisco.place(x=177, y=52)

b_quatro = Button(frame_body, command = lambda: entrada_valores('4'), text="4", width=5, height=2 ,bg=grey, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_quatro.place(x=0, y=104)

b_cinco = Button(frame_body, command = lambda: entrada_valores('5'), text="5", width=5, height=2 ,bg=grey, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_cinco.place(x=60, y=104)

b_seis = Button(frame_body, command = lambda: entrada_valores('6'), text="6", width=5, height=2 ,bg=grey, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_seis.place(x=118, y=104)

b_menos = Button(frame_body, command = lambda: entrada_valores('-'), text="-", width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_menos.place(x=177, y=104)

b_um = Button(frame_body, command = lambda: entrada_valores('1'), text="1", width=5, height=2 ,bg=grey, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_um.place(x=0, y=155)

b_dois = Button(frame_body, command = lambda: entrada_valores('2'), text="2", width=5, height=2 ,bg=grey, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_dois.place(x=60, y=155)

b_tres = Button(frame_body, command = lambda: entrada_valores('3'), text="3", width=5, height=2 ,bg=grey, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_tres.place(x=118, y=155)

b_mais = Button(frame_body, command = lambda: entrada_valores('+'), text="+", width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_mais.place(x=177, y=155)

b_zero = Button(frame_body, command = lambda: entrada_valores('0'), text="0", width=11, height=2, bg=grey, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_zero.place(x=0, y=205)

b_ponto = Button(frame_body, command = lambda: entrada_valores('.'), text=".", width=5, height=2 ,bg=grey, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_ponto.place(x=118, y=205)

b_igual = Button(frame_body, command= calcular, text="=", width=5, height=2, bg=orange, fg=white, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_igual.place(x=177, y=205)

#botões-fim



janela.mainloop()