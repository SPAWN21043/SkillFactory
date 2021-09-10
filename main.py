def information():
    print("I    Добро пожаловать!    I")
    print("I  В игру крестики нолики I")
    print("I-------------------------I")
    print("I  Для победы необходимо  I")
    print("I      поставить вряд     I")
    print("I        3 крестика       I")
    print("I           или           I")
    print("I        3 нолика         I")
    print("I-------------------------I")
    print("I    формат ввода: x y    I")
    print("I    x - номер строки     I")
    print("I    y - номер столбца    I")
    print()


information()


field = [[" "] * 3 for i in range(3)]  # Игровое поле из пробелов через цикл и range


def show():  # Функция вывода поля
    print(f"  | 0 | 1 | 2 |")
    print(f"---------------")
    for i in range(3):
        print(f'{i} | {field[i][0]} | {field[i][1]} | {field[i][2]} |')
        print(f"---------------")


def ask():
    while True:

        coord = input("Введите цифры через пробел  Ваш ход: ").split()

        if len(coord) != 2:
            print("Введите цифры через пробел")
            continue

        x, y = coord

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break
