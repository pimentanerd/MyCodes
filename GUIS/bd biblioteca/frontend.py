from tkinter import *
from backend import *
import datetime

#cria uma janela
window = Tk()
window.title("BD para biblioteca")
window.minsize(width=540, height=310)
window.maxsize(width=540, height=310)

def devo():
	now = datetime.datetime.now()
	if datetime.date(devolucao_text) > datetime.date.now():
		l1=Label(window, text="Fora de prazo", foreground = 'red')
		l1.grid(row=11, column=2)
	else:
		l1=Label(window, text="Dentro de prazo", foreground = 'blue')
		l1.grid(row=11, column=2)

def close_window():
    window.destroy()
#todos os objetos dessa janela devem ser declaradas nesse espaço
#Colunas/linhas da tabela
l1=Label(window, text="Titulo")
l1.grid(row=0, column=0)

l1=Label(window, text="Autor")
l1.grid(row=0, column=2)

l1=Label(window, text="Ano")
l1.grid(row=1, column=0)

l1=Label(window, text="Data de devolução (aaaa, mm, dd)")
l1.grid(row=1, column=2)

#Campos
def insert():
	conn = sqlite3.connect("livro.db")
	cur = conn.cursor()
	titulo = e1.get()
	ano = e2.get()
	autor = e3.get()
	devolucao = e4.get()
	cur.execute("""
	INSERT INTO livro(titulo, autor, ano, devolucao)
	VALUES (?,?,?,?)
	""", (titulo, autor, ano, devolucao))
	conn.commit()
	conn.close()

titulo_text=StringVar()
e1=Entry(window, textvariable=titulo_text)
e1.grid(row=0, column=1)

autor_text=StringVar()
e2=Entry(window, textvariable=autor_text)
e2.grid(row=0, column=3)

ano_text=StringVar()
e3=Entry(window, textvariable=ano_text)
e3.grid(row=1, column=1)

devolucao_text=int()
e4=Entry(window, textvariable=devolucao_text)
e4.grid(row=1, column=3)

def view():
	conn=sqlite3.connect("livro.db")
	cur=conn.cursor()
	cur.execute('''
	SELECT * FROM livro;
	''')

	for line in cur.fetchall():
		list1.insert(END, line)
#defina a ListBox
list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

#Adicionar a scrollbar para a lista
sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#Definir os botoes
b1 = Button(window, text="Ver tudo", width=18, command = view)
b1.grid(row=2, column=3)

b1 = Button(window, text="Procurar entrada", width=18, command = search)
b1.grid(row=3, column=3)

b1 = Button(window, text="Adicionar entrada", width=18, command = insert)
b1.grid(row=4, column=3)

b1 = Button(window, text="Atualizar selecionado", width=18, command = update)
b1.grid(row=5, column=3)

b1 = Button(window, text="Deletar selecionado", width=18)
b1.grid(row=6, column=3)

b1 = Button(window, text="Conectar", width=18, command = connect)
b1.grid(row=7, column=3)

b1 = Button(window, text="Fechar", width=18, command = close_window)
b1.grid(row=8, column=3)

b1 = Button(window, text="Verificar se está no prazo", width=18, command = devo)
b1.grid(row=9, column=3)


	
window.mainloop()