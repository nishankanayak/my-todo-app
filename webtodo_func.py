FILEPATH="web_todo.txt"
def get_todos(filepath=FILEPATH):
    """reading the file and returning the variable"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    """writing the file wihtout returning it"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

