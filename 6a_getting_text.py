#getting the data from  text file to python

while True:
    ask_choice = input("Please tell if you want to add , show , edit , complete or exit : ")
    ask_choice =ask_choice.strip()


    match ask_choice:
        case 'add':
            todo = input("Enter a todo : ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Enter the number of todo you want to edit : "))
            number = number - 1
            new_todo = input("Enter the new todo. ")
            todos[number]= new_todo


        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)


        case 'exit':
            break
        case whatever:
            print("Hey ! You entered an unknown case ...")
print("BYE !!!!")