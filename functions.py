file_1 = 'todos.txt'


def get_todos(filepath=file_1):
    """ Reads a text file and return the list of 
    todo items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=file_1):
    """ writes or deletes a line of data in a txt file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":

    print('hello from functions')
    print(get_todos())
