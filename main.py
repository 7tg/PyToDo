# !usr/bin/python3
import os
import platform
import time
import sys
from colorama import init
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format


ver = "0.03"


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
    return lines


def selectFile(folder):
    item_list = os.listdir("./" + folder + "/")
    item_enum = list(enumerate(item_list, 1))
    for count, item in item_enum:
        cprint("[" + str(count) + "]\t" + item, color='cyan')
    cprint("Select file to read-->    ", color='green', end='')
    select = int(input()) - 1
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


def printMenu():
    cprint(figlet_format('PyTo-Do', font='larry3d'),
           'green', attrs=['bold'])
    cprint("""----------------------   ver {}  -----------------------""".format(ver),
           color='yellow')
    cprint("""----------------------    By. TG   -----------------------""",
           color='cyan')
    print("")
    cprint("[1]  List To-Do", color='green', attrs=['bold'])
    cprint("[2]  Remove item from To-Do", color='cyan', attrs=['bold'])
    cprint("[3]  List Done", color='magenta', attrs=['bold'])
    cprint("[0]  Exit", color='red', attrs=['bold'])


def listToDo():
    clear()
    file = selectFile("todo")
    todo = readTodo(file)
    for count, line in todo:
        cprint("[" + str(count) + "]\t" + line, color='cyan')
    return file


def listDone():
    clear()
    done = readDone(selectFile("done"))
    for line in done:
        cprint(line, color='cyan')


def removeToDo():
    clear()
    file = listToDo()
    todo = readTodo(file)
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
    cprint("-->  ", color='green', end='', attrs=['bold'])
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
    elif select == "0":
        cprint("\nHave a good day..", color='cyan', attrs=['bold'])
        exit()
    main()


if __name__ == "__main__":
    main()
