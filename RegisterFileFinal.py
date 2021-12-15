import os
NewUsername = input('Username: ')
NewPassword = input('Password: ')
LoginFile = ('''import time
import keyboard
import webbrowser
global Username; Username = '{1}'
global Password; Password = '{0}'
def PasswordCheck():
    EnteredUsername = input('Username: ')
    EnteredPassword = input('Password: ')
    global CorrectPassword; CorrectPassword = True if EnteredPassword == Password else False
    global CorrectUsername; CorrectUsername = True if EnteredUsername == Username else False
    print('Correct!') if CorrectPassword and CorrectUsername else print('Incorrect!'); Program(); print('Press enter to close...')
    while True: exit() if keyboard.is_pressed('enter') == True else time.sleep(0.001)
def Program():
    if CorrectPassword and CorrectUsername: 
        print('\\n','---'*10,'\\n',sep=''); print('Redirecting...'); print('\\n','---'*10,sep='') 
PasswordCheck()''').format(str(NewPassword),str(NewUsername))
open('LoginFile.py','a').write(LoginFile)
os.remove('RegisterFileFinal.py')
