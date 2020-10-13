# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan = input('Введите VLAN ID: ')
with open('CAM_table.txt', 'r') as start:
    lists = [] 
    for line in start: 
        if line.count('.') == 2: 
            a = line.strip('\n').split() 
            a.pop(-2) 
            if a[0] == vlan:
                print(a[0] + '    ' + a[1] + '   ' + a[2])
