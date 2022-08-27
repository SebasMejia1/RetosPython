'''Una compañía de software contable, paga a su personal de ventas un salario de 3'500.000 mensuales,
mas una comisión de 1'500.000 por cada licencia de software vendida menos el (5% del salario total +
comisiones de deducciones) por impuestos. Codifica un programa que calcule e imprima el salario
mensual de un vendedor dado recibiendo el numero de ventas realizadas'''
cantlicencias = int(input("Digita la cantidad de licencias vendidas: "))
comision = 1500000*cantlicencias
porc = 3500000*0.05
total = (comision - porc)+3500000
print(f'El pago total del empleado es de {total}')

##?????+comisiones de deducciones?????
'''Este ejercicio puede tener errores ya que no entendí bien el tema de las deducciones '''