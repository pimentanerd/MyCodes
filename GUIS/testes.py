from tkinter import *

window = Tk()
window.title('Meus testes :D')
window.minsize(width=420, height=310)
window.maxsize(width=2000, height=2000)

#Colunas/linhas
l1 = Label(window, text = "Linha 1")
l1.grid(row = 0, column = 0)

l1 = Label(window, text = "\tLinha1 na Coluna2")
l1.grid(row = 0, column = 2)

l1 = Label(window, text = "Linha 2")
l1.grid(row = 1, column = 0)

l1 = Label(window, text = "\tLinha2 na Coluna2")
l1.grid(row = 1, column = 2)

l1 = Label(window, text = "\n\n\n")
l1.grid(row = 1, column = 0)

#campos
text1 = StringVar()
e1 = Entry(window, textvariable = text1)
e1.grid(row = 0, column = 1)

text2 = StringVar()
e2 = Entry(window, textvariable = text2)
e2.grid(row = 1, column = 1)

text3 = StringVar()
e3 = Entry(window, textvariable = text3)
e3.grid(row = 0, column = 3)

text4 = StringVar()
e4 = Entry(window, textvariable = text4)
e4.grid(row = 1, column = 3)

text = Text(window, width = 20, height = 10)
text.grid(row=2, column=1, rowspan=6, columnspan=2)

window.mainloop()