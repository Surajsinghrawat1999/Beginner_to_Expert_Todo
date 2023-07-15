#optimize code
while True:
    ask_choice = input("Please tell if you want to add , show , edit , complete or exit : ")
    ask_choice = ask_choice.strip()

    if ask_choice.startswith('add'):
        todo = ask_choice[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)


    elif  ask_choice.startswith('show'):

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)


    elif ask_choice.startswith('edit'):
        number =int(ask_choice[5:]) #There is a error in this line and will be corrected in next code (10_trycatch)
        print(number)

        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter the new todo. ")
        todos[number] = new_todo + '\n'


        with open('todos.txt', 'w') as file:
            file.writelines(todos)


    elif ask_choice.startswith('complete'):
        number = int(ask_choice[9:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todos[index].strip('\n')

        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove } was removed from the list."
        print(message)


    elif ask_choice.startswith('exit'):
        break

    else :
        print("Command is not valid . ")

print("BYE !!!!")