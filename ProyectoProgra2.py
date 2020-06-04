import random

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
Provincia=["San José", "Alajuela", "Cartago", "Heredia", "Puntarenas", "Guanacaste", "Limón"]
def Inicio():

  Login=int(input("Digite el numero correspondiente si desea iniciar sesion como: 1.Administrador 2.Analista 3.Usuario:  "))
  if Login == 1 :
      Login="Administrador"
  elif Login == 2:
      Login="Analista"
  elif Login == 3 :
      Login="Usuario"
  else :
      print("Esa opción no está")
    

  return Login 
Login=Inicio()

def CreaCedula():
    Ced=1000000
    while Ced in Datos[0]["cedula"] :
     Ced=Ced+1
    Datos[0]["cedula"].append(Ced)
    return


def CreaRostro():
    Rostros=["Redondo", "Alargado", "Corazón", "Cuadrado", "Ovalado", "Rectangular"]
    Datos[0]["FormaDeRostro"].append(random.sample(Rostros,1))
    return

def CreaPiel():
    Piel=["Negra", "Marrón", "Morena", "Clara", "Blanca"]
    Datos[0]["Piel"].append(random.sample(Piel,1))
    return 

def CreaEmociones():
    Emociones=["Felicidad", "Tristeza", "Seriedad", "Indiferencia", "Enojo", "Temor", "Estrez"]
    Datos[0]["Emociones"].append(random.sample(Emociones,1))
    return

def CreaGenero():
    Generos=["Masculino", "Femenino"]
    Datos[0]["Genero"].append(random.sample(Generos,1))
    return

def CreaGrupo():
    return


def CreaAccesorios():
    Accesorios=["lentes", "Aretes", "Percing", "Tatuajes", "Collar", "Ninguno", "Ninguno", "Ninguno", "Ninguno", "Ninguno"]
    Datos[0]["Accesorios"].append(random.sample(Accesorios,1))
    return


def CreaCabello():
    ColorDelPelo=["negro", "rubio", "café", "castaño", "gris", "invisible"]
    Densidad=["Escaso", "Moderado", "Abundante"]
    Textura=["lacio", "Ondulado", "Rizado"]
    Pelo=[]
    Pelo.append(random.sample(ColorDelPelo,1))
    if "invisible" in Pelo[0] :
     Pelo.append(["invisible"])
     Pelo.append(["invisible"])
    else :
     Pelo.append(random.sample(Densidad,1))
     Pelo.append(random.sample(Textura,1))
    Datos[0]["Cabello"].append(Pelo)
    return

def CreaOjos():
    Forma=["almendrados", "separados", "redondos", "caídos", "saltones", "juntos", "profundos", "asiático"]
    Color=["negro", "castaño", "ámbar", "avellana", "verde", "azul", "gris"]
    Datos[0]["Ojos"].append(random.sample(Forma,1))
    Datos[0]["Ojos"].append(random.sample(Color,1))
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



def CreaProvincia():
    Provincia=["San José", "Alajuela", "Cartago", "Heredia", "Puntarenas", "Guanacaste", "Limón"]
    Datos[0]["Provincia"].append(random.sample(Provincia,1))
    return
print(Login)

Datos=[{"cedula":[], "Edad":[], "FormaDeRostro":[], "Piel":[], "Emociones":[], "Genero":[], "Grupo":[], "Accesorios":[], "Cabello":[], "Ojos":[], "Provincia":[]}]

def CrearPersonaAleatoria(Contador):
    X=0
    while X != Contador:
        CreaCedula()
        print(Datos[0]["cedula"])

        #Creaedad

        CreaRostro()
        print(Datos[0]["FormaDeRostro"])

        CreaPiel()
        print(Datos[0]["Piel"])

        CreaEmociones()
        print(Datos[0]["Emociones"])

        CreaGenero()
        print(Datos[0]["Genero"])

        CreaGrupo()

        CreaAccesorios()
        print(Datos[0]["Accesorios"])

        CreaCabello()
        print(Datos[0]["Cabello"])

        CreaOjos()
        print(Datos[0]["Ojos"])

        CreaProvincia()
        print(Datos[0]["Provincia"])
        X=X+1
    menu()
    return


def CreaPersonajeManualmente():


    CreaCedula()
    Datos[0]["Edad"].append([input("Digite la edad correspondiente en el siguiente formato dia/mes/año:  ")])
    Datos[0]["FormaDeRostro"].append([Rostros[int(input("Digite el numero correspondiente al rostro que desea: 0.Redondo 1.Alargado 2.Corazon 3.Cuadrado 4.Ovalado 5.Rectangular:  "))]])
    Datos[0]["Piel"].append([Piel[int(input("Digite el numero correspondiente al color de piel que desea: 0.Negra 1.Marrón 2.Morena 3.Clara 4.Blanca:  "))]])
    Datos[0]["Emociones"].append([Emociones[int(input("Digite el numero de la emocion correspondiente: 0.Felicidad 1.Tristeza 2.Seriedad 3.Indiferencia 4.Enojo 5.Temor 6.Estrez"))]])
    Datos[0]["Genero"].append([Generos[int(input("Digite el numero correspondiente al color de piel que desea: 0.Negra 1.Marrón 2.Morena 3.Clara 4.Blanca:  "))]])
    #Datos[0]["Grupo"].append(Grupo[int(input("Digite el numero correspondiente al color de piel que desea: 0.Negra 1.Marrón 2.Morena 3.Clara 4.Blanca:  "))])
    Datos[0]["Accesorios"].append([Accesorios[int(input("Digite el numero correspondiente al color de piel que desea: 0.Negra 1.Marrón 2.Morena 3.Clara 4.Blanca:  "))]])
    Pelo=[]
    Pelo.append([ColorDelPelo[int(input("Digite el numero correspodiente al color del cabello: 0.negro 1.rubio 2.café 3.castaño 4.gris 5.invisible"))]])
    Pelo.append([Densidad[int(input("Digite el numero correspodiente a la densidad del cabello: 0.Escaso 1.Moderado 2.Abundante"))]])
    Pelo.append([Textura[int(input("Digite el numero correspodiente a la textura del cabello: 0.lacio 1.Ondulado 2.Rizado"))]])

    Datos[0]["Cabello"].append(Pelo) 

    Datos[0]["Ojos"].append([Forma[int(input("Digite el numero correspondiente a la forma de ojos que desea: 0.Negra 1.Marrón 2.Morena 3.Clara 4.Blanca:  "))]])        
    Datos[0]["Ojos"].append([Color[int(input("Digite el numero correspondiente al color de ojod que desea: 0.Negra 1.Marrón 2.Morena 3.Clara 4.Blanca:  "))]])


        
    Datos[0]["Provincia"].append([Provincia[int(input("Digite el numero correspondiente a su provincia: 0.San José 1.Alajuela 2.Cartago 3.Heredia 4.Puntarenas 5.Guanacaste 6.Limón"))]])



    menu()
    return



def menu():
    print("¿Que desea hacer? ")
    E=int(input("1.Crear persona aleatoriamente 2.Crear persona manualmente 3.Para terminar:   "))
    if E==1:
        if Login=="Administrador":
            contador=int(input("Cuantas personas desea Crear"))
            CrearPersonaAleatoria(contador)
        else:
            print("Esta funcion es para administradores")
            Inicio()
    elif E==2:
        if Login=="Administrador":
            CreaPersonajeManualmente()
        else :
            print("Esta funcion es para administradores")
            Inicio()
    elif E==3:
        #ModificarPersona()
        print("fin")



    return
