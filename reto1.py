salarioBase, cantidadHoras, desempeño = input().split()
salario = float(salarioBase)
hora = salario/192
hora_extra = (hora*0.25) + hora
canitdad_horas_extra = int(cantidadHoras)
desemp = int(desempeño)
bono = salario*0.05
if (canitdad_horas_extra >= 1):
    pago_horas = hora_extra*canitdad_horas_extra
    if (desemp == 1):
        salario_total = salario+bono+pago_horas
    else:
        salario_total = salario+pago_horas
    salud = salario_total*0.035
    pension = salario_total*0.04
    caja = salario_total*0.01
    descuento = salud+pension+caja
    pago = salario_total-descuento
    print(round(pago, 1))
else:
    if (desemp == 1):
        salario_total = salario+bono
    else:
        salario_total = salario
    salud = salario_total*0.035
    pension = salario_total*0.04
    caja = salario_total*0.01
    descuento = salud+pension+caja
    pago = salario_total-descuento
    print(round(pago, 1))
