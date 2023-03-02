import time
def menu():
    if input("Хотите сыграть? (y / n): ") == "y":
        pole_reload()

    else:
        print("Жаль, всего хорошего!")
        exit()

def pole_reload():
    print("\n" * 10)
    for i in range(len(pole)):
        for j in range(len(pole[i])):
            print(pole[i][j], end=' ')
        print()

def hod():
    while True:
        coord = input("Введите координаты: ").split()
        if len(coord) != 2:
            print("Введите 2 координата.")
            continue

        a, b = coord

        if not (a.isdigit()) or not (b.isdigit()):
            print("Введите числа!")
            continue

        a, b = int(a), int(b)

        if 1 > a > 3 and 1 > b > 3:
            print("Координаты вне игрового поля, попробуйте еще раз")
            continue

        if pole[a - 1][b - 1] != ".":
            print("Квадрат занят, попробуйте другой")
            continue

        return a, b

def proverka():
    winner = [((0, 0), (0, 1), (0, 2)), ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)), ((1, 0), (1, 1), (1, 2)),
              ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in winner:
        x, y, z = cord[0],cord[1],cord[2]
        if pole[x[0]][x[1]]==pole[y[0]][y[1]]==pole[z[0]][z[1]]!=".":
            pole_reload()
            print(f"Победили {pole[x[0]][x[1]]}!")
            return True
    return False

count = 0
pole = [["."]*3 for i in range(3)]
menu()

while True:
    count += 1

    pole_reload()

    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    a, b = hod()

    if count % 2 == 1:
        pole[a - 1][b - 1] = "X"
    else:
        pole[a - 1][b - 1] = "0"

    if proverka():
        break


    if count == 9:
        print("Ходы закончились")
        break


time.sleep(3)
