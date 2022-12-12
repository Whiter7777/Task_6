import math as m
from haversine import haversine, Unit

a = (-77.189254, 40.201689)
b = (-84.376724, 33.725504)

print(haversine(a, b, unit=Unit.MILES))

# d = m.acos(m.sin(x1) * m.sin(x2) + m.cos(x1) * m.cos(x2) * m.cos(y1 - y2))
#
# R = 6371
#
# L = d * R
#
# print(L)

# d = arccos {sin(Фa)·sin(Фb) + cos(Фa)·cos(Фb)·cos(Лa - Лb)},
#
# где Фa и Фb — широты, Лa, Лb — долготы данных пунктов, d — расстояние между пунктами, измеряемое в радианах длиной дуги большого круга земного шара.
# Расстояние между пунктами, измеряемое в километрах, определяется по формуле:
#
# L = d·R,
#
# где R = 6371 км — средний радиус земного шара.