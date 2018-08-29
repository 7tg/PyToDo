# !usr/bin/python3
import os
import platform
import time
import sys
from colorama import init
from termcolor import cprint
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected


ver = "0.05"


def readTodo(file):
    """Function for read todo.txt and turn it into a tuple list with counts
    Ex: [(1,"Blah Blah"),(2,"Blah Blah")]"""
    _file = open(file, 'r', encoding='utf8')
    file = _file.readlines()
    _file.close()
    lines = []
    for line in file:
        lines.append(line.strip())
    return list(enumerate(lines, 1))


def readDone(file):
    _file = open(file, 'r', encoding='utf8')
    file = _file.readlines()
    _file.close()
    lines = []
    for line in file:
        lines.append(line.strip())
    return list(enumerate(lines, 1))


def selectFile(folder):
    item_list = os.listdir("./" + folder + "/")
    item_enum = list(enumerate(item_list, 1))
    for count, item in item_enum:
        cprint("[" + str(count) + "]\t" + item, color='cyan')
    cprint("Select file to read-->    ", color='green', end='')

    inpt = input()
    if len(inpt) < 1:
        return selectFile(folder)

    select = int(inpt) - 1
    if select > len(item_enum) or select < 0:
        cprint("Input is out of index!", color='red', attrs=['bold'])
        wait()
        selectFile()
    _, file_name = item_enum[select]
    clear()
    return os.getcwd() + "/" + folder + "/" + file_name


def wait():
    input("\nPress enter to continue...")


def clear():
    current_os = platform.system()
    if current_os == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def help():
    clear()
    cprint("""Hi, this is the help text!
In order to see your to-do lists, you need to place them under the "todo/"
folder, your done jobs will be listed under "done/" folder.
For further questions contact me on GitHub :).
        """,
           color='cyan')


def printMenu():
    cprint("""
██████╗ ██╗   ██╗    ████████╗ ██████╗       ██████╗  ██████╗ 
██╔══██╗╚██╗ ██╔╝    ╚══██╔══╝██╔═══██╗      ██╔══██╗██╔═══██╗
██████╔╝ ╚████╔╝        ██║   ██║   ██║█████╗██║  ██║██║   ██║
██╔═══╝   ╚██╔╝         ██║   ██║   ██║╚════╝██║  ██║██║   ██║
██║        ██║          ██║   ╚██████╔╝      ██████╔╝╚██████╔╝
╚═╝        ╚═╝          ╚═╝    ╚═════╝       ╚═════╝  ╚═════╝  """,
           'green', attrs=['bold'])
    cprint("""  ----------------------   ver {}  -----------------------  """.format(ver),
           color='yellow')
    cprint("""      ------------------    By. TG   -------------------      """,
           color='cyan')
    print("")
    cprint("[1]  List To-Do", color='green', attrs=['bold'])
    cprint("[2]  Remove item from To-Do", color='cyan', attrs=['bold'])
    cprint("[3]  List Done", color='magenta', attrs=['bold'])
    cprint("[4]  Recover from Done", color='blue', attrs=['bold'])
    cprint("[9]  Help", color='white', attrs=['bold'])
    cprint("[0]  Exit", color='red', attrs=['bold'])


def listToDo():
    clear()
    file = selectFile("todo")
    todo = readTodo(file)
    for count, line in todo:
        cprint("[" + str(count) + "]\t" + line, color='cyan')
    cprint("\nTotal to-do's : " + str(len(todo)), color='magenta')
    return file, todo


def listDone(recover=False):
    clear()
    file = selectFile("done")
    done = readDone(file)
    for count, line in done:
        if recover is True:
            cprint("[" + str(count) + "]\t" + line, color='cyan')
        else:
            cprint(line, color='cyan')

    cprint("\nTotal done : " + str(len(done)), color='magenta')
    return file, done


def recoverFromDone():
    file, done = listDone(recover=True)

    cprint(
        "\nSingle [1] or [1,2,3,4,5], [0] to return to main menu", color='yellow')

    cprint("Select item to remove-->    ", color='green', end='')
    select = list(map(lambda x: int(x), input().split(',')))

    # Checking 0
    main() if 0 in select else 0

    # Checking if the select is out of index
    if max(select) > len(done) or min(select) < 1:
        cprint("Input is out of index!", color='red', attrs=['bold'])
        wait()
        recoverFromDone()
    print(file.replace('done', 'todo'))
    # print(done[select[0]][1].split("\t"))
    # Restoring item from done.txt

    todoFile = open(file.replace('done', 'todo'), 'r', encoding='utf8')
    todoLines = todoFile.readlines()
    todoFile.close()

    todoFile = open(file.replace('done', 'todo'), 'w', encoding='utf8')
    for i in select:
        line = done[i - 1][1].split("\t")[0]
        todoFile.write(line + "\n")
        cprint(
            "Recovered [" + line + "] from dodo.txt!", color='cyan', attrs=['bold'])
    for line in todoLines:
        todoFile.write(line)
    todoFile.close()

    doneFile = open(file, 'r', encoding='utf8')
    doneLines = doneFile.readlines()
    doneFile.close()

    doneFile = open(file, 'w', encoding='utf8')
    for count, line in enumerate(doneLines, 1):
        if count in select:
            continue
        doneFile.write(line)
    doneFile.close()


def removeToDo():
    clear()
    file, todo = listToDo()
    cprint(
        "\nSingle [1] or [1,2,3,4,5], [0] to return to main menu", color='yellow')

    cprint("Select item to remove-->    ", color='green', end='')
    select = list(map(lambda x: int(x), input().split(',')))

    # Checking 0
    main() if 0 in select else 0

    # Checking if the select is out of index
    if max(select) > len(todo) or min(select) < 1:
        cprint("Input is out of index!", color='red', attrs=['bold'])
        wait()
        removeToDo()

    # Removing item from todo.txt
    todoFile = open(file, 'w', encoding='utf8')
    for count, line in todo:
        if count in select:
            continue
        todoFile.write(line + "\n")
    todoFile.close()

    # Writing item to done.txt
    doneFile = open(os.getcwd() + '/done/' +
                    file.split('/')[-1].split('.')[0] + '.txt', 'a', encoding='utf8')
    for count, line in todo:
        if count in select:
            doneFile.write(
                line + "\t" + time.asctime(time.localtime(time.time())) + "\n")
            cprint(
                "Removed [" + line + "] from todo.txt, Good Job!", color='cyan', attrs=['bold'])
    doneFile.close()


def main():
    clear()
    printMenu()
    cprint("\n~/$>  ", color='green', end='', attrs=['bold'])
    select = input()
    if select == "1":
        listToDo()
        wait()
    elif select == "2":
        removeToDo()
        wait()
    elif select == "3":
        listDone()
        wait()
    elif select == "4":
        recoverFromDone()
        wait()
    elif select == "9":
        help()
        wait()
    elif select == "0":
        cprint("\nHave a good day..", color='cyan', attrs=['bold'])
        exit()
    main()


if __name__ == "__main__":
    main()
