#optimize code
while True:
    ask_choice = input("Please tell if you want to add , show , edit , complete or exit : ")
    ask_choice = ask_choice.strip()
    match ask_choice:
        case 'add':
            todo = input("Enter a todo : ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)


        case 'show':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)


        case 'edit':
            number = int(input("Enter the number of todo you want to edit : "))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter the new todo. ")
            todos[number] = new_todo + '\n'


            with open('todos.txt', 'w') as file:
                file.writelines(todos)


        case 'complete':
            number = int(input("Number of the todo to complete: "))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove } was removed from the list."
            print(message)


        case 'exit':
            break


        case whatever:
            print("Hey ! You entered an unknown case ...")

print("BYE !!!!")