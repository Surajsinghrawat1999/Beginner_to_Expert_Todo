todos = []
while True:
    ask_choice = input("Please tell if you want to add , show or exit the list ! ")

    match ask_choice:
        case 'add':
            todo = input("Enter a todo : ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break
print("BYE !!!!")