# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('ospf.txt', 'r') as text:
    ospfline = text.readlines()
    for lines in ospfline:
        ospf = lines.strip().split()
        prefix = ospf[0]
        admetric = ospf[1]
        nexthop = ospf[3]
        lastupdate = ospf[4]
        interface = ospf[5]

        admetric = admetric.strip('[]')
        nexthop = nexthop.rstrip(',')
        lastupdate = lastupdate.rstrip(',')

        ospf_route = """
        Prefix:                {0:19}
        AD/Metric:             {1:19}
        Next-Hop:              {2:19}
        Last lastupdate:       {3:19}
        Outbound Interface:    {4:19}
        """
        print(ospf_route.format(prefix,admetric,nexthop,lastupdate,interface))