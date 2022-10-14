def check_if_empty(array):

    if array == []:
        return 0

    filled = 0

    if array[0] != '':
        filled = 1

    return filled + check_if_empty(array[1:])
