import model

def input_number():
    number = int(input('Введите число: '))
    return number

def input_operation():
    operation = input('Введите операцию (+, -, *, /, = : ')
    return operation

def get_intermediate_result():
    global intermediate_result
    return intermediate_result

def print_result(smth):
    print(smth)