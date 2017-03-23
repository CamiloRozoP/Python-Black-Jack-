from random import sample

def juego(lJugador, lCasa, lista):
    print(lJugador)
    if(len(lJugador)==0 and len(lCasa)==0):
        repartirIni(lJugador, lCasa, lista)
        return "primera"
    else:
        if(contador(lJugador) <= 21):
            if(input("Desea continuar JUGADOR? (Y/N)").upper() != "N"):
                repartir(lJugador,lCasa,lista,0)
            else:
                print ("JUGADOR SU PUNTAJE ES " ,comprobacion(lJugador,contador(lJugador)))
                repartir(lJugador,lCasa,lista,1)
        else:
            return print("Perdio el JUGADOR , tiene: " + str(comprobacion(lJugador,contador(lJugador))))

def juego1(lJugador, lCasa, lista):
    if(comprobacion(lCasa,contador(lCasa)) <= 21):
        print ("CASA SU PUNTAJE ES " ,comprobacion(lCasa,contador(lCasa)))
        if(comprobacion(lCasa,contador(lCasa)) < comprobacion(lJugador,contador(lJugador))):
            repartir(lJugador,lCasa,lista,1)
        elif(comprobacion(lCasa,contador(lCasa))) >= comprobacion(lJugador,contador(lJugador)):
            print("La casa gano: " + str(comprobacion(lCasa,contador(lCasa))) + " a " + str(comprobacion(lJugador,contador(lJugador))))
            return "final"
        elif(comprobacion(lJugador,contador(lJugador)) >= comprobacion(lCasa,contador(lCasa))):
            print("El jugador gano: " + str(comprobacion(lJugador,contador(lJugador))) + " a " + str(comprobacion(lCasa,contador(lCasa))))
            return "final"

    else:
        return print("Perdio la CASA  tiene: " + str(comprobacion(lCasa,contador(lCasa))))


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
        return contador(lista[1:])+valor(lista[0])

def comprobacion(lista,numero):
    if lista == []:
        return numero
    elif lista[0] in [('A', 'CORAZONES'),('A', 'DIAMANTES'),('A', 'PICAS'),('A', 'TREBOLES')] and numero+10<22:
        return comprobacion(lista[1:],numero+10)
    else:
        return comprobacion(lista[1:],numero)

def repartirIni(lJugador, lCasa, lista):
    lJugador.append(lista[0])
    lJugador.append(lista[20])
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
while True:
  juego([],[],creadorbaraja())
  if(input("Desea continuar JUGANDO BLACK JACK? (Y/N)").upper() != "Y"):
    break
    
