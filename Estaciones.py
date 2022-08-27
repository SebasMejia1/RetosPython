'''Hacer un programa que calcule segun dia y mes en que estacion del año se encuentra'''
##Primavera: 1 marzo hasta 31 mayo
##Verano: 1 junio hasta 31 agosto
##Otoño: 1 septiembre hasta 30 noviembre
##Invierno: 1 diciembre hasta 28 febrero
mes = input("Digite el mes de año en minus: ")
dia = int(input("Digite el dia: "))
if(mes=="marzo" or mes=="mayo" and dia>=1 and dia<=31):
    print(f'Estas en primavera')
elif(mes=="junio" or mes=="agosto" and dia>=1 and dia<=31):
    print(f'Estas en verano')
elif(mes=="septiembre" or mes=="noviembre" and dia>=1 and dia<=30):
    print(f'Estas en otoño')
elif(mes=="diciembre" or mes=="febrero" and dia>=1 and dia<=28):
    print(f'Estas en invierno')