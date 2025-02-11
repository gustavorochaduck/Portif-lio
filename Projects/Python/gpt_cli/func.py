import os 
import time
import platform
import sys

sys_op = platform.system()

def typingAnimationClearProgram(text):
    count = 0
    while count < 3:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(0.5)
        clearProgram()
        count += 1 

def clearProgram():
    os.system('cls' if os.name == "nt" else "clear")

def installLibrary():
    #if sys_op == 'Windows':
    print(os.system("pip install openai"))
    return True

def computer_acsii():
    print(''' 
                                .,,uod8B8bou,,.
                        ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
                    ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
                    !...:!TVBBBRPFT||||||||||!!^^""'   ||||
                    !.......:!?|||||!!^^""'            ||||
                    !.........||||                     ||||
                    !.........||||   #By Gustavo       ||||
                    !.........||||                     ||||
                    !.........||||                     ||||
                    !.........||||                     ||||
                    !.........||||                     ||||
                    `.........||||                    ,||||
                    .;.......||||               _.-!!|||||
            .,uodWBBBBb.....||||       _.-!!|||||||||!:'
            !YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
            !..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
            !....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
            !......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
            !........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
            `..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
            `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
                `........::::::::::::::::;iof688888888888888888888b.     `
                `......:::::::::;iof688888888888888888888888888888b.
                    `....:::;iof688888888888888888888888888888888899fT!
                    `..::!8888888888888888888888888888888899fT|!^"'
                        `' !!988888888888888888888888899fT|!^"'
                            `!!8888888888888888899fT|!^"'
                            `!988888888899fT|!^"'
                                `!9899fT|!^"'
                                `!^"'
        ''')
    
    