"""
David solicitó un crédito a 30 años para comprar una vivienda, 
con una tasa fija nominal anual del 5%. 
Pidió $500000 al banco y acordó 
un pago mensual fijo de $2684,11.
 El siguiente es un programa calcula 
 el monto total que pagará David a lo largo de los años:
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
pago_extra = 1000
while saldo > 0:
    pago=pago_mensual;
    if (meses>=pago_extra_mes_comienzo 
        and meses<=pago_extra_mes_fin):
        pago=pago+pago_extra
    saldo = saldo * (1+tasa/12) - pago
    total_pagado = total_pagado + pago
    meses=meses+1
    print(meses,round(total_pagado,2), round(saldo,2))

print('Total pagado:', round(total_pagado, 2))
print('Meses:',meses)