import os
import time
from subprocess import call

echo = print



def open_py_file():
    call(["python", "chatbot.py"])

print("initializing emulator")
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
print("startup successful")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("initializing somewhat dos")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
call(["python","Update.py"])
print('type dir to see files, type a file name to launch it, type exit to exit,')


UserInput = ""

convoQue = 0
while (convoQue <= 5):   
  convoQue = int(convoQue + 0)
  UserInput = str.lower(input(": "))

  if UserInput == 'hi': 
    print('hola')

  if UserInput == 'what are you':
    print('I am a python dos emulator')

  if UserInput == 'what can you do':
    print('I can launch a few files')

  if UserInput == 'chatbot.py':
    os.system('clear')
    call(["python", "chatbot.py"])

  if UserInput == 'exit':
    exit()
  if UserInput == 'tictactoe.py':
    call(["python", "tictactoe.py"])
  
  if UserInput == 'dir':
     print('chatbot.py tictactoe.py')


  if UserInput == 'chatgpt':
    call(["python", "chatgpt.py"])
  
  if UserInput == 'help':
    print('type dir to see files, type a file name to launch it, type exit to exit, and comment your ideas for files')

  echo = print
  
