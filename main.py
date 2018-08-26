# !usr/bin/python3
import os
import platform
import time


ver = "0.01"


def readTodo():
    """Function for read todo.txt and turn it into a tuple list with counts
    Ex: [(1,"Blah Blah"),(2,"Blah Blah")]"""
    _file = open('todo.txt', 'r')
    file = _file.readlines()
    _file.close()
    lines = []
    for line in file:
        lines.append(line.strip())
    return list(enumerate(lines, 1))


def readDone():
    _file = open('done.txt', 'r')
    file = _file.readlines()
    _file.close()
    lines = []
    for line in file:
        lines.append(line.strip())
    return lines


def wait():
    input("\nPress enter to continue...")


def clear():
    current_os = platform.system()
    if current_os == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def printMenu():
    print("-------		Py To-Do	-------")
    print("-------		ver {}	-------".format(ver))
    print("-------		   TG   	-------")
    print()
    print("[1]	List To-Do")
    print("[2]	Remove item from To-Do")
    print("[3]	List Done")
    print("[0]	Exit")


def listToDo():
    clear()
    todo = readTodo()
    for count, line in todo:
        print("[" + str(count) + "]\t" + line)


def listDone():
    clear()
    done = readDone()
    for line in done:
        print(line)


def removeToDo():
    clear()
    listToDo()
    todo = readTodo()
    select = int(input("Select item to remove-> 	"))

    # Checking if the select is out of index
    if select > len(todo) or select < 1:
        print("Input is out of index!")
        wait()
        removeToDo()

    # Removing item from todo.txt
    todoFile = open('todo.txt', 'w')
    for count, line in todo:
        if count == select:
            continue
        todoFile.write(line + "\n")
    todoFile.close()

    # Writing item to done.txt
    doneFile = open('done.txt', 'a')
    _, line = todo[select - 1]
    doneFile.write(
        line + "\t" + time.asctime(time.localtime(time.time())) + "\n")
    doneFile.close()

    print("Removed [" + line + "] from todo.txt, Good Job!")


def main():
    clear()
    printMenu()
    select = input("->	")
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
        print("\nHave a good day..")
        exit()
    main()


if __name__ == "__main__":
    main()
