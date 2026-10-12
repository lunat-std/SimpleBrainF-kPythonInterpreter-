
index = 0   
maxCells = 100
cells = [0] * maxCells
commands = []
validCommands = "><+-.,[]"
commandIndex = 0
bfCommand = input()

debugMode = True

commands = [c for c in bfCommand if c in validCommands]
def moveRight():
    global index
    index += 1 
    if(index >= maxCells):
        index = 0
 
def moveLeft():
    global index
    index -= 1 
    if(index < 0):
        index = maxCells - 1

def Increment():
    cells[index] += 1

def decrement():
    cells[index] -= 1 

def write():
    cells[index] = int(input())

def printCell():
    print(chr(cells[index]), end='' + "\n")

commandIndex = 0
while commandIndex < commands.__len__():
    c = commands[commandIndex]

    if(c == '>'):
        moveRight()
    elif(c == '<'):
        moveLeft()
    elif(c == '+'):
        Increment()
    elif(c == '-'):
        decrement()
    elif(c == ','):
        write()    
    elif(c == '.'):
        printCell()
    elif c == '[':
        if cells[index] == 0:
            nest = 1
            while nest > 0:
                commandIndex += 1
                if commands[commandIndex] == '[':
                    nest += 1
                elif commands[commandIndex] == ']':
                    nest -= 1
    elif c == ']':
        if cells[index] != 0:
            nest = 1
            while nest > 0:
                commandIndex -= 1
                if commands[commandIndex] == ']':
                    nest += 1
                elif commands[commandIndex] == '[':
                    nest -= 1

    commandIndex += 1
if(debugMode):
    print("memory: ")
    for c in cells:
        print(c)            