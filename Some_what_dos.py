import subprocess
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
     print('chatbot.py tictactoe.py Win_Chrome.exe Wind_Edge.exe Win_FireFox.exe')


 
  
  if UserInput == 'help':
    print('type dir to see files, type a file name to launch it, type exit to exit, and comment your ideas for files')

  if UserInput == 'Win_Chrome.exe':
    chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"

    subprocess.Popen(chrome)

  if UserInput == 'Win_Edge.exe':
    edge = " C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    subprocess.Popen(edge)

  if UserInput == 'Win_FireFox.exe':
    firefox = "C:\Program Files\Mozilla Firefox\firefox.exe"
  subprocess.Popen(firefox)
#amogus



  echo = print
  
