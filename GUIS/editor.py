from tkinter import *
from tkinter import filedialog

root = Tk("editor de texto")
root.title('Editor de texto By: Jhonny')
text = Text(root)
text.grid()

#Função para salvar o arquivo
def saveas():
    global text  
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()

button = Button(root, text = "Save", command = saveas) 
button.grid()

def FontHelvetica():
   global text
   text.config(font="Helvetica")
def FontCourier():
   global text
   text.config(font="Courier")
def Arial():
	global text
	text.config(font = "Arial")

font=Menubutton(root, text="Font") 
font.grid() 
font.menu=Menu(font, tearoff=0) 
font["menu"]=font.menu
Helvetica=IntVar() 
arial=IntVar() 
times=IntVar() 
Courier=IntVar()
font.menu.add_checkbutton(label="Courier", variable=Courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=Helvetica, command=FontHelvetica) 
font.menu.add_checkbutton(label = "Arial", variable = Arial, command = Arial)


root.mainloop()