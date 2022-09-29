import os
import platform

platform.system()  # returns the OS

print(os.name)  # OS

print('\n'.join(os.environ))  # returns enviroment info in a dictionary

print(os.environ['ONEDRIVE'])

os.getpid()  # actual process id

os.getcwd()  # actual directory

print(__file__)  # actual archive

print(os.path.basename(__file__))  # actual archive name

print(os.path.dirname(__file__))  # actual archive directory

print(os.path.abspath(__file__))  # absolute path

os.listdir()  # list the items in a directorty, if don't send any parameter, it will list the actual directory


