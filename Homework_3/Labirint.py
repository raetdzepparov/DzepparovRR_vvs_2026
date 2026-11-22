from random import randint
from time import sleep
import keyboard

room = [[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]
x,y = randint(0,4),randint(0,4)
room[y][x] = 1
kx, ky = randint(0,4),randint(0,4)
t1x, t1y, t2x, t2y, t3x, t3y = randint(0,4),randint(0,4),randint(0,4),randint(0,4),randint(0,4),randint(0,4)
t1 = t2 = t3 = 1
px = py = 10
while (kx == t1x and ky == t1y) or (kx == t2x and ky == t2y) or (kx == t2x and ky == t2y):
        kx, ky = randint(0, 4), randint(0, 4)
k = 0
hp = 3
print('2 - ловушка   7 - кнопка   9 - сундук   8 - портал   1 - игрок')
print("Вы на ", "x:", x + 1, "y:", y + 1)
for i in room: print(i)
print("hp:", hp)
p = 0
while not(keyboard.is_pressed('space')):
        if keyboard.is_pressed('w') or keyboard.is_pressed('d') or keyboard.is_pressed('s') or keyboard.is_pressed('a'):
                if keyboard.is_pressed('w'):
                        if y-1 >= 0:
                                room[y][x] = p
                                p = 0
                                y -= 1
                if keyboard.is_pressed('s'):
                        if y+1 <= 4:
                                room[y][x] = p
                                p = 0
                                y += 1
                if keyboard.is_pressed('a'):
                        if x-1 >= 0:
                                room[y][x] = p
                                p = 0
                                x -= 1
                if keyboard.is_pressed('d'):
                        if x+1 <= 4:
                                room[y][x] = p
                                p = 0
                                x += 1
                room[y][x] = 1
                print('\n' * 48)
                print('2 - ловушка   7 - кнопка   9 - сундук   8 - портал   1 - игрок')
                print("Вы на ", "x:", x+1, "y:", y+1)
                for i in room: print(i)
                print("hp:", hp)
                sleep(0.2)
        if k and (x == px and y == py):
                print("Нажмите E, чтобы зайти в портал")
                keyboard.wait('e')
                print('\n' * 48, "Winner Winner Chicken dinner")
                break
        if x == kx and y == ky:
                p = 7
                if not(k):
                        px,py = randint(0,4),randint(0,4)
                        room[px][py] = 8
                        print('\n' * 48)
                        print('2 - ловушка   7 - кнопка   9 - сундук   8 - портал   1 - игрок')
                        print("Вы на ", "x:", x + 1, "y:", y + 1)
                        for i in room: print(i)
                        print("Поздравляю, вы активировали портал!")
                        print("hp:", hp)
                        k = 1
        if (x == t1x and y == t1y):
                p = 2
                if t1:
                        t1 = 0
                        hp -= 1
                        p = '*'
                        print('\n' * 48)
                        print('2 - ловушка   7 - кнопка   9 - сундук   8 - портал   1 - игрок')
                        print("Вы на ", "x:", x+1, "y:", y+1)
                        for i in room: print(i)
                        print("Ловушка!")
                        print("hp:", hp)

        elif (x == t2x and y == t2y):
                p = 2
                if t2:
                        t2 = 0
                        hp -= 1
                        print('\n' * 48)
                        print('2 - ловушка   7 - кнопка   9 - сундук   8 - портал   1 - игрок')
                        print("Вы на ", "x:", x+1, "y:", y+1)
                        for i in room: print(i)
                        print("Ловушка!")
                        print("hp:", hp)
        elif (x == t3x and y == t3y):
                p = 2
                if t3:
                        t3 = 0
                        hp -= 1
                        print('\n' * 48)
                        print('2 - ловушка   7 - кнопка   9 - сундук   8 - портал   1 - игрок')
                        print("Вы на ", "x:", x+1, "y:", y+1)
                        for i in room: print(i)
                        print("Ловушка!")
                        print("hp:", hp)
        if hp == 0:
                print('\n' * 48)
                print("GAME OVER!")
                break