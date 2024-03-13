import os
import time
from subprocess import call

print("initializing chatbot.py")
time.sleep(3)
os.system("clear")
print("startup successful")
time.sleep(1)
os.system("clear")
print("initializing chat_bot")
time.sleep(1)
os.system("clear")


UserInput = ""
ChatBot_Name = "Ron"
Username = ""



convoQue = 0
while (convoQue <= 5):   
  convoQue = int(convoQue + 0)
  UserInput = str.lower(input(": "))

  if UserInput == 'exit':
    exit()
  if UserInput == 'hi':
    print ("Hi")
  
  if UserInput == 'updatelog':
    print (" version 0.8 or something added update log, readding 'commands' ")
    

  
  
  
if UserInput == 'exit':
  call(['python', 'main.py'])
    

  

    
    
    

  

