# function definition.Also ensure that variables in your function are not the same as variables in the main program.
FILEPATH = "todos.txt"  # this is a constant varialbe


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, 'r') as file_local:  # this is better way for handling file than the above commented file handling codes
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in a text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


