

def input_number():
    number = int(input('введите число:  '))
    return number

def input_operation():
    operation = input('введите операцию +, -, *, /, = :  ')
    return operation

def print_result(smth):
    print(smth)

def choice_calc():
    calc_version = input('Выберите вид калькулятора, который вы хотите использовать:\n'
                         'к1 - строковый, к2 - кнопочный: ')
    return calc_version

def else_res():
    print('Вы ввели не тот вариант, введите "к1" или "к2": ')

def enter_expression():
    a = input('Введите выражение, которое необходимо посчитать: ')
    res = eval(a)
    return a, res