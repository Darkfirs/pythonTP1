import random

SPRITE_CHAR = '█'
EMPTY_CHAR = ' '
ERROR_alpha = 0
ERROR_digit = 0


def generate_symmetric_sprite(size_s):
    sprite = []
    for i in range(size_s // 2):
        row = [SPRITE_CHAR if random.choice([True, False]) else EMPTY_CHAR for _ in range(size_s)]
        sprite.append(row + row[::-1])

    if size_s % 2 == 1:
        center_row = [SPRITE_CHAR if random.choice([True, False]) else EMPTY_CHAR for _ in range(size_s)]
        sprite.append(center_row + center_row[::-1])

    return sprite


def draw_sprite(sprite):
    for row in sprite:
        print(''.join(row))


def check_number(size_s):
    global ERROR_alpha, ERROR_digit
    if str(size_s).isalpha():
        ERROR_alpha += 1
        return False
    if int(size_s) > 0:
        return True
    ERROR_digit += 1
    return False


def main(size_s):
    global ERROR_alpha, ERROR_digit
    if check_number(size_s):
        size_s = int(size_s)
        while True:
            sprite = generate_symmetric_sprite(size_s)
            draw_sprite(sprite)

            more = input("Хотите сгенерировать еще один спрайт? (y/n): ").lower()
            if more == 'y':
                continue
            else:
                break
    else:
        if ERROR_alpha != 0:
            print("Вы должны ввести число")
            ERROR_alpha = 0
        if ERROR_digit != 0:
            ERROR_digit = 0
            print("Число должно быть больше 0")


if __name__ == "__main__":
    size_s = input("Введите размер стороны спрайта в пикселях (целое число): ")
    main(size_s)
