a = [1,2,3,4,5,6,7]
b = int(input('Введите номер дня недели '))
if b in a:
    if b == 6 or b == 7:
        print('Да')
    else:
        print('Нет')
else:
    print('Нет такого дня недели')