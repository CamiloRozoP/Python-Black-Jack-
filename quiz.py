from random import sample

def juego(lJugador, lCasa, lista):
    print(lJugador)
    if(len(lJugador)==0 and len(lCasa)==0):
        repartirIni(lJugador, lCasa, lista)
        return "primera"
    else:
            print (contador(lJugador))


def juego1(lJugador, lCasa, lista):
    
        return print("Perdio la CASA tiene (5): " + str(contador(lCasa)))

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
        if (lista[0]==('A', 'CORAZONES') or lista[0]==('A', 'DIAMANTES') or lista[0]==('A', 'PICAS') or lista[0]==('A', 'TREBOLES')):
            if(contador(lista[1:])+valor(lista[0])+10<22):
                return contador(lista[1:])+valor(lista[0])+10
        return contador(lista[1:])+valor(lista[0])
        

def repartirIni(lJugador, lCasa, lista):
    lista[20]=('A', 'DIAMANTES')
    lJugador.append(lista[20])
    lJugador.append(lista[2])
    lJugador.append(lista[0])
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
