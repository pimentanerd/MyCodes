import os
import subprocess

x = True

while x == True:
	os.system('color 0e')
	print('========================================================================================================================\n')
	print('\t\t\t\t\t\t\tQuick Launch\n')
	print('========================================================================================================================')

	print('\t1 - Sublime Text')
	print('\t2 - Minecraft')
	print('\t3 - Steam')
	print('\t4 - SquareCraft')

	choice = input('\t> ')

	if choice == '1':
		subprocess.Popen([r'C:\Program Files\Sublime Text 3\\sublime_text.exe', '-new-tab'])

	elif choice == '2':
		subprocess.call(r'C:\Users\DESK\Desktop\Jhonny\jogos\\minecraft.jar', shell=True)

	elif choice == '3':
		subprocess.Popen([r'C:\Program Files (x86)\Steam\\Steam.exe', '-new-tab'])

	elif choice == '4':
		subprocess.Popen(r'C:\Users\DESK\Desktop\Jhonny\SquareCraft (hamachi)\\start.bat', shell=True)

	print('\n\tDeseja adicionar mais algum? (y/n)')
	loop = input('\t> ')
	if loop == 'y':
		os.system('cls')
		x = True
	else:
		x = False