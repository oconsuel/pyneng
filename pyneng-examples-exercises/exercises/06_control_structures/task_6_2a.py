# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip = input('Введите IP-адрес: ')
pointer = ip.count('.')
if pointer != 3:
      print('Неправильный IP-адрес')
else:
      ip = ip.strip().split('.')
      firstint = ip[0].isdigit()
      secondint = ip[1].isdigit()
      thirdint = ip[2].isdigit()
      fourthint = ip[3].isdigit()
      if firstint is not True and secondint is not True and thirdint is not True and fourthint is not True:
         print('Введены не только числа')
      else:
            firstok = int(ip[0])
            secondok = int(ip[1])
            thirdok = int(ip[2])
            fourthok = int(ip[3])
            rangelist = list(range(0, 256))
            if firstok not in rangelist or secondok not in rangelist or thirdok not in rangelist or oktet4 not in rangelist:
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


