import random
import sys

Rostros=["Redondo", "Alargado", "Corazón", "Cuadrado", "Ovalado", "Rectangular"]
Piel=["Negra", "Marrón", "Morena", "Clara", "Blanca"]
Emociones=["Felicidad", "Tristeza", "Seriedad", "Indiferencia", "Enojo", "Temor", "Estrez"]
Generos=["Masculino", "Femenino"]
Accesorios=["lentes", "Aretes", "Percing", "Tatuajes", "Collar", "Ninguno", "Ninguno", "Ninguno", "Ninguno", "Ninguno"]
ColorDelPelo=["negro", "rubio", "café", "castaño", "gris", "invisible"]
Densidad=["Escaso", "Moderado", "Abundante"]
Textura=["lacio", "Ondulado", "Rizado"]
Forma=["almendrados", "separados", "redondos", "caídos", "saltones", "juntos", "profundos", "asiático"]
Color=["negro", "castaño", "ámbar", "avellana", "verde", "azul", "gris"]
Provincia=["","San José", "Alajuela", "Cartago", "Heredia", "Puntarenas", "Guanacaste", "Limón"]
def Inicio():

  Login=int(input("Digite el numero correspondiente si desea iniciar sesion como: 1.Administrador 2.Analista 3.Usuario:  "))
  if Login == 1 :
      Login="Administrador"
  elif Login == 2:
      Login="Analista"
  elif Login == 3 :
      Login="Usuario"
  else :
      print("Esa opcioon no está")
  return Login 


def CreaCedula():
    Ced=1000000
    while Ced in Datos[0]["cedula"] :
     Ced=Ced+1
    Datos[0]["cedula"].append(Ced)
    return


def CreaRostro():
    Datos[0]["FormaDeRostro"].append(random.randint(0, 5))
    return

def CreaPiel():
    Datos[0]["Piel"].append(random.randint(0, 4))
    return 

def CreaEmociones():
    Datos[0]["Emociones"].append(random.randint(0, 6))
    return 

def CreaGenero():

    Datos[0]["Genero"].append(random.randint(0, 1))
    return

def CreaGrupo():
    return


def CreaAccesorios():

    Datos[0]["Accesorios"].append(random.randint(0, 9))
    return

def CreaEdad ():
     c=random.randint(1920,2020)
     print(c)
     Años=c
            
             
     i=random.randint(1,12)
     print(i)
     Meses=i
     
             
     d=random.randint(1,30)
     print(d)
     Dias=d

     EdadPersona= [ Años,Meses,Dias]
     Datos[0]["Edad"].append(EdadPersona) 
     return CreaEdad

def CreaCabello():

    Pelo=[]
    x=random.randint(0, 5)
    Pelo.append(x)

    if x == 5 :
     Pelo.append(5)
     Pelo.append(5)
    else :
     Pelo.append(random.randint(0, 2))
     Pelo.append(random.randint(0, 2))
    Datos[0]["Cabello"].append(Pelo)
    return

def CreaOjos():
    ojos=[]
    ojos.append(random.randint(0, 7))
    ojos.append(random.randint(0, 6))
    Datos[0]["Ojos"].append(ojos)
    return


def CreaProvincia():

    Datos[0]["Provincia"].append(random.randint(1, 7))
    return

Datos=[{"cedula":[], "Edad":[], "FormaDeRostro":[], "Piel":[], "Emociones":[], "Genero":[], "Grupo":[], "Accesorios":[], "Cabello":[], "Ojos":[], "Provincia":[]}]

def CrearPersonaAleatoria(Contador):
    X=0
    while X != Contador:
        CreaCedula()
        #print(Datos[0]["cedula"])
        
  
        #CreaEdad()

        CreaRostro()
        #print(Datos[0]["FormaDeRostro"])

        CreaPiel()
        #print(Datos[0]["Piel"])

        CreaEmociones()
        #print(Datos[0]["Emociones"])

        CreaGenero()
        #print(Datos[0]["Genero"])

        CreaGrupo()

        CreaAccesorios()
        #print(Datos[0]["Accesorios"])

        CreaCabello()
        #print(Datos[0]["Cabello"])

        CreaOjos()
        #print(Datos[0]["Ojos"])

        CreaProvincia()
        #print(Datos[0]["Provincia"])
        X=X+1
    menu()
    return


def CreaPersonajeManualmente():


    CreaCedula()
    Datos[0]["Edad"].append([input("Digite la edad correspondiente en el siguiente formato dia/mes/año:  ")])
    Datos[0]["FormaDeRostro"].append(int(input("Digite el numero correspondiente al rostro que desea: 0.Redondo 1.Alargado 2.Corazon 3.Cuadrado 4.Ovalado 5.Rectangular:  ")))
    Datos[0]["Piel"].append(int(input("Digite el numero correspondiente al color de piel que desea: 0.Negra 1.Marrón 2.Morena 3.Clara 4.Blanca:  ")))
    Datos[0]["Emociones"].append(int(input("Digite el numero de la emocion correspondiente: 0.Felicidad 1.Tristeza 2.Seriedad 3.Indiferencia 4.Enojo 5.Temor 6.Estrez")))
    Datos[0]["Genero"].append(int(input("Digite el numero correspondiente al color de piel que desea: 0.Negra 1.Marrón 2.Morena 3.Clara 4.Blanca:  ")))
    #Datos[0]["Grupo"].append(Grupo[int(input("")
    Datos[0]["Accesorios"].append(int(input("Digite el numero correspondiente al color de piel que desea: 0.Negra 1.Marrón 2.Morena 3.Clara 4.Blanca:  ")))
    Pelo=[]
    Pelo.append(int(input("Digite el numero correspodiente al color del cabello: 0.negro 1.rubio 2.café 3.castaño 4.gris 5.invisible")))
    Pelo.append(int(input("Digite el numero correspodiente a la densidad del cabello: 0.Escaso 1.Moderado 2.Abundante")))
    Pelo.append(int(input("Digite el numero correspodiente a la textura del cabello: 0.lacio 1.Ondulado 2.Rizado")))

    Datos[0]["Cabello"].append(Pelo) 
    ojos=[]
    ojos.append(int(input("Digite el numero correspondiente a la forma de ojos que desea: 0.almendrados 1.separados 2.redondos 3.caídos 4.saltones 5.juntos 6.profundos 7.asiático:  ")))        
    ojos.append(int(input("Digite el numero correspondiente al color de ojod que desea: 0.Negra 1.Marrón 2.Morena 3.Clara 4.Blanca:  ")))
    Datos[0]["Ojos"].append(ojos)

        
    Datos[0]["Provincia"].append(int(input("Digite el numero correspondiente a su provincia: 1.San José 2.Alajuela 3.Cartago 4.Heredia 5.Puntarenas 6.Guanacaste 7.Limón:   ")))



    menu()
    return

def Imprimir():
    contador=0
    print(Datos[0]["cedula"])
    print(Datos[0]["Edad"])
    print(Datos[0]["FormaDeRostro" ])
    print(Datos[0]["Piel"])
    print(Datos[0]["Emociones" ])
    print(Datos[0]["Genero"])
    print(Datos[0]["Grupo"])
    print(Datos[0]["Accesorios"])
    print(Datos[0]["Cabello"])
    print(Datos[0]["Ojos" ])
    print(Datos[0]["Provincia"])
    print("______________________________________")
    for ced in Datos[0]["cedula"]:
        print(ced) 
        print("forma de rostro:  ", Rostros[Datos[0]["FormaDeRostro" ][contador]])
        print("color de piel:  ", Piel[Datos[0]["Piel"][contador]])
        print("emocion:  ", Emociones[Datos[0]["Emociones" ][contador]]) 
        print("Genero:  ", Generos[Datos[0]["Genero"][contador]])
        print("Accesorio:  ", Accesorios[Datos[0]["Accesorios"][contador]])
        print("Color del cabello:  ", ColorDelPelo[Datos[0]["Cabello"][contador][0]])
        print("Densidad del cabello:  ", Densidad[Datos[0]["Cabello"][contador][1]])
        print("Textura del cabello:  ", Textura[Datos[0]["Cabello"][contador][2]])


        print("Forma de ojos:  ", Forma[Datos[0]["Ojos"][contador][0]])
        print("Color de ojos:  ", Color[Datos[0]["Ojos"][contador][1]])
        print("Provincia:  ", Provincia[Datos[0]["Provincia"][contador]])
        print("-------------------------------------")
        contador=contador+1
        

    menu()
        
    return

def ColsuntarPersona():
    for ced in Datos[0]["cedula"]:
        print(ced)
 
    contador=Datos[0]["cedula"].index(int(input("Digite la cedula de la persona que desea consultar")))

    print(ced) 
    print("forma de rostro:  ", Rostros[Datos[0]["FormaDeRostro" ][contador]])
    print("color de piel:  ", Piel[Datos[0]["Piel"][contador]])
    print("emocion:  ", Emociones[Datos[0]["Emociones" ][contador]]) 
    print("Genero:  ", Generos[Datos[0]["Genero"][contador]])
    print("Accesorio:  ", Accesorios[Datos[0]["Accesorios"][contador]])
    print("Color del cabello:  ", ColorDelPelo[Datos[0]["Cabello"][contador][0]])
    print("Densidad del cabello:  ", Densidad[Datos[0]["Cabello"][contador][1]])
    print("Textura del cabello:  ", Textura[Datos[0]["Cabello"][contador][2]])


    print("Forma de ojos:  ", Forma[Datos[0]["Ojos"][contador][0]])
    print("Color de ojos:  ", Color[Datos[0]["Ojos"][contador][1]])
    print("Provincia:  ", Provincia[Datos[0]["Provincia"][contador]])
    return


def ModificarPersona():
    for ced in Datos[0]["cedula"]:
        print(ced)

    C=Datos[0]["cedula"].index(int(input("Digite la cedula de la persona que desea cambiar:  ")))
    Datos[0]["Provincia"][C]=int(input("Digite el numero correspondiente a su nueva provincia: 1.San José 2.Alajuela 3.Cartago 4.Heredia 5.Puntarenas 6.Guanacaste 7.Limón:   "))
    Datos[0]["Emociones"][C]=int(input("Digite el numero de la emocion correspondiente: 0.Felicidad 1.Tristeza 2.Seriedad 3.Indiferencia 4.Enojo 5.Temor 6.Estrez"))
    return


def menu():
    print("¿Que desea hacer? ")
    E=int(input("1.Crear persona aleatoriamente 2.Crear persona manualmente 3.Mostrar toda la lista 4.Para consultar una persona 5.Para modificar persona 6.Para terminar:   "))
    if E==1:
        if Login=="Administrador":
            contador=int(input("Cuantas personas desea Crear"))
            CrearPersonaAleatoria(contador)
        else:
            print("Esta funcion es para administradores")
    elif E==2:
        if Login=="Administrador":
            CreaPersonajeManualmente()
        else :
            print("Esta funcion es para administradores")
    elif E==3:
            Imprimir()
    elif E==4:
        if Login=="Usuario":
            ColsuntarPersona()
        else :
            print("Esta funcion es para Usuarios")
    elif E==5:
        if Login=="Usuario":
            ModificarPersona()
        else :
            print("Esta funcion es para Usuarios")
    elif E==6:
        print("fin")
        sys.exit()


    menu()
    return
    
Login=Inicio()
menu()