import random
import time
#Funció import per a fer un clear de pantalla
import platform
import os
import socket
sistema = platform.system()
def clear_pantalla():
    if sistema == "Windows":
        os.system ("cls")
    elif sistema == "Linux":
        os.system ("clear")
equip = socket.gethostname()
print("----------Benvingut al Trivial!----------")
time.sleep(1)
print("Instruccions:")
time.sleep(2)
print("   -El torn d'inici i l'ordre dels jugadors és aleatori!\n   -Per a guanyar has de contestar 3 preguntes correctes!\n   -Si falles li toca a un altre jugador!\n   -Cada jugador anirà responent preguntes fins que falli!\n   -Si s'acaben les preguntes s'acaba el joc!")
time.sleep(4)
print(input("Dóna-li al botó enter per continuar!"))

#Executa fins que l'usuari digui un número entre 2 i 4
while True:
    jugadors_totals=input("Indica el nombre total de jugadors (Min 2 - Max 4) ")

    if jugadors_totals.isnumeric()==False or int(jugadors_totals)<2 or int(jugadors_totals)>4:
        print("\nHas d'indicar un número entre 2 i 4\n")
    elif int(jugadors_totals)==2:
        jugador1=input("Indica el nom del jugador 1 ").capitalize()
        jugador2=input("Indica el nom del jugador 2 ").capitalize()
        break
    elif int(jugadors_totals)==3:
        jugador1=input("Indica el nom del jugador 1 ").capitalize()
        jugador2=input("Indica el nom del jugador 2 ").capitalize()
        jugador3=input("Indica el nom del jugador 3 ").capitalize()
        break
    elif int(jugadors_totals)==4:
        jugador1=input("Indica el nom del jugador 1 ").capitalize()
        jugador2=input("Indica el nom del jugador 2 ").capitalize()
        jugador3=input("Indica el nom del jugador 3 ").capitalize()
        jugador4=input("Indica el nom del jugador 4 ").capitalize()
        break
clear_pantalla()
#Executa fins que l'usuari digui un número entre 10 i 20.
while True:
    preguntes_totals=input("Indica amb quantes preguntes voleu jugar, MIN 10 MAX 20: ")
    if preguntes_totals.isnumeric()==False :
        print("Has d'indicar un número")
    elif int(preguntes_totals) <10 or int(preguntes_totals) >20:
        print("Has d'indicar un número entre 10 i 20")
    else: break
clear_pantalla()
#Guarda l'ordre de les preguntes
preguntes=[int(x) for x in range(int(preguntes_totals))]
preguntes_finals=[int()]
#Els números parells són les preguntes i els números senars són les respostes.
#Guarda els números parells a una nova llista.
for i in preguntes:
    if i %2 !=0 and int(preguntes_totals)%2==0:
        i+=int(preguntes_totals)-1
        preguntes_finals.append(i)
    elif i%2 !=0 and int(preguntes_totals)%2!=0:
        i+=int(preguntes_totals)
        preguntes_finals.append(i)
#Elimina els números senars de la llista.
for i in preguntes:
    if i%2!=0:
        preguntes.remove(i)
#Junta les dos llistes i elimina la posició 0, si no s'elimina la posició 0 hi haurà 2 valors 0.
preguntes_finals.extend(preguntes)
preguntes_finals.pop(0)
#Randomitza l'ordre de les preguntes.
random.shuffle(preguntes_finals)

longitud=len(preguntes_finals)
comptador_jugador1=0
comptador_jugador2=0
comptador_jugador3=0
comptador_jugador4=0
comptador_preguntes=0
#Llista per a agafar el número de jugadors i randomitza l'ordre.
ordre_jugadors=[int(x1) for x1 in range(int(jugadors_totals))]
random.shuffle(ordre_jugadors)

preguntes_llista=[["Que significa el símbol del Podcast de YO,INTERNETO?"],[["Un tridente",False],["Un cable Ethernet",True],["Un raspall",False]],
["Quin va ser el primer virus informàtic?"],[["Creeper",True],["Stuxnet",False],["Nimda",False]],
["Qui és el protagonista de One Piece"],[["Luffy",True],["Ninfy",False],["Ruffy",False]],
["Com es diu el músic de la tripulació de Luffy?"],[["Brook",True],["Franky",False],["Sanji",False]],
["En quin any va ser llançat el Minecraft?"],[["2011",True],["2010",False],["2001",False]],
["Qui és el davanter de la neu a Inazuma Eleven?"],[["Shawn Frost",True],["Tom Dark",False],["Axel Blaze",False]],
["Quina fruita del diable es va menjar Luffy?"],[["Fruita Gomu Gomu",True],["Fruita Ope Ope",False],["Fruita Uo Uo",False]],
["Quants fills té Vegeta?"],[["Dos",True],["Un",False],["Tres",False]],
["Qui és el guanyador de la Lliga Pokemon de Alola?"],[["Ash Ketchum",True],["Gladion",False],["Kiawe",False]],
["Quin va ser el primer Pokemon de Ash Ketchum?"],[["Caterpie",True],["Pikachu",False],["Pidgey",False]],
["Quin és el nom real de L?"],[["L Lawliet",True],["Light Yagami",False],["Kira",False]],
["Quin és el nom del protagonista de Jujutsu Kaisen 0?"],[["Yuuji Itadori",False],["Yuta Okkotsu",True],["Roronoa Zoro",False]],
["Quins són els noms dels fills de Goku?"],[["Gohan i Goten",True],["Goten i Trunks",False],["Pan i Videl",False]],
["Quants anys té Goku?"],[[44,True],[40,False],[47,False]],
["Quants fills té Odin?"],[[2,True],[1,False],[4,False]],
["Quin és el nom del actor de Iron Man?"],[["Robert Downey Jr.",True],["Chris Evans",False],["Tobey Maguire",False]],
["Quin és el nom real de Spider-Man?"],[["Peter Parker",True],["Andrew Garfield",False],["Tom Holland",False]],
["Quin es el nom real de Batman?"],[["Bruce Wayne",True],["Ben Affleck",False],["Robert Pattinson",False]],
["Quin és el nom del antic Rei Pirata?"],[["Gold Roger",False],["Gol D. Roger",True],["Monkey D. Luffy",False]],
["Qui vol ser el millor espadachin del món (One Piece)?"],[["Roronoa Zoro",True],["Monkey D. Luffy",False],["Edward Newgate",False]]
]
#Creació de la varible torn per a canviar de jugador.               
turn=int(0)
#Creació de la variable interruptor per a mostrar el missatge "li toca a..." sols quan es troba en True.
interruptor=True
#Creació de la variable ordre per a mostrar sols una vegada l'ordre dels jugadors.
ordre=True
for z in preguntes_finals:
    if ordre==True:
        print("L'ordre dels jugadors és:")
        for r in ordre_jugadors:
            if r==0:
                print(jugador1)
            elif r==1:
                print(jugador2)
            elif r==2:
                print(jugador3)
            elif r==3:
                print(jugador4)
        ordre=False
        print("\n")
        time.sleep(3)

    res_str=""
    comptador_preguntes+=1
    #Si algún dels 4 comptadors arriba a 3 s'acaba el bucle.
    if comptador_jugador1 ==3 or comptador_jugador2==3 or comptador_jugador3==3 or comptador_jugador4==3:
        break
    #si turn és igual que els jugadors que juguen es ficarà a 0 per a tornar a comensar amb el primer jugador.
    if turn ==int(jugadors_totals):
        turn=int(0)
    #i1 és igual a la posició de turn, exemple ordre jugadors=[0,3,1,2] i turn és 1, allavons i1=3.
    i1=ordre_jugadors[turn]
    if i1 ==0 and interruptor==True:
        print("----Li toca a",jugador1+"----")
    elif i1 ==1 and interruptor==True:
        print("----Li toca a",jugador2+"----")
    elif i1 ==2 and interruptor==True:
        print("----Li toca a",jugador3+"----")
    elif i1 ==3 and interruptor==True:
        print("----Li toca a",jugador4+"----")
    print("------------------------")
    #Mostra el marcador depenen els jugadors que juguen
    if jugadors_totals=="2" :
        print(" El marcador actual és:\n"+" ",jugador1,":",comptador_jugador1,"\n"+" ",jugador2,":",comptador_jugador2) 
        print("------------------------")
        print(input("Dóna-li al botó enter per continuar!"))
        clear_pantalla()
    elif jugadors_totals=="3" :
        print(" El marcador actual és:\n"+" ",jugador1,":",comptador_jugador1,"\n"+" ",jugador2,":",comptador_jugador2,"\n"+" ",jugador3,":",comptador_jugador3) 
        print("------------------------")
        print(input("Dóna-li al botó enter per continuar!"))
        clear_pantalla()
    elif jugadors_totals=="4" :
        print(" El marcador actual és:\n"+" ",jugador1,":",comptador_jugador1,"\n"+" ",jugador2,":",comptador_jugador2,"\n"+" ",jugador3,":",comptador_jugador3,"\n"+" ",jugador4,":",comptador_jugador4) 
        print("------------------------")
        print(input("Dóna-li al botó enter per continuar!"))
        clear_pantalla()
    #randomitza les respostes
    random.shuffle(preguntes_llista[z+1])
    #Imprimeix la pregunta
    print(preguntes_llista[z][0])
    #Imprimeix les respostes
    print("1.",preguntes_llista[z+1][0][0],"\n2.",preguntes_llista[z+1][1][0],"\n3.",preguntes_llista[z+1][2][0])
    #Un bucle fins que l'usuari fique un número de l'1 al 3.
    while True:
        res_str=input()
        if res_str.isnumeric()==False:
            print("Has d'indicar un número")
        elif res_str.isnumeric()==True:
            res=int(res_str)
            if res >0 and res <4:
                break
            else:print("Has d'indicar un número entre 1 i 3")
    #Si la resposta és correcta seguirà el mateix jugador i sumarà 1 al comptador.
    if preguntes_llista[z+1][res-1][1]==True and i1==0:
        print("Correcte!")
        comptador_jugador1+=1
        print(input("Dóna-li al botó enter per continuar!"))
        interruptor=False
    elif preguntes_llista[z+1][res-1][1]==True and i1==1:
        print("Correcte!")
        comptador_jugador2+=1
        print(input("Dóna-li al botó enter per continuar!"))
        interruptor=False
    elif preguntes_llista[z+1][res-1][1]==True and i1==2:
        print("Correcte!")
        comptador_jugador3+=1
        print(input("Dóna-li al botó enter per continuar!"))
        interruptor=False
    elif preguntes_llista[z+1][res-1][1]==True and i1 ==3:
        print("Correcte!")
        comptador_jugador4+=1
        print(input("Dóna-li al botó enter per continuar!"))
        interruptor=False
    #Si el jugador falla mostra la resposta correcta i suma 1 al turn per a canviar de jugador.
    #interruptor és fica en True per a tornar a mostrar el missatge "li toca a..."
    elif preguntes_llista[z+1][res-1][1]==False:
        print("\nIncorrecte!") 
        if preguntes_llista[z+1][0][1]==True:
            print("La resposta correcta era:",preguntes_llista[z+1][0][0])
        elif preguntes_llista[z+1][1][1]==True:
            print("La resposta correcta era:",preguntes_llista[z+1][1][0])
        if preguntes_llista[z+1][2][1]==True:
            print("La resposta correcta era:",preguntes_llista[z+1][2][0])            
        turn+=1
        print(input("Dóna-li al botó enter per continuar!"))
        interruptor=True
    clear_pantalla()

clear_pantalla()
print("Tenim un resultat final...")
#Un bucle per a guardar del número 1 al 5.
cuenta_atras=[int(back) for back in range(1,6)]
#Un bucle per a imprimir pantalla comensant pel número final.
for back in cuenta_atras[::-1]:
    time.sleep(1)
    print(back)

time.sleep(1)
#Un condicional per a mostrar el guanyador o un missatge dient que s'han acabat les preguntes.
if comptador_preguntes==longitud:
    print("No hi ha cap jugador guanyador, s'han acabat les preguntes,",equip)
elif comptador_jugador1 > comptador_jugador2 and comptador_jugador1> comptador_jugador3 and comptador_jugador1 > comptador_jugador4:
    print("-----------------\nFelicitats",jugador1,"\nHas guanyat\n-----------------")
elif comptador_jugador2 > comptador_jugador1 and  comptador_jugador2 > comptador_jugador3 and comptador_jugador2> comptador_jugador4:
    print("-----------------\nFelicitats",jugador2,"\nHas guanyat\n-----------------")
elif comptador_jugador3 > comptador_jugador2 and comptador_jugador3> comptador_jugador4 and comptador_jugador3> comptador_jugador1:
    print("-----------------\nFelicitats",jugador3,"\nHas guanyat\n-----------------")
elif comptador_jugador4 > comptador_jugador1 and comptador_jugador4> comptador_jugador2 and comptador_jugador4 >comptador_jugador3:
    print("-----------------\nFelicitats",jugador4,"\nHas guanyat\n-----------------")
