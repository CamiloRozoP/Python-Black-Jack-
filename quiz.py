from random import sample

def juego(lJugador, lCasa, lista):
    print(lJugador)
    if(len(lJugador)==0 and len(lCasa)==0):
        repartirIni(lJugador, lCasa, lista)
        return "primera"
    else:
        if(contador(lJugador) <= 21):
            for i in range(0,len(lJugador)):
                if(lJugador[i]=='A'):
                    if(contador(lJugador)+10<22):
                        contador(lJugador)+10
            if(input("Desea continuar JUGADOR? (Y/N)").upper() != "N"):
                repartir(lJugador,lCasa,lista,0)
            else:
                    repartir(lJugador,lCasa,lista,1)
        else:
                return print("Perdio el JUGADOR tiene: " + str(contador(lJugador)))

def juego1(lJugador, lCasa, lista):
    if(contador(lCasa) <= 21):
        for j in range(0,len(lJugador)):
            if(lJugador[j]=='A'):
                if(contador(lJugador)+10<22):
                    contador(lJugador)+10
                    if(contador(lCasa) < contador(lJugador)+10):
                        repartir(lJugador,lCasa,lista,1)
                    elif(contador(lCasa) >= contador(lJugador)+10):
                        print("La casa gano (1): " + str(contador(lCasa)) + " a " + str(contador(lJugador)+10))
                        return "final"
                    elif(contador(lJugador)+10 >= contador(lCasa)):

                        print("El jugador gano  (1):" + str(contador(lJugador)+10) + " a " + str(contador(lCasa)))
                        return "final"
                           
        for i in range(0,len(lCasa)):
            if(lCasa[i]=='A'):
                if(contador(lCasa)+10<22):
                    contador(lCasa)+10
                    if(contador(lCasa)+10 < contador(lJugador)):
                        repartir(lJugador,lCasa,lista,1)
                    elif(contador(lCasa)+10 >= contador(lJugador)):
                        print("La casa gano (3): " + str(contador(lCasa)+10) + " a " + str(contador(lJugador)))
                        return "final"
                    elif(contador(lJugador) >= contador(lCasa)+10):
                        print("El jugador gano (3): " + str(contador(lJugador)) + " a " + str(contador(lCasa)+10))
                        return "final"
    
            if(contador(lCasa) <= 21 and contador(lCasa)+10>22):
                if(contador(lCasa) < contador(lJugador)):
                    repartir(lJugador,lCasa,lista,1)
                elif(contador(lCasa) >= contador(lJugador)):
                    print("La casa gano (5): " + str(contador(lCasa)) + " a " + str(contador(lJugador)))
                    return "final"
                elif(contador(lJugador) >= contador(lCasa)):
                    print("El jugador gano  (5):" + str(contador(lJugador)) + " a " + str(contador(lCasa)))
                    return "final"                
                    

    else:
        return print("Perdio la CASA tiene: " + str(contador(lCasa)))

def creadorbaraja():
    return sample([(x,y)for x in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']for y in ['DIAMANTES','TREBOLES','PICAS','CORAZONES']], 52)

def valor(carta):
    if carta[0] == 'J' or  carta[0] == 'K' or  carta[0] == 'Q':
        return 10
    elif carta[0] == 'A':
            return 1

    else:
        return carta[0]

def contador(lista):
    if(len(lista)==0):
        return 0
    else:
        for i in range(0,len(lista)):
            return contador(lista[1:])+valor(lista[0])

def repartirIni(lJugador, lCasa, lista):
    lJugador.append(lista[0])
    lJugador.append(lista[2])
    lCasa.append(lista[1])
    print("Cartas jugador: " + str(lJugador))
    print("Cartas casa: " + str(lCasa))
    juego(lJugador, lCasa, lista[4:])

def repartir(lJugador, lCasa, lista,turno):
    if turno==0:
        lJugador.append(lista[0])
        print("Cartas jugador: " + str(lJugador))
        print("Cartas casa: " + str(lCasa))
        juego(lJugador, lCasa, lista[2:])
    if turno==1:
        lCasa.append(lista[1])
        print("Cartas jugador: " + str(lJugador))
        print("Cartas casa: " + str(lCasa))
        juego1(lJugador, lCasa, lista[2:])

juego([],[],creadorbaraja())
