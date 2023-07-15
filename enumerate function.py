todos = []
while True:
    ask_choice = input("Please tell if you want to add , show , edit or exit the list ! ")
    ask_choice =ask_choice.strip()
    match ask_choice:
        case 'add':
            todo = input("Enter a todo : ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                print(index, "-", item)
        case 'edit':
            number = int(input("Enter the number of todo you want to edit : "))
            number = number - 1
            new_todo = input("Enter the new todo. ")
            todos[number]= new_todo
        case 'exit':
            break
        case whatever:
            print("Hey ! You entered an unknown case ...")
print("BYE !!!!")