# Лошкарев Антон 559704, 4 вариант

import time, os

RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
BLUE = '\u001b[44m'
RESET = '\u001b[0m'
pixel = ' '
COLORS = [RED, WHITE, BLACK, BLUE]
RIGHT = '\x1b['


def loading():
    for proc in range(100):
        print(f'\u001b[20DLoading... {proc + 1}%', end='', flush=True)
        time.sleep(0.05)
    print(' Done!')


# loading()

# Первое задание - сделать флаг Польши
def flag():
    width = 30
    height = 10
    for i in range(height):
        if i < height // 2:
            print(WHITE + pixel * width + RESET)
        else:
            print(RED + pixel * width + RESET)


# Второе задание, сделал узор под номером d
def pattern(scale=3, repeat=2):
    width = 11 * scale
    height = 5 * scale
    for i in range(height // 10):
        print(BLACK + pixel * width * repeat + RESET)
    for n in range(repeat):
        for j in range(height // 10):
            print((WHITE + pixel * 5 * scale + BLACK + pixel * scale + WHITE + pixel * 5 * scale) * repeat + RESET)
        for k in range(height // 10):
            print(BLACK + pixel * width * repeat + RESET)
        for l in range(height // 10):
            print((WHITE + pixel * 2 * scale + BLACK + pixel * scale + WHITE + pixel * 5 * scale + BLACK + pixel * scale + WHITE + pixel * 2 * scale) * repeat + RESET)
        for m in range(height // 10):
            print(BLACK + pixel * width * repeat + RESET)


# Третье задание - анимация из 4 кадров, фигура сдвигается вправо
def animation():
    for n in range(3):
        for color in COLORS:
            shift = COLORS.index(color) * 10 + 1
            for i in range(1, 21):
                if i < 11:
                    print(f'{RIGHT}{shift}C{color}{pixel * i * 2}{RESET}')
                else:
                    print(f'{RIGHT}{shift}C{color}{pixel * 2 * (21 - i)}{RESET}')
            time.sleep(1)
            os.system('cls')


# Четвертое задание - диаграмма средних по модулю первых и вторых 125 чисел
def sequence():
    file = open('sequence.txt', 'r')
    nums_data = []
    for line in file:

        nums_data.append(float(line))
    sum1 = 0
    sum2 = 0
    list1 = []
    list2 = []
    for num in nums_data:
        if len(list1) < 125:
            list1.append(abs(num))
        else:
            list2.append(abs(num))
    for i in range(125):
        sum1 += list1[i]
        sum2 += list2[i]
    file.close()
    average1 = sum1 / len(list1)
    average2 = sum2 / len(list2)
    average = average1 + average2
    print(f'{BLUE}{" " * int(average1 / average * 50)}{RESET} {average1 / average * 100:.3f}%')
    print(f'{RED}{" " * int(average2 / average * 50)}{RESET} {average2 / average * 100:.3f}%')


# Дополнительное задание - сгенерировать график y = x ** 0.5
def function():
    height = 10
    width = 41
    x_max = 81
    result = []
    for j in range(width):
        x = j * x_max / (width - 1)
        result.append(x ** 0.5)
    step = round((result[width - 1] - result[0]) / (height - 1))
    plot_list = [[0 for j in range(width)] for i in range(height)]
    for j in range(width):
        row = round(result[j] / step)
        plot_list[height - 1 - row][j] = 1
    for i in range(height):
        line = f'{step * (height - 1 - i)} |'
        for j in range(width):
            if plot_list[i][j] == 1:
                line += WHITE + pixel + RESET
            else:
                line += pixel
        print(line)
    print(pixel * 2 + '+' + '-' * width)
    print(pixel * 3 + '0' + pixel * (width - 3) + str(x_max))


#animation()
#loading()
#flag()
#loading()
#pattern()
#loading()
#sequence()
#loading()
#function()
