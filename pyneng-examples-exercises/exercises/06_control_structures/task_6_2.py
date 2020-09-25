# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите IP-адрес: ')
ip = ip.strip().split('.')
firstok = int(ip[0])
secondok = int(ip[1])
thirdok = int(ip[2])
fourthok = int(ip[3])

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