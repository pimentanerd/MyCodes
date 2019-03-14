from cx_Freeze import setup, Executable 

setup (
	name="ChatBot by:Jhonny",
	version = "1.0",
	description = "TextBot",
	executables = [Executable ("textbot.py")])