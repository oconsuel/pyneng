# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите IP-адрес: ')
status = False
while not status:
    pointer = ip.count('.')
    if pointer != 3:
        print('Неправильный IP-адрес')
    elif firstint is not True and secondint is not True and thirdint is not True and fourthint is not True:        
        ip = ip.strip().split('.')
        firstint = ip[0].isdigit()
        secondint = ip[1].isdigit()
        thirdint = ip[2].isdigit()
        fourthint = ip[3].isdigit()
        print('Введены не только числа')
    elif firstok not in rangelist or secondok not in rangelist or thirdok not in rangelist or fourthok not in rangelist:      
        firstok = int(ip[0])
        secondok = int(ip[1])
        thirdok = int(ip[2])
        fourthok = int(ip[3])
        rangelist = list(range(0, 256))
        print('Введен неправильный диапазон')
    else:
        unicast = list(range(1, 224))
        multicast = list(range(224, 240))
        locbroadcast = [255,255,255,255]
        unassigned = [0,0,0,0]            

        if firstok in unicast:
            print('unicast IP')
        elif firstok in multicast:
            print('multicast IP')
        elif firstok in locbroadcast and secondok in locbroadcast and thirdok in locbroadcast and fourthok in locbroadcast:
            print('locbroadcast IP')
        elif firstok  in unassigned and secondok in unassigned and thirdok in unassigned and fourthok in unassigned:
            print('unassigned IP')
        else:
            print('unused IP')
        status = True
        continue
    ip = input('Введите IP-адрес ещё раз: ')

"""
ip = input('Введите IP-адрес(например 10.0.1.1): ')
status = False
while not status:
    if ip.count('.') != 3:
        print('Incorrect IPv4 address, add 3 dots between')
    elif ip.strip().split('.')[0].isdigit() is False or ip.strip().split('.')[1].isdigit() is False or ip.strip().split('.')[2].isdigit() is False or ip.strip().split('.')[3].isdigit() is False:
        print('Incorrect IPv4 address, ip must be a number')
    elif int(ip.strip().split('.')[0]) not in list(range(0, 256)) or int(ip.strip().split('.')[1]) not in list(range(0, 256)) or int(ip.strip().split('.')[2]) not in list(range(0, 256)) or int(ip.strip().split('.')[3]) not in list(range(0, 256)):
        print('Incorrect IPv4 address, use only numbers in range 0-255')
    else:
        ip = ip.strip().split('.')
        oktet1 = int(ip[0])
        oktet2 = int(ip[1])
        oktet3 = int(ip[2])
        oktet4 = int(ip[3])
        unicast = list(range(1, 224))
        multicast = list(range(224, 240))
        broadcast = [255,255,255,255]
        unassigned = [0,0,0,0]
        if oktet1 in unicast:
            print('This is unicast IP')
        elif oktet1 in multicast:
            print('This is multicast')
        elif oktet1 in broadcast and oktet2 in broadcast and oktet3 in broadcast and oktet4 in broadcast:
            print('This is broadcast IP')
        elif oktet1  in unassigned and oktet2 in unassigned and oktet3 in unassigned and oktet4 in unassigned:
            print('This is unassigned IP')
        else:
            print('This is unused IP')
        status = True
        continue
    ip = input('Введите IP-адрес ещё раз: ')

    """