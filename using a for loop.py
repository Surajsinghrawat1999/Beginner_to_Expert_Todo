todos = []
while True:
    ask_choice = input("Please tell if you want to add , show or exit the list ! ")
    ask_choice =ask_choice.strip()
    match ask_choice:
        case 'add':
            todo = input("Enter a todo : ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
        case whatever:
            print("Hey ! You entered an unknown case ...")
print("BYE !!!!")