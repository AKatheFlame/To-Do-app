FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns a list of to-do items."""
    with open(filepath,'r') as file:
        todos=file.readlines()
    return todos


def write_todos(todos, filepath=FILEPATH):
    """ Writes a to-do items list in a text file."""
    with open(filepath,'w') as file:
        file.writelines(todos)
        

if __name__=="__main__":
    print("Hello")