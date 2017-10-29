import random

def game(gamer):
    line_1 = [field[1], field[2], field[3]]
    line_2 = [field[4], field[5], field[6]]
    line_3 = [field[7], field[8], field[9]]
    column_1 = [field[1], field[4], field[7]]
    column_2 = [field[2], field[5], field[8]]
    column_3 = [field[3], field[6], field[9]]
    diag_1 = [field[1], field[5], field[9]]
    diag_2 = [field[3], field[5], field[7]]
    lines = [line_1, line_2, line_3, column_1, column_2, column_3, diag_1, diag_2]
    for line in lines:
        if line[0] == line[1] == line[2] != '-':
            return gamer
    return True



def print_field(field):
    print(field[1], field[2], field[3])
    print(field[4], field[5], field[6])
    print(field[7], field[8], field[9])

def game_comp():
    while game(user) is True:
        if len(field_list) == 0:
            return 'НИЧЬЯ!'
        else:
            print('мой ход:')
            m = random.choice(field_list)
            field[m] = comp
            field_list.remove(m)
            print_field(field)
            return game_user()
    print('YOU_WIN!')


def game_user():
    while game(comp) is True:
        if len(field_list) == 0:
            return 'НИЧЬЯ!'
        else:
            n = int(input('выбери номер любой пустой клеточки'))
            if n in field_list:
                field[n] = user
                field_list.remove(n)
                print_field(field)
                return game_comp()
            else:
                print('ЕЩЕ РАЗ')
                game_user()
    print('I_WIN!')



def choice_gamer():
    user = input('выбери X или O:')
    if user == 'X' or user == 'x' or user == 'Х' or user == 'х':
        user = 'X'
        return [user, 'O']
    elif user == '0' or user == 'O' or user == 'О':
        user == 'O'
        return [user, 'X']
    else:
        print('неверно')
        return choice_gamer()


field_list = [int(i) for i in range(1,10)]

field = dict.fromkeys(field_list, '-')
field_exp = {a: a for a in range(1, 10)}
print('запомни нумерацию клеток:')
print_field(field_exp)
print()

user, comp = choice_gamer()

print('You are', user)
print('I am', comp)
print()

# print('запомни нумерацию клеток:')
# print_field(field_exp)
# print()

if user == 'X':
    print_field(field)
    print(game_user())
else:
    print(game_comp())


