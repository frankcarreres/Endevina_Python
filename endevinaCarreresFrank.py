import random

# Fet per: Frank Carreres Catalá


continuar = True  # <--- Aquesta variable booleana s'utilitza per a comprobar si es vol continuar jugant o no.
partidesJugades= 0
partidesGuanyades = 0
sumaIntentsPartidesGuanyades = 0
maxIntents = 0
minIntents = 100


while continuar :

    partidesJugades = partidesJugades + 1
    intentsPartidaGuanyada = 0

    print("")
    print("----------------------ENDEVINA------------------------")
    print("")
    qIntents = int(input("Dis-me la quantitat d'intents: "))
    print("")
    print ("------------------------------------------------------")
    print("")

    haGuanyat = False
    valorMajor = 100
    valorMenor = 1
    numeroSecret= random.randint(valorMenor, valorMajor)

    print(numeroSecret)
    for intents in range (1, qIntents + 1):

       

        numero = int(input (f"Dis-me un número ({valorMenor} - {valorMajor}) : "))   # <--- ENTRADA DE DADES
    

        if numero > valorMajor or numero < valorMenor:

            print ("El número introduït no es possible, has perdut un intent.")  # <--- ENTRADA DE DADES

        elif  numero == numeroSecret:

            sumaIntentsPartidesGuanyades = sumaIntentsPartidesGuanyades + intents # <--- Aquest acumulador, acumula tots els intents que s'han realitzat per partida.
            partidesGuanyades = partidesGuanyades + 1 # <--- Aquest comptador, compta les vegades que s'ha guanyat una partida.
            intentsPartidaGuanyada = intentsPartidaGuanyada + intents # <--- Aquest acumulador, acumula tots els intents que s'han realitzat per partida guanyada.
            haGuanyat = True # <--- Aquesta variable booleana s'utilitza per

            print ("")
            print("· ENHORABONA!! HAS ENCERTAT EL NÚMERO SECRET")
            print ("")

            if intents == 1:
                print (f"- Ho has encertat en {intents} intent.")
            else:
                print (f"- Ho has encertat en {intents} intents.")

            break

        # AQUESTES CONDICIONS S'UTILITZEN PER COMPROBAR ELS RANGS DELS NUMEROS INTRODUÏTS: 

        if numero > numeroSecret:

            if numero <= valorMajor:

                valorMajor = numero - 1

            print (f"Es menor, esta entre {valorMenor} i {valorMajor}")

        elif numero < numeroSecret :

            if numero >= valorMenor:

                valorMenor = numero + 1

            print (f"Es major, esta entre  {valorMenor} i {valorMajor}")
        
    else:
        print("")
        print (f"HAS UTILITZAT {qIntents} INTENTS, NO POTS CONTINUAR...")
        print("")
        print (f"El número secret era {numeroSecret}.")

    # AQUESTES CONDICIONS S'UTILITZEN PER A COMRPOBAR EL MAXIM I EL MINIM DE INTENTS, PER PARTIDA GUANYADA

    if (haGuanyat):

        if minIntents > intentsPartidaGuanyada:
            minIntents = intentsPartidaGuanyada
        if maxIntents < intentsPartidaGuanyada:
            maxIntents = intentsPartidaGuanyada
            
      

    # En aquesta part es realitza un bucle amb dos variables boleanes, (not altraPartidaOK) s'utilitza per a comprobar si la resposta introduïda en la variable
    # resposta es una de les asignades (S, s ,N, n) si es aixi ix del bucle i la booleana pasaría a estar en True, encambi si es dona una resposta no esperada
    # el bucle es tornara a repetir de nou fins que siga True.

    altraPartidaOK = False

    while (not altraPartidaOK):

        print("")
        resposta = input("Vols continuar jugant (S,s/N,n): ")
        print("")
            
        if resposta == "S" or resposta == "s" or resposta == "N" or resposta == "n":
            altraPartidaOK = True

        else:
            print("Aquest valor no em val, introdueix de nou el valor...")
            print("")
            
    if resposta == "N" or resposta == "n":
        continuar = False




# EIXIDA DE DADES:

print("")
print ("-----------------------------------------------------------------------------------------------------------------------")
print ("· EL PROGRAMA HA FINALITZAT AQUESTOS SON ELS RESULTATS:")
print("")

if partidesJugades == 1:

    print(f"- S'ha jugat {partidesJugades} partida.")

else:

    print(f"- S'han jugat {partidesJugades} partides.")

if partidesGuanyades == 0:

    print ("")
    print ("- No s'ha guanyat cap partida.")
    print ("")
    print ("- No puc traure la resta de resultats si no dispose de cap partida guanyada.")
    print ("")

else:

    mitjaIntents = sumaIntentsPartidesGuanyades / partidesGuanyades
    print ("")
    print (f"- La mitja dels intents entre les partides guanyades és de {mitjaIntents} intents.")
    print ("")
    print (f"- El màxim d'intents usats per a guanyar es {maxIntents} i el mínim d'intents usats per a guanyar és {minIntents}.")
    print ("")

print("")
print("- PREMI\n" * partidesGuanyades)
print("")

print ("-----------------------------------------------------------------------------------------------------------------------")