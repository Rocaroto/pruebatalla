import random
#////////////////////////////////////////////////////////////////////////
stats={"vida":100,"daño espada":10,"dinero":100,"daño":5}
inventario={"pociones":2}
equipo=["espada","escudo"]            #creación de listas y diccionarios
equipo2={"armadura":30}
#////////////////////////////////////////////////////////////////////////
vida=stats.get("vida")
dañog=stats.get("daño")
dañoa=stats.get("daño espada")        #variables para las listas y diccionarios
dinero=stats.get("dinero")
pocion=inventario.get("pociones")
armor=equipo2.get("armadura")
#/////////////////////////////////////////////////////////////////////////
inicio = 1
while inicio == 1:
    difi = input("\n\telige la dificultad\nfacil|1|\ndificil|2|\n")
    if difi =="1":
            eld = 50
            vidamalo = 100
            inicio = 0
    elif difi =="2":                    #se elige la dificultad. aumenta el daño del enemigo.
            eld = 100
            vidamalo = 1000
            inicio = 0
    else:
        print("\tponle una dificultad\n")

#/////////////////////////////////////////////////////////////////////////
#inicia el programa
ei=input('escribe "empezar" para iniciar el juego\n')
while ei == "empezar":
    print("bienvenido elige que quieres hacer") #elegir que hacer
    print("""\n
            1 - ir a la tienda              
            2 - pelear
            3 - salir
    \n""")
    lpd=input("\t\t")
#/////////////////////////////////////////////////////////////////////////
#opcion de la tienda
    if lpd =="1":
        while dinero >= 1:
            print("bienvenido a la tienda. Que deseas?\n")
            print("este es tu dinero-",dinero,"-")
            print("""
                    1 - pocion = 100$ 
                    2 - escudo = 300$
                    3 - mejorar armadura = 1500$
                    4 - mejorar espada = 1000$
                    5 - salir de la tienda
            """)
            lsd=input("\t\t")
            if lsd == "1":
                if dinero >=100:
                    print("compraste una pocion\n")
                    pocion+=1
                    dinero-=100
                else:
                    print("no tienes suficiente dinero\n")
            elif lsd=="2":
                if dinero >=300:
                    print("compraste un escudo\n")
                    equipo.append("escudo")
                    dinero-=300
                else:
                    print("no tienes suficiente dinero\n")
            elif lsd=="3":
                if dinero >=1500:
                    print("mejoraste tu armadura\n")
                    armor+=30
                    dinero-=1500
                else:
                    print("no tienes suficiente dinero\n")
            elif lsd=="4":
                if dinero >=1000:
                    print("mejoraste tu espada\n")
                    dañoa+=10
                    dinero-=1000
                else:
                    print("no tienes suficiente dinero\n")
            elif lsd=="5":

                print("saliendo de la tienda\n\n")
                break
    elif lpd =="3":
        print("cerro el juego")
        break
    #/////////////////////////////////////////////////////////////////////////////////
    #inicia la batalla
    print("¡oh no! te topaste con un villano tendras que derrotarlo para avanzar\r\n")
    print("\n\testas son tus stats\r\n")
    print("vida: ",vida)
    print("daño con espada: ",dañoa)
    print("dinero: ",dinero)
    print("daño a golpes: ",dañog)
    print("\n\teste es tu inventario\r\n")
    print("pociones: ",pocion)
    print("\n\teste es tu equipo\r\n")
    for a2 in equipo:
        print(a2)
    print("Armadura: ",armor)

    while vida >= 1:
        print("///////////////////////////////////////////////////////////////////////")
        daño = random.randint(0,eld)
        dañopor=daño*armor/100
        totald=int(daño-dañopor)
        #//////////////////////////////
        print("vida: ",vida)
        print("enemigo: ",vidamalo)
        print("///////////////////////////////////////////////////////////////////////")
        print("\tque haces?\n\natacar(1)\ndefenderte(2)\ncurarte(3)\nhuir(4)\n")
        accion = input("\t\t")
        if accion =="1":
            if "espada" in equipo:
                print("genial lograste quitarle {} de vida".format(dañoa))
                vidamalo -= dañoa
                print("sufres {} de daño por parte del villano".format(totald))
                vida -= totald

            else:
                print("no tienes con que pelear asi que logra hacerle {} de daño a golpes".format(dañog))
                vidamalo -= dañog
                print("sufres {} de daño por parte del villano".format(totald))
                vida -= totald

        elif accion =="2":
            if "escudo" in equipo:
                print("gracias a tu escudo sientes como te defiendes del daño y logras recuperar 50 de vida, pero se rompe tu escudo\n\n")
                vida += 50
                equipo.remove("escudo")
            else:

                print("no tienes con que defenderte y recibes ",totald," de daño \r\n\n")
                vida -= totald

        elif accion =="3":
            if pocion >= 1:
                print("te tomas la pocion grande. Recuperas 100 de salud\n\n")
                vida += 100
                pocion -= 1
            else:
                print("no tienes con que curarte. y recibes {} de daño\n\n".format(totald))
                vida -= totald
        elif accion =="4":
            if vida <=50:
                print("¡QUE MAL! solo tienes {} de salud hay que huir".format(vida))
                break
            else:
                print("porque quieres huir? aun tienes suficiente salud. ¡PELEA!\n\n")

        if vida <= 0:
            print("perdiste todas tus vidas. Termino el juego.")
            ei="no"
        if vidamalo <= 0:
            print("mataste al enemigo")
            ttal = random.randint(100,500)
            dinero += ttal
            if difi =="2":
                vidamalo=1000
            elif dañoa==100:
                vidamalo+=10
            else:
                vidamalo=100
            print("obtienes {} de dinero.".format(ttal))
            print("\n\n")
            break
