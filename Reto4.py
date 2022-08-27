'''Juan tiene N cantidad de pesos, Camila tiene la mitad de lo que posee Juan y Ricardo tiene la mitad de
lo que poseen Camila y Juan Juntos. ¿Puede PYTHON ayudarme a calcular la cantidad de dinero de
los 3?'''
juan = int(input("Digite la cantidad de pesos que posee Juan: "))
camila = juan/2
ricardo = juan+camila
total = juan+camila+ricardo
print(f'La cantidad de juan es {int(juan)}, la de camila es {int(camila)} y la ricardo es {int(ricardo)}')