from cx_Freeze import setup, Executable

setup(name='PyToDo',
 version='0.04',
 description='PyTo-Do by Tayyip Gören',
 executables=[Executable('main.py')])