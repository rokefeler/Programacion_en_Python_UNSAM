"""
David solicitó un crédito a 30 años para comprar una vivienda, 
con una tasa fija nominal anual del 5%. 
Pidió $500000 al banco y acordó 
un pago mensual fijo de $2684,11.
 El siguiente es un programa calcula 
 el monto total que pagará David a lo largo de los años:
:. Supongamos que David adelanta pagos extra de 
   $1000/mes durante los primeros 12 meses de la hipoteca. 
"""
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
meses = 0
adelanto = 1000    #adelanto inicial
mesesAdelanto = 12 #nueva variable de control ira disminuyendo
while saldo > 0:
    pago=pago_mensual;
    if mesesAdelanto>0:
        pago=pago+adelanto
    saldo = saldo * (1+tasa/12) - pago
    total_pagado += pago
    meses += 1
    mesesAdelanto -= 1

print('Total pagado:', round(total_pagado, 2), "En", meses, " meses")