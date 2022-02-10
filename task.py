import sys
from typing import Text

def help():
    help = '''Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics
'''
    sys.stdout.buffer.write(help.encode('utf8'))


def getTask():
    with open("task.txt", "r") as f:
        text = f.read()
        return text

def setData():
    with open("task.txt", "a") as f:
        f.write(f"{sys.argv[2]} {sys.argv[3]}")
        f.write("\n")

def sort(line):
    line_fields = line.strip().split(' ')
    amount = float(line_fields[0])
    return amount

def sortFile():
    fp = open("task.txt", 'r')
    contents = fp.readlines()
    contents.sort(key=sort)
    fp.close()

    fp = open("task.txt", "w")
    for line in contents:
        fp.write(line)
    fp.close()
    


def add():
    setData()
    addStatement = f'''Added task: "{sys.argv[3]}" with priority {sys.argv[2]}''' + "\n"
    sys.stdout.buffer.write(addStatement.encode('utf8'))


def ls(): 
    sortFile()
    fp = open("task.txt", "r")
    contents = fp.readlines()
    if(len(contents) > 0):
        i = 1
        for line in contents:
            temp = line.split(' ', 1)
            printIndex = f"{i}. "
            sys.stdout.buffer.write(printIndex.encode('utf8'))
            i = i + 1
            Temp = temp[1].strip('\n')
            printTemp = f"{Temp} [{temp[0]}]\n"
            sys.stdout.buffer.write(printTemp.encode('utf8'))
            # print(f"[{temp[0]}]")
    elif(len(contents)<=0):
        fault = "There are no pending tasks!" 
        sys.stdout.buffer.write(fault.encode('utf8'))
    fp.close()

def delete(index):
    f = open("task.txt")
    contents = f.readlines()
    if(len(contents)<index or index<=0):
        Error = f"Error: task with index #{index} does not exist. Nothing deleted." + '\n'
        sys.stdout.buffer.write(Error.encode('utf8'))
    else:
        contents.pop(index-1)
        printDel = f"Deleted task #{index}"
        sys.stdout.buffer.write(printDel.encode('utf8'))
    f.close()

    f = open("task.txt", "w")
    for line in contents:
        f.write(line)
    f.close()

def done(index):
    f = open("task.txt")
    contents = f.readlines()
    if(len(contents)<index or index <= 0):
        Error = f"Error: no incomplete item with index #{index} exists."
        sys.stdout.buffer.write(Error.encode('utf8'))
    else:
        completed = contents[index-1] 
        contents.pop(index-1)
        printDone = "Marked item as done." 
        sys.stdout.buffer.write(printDone.encode('utf8'))
    f.close()

    f = open("task.txt", "w")
    for line in contents:
        f.write(line)
    f.close()
    
    task = completed.split(" ", 1)

    f = open("completed.txt", "a")
    f.write(task[1])
    f.close()

def report():
    f = open("task.txt")
    contents = f.readlines()
    printPending = f"Pending : {len(contents)}\n"
    # sys.stdout.buffer.write(printPending.encode('utf8'))
    i = 1
    test = printPending + ""
    for line in contents:
        temp = line.split(' ', 1)
        printIndex = f"{i}. "
        test = test + printIndex
        # sys.stdout.buffer.write(printIndex.encode('utf8'))
        i = i + 1
        Temp = temp[1].strip('\n')
        printTemp = f"{Temp} [{temp[0]}] \n"
        test = test + printTemp
        # sys.stdout.buffer.write(printTemp.encode('utf8'))
    f.close()

    # newline = "\n"
    # sys.stdout.buffer.write(newline.encode('utf8'))
    
    # print("\n")

    f = open("completed.txt")
    text = f.read()
    list = text.split("\n")
    count = len(list)
    printCompleted = f"Completed : {count-1}\n"
    # sys.stdout.buffer.write(printCompleted.encode('utf8'))
    test = test + printCompleted
    m = 1
    for i in list:
        if(m<count):
            printCompletedTask = f"{m}. {i}\n"
            # sys.stdout.buffer.write(printCompletedTask.encode('utf8'))
            test = test + printCompletedTask
            m = m + 1
        else:
            break
    f.close()
    return test
    # sys.stdout.buffer.write(test.encode('utf8'))

def switch(utility):
    if(len(sys.argv) > 1):
        if(utility[1] == "help" ):
            help()
        elif(utility[1] == "add"):
            if(len(utility)<3):
                Error = "Error: Missing tasks string. Nothing added!"
                sys.stdout.buffer.write(Error.encode('utf8'))
            else: 
                add()
        elif(utility[1] == "ls"):
            ls()
        elif(utility[1] == "del"):
            if(len(utility)>2):
                index = int(utility[2])
                delete(index)
            else:
                printError = "Error: Missing NUMBER for deleting tasks."
                sys.stdout.buffer.write(printError.encode('utf8'))
        elif(utility[1] == "done"):
            if(len(utility)>2):
                index = int(utility[2])
                done(index)
            else:
                printError = "Error: Missing NUMBER for marking tasks as done."
                sys.stdout.buffer.write(printError.encode('utf8'))
        elif(utility[1] == "report"):
            sys.stdout.buffer.write(report().encode('utf8'))
        else:
            wrongInput = "wrong input"
            sys.stdout.buffer.write(wrongInput.encode('utf8'))
    else:
        help()


utility = sys.argv


switch(utility)

