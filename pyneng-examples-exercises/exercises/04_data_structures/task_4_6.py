# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last lastupdate           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = '      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf = ospf_route.split()

prefix = ospf[0]
admetric = ospf[1]
nexthop = ospf[3]
lastupdate = ospf[4]
interface = ospf[5]

admetric = admetric.strip('[]')
nexthop = nexthop.rstrip(',')
lastupdate = lastupdate.rstrip(',')

"""print(prefix)
print(admetric)
print(nexthop)
print(lastupdate)
print(interface)"""

ospf_route = """
Prefix:                {0:19}
AD/Metric:             {1:19}
Next-Hop:              {2:19}
Last lastupdate:       {3:19}
Outbound Interface:    {4:19}
"""
print(ospf_route.format(prefix,admetric,nexthop,lastupdate,interface))