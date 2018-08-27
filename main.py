# !usr/bin/python3
import os
import platform
import time


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
        print("[" + str(count) + "]\t" + item)
    select = int(input("Select file to read->    ")) - 1
    if select > len(item_enum) or select < 0:
        print("Input is out of index!")
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
    print("""
██████╗ ██╗   ██╗████████╗ ██████╗       ██████╗  ██████╗ 
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔═══██╗      ██╔══██╗██╔═══██╗
██████╔╝ ╚████╔╝    ██║   ██║   ██║█████╗██║  ██║██║   ██║
██╔═══╝   ╚██╔╝     ██║   ██║   ██║╚════╝██║  ██║██║   ██║
██║        ██║      ██║   ╚██████╔╝      ██████╔╝╚██████╔╝
╚═╝        ╚═╝      ╚═╝    ╚═════╝       ╚═════╝  ╚═════╝                                                       
""")
    print("""----------------------   ver {}  -----------------------""".format(ver))
    print("""----------------------    By. TG   -----------------------""")
    print("")
    print("[1]  List To-Do")
    print("[2]  Remove item from To-Do")
    print("[3]  List Done")
    print("[0]  Exit")


def listToDo():
    clear()
    file = selectFile("todo")
    todo = readTodo(file)
    for count, line in todo:
        print("[" + str(count) + "]\t" + line)
    return file


def listDone():
    clear()
    done = readDone(selectFile("done"))
    for line in done:
        print(line)


def removeToDo():
    clear()
    file = listToDo()
    todo = readTodo(file)
    print("\nSingle [1] or [1,2,3,4,5], [0] to return to main menu")

    select = list(map(lambda x: int(x), input(
        "Select item to remove->    ").split(',')))

    # Checking 0
    main() if 0 in select else 0

    # Checking if the select is out of index
    if max(select) > len(todo) or min(select) < 1:
        print("Input is out of index!")
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
            print("Removed [" + line + "] from todo.txt, Good Job!")
    doneFile.close()


def main():
    clear()
    printMenu()
    select = input("->  ")
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
