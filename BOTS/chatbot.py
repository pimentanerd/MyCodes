import os
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

chatbot = ChatBot('Sagiri')



greetings = ['Oi',
	   		 'Olá, tudo bem?',
	   		 'Tudo, e você?',
	   		 'Eu também, obrigado']


chatbot.set_trainer(ListTrainer)

chatbot.train(greetings)

os.system('cls')

while True:
	os.system('color 0e')
	voce = input('\tVocê: ')
	response = chatbot.get_response(voce)
	print('\tSagiri: ', response)