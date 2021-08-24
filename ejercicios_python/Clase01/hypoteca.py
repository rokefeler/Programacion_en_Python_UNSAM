#hypoteca.py
"""
Developer: rokefeler@gmail.com
Enunciado: David solicitó un crédito a 30 años para comprar una vivienda,
con una tasa fija nominal anual del 5%.
Pidió $500000 al banco y acordó
un pago mensual fijo de $2684,11.
:. ¿Cuánto pagaría David si agrega $1000 por mes
   durante cuatro años, comenzando en el sexto año
   de la hipoteca (es decir, luego de 5 años)?.
:. Modicá tu programa para que imprima una tabla
   mostrando el mes, el total pagado hasta el momento
   y el saldo restante.
"""
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
meses=0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000.00
printpagoextra=0.00
while saldo > 0:
    meses += 1
    pago=pago_mensual;
    printpagoextra=0.00
    if (meses>=pago_extra_mes_comienzo
        and meses<=pago_extra_mes_fin):
        pago += pago_extra
        printpagoextra=pago_extra
    saldo = saldo * (1+tasa/12) - pago
    total_pagado += pago
    if saldo<pago_mensual:
        pago_mensual = saldo * (1+tasa/12)
    print(f'{meses}\t${round(total_pagado,2):0.2f}\t ${round(saldo,2):9.2f}\t PagoExtra:${round(printpagoextra,2):0.2f}')
    #print(meses,round(total_pagado,2), round(saldo,2))

print(f'Total pagado ${round(total_pagado,2):0.2f}')
print(f'Total Meses: {meses}')
