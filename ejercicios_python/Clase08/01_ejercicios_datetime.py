# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 22:45:52 2021

@author: rokefeler@gmail.com
"""

#%%
import datetime

fecha_hora = datetime.datetime.now()
print(fecha_hora)
#2021-10-04 22:35:47.321157

fecha = datetime.date.today()

print(fecha)
#2021-10-04

print(dir(datetime))
#['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__'
#, '__file__', '__loader__', '__name__', '__package__', '__spec__',
#'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta',
#'timezone', 'tzinfo']

d = datetime.date(2019, 4, 13)
print(d)
#2019-04-13

#%%
from datetime import date

d = date(2019, 4, 13)

print(d)
#2019-04-13

timestamp = date.fromtimestamp(1326244364)

print(timestamp)
#2012-01-10

hoy = date.today()

print('Año actual:', hoy.year)
print('Mes actual:', hoy.month)
print('Día actual:', hoy.day)
print('Día de la semana:', hoy.weekday()) # va de 0 a 6 empezando en lunes
# Año actual: 2021
# Mes actual: 10
# Día actual: 4
# Día de la semana: 0

#%%
from datetime import time

a = time()

print('a =', a)
#a = 00:00:00

b = time(11, 34, 56)

print('b =', b)
#b = 11:34:56

c = time(hour = 11, minute = 34, second = 56)

print(c)
#11:34:56

#%%
from datetime import time

a = time(11, 34, 56)

print('hour =', a.hour)
print('minute =', a.minute)
print('second =', a.second)
print('microsecond =', a.microsecond)
# hour = 11
# minute = 34
# second = 56
# microsecond = 0

#%%
from datetime import datetime

print(a)
#11:34:56

b = datetime(2021, 4, 21, 6, 53, 31, 342260)

print(b)
#2021-04-21 06:53:31.342260

#%%
from datetime import datetime

a = datetime(2021, 4, 21, 6, 53, 31, 342260)
print('año =', a.year)
print('mes =', a.month)
print('día =', a.day)
print('hora =', a.hour)
print('minuto =', a.minute)
print('timestamp =', a.timestamp())
# año = 2021
# mes = 4
# día = 21
# hora = 6
# minuto = 53
# timestamp = 1619006011.34226

#%%
from datetime import datetime, date

t1 = date(year = 2021, month = 4, day = 21)

t2 = date(year = 2020, month = 8, day = 23)

t3 = t1 - t2

print(t3)
#241 days, 0:00:00

t4 = datetime(year = 2020, month = 7, day = 12, hour = 7, minute = 9, second = 33)

t5 = datetime(year = 2021, month = 6, day = 10, hour = 5, minute = 55, second = 13)

t6 = t4 - t5

print(t6)
#-333 days, 1:14:20

print('tipo de t3 =', type(t3))
#tipo de t3 = <class 'datetime.timedelta'>

print('tipo de t6 =', type(t6))
#tipo de t6 = <class 'datetime.timedelta'>
#%%
from datetime import timedelta

t1 = timedelta(weeks = 1, days = 2, hours = 1, seconds = 33)
t2 = timedelta(days = 6, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2
print('t3 =', t3)
#t3 = 2 days, 13:55:39
#%%
#Ejemplo: Imprimir objetos timedelta negativos
from datetime import timedelta

t1 = timedelta(seconds = 21)
t2 = timedelta(seconds = 55)
t3 = t1 - t2

print(t3)
#-1 day, 23:59:26

print(abs(t3))
#0:00:34
#%%
#Ejemplo: Duración en segundos
from datetime import timedelta

t = timedelta(days = 1, hours = 2, seconds = 30, microseconds = 100000)
print('segundos totales =', t.total_seconds())
#segundos totales = 93630.1

#%%
#Formato para fechas y horas
#Python strftime() - convertir un objeto datetime a string
from datetime import datetime

now = datetime.now()

t = now.strftime('%H:%M:%S')
print('hora:', t)
#hora: 14:40:06

s1 = now.strftime('%m/%d/%Y, %H:%M:%S')
# en formato mm/dd/YY H:M:S
print('s1:', s1)
#s1: 10/04/2021, 22:54:19


s2 = now.strftime('%d/%m/%Y, %H:%M:%S')
# en formato dd/mm/YY H:M:S
print('s2:', s2)
#s2: 04/10/2021, 22:54:19

# En el programa de arriba, t, s1 y s2 son cadenas. Y los códigos de formato son:
#     %Y - año [0001,..., 2018, 2019,..., 9999]
#     %m - mes [01, 02, ..., 11, 12]
#     %d - día [01, 02, ..., 30, 31]
#     %H - hora [00, 01, ..., 22, 23
#     %M - minuto [00, 01, ..., 58, 59]
#     %S - segundo [00, 01, ..., 58, 59]

#%%
#Python strptime() - convertir una cadena a un objeto datetime
#Ejemplo: strptime()
from datetime import datetime

cadena_con_fecha= '21 September, 2021'
print('date_string =', cadena_con_fecha)
#date_string = 21 September, 2021

date_object = datetime.strptime(cadena_con_fecha, '%d %B, %Y')
print('date_object =', date_object)
#date_object = 2021-09-21 00:00:00

#%%