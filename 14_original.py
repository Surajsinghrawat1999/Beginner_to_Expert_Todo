#from function import get_todos,write_todos
import function

while True:
    ask_choice = input("Please tell if you want to add , show , edit , complete or exit : ")
    ask_choice = ask_choice.strip()


    if ask_choice.startswith('add'):
        todo = ask_choice[4:]

        todos = function.get_todos()

        todos.append(todo + '\n')

        function.write_todos(todos)


    elif  ask_choice.startswith('show'):

        todos = function.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)


    elif ask_choice.startswith('edit'):
        try :
            number =int(ask_choice[5:])                          #There is a error in this line and will be corrected in next code (10_trycatch)
            print(number)

            number = number - 1

            todos = function.get_todos()

            new_todo = input("Enter the new todo. ")
            todos[number] = new_todo + '\n'

            function.write_todos(todos)


        except ValueError:
            print("Your command is not valid . ")
            continue




    elif ask_choice.startswith('complete'):
        try:
            number = int(ask_choice[9:])

            todos = function.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            function.write_todos(todos)

            message = f"Todo {todo_to_remove } was removed from the list."
            print(message)
        except ValueError:
            print("Sorry there is no item with that name ! ")
            continue


    elif ask_choice.startswith('exit'):
        break

    else:
        print("Command is not valid . ")

print("BYE !!!!")