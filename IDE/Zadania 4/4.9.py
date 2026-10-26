def input_string(message):
    a=str(input(message))
    return a

def input_integer(message):
    a=int(input(message))
    return a

def input_real(message):
    a=float(input(message))
    return a

def input_boolean(message):
    if message =='y':
        return True
    else:
        return False