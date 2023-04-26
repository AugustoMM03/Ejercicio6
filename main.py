from claseViajeroFrecuente import ViajeroFrecuente as VF

if __name__ == '__main__':
    viajero1 = VF(210,32875738,'Juan','Perez',12500)
    viajero2 = VF(211,29277486,'Ana','Garcia',7600)
    mayormillas = viajero1 if viajero1 > viajero2 else viajero2
    acumularmillas = viajero1 + viajero2
    canjearmillas = viajero1 - viajero2
    print("Cliente\t\tDNI\t\tNombre\t\tMillas")    
    print("{}\t\t{}\t{} {}\t{}".format(viajero1.getNumViajero(), viajero1.getDNI(),viajero1.getNombre(), viajero1.getApellido(), viajero1.getMillas()))
    print("{}\t\t{}\t{} {}\t{}".format(viajero2.getNumViajero(), viajero2.getDNI(),viajero2.getNombre(), viajero2.getApellido(), viajero2.getMillas()))
    print('El viajero con mayor cantidad de millas acumuladas es: {} {} (millas:{})'.format(mayormillas.getNombre(),mayormillas.getApellido(),mayormillas.getMillas()))
    print('La acumulacion de millas es: {}' .format(acumularmillas.getMillas()))
    print('El resultado de canjear millas es: {}' .format(canjearmillas.getMillas()))
