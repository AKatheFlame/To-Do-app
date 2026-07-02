# from functions import get_todos,write_todos
import functions
import time

now=time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_prompt="Type add , show ,edit, complete or exit: "
    choice=input(user_prompt).lower().strip()

    if choice.startswith('add'):
        todo=choice[4:]

        todos=functions.get_todos()

        todos.append(todo+ '\n')

        functions.write_todos(todos, 'todos.txt' )

    elif choice.startswith('show'):
        todos=functions.get_todos()
        new_todo=[i.strip('\n') for i in todos]
        for index,i in enumerate(new_todo):
            i=i.capitalize()
            print(f"{index+1}.{i}")

    elif choice.startswith('edit'):
        try:
            n=int(choice[5:])
            n-=1
            todos=functions.get_todos()

            new_todo=input("Enter new todo: ") +'\n'
            todos[n]=new_todo + '\n'

            functions.write_todos(todos, 'todos.txt')
        
        except ValueError:
            print("Your command is not valid")
            continue

    elif choice.startswith('complete'):
        try:
            num=int(choice[9:])
            todos=functions.get_todos()
            index=num-1
            removed=todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos, 'todos.txt')
            
            message=f"Todo {removed} was removed from the list."
            print(message)
        
        except IndexError:
            print("There is no item with that number.")
            continue

    elif choice.startswith('exit'):
        break
    
    else:
        print("Invalid choice.")

print("Bye!")