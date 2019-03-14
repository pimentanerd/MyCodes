import os

#def my_function() cria uma funçao, quando eu dei print(fname+"pimenta") eu defini a funçao com o nome de fname e somei com pimenta, ou seja, sempre q eu clc my_function("...") logo a frente vai aparecer o pimenta

print("\n")
def my_function(fname):
  print(fname+" Pimenta")

my_function("Jônatas Fernandes")
my_function("Marisa de O. Fernandes")
my_function("Ezequiel")
my_function("Ester Fernandes")

print("\n")
#Aqui eu defini para que toda funçao que ficar em "branco" vai aparecer Brasil
def my_function(country = "Brasil"):
  print("Eu nasci no(a) "+country)

my_function("India")
my_function("Arabia")
my_function("Japão")
#Aqui no caso é a funçao em "branco"
my_function()


#Basicamente aqui a funçao foi uma incognita, eu usei o return 5 * x para multiplicar o 5 por qualquer numero que ocupar a funçao de x
def my_function(x):
  return 5 * x

print("\n")
print(my_function(3))
#Aqui o 2 está ocupando a funçao de 2
print(my_function(2))

#Aqui eu defini o nome da classe como pessoa e defini que irá aparecer o nome se eu der self.nome (o mesmo para idade e telefone), tambem defini p1(pessoa 1) colocando o nome, idade e o telefone
#Assim que a pessoa der print(p1.(nome, idade ou telefone)) vai aparecer na tela
print("\n")
class Pessoa:
	def __init__(self, nome, idade, telefone):
		self.nome = nome
		self.idade = idade
		self.telefone = telefone

p1 = Pessoa ("Jônatas", 15, 40028922)
print(p1.nome)
print(p1.idade)
print(p1.telefone)
#Tambem da para colocar tudo de uma só vez
print(p1.nome, p1.idade, p1.telefone)

print("\n")
#Coloque uma funçao que mostra uam mensagem de apresentação, e execute isso no objeto p1::
class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def myfunc(self):
    print("Olá meu nome é " + self.nome)

p1 = Pessoa("Jônatas", 15)
p1.myfunc()

print("\n")

class Pessoa:
	def __init__(self, nome, idade):
	  self.nome = nome
	  self.idade = idade

	def myfunc(self):
		print("Olá me chamo " + self.name)
#Aqui tinhamos que Joao tem 36 anos, porém podemos alterar o numero da idade e mostrar a idade.
#Podemos tambem deletar uma propriedade do objeto dando -> "del p1.idade" por exemplo.
#E também deletar um objeto dando -> "del p1" por exemplo.
p1 = Pessoa("Joao", 36)

p1.idade = 13

print(p1.idade)

print("\n")

#Modulos: modulo é um arquivo que contem um "set" de funçoes que você quer incluir no seu app.
#Aqui eu ja criei um modulo chamado "modulo.py" (modulos sao feitos em outros arquivos .py) vamos importa-lo:

import modulo

modulo.greeting("Jonathan")
print ("\n")
#Aqui importamos apenas a idade de p1 (Olha la no arquivo modulo.py :D)
import modulo

a = modulo.p1["idade"]
print(a)

#Tambem podemos renomear um modulo
import modulo as mm
a = mm.p1["idade"]
print(a)

#Aqui um modulozinho que mostra o seu SO
import platform

x = platform.system()
print(x)

print("\n")

#Este comando mostra a data e horario atual (em ingles)
import datetime

x = datetime.datetime.now()
print(x)

#Este mostra apenas o ano e o dia da semana (em ingles)
import datetime

x = datetime.datetime.now()

print(x.year)
#Dependo do valor a frente de "%" mostra-ra algo diferente
print(x.strftime("%A"))

os.system('pause')