"""
AUTORES: Paulo Rojas,Leonardo Bolaños
FECHA:  07/06/2020
"""

"""
DESCRIPCIÓN:Es un programa que puede crear personas aleatoria y manualmente
ENTRADAS:Datos de la características de las personas
SALIDAS:Personas y informes.
RESTRICCIONES:
"""
import random #se importa el módulo random que permite generar valores aleatorios.
import sys #se importa el módulo sys que permite cerrar ciclos.

Rostros=["Redondo", "Alargado", "Corazón", "Cuadrado", "Ovalado", "Rectangular"] #se declara la variable"Rostros" con una lista que tiene las diferentes formas que pueden tener las caras de las personas.
Piel=["Negra", "Marrón", "Morena", "Clara", "Blanca"] #se declara la variable "Piel" con una lista que tiene los diferentes colores de piel que tendrían las personas.
Emociones=["Felicidad", "Tristeza", "Seriedad", "Indiferencia", "Enojo", "Temor", "Estrés"] #se declara la variable "Emociones" con una lista que tiene las diferentes emociones que llegarán a tener las personas.
Generos=["Masculino", "Femenino"] #se declara la variable "Generos" con una lista que contiene el genero que tendrá cada persona.
Accesorios=["lentes", "Aretes", "Percing", "Tatuajes", "Collar", "Ninguno"] #se declara la variable "Accesorios" con una lista que almacena los distintos accsorios que llegarían a tener las personas.
ColorDelPelo=["negro", "rubio", "café", "castaño", "gris", "invisible"] #se declara la variable "ColorDelPelo" con una lista que almacena los diferentes colores de pelo que tienen las personas.
Densidad=["Escaso", "Moderado", "Abundante","","","invisible"] #se declara una variable "Densidad" con una lista que almacena las diferentes cantidades de cabello que tendrán las personas.
Textura=["lacio", "Ondulado", "Rizado","","","invisible"] #se declara la variable "Textura" con una lista que almacena las distintas texturas de cabello que tendrán las personas.
Forma=["almendrados", "separados", "redondos", "caídos", "saltones", "juntos", "profundos", "asiático"] #se declara la variable "Forma" con una lista que almacena las diferentes formas de los ojos que pueden tener las personas.
Color=["negro", "castaño", "ámbar", "avellana", "verde", "azul", "gris"] #se declara la variable "Color" con una lista que contiene los distintos colores de ojos que tienen las personas.
Provincia=["","San José", "Alajuela", "Cartago", "Heredia", "Puntarenas", "Guanacaste", "Limón"] #se declara la variable "Provincia" con una lista que almacena las privincias en  la viven cada persona.
Ropa=["Blusa", "Saco", "Faja", "Sombrero", "Corbata", "Camisa", "Camiseta", "Pantalón", "Short", "Medias", "Ropa Interior"]#datos quemados de la ropa
Calzado=["Tenis deportivas", "Tacones", "Tenis de baloncesto", "Tacos", "Zapato de tacon", "Sandalias", "Botas de hule", "Botas de cuero"]#daors quemados del calzado

def Inicio(): #con la función "Inicio" se inicia el login del programa

    N=int(input("Digite el numero correspondiente si desea iniciar sesion como: 1.Administrador 2.Analista 3.Usuario:  ")) #se declara la variable "N" con un input de números enteros.
    if N == 1 : #se inicia un if para el login,que dice que si se selecciona el número 1 se loguea como administrador
      Login="Administrador" 
    elif N == 2: #elif dice que si se selecciona el número 2 se loguea como analista.
      Login="Analista"
    elif N == 3 : #elif dice que si se selecciona el número 3 se loguea como usuario.
      Login="Usuario"
    else :# Se finaliza el if con un else que dice que si no se selecciona ninguno de estas tres opciones la opción que escogió no existe
      print("Esa opción no está") #se imprime esa opción no está
    return Login #se returna el login.



def CreaCedula(): #se crea la función CreaCedula
    Ced=1000000 #la variable "Ced" es igual a 1000000,número que entrará en un contador que irá cambiando sus números de izquierda a derecha para generar nuevas cédulas
    while Ced in Datos[0]["cedula"] : #se hace un ciclo while para recorrer "Ced".
     Ced=Ced+1 #el contador "ced=ced+1" hace que los números de las cédulas vayan cambiando.
    Datos[0]["cedula"].append(Ced) #se hace un .append para guardar la variable "Ced" en la ubicación Datos[0]["cedula"]
    return #se returna la función CreaCedula

def CreaEdad (): #se cre la función "CreaEdad"
    c=random.randint(1920,2020) #se declara la variable "c" con un random.randint entre 1920 y 2020 para crear el año de nacimiento de las personas aleatoriamente.
    Años=c #se declara la variable "Años" que es igual a "c"


    i=random.randint(1,12) #se declara la variable "i" con un random.randint entre 1 y 12 para crear el mes del año de nacimiento de las personas aleatoriamente.
    Meses=i #se declara la variable "Meses" que es igual a "i"
     
             
    d=random.randint(1,30)#se declara la variable "d" con un random.randint entre 1 y 30 para crear el día del mes de nacimiento de las personas aleatoriamente.
    Dias=d #se declara la variable "Dias" que es igual a "c"

    EdadPersona= [ Años,Meses,Dias] #se declara la variable "EdadPersona" con una lista que almacena las variables:Años,Meses y Dias.
    Datos[0]["Edad"].append(EdadPersona) #se hace un .append para guardar la variable "EdadPersona" en la dirección Datos[0]["Edad"]
    return #se returna la función CreaEdad


def CreaRostro(): #se crea la función CreaRostro
    Datos[0]["FormaDeRostro"].append(random.randint(0, 5)) #se utiliza un .append para guardar el random.randint que va de 0 a 5 (que son la posición de las distintas formas de rostro)y selecciona un valor aleatorio en la dirección Datos[0]["FormaDeRostro"]
    return #se returna la función CreaRostro

def CreaPiel(): #se crea la función CreaPiel
    Datos[0]["Piel"].append(random.randint(0, 4)) #se utiliza un .append para guardar el random.randint que va de 0 a 4 (que son la posición de los distintos colores de piel)y selecciona un valor aleatorio en la dirección Datos[0]["Piel"]
    return 

def CreaEmociones(): #se crea la función CreaEmociones
    Datos[0]["Emociones"].append(random.randint(0, 6)) #se utiliza un .append para guardar el random.randint que va de 0 a 6 (que son la posición de las distintas emociones)y selecciona un valor aleatorio en la dirección Datos[0]["Emociones"]
    return 

def CreaGenero(): #se crea la función CreaGenero
    Datos[0]["Genero"].append(random.randint(0, 1)) #se utiliza un .append para guardar el random.randint que va de 0 a 1 (que son la posición de los distintos generos)y selecciona un valor aleatorio en la dirección Datos[0]["Genero"]
    return

def CreaGrupo(): #se crea la función CreaGrupo
    return #se returna la función CreaGrupo


def CreaAccesorios(): #se crea la función CreaAccesorios

    Datos[0]["Accesorios"].append(random.randint(0, 9)) #se utiliza un .append para guardar el random.randint que va de 0 a 9 (que son la posición de los distintos accesorios) y selecciona un valor aleatorio en la dirección Datos[0]["Accesorios"]
    return #se returna la función CreaAccesorios

def CreaRopa(): #se crea la función CreaAccesorios

    Datos[0]["Ropa"].append(random.randint(0, 11)) #se utiliza un .append para guardar el random.randint que va de 0 a 9 (que son la posición de los distintas ropas) y selecciona un valor aleatorio en la dirección Datos[0]["Ropa"]
    return #se returna la función CreaRopa

def CreaCalzado(): #se crea la función CreaAccesorios

    Datos[0]["Calzado"].append(random.randint(0, 11)) #se utiliza un .append para guardar el random.randint que va de 0 a 9 (que son la posición de los distintos calzados) y selecciona un valor aleatorio en la dirección Datos[0]["Calzado"]
    return #se returna la función CreaCalzado

def CreaCabello(): #se crea la función CreaCabello

    Pelo=[] #se declara la variable Pelo con una lista sin elementos 
    x=random.randint(0, 5) #se declara la variable x con un random.randint que va entre 0 y 5 (posiciones de los distintos colores de cabello) y selecciona un valor aleatorio
    Pelo.append(x) #se utiliza un .append para guardar la variable x en la variable Pelo

    if x == 5 :
     Pelo.append(5)
     Pelo.append(5)
    else :
     Pelo.append(random.randint(0, 2))
     Pelo.append(random.randint(0, 2))
    Datos[0]["Cabello"].append(Pelo)
    return
 #se utliza un if con que va seleccionando valores aleatorios y con un .append los guarda en la dirección Datos[0]["Cabello"].luego returna la función CreaCabello

def CreaOjos():  #se crea la función CreaOjos.
    ojos=[] #se declara la variable ojos con una lista vacía.
    ojos.append(random.randint(0, 7))
    ojos.append(random.randint(0, 6))
    Datos[0]["Ojos"].append(ojos)
    return
 #se utlizan random.randint para obtener valores random y guardarlos en la lista ojos con un .append .Luego la variable ojos se guarda con un .append en la dirección  Datos[0]["Ojos"] y después se returna CreaOjos

def GrupoEtario(edad): #se crea la función GrupoEtario con el parámetro (edad)
    if edad[0]>=2019: 
        etario="Bebe" #si la edad de la persona es menor o igual al año 2019 su grupo etario es bebé.
    elif edad[0]<2019 and edad[0]>=2008:
        etario="Niño" #si la edad de la persona es mayor al año 2019 y menor o igual aal año 2008 su grupo etario es niño
    elif edad[0]<2008 and edad[0]>=2002:
        etario="Adolescente" #si la edad de la persona es mayor al año  2008 y menor o igual al año 2002 su grupo etario es adolescente
    elif edad[0]<2002:
        etario="Adulto" #si la edad de la persona es mayor al año 2002 su grupo etario es adulto
    return etario #se returna la variable etario
    #se utiliza un if para comparar el año de nacimiento de la persona con su grupo etario, también se utiliza and para el rango de edad de las comparaciones de niños y adolescentes.
        


def CreaProvincia(): #se crea la función CreaProvincia

    Datos[0]["Provincia"].append(random.randint(1, 7)) #utilizando un .append se introducen valores aleatorios en la dirección Datos[0]["Provincia"]
    return #se returna la función CreaProvincia

Datos=[{"cedula":[], "Edad":[], "FormaDeRostro":[], "Piel":[], "Emociones":[], "Genero":[], "Grupo":[], "Accesorios":[], "Cabello":[], "Ojos":[], "Provincia":[], "Calzado":[], "Ropa":[] }] 
#se declara la variable "Datos"con una lista que contiene un diccionario, que almacena todas las funciones de las características de las personas que se convierten en claves  y cada una de ellas tiene como valoruna lista vacía 

def CrearPersonaAleatoria(Contador): #se crea la función CreaPersonaAleatoria con el parámetro (contador)
    X=0
    while X != Contador:
        CreaCedula()

        CreaEdad ()

        CreaRostro()

        CreaPiel()

        CreaEmociones()

        CreaGenero()

        CreaGrupo()

        CreaAccesorios()

        CreaCabello()

        CreaOjos()

        CreaProvincia()

        CreaRopa()

        CreaCalzado()
        X=X+1
    menu()
    return
 #Se declara la variable "X" la cual va a recorrer un while que es un contador la variable "X" va sumando 1 conforme se van invocando todas las funciones y luego vuelve al menú.Por último se returna la función CreaPersonaAleatoria

def CreaPersonajeManualmente(): #se declara la función CreaPersonajeManualmente


    CreaCedula() #se invoca CreaCedula
    Fecha=[] #se declara la variable Fecha con una lista vacía
    Fecha.append(int(input("Digite su año de nacimieto:  "))) #se hace un input en el cual se le pide a la persona que digite su año de nacimiento el cual con un .append se guarda en la lista Fecha
    Fecha.append(int(input("Digite su mes de nacimieto:  "))) #se hace un input en el cual se le pide a la persona que digite su mes de nacimiento el cual con un .append se guarda en la lista Fecha
    Fecha.append(int(input("Digite su dia de nacimieto:  "))) #se hace un input en el cual se le pide a la persona que digite su dia del mes de nacimiento el cual con un .append se guarda en la lista Fecha
    Datos[0]["Edad"].append(Fecha) #con un .append se guarda la variable Fecha en la dirección  Datos[0]["Edad"]
    Datos[0]["FormaDeRostro"].append(int(input("Digite el numero correspondiente al rostro que desea: 0.Redondo 1.Alargado 2.Corazon 3.Cuadrado 4.Ovalado 5.Rectangular:  ")))#con un input se le pide a la persona que digite el numero correspondiente a la forma del rostro que desea y con un .append guarda los datos en la dirección Datos[0]["FormaDeRostro"].
    Datos[0]["Piel"].append(int(input("Digite el numero correspondiente al color de piel que desea: 0.Negra 1.Marrón 2.Morena 3.Clara 4.Blanca:  ")))#con un input se le pide a la persona que digite el numero correspondiente al color de piel que desea y con un .append guarda los datos en la dirección Datos[0]["Piel"]
    Datos[0]["Emociones"].append(int(input("Digite el numero de la emocion correspondiente: 0.Felicidad 1.Tristeza 2.Seriedad 3.Indiferencia 4.Enojo 5.Temor 6.Estrez")))#con un input se le pide a la persona que digite el numero correspondiente a la emoción que desea y con un .append guarda los datos en la dirección Datos[0]["Emociones"]
    Datos[0]["Genero"].append(int(input("Digite el numero correspondiente al género que desea:0.Masculino,1.Femenino:  ")))#con un input se le pide a la persona que digite el numero correspondiente género que desea y con un .append guarda los datos en la dirección  Datos[0]["Genero"]
    Datos[0]["Accesorios"].append(int(input("Digite el numero correspondiente al accesorio que desea:0.lentes,1.Aretes,2.Percing,3.Tatuajes,4.Collar,5.Ninguno ")))#con un input se le pide a la persona que digite el numero correspondiente al accesorio que desea y con un .append guarda los datos en la dirección Datos[0]["Accesorios"]
    Pelo=[] #se crea la variable "Pelo" con una lista vacía
    Pelo.append(int(input("Digite el numero correspodiente al color del cabello: 0.negro 1.rubio 2.café 3.castaño 4.gris 5.invisible"))) #se hace un input en el cual se le pide a la persona que digite el numero correspondiente al color de cabello que desea el cual con un .append se guarda en la lista Pelo
    Pelo.append(int(input("Digite el numero correspodiente a la densidad del cabello: 0.Escaso 1.Moderado 2.Abundante"))) #se hace un input en el cual se le pide a la persona que digite el numero correspondiente a la densidad de cabello que desea el cual con un .append se guarda en la lista Pelo
    Pelo.append(int(input("Digite el numero correspodiente a la textura del cabello: 0.lacio 1.Ondulado 2.Rizado"))) #se hace un input en el cual se le pide a la persona que digite el numero correspondiente a la textura de cabello que desea el cual con un .append se guarda en la lista Pelo
    Datos[0]["Cabello"].append(Pelo)  #con un .append se guarda la variable Pelo en la dirección  Datos[0]["Edad"]
    ojos=[] #se crea la variable "ojos" con una lista vacía
    ojos.append(int(input("Digite el numero correspondiente a la forma de ojos que desea: 0.almendrados 1.separados 2.redondos 3.caídos 4.saltones 5.juntos 6.profundos 7.asiático:  ")))  #se hace un input en el cual se le pide a la persona que digite el numero correspondiente a la forma  que desea el cual con un .append se guarda en la lista ojos.   
    ojos.append(int(input("Digite el numero correspondiente al color de ojos que desea: 0.Negra 1.Marrón 2.Morena 3.Clara 4.Blanca:  "))) #se hace un input en el cual se le pide a la persona que digite el el numero correspondiente al color de los que desea el cual con un .append se guarda en la lista ojos
    Datos[0]["Ojos"].append(ojos)  #con un .append se guarda la variable ojos en la dirección  Datos[0]["Ojos"]

        
    Datos[0]["Provincia"].append(int(input("Digite el numero correspondiente a su provincia: 1.San José 2.Alajuela 3.Cartago 4.Heredia 5.Puntarenas 6.Guanacaste 7.Limón:   ")))
    #con un input se le pide a la persona que digite el numero correspondiente a la provincia que desea y con un .append guarda los datos en la dirección Datos[0]["Provincia"].


    menu() #vuelve al menú
    return #returna la función CreaPersonajeManualmente



def ConsultarPersona(): #se crea la función "ConsultarPersona"
    for ced in Datos[0]["cedula"]: #con un ciclo for se recorre  Datos[0]["cedula"]
        print(ced) #se imprime ced
 
    contador=Datos[0]["cedula"].index(int(input("Digite la cedula de la persona que desea consultar"))) 
     #se declara la variable contador que su función es con un .index se puedan ver las cédulas y digitar la que se quiera consultar.

    print(ced)  #se imprime ced
    print("forma de rostro:  ", Rostros[Datos[0]["FormaDeRostro" ][contador]])
    print("color de piel:  ", Piel[Datos[0]["Piel"][contador]])
    print("emocion:  ", Emociones[Datos[0]["Emociones" ][contador]]) 
    print("Genero:  ", Generos[Datos[0]["Genero"][contador]])
    print("Grupo etario:  ", GrupoEtario(Datos[0]["Edad"][contador]))
    print("Accesorio:  ", Accesorios[Datos[0]["Accesorios"][contador]])
    print("Color del cabello:  ", ColorDelPelo[Datos[0]["Cabello"][contador][0]])
    print("Densidad del cabello:  ", Densidad[Datos[0]["Cabello"][contador][1]])
    print("Textura del cabello:  ", Textura[Datos[0]["Cabello"][contador][2]])
    print("Forma de ojos:  ", Forma[Datos[0]["Ojos"][contador][0]])
    print("Color de ojos:  ", Color[Datos[0]["Ojos"][contador][1]])
    print("Provincia:  ", Provincia[Datos[0]["Provincia"][contador]])
    menu()
    return
 #al imprimir ced se muestran todas las características de la persona,luego vuelve al menú y returna la función ConsultarPersona.

def ModificarPersona(): #se crea la función ModificarPersona
    for ced in Datos[0]["cedula"]: #con un ciclo se recorre Datos[0]["cedula"]
        print(ced) #se imprime ced

    C=Datos[0]["cedula"].index(int(input("Digite la cedula de la persona que desea cambiar:  "))) #se declara la variable "c" que su función es con un .index se puedan ver las cédulas y digitar la que se quiera modificar.
    Datos[0]["Provincia"][C]=int(input("Digite el numero correspondiente a su nueva provincia: 1.San José 2.Alajuela 3.Cartago 4.Heredia 5.Puntarenas 6.Guanacaste 7.Limón:   ")) #con un input se le pide que digite el numero correspondiente a la provincia que desea modificar.
    Datos[0]["Emociones"][C]=int(input("Digite el numero de la emocion correspondiente: 0.Felicidad 1.Tristeza 2.Seriedad 3.Indiferencia 4.Enojo 5.Temor 6.Estrez")) #con un input se le pide que digite el numero correspondiente a la emoción que desea modificar.
    menu() #se regresa al menú
    return # se returna la función ModificarPersona

def ImprimirInformes(Lista): #se crea la función ImprimirInformes con el parámetro (Lista)
    for ced in Lista: #ced recorre Lista mediante un ciclo for
       contador=Datos[0]["cedula"].index(ced) #se declara la variable "contador" que su función es con un .index se puedan ver las cédulas y mostrar informes.
       print(ced) #se imprime ced
       print("forma de rostro:  ", Rostros[Datos[0]["FormaDeRostro" ][contador]])
       print("color de piel:  ", Piel[Datos[0]["Piel"][contador]])
       print("emocion:  ", Emociones[Datos[0]["Emociones" ][contador]]) 
       print("Genero:  ", Generos[Datos[0]["Genero"][contador]])
       print("Grupo etario:  ", GrupoEtario(Datos[0]["Edad"][contador]))
       print("Accesorio:  ", Accesorios[Datos[0]["Accesorios"][contador]])
       print("Color del cabello:  ", ColorDelPelo[Datos[0]["Cabello"][contador][0]])
       print("Densidad del cabello:  ", Densidad[Datos[0]["Cabello"][contador][1]])
       print("Textura del cabello:  ", Textura[Datos[0]["Cabello"][contador][2]])
       print("Forma de ojos:  ", Forma[Datos[0]["Ojos"][contador][0]])
       print("Color de ojos:  ", Color[Datos[0]["Ojos"][contador][1]])
       print("Provincia:  ", Provincia[Datos[0]["Provincia"][contador]])
    return
 #al imprimir ced se muestran los informes con las características de las personas

def informes(): #se crea la función informes
    SanJose=0
    SanJoseBebe=[]
    SanJoseNiño=[]
    SanJoseAdolescente=[]
    SanJoseAdulto=[]
    Alajuela=0
    AlajuelaBebe=[]
    AlajuelaNiño=[]
    AlajuelaAdolescente=[]
    AlajuelaAdulto=[]
    Cartago=0
    CartagoBebe=[]
    CartagoNiño=[]
    CartagoAdolescente=[]
    CartagoAdulto=[]
    Heredia=0
    HerediaBebe=[]
    HerediaNiño=[]
    HerediaAdolescente=[]
    HerediaAdulto=[]
    Limon=0
    LimonBebe=[]
    LimonNiño=[]
    LimonAdolescente=[]
    LimonAdulto=[]
    Guanacaste=0
    GuanacasteBebe=[]
    GuanacasteNiño=[]
    GuanacasteAdolescente=[]
    GuanacasteAdulto=[]
    Puntarenas=0
    PuntarenasBebe=[]
    PuntarenasNiño=[]
    PuntarenasAdolescente=[]
    PuntarenasAdulto=[]
   #se declaran variables de cada una de las provincias a cada provincia se le asignan los distintos grupos etarios a los que pueden pertenecer sus ciudadanos.
   
    for persona in Datos[0]["cedula"]: #se hace un ciclo for para recorrer Datos[0]["cedula"]

        if Datos[0]["Provincia"][Datos[0]["cedula"].index(persona)] == 1:
            SanJose=SanJose+1
            if GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Bebe":
               SanJoseBebe.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Niño":
                SanJoseNiño.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adolescente":
                SanJoseAdolescente.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adulto":
                SanJoseAdulto.append(persona)
        elif Datos[0]["Provincia"][Datos[0]["cedula"].index(persona)] == 2:
            Alajuela=Alajuela+1
            if GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Bebe":
                AlajuelaBebe.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Niño":
                AlajuelaNiño.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adolescente":
                AlajuelaAdolescente.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adulto":
                AlajuelaAdulto.append(persona)
        elif Datos[0]["Provincia"][Datos[0]["cedula"].index(persona)] == 3:
            Cartago=Cartago+1
            if GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Bebe":
                CartagoBebe.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Niño":
                CartagoNiño.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adolescente":
                CartagoAdolescente.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adulto":
                CartagoAdulto.append(persona)
        elif Datos[0]["Provincia"][Datos[0]["cedula"].index(persona)] == 4:
            Heredia=Heredia+1
            if GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Bebe":
                HerediaBebe.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Niño":
                HerediaNiño.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adolescente":
                HerediaAdolescente.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adulto":
                HerediaAdulto.append(persona)
        elif Datos[0]["Provincia"][Datos[0]["cedula"].index(persona)] == 5:
            Puntarenas=Puntarenas+1
            if GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Bebe":
                PuntarenasBebe.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Niño":
                PuntarenasNiño.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adolescente":
                PuntarenasAdolescente.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adulto":
                PuntarenasAdulto.append(persona)
        elif Datos[0]["Provincia"][Datos[0]["cedula"].index(persona)] == 6:
            Guanacaste=Guanacaste+1
            if GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Bebe":
                GuanacasteBebe.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Niño":
                GuanacasteNiño.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adolescente":
                GuanacasteAdolescente.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adulto":
                GuanacasteAdulto.append(persona)
        elif Datos[0]["Provincia"][Datos[0]["cedula"].index(persona)] == 7:
            Limon=Limon+1
            if GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Bebe":
                LimonBebe.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Niño":
                LimonNiño.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adolescente":
                LimonAdolescente.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adulto":
                LimonAdulto.append(persona)
 #se hacen if en cada una de las 7 provincias, en las cuales mediante un index que busca la cedula de cada persona, con la cedula busca la edad y dependiendo de la edad selecciona el grupo etario y lo guarda persona.Al pasar por cada provincia se le suma uno al contador para recorrer todas. 

    TotalDeCostaRicenses=len(Datos[0]["cedula"]) #se declara la variable "TotalDeCostarricenses" la cual es la cantidad de cédulas que existan.
    print("Total de bebes en San Jose:  ", len(SanJoseBebe),"Equivale a un:", len(SanJoseBebe)/TotalDeCostaRicenses, "%")
    ImprimirInformes(SanJoseBebe)
    print("Total de niños en San Jose:  ", len(SanJoseNiño),"Equivale a un:",len(SanJoseNiño)/TotalDeCostaRicenses, "%")
    ImprimirInformes(SanJoseNiño)
    print("Total de adolescentes en San Jose:  ", len(SanJoseAdolescente),"Equivale a un:",len(SanJoseAdolescente)/TotalDeCostaRicenses, "%")
    ImprimirInformes(SanJoseAdolescente)
    print("Total de Adultos en San Jose:  ", len(SanJoseAdulto),"Equivale a un:",len(SanJoseAdulto)/TotalDeCostaRicenses, "%")
    ImprimirInformes(SanJoseAdulto)
    print("Total de bebes en Alajuela:  ", len(AlajuelaBebe),"Equivale a un:",len(AlajuelaBebe)/TotalDeCostaRicenses, "%")
    ImprimirInformes(AlajuelaBebe)
    print("Total de niños en Alajuela:  ", len(AlajuelaNiño),"Equivale a un:",len(AlajuelaNiño)/TotalDeCostaRicenses, "%")
    ImprimirInformes(AlajuelaNiño)
    print("Total de adolescentes en Alajuela:  ", len(AlajuelaAdolescente),"Equivale a un:",len(AlajuelaAdolescente)/TotalDeCostaRicenses, "%")
    ImprimirInformes(AlajuelaAdolescente)
    print("Total de Adultos en Alajuela:  ", len(AlajuelaAdulto),"Equivale a un:",len(AlajuelaAdulto)/TotalDeCostaRicenses, "%")
    ImprimirInformes(AlajuelaAdulto)    
    print("Total de bebes en Cartago:  ", len(CartagoBebe),"Equivale a un:",len(CartagoBebe)/TotalDeCostaRicenses, "%")
    ImprimirInformes(CartagoBebe)
    print("Total de niños en Cartago:  ", len(CartagoNiño),"Equivale a un:",len(CartagoNiño)/TotalDeCostaRicenses, "%")
    ImprimirInformes(CartagoNiño)
    print("Total de adolescentes en Cartago:  ", len(CartagoAdolescente),"Equivale a un:",len(CartagoAdolescente)/TotalDeCostaRicenses, "%")
    ImprimirInformes(CartagoAdolescente)
    print("Total de Adultos en Cartago:  ", len(CartagoAdulto),"Equivale a un:",len(CartagoAdulto)/TotalDeCostaRicenses, "%")
    ImprimirInformes(CartagoAdulto)
    print("Total de bebes en Heredia:  ", len(HerediaBebe),"Equivale a un:",len(HerediaBebe)/TotalDeCostaRicenses, "%")
    ImprimirInformes(HerediaBebe)
    print("Total de niños en Heredia:  ", len(HerediaNiño),"Equivale a un:",len(HerediaNiño)/TotalDeCostaRicenses, "%")
    ImprimirInformes(HerediaNiño)
    print("Total de adolescentes en Heredia:  ", len(HerediaAdolescente),"Equivale a un:",len(HerediaAdolescente)/TotalDeCostaRicenses, "%")
    ImprimirInformes(HerediaAdolescente)
    print("Total de Adultos en Heredia:  ", len(HerediaAdulto),"Equivale a un:",len(HerediaAdulto)/TotalDeCostaRicenses, "%")
    ImprimirInformes(HerediaAdulto)
    print("Total de bebes en Puntarenas:  ", len(PuntarenasBebe),"Equivale a un:",len(PuntarenasBebe)/TotalDeCostaRicenses, "%")
    ImprimirInformes(PuntarenasBebe)
    print("Total de niños en Puntarenas:  ", len(PuntarenasNiño),"Equivale a un:",len(PuntarenasNiño)/TotalDeCostaRicenses, "%")
    ImprimirInformes(PuntarenasNiño)
    print("Total de adolecentes en Puntarenas:  ", len(PuntarenasAdolescente),"Equivale a un:",len(PuntarenasAdolescente)/TotalDeCostaRicenses, "%")
    ImprimirInformes(PuntarenasAdolescente)
    print("Total de Adultos en Puntarenas:  ", len(PuntarenasAdulto),"Equivale a un:",len(PuntarenasAdulto)/TotalDeCostaRicenses, "%")
    ImprimirInformes(PuntarenasAdulto)
    print("Total de bebes en Puntarenas:  ", len(PuntarenasBebe),"Equivale a un:",len(PuntarenasBebe)/TotalDeCostaRicenses, "%")
    ImprimirInformes(GuanacasteBebe)
    print("Total de niños en Puntarenas:  ", len(GuanacasteNiño),"Equivale a un:",len(GuanacasteNiño)/TotalDeCostaRicenses, "%")
    ImprimirInformes(GuanacasteNiño)
    print("Total de adolescentes en Puntarenas:  ", len(GuanacasteAdolescente),"Equivale a un:",len(GuanacasteAdolescente)/TotalDeCostaRicenses, "%")
    ImprimirInformes(GuanacasteAdolescente)
    print("Total de Adultos en Puntarenas:  ", len(GuanacasteAdulto),"Equivale a un:",len(GuanacasteAdulto)/TotalDeCostaRicenses, "%")
    ImprimirInformes(GuanacasteAdulto)
    print("Total de bebes en Puntarenas:  ", len(LimonBebe),"Equivale a un:",len(LimonBebe)/TotalDeCostaRicenses, "%")
    ImprimirInformes(LimonBebe)
    print("Total de niños en Puntarenas:  ", len(LimonNiño),"Equivale a un:",len(LimonNiño)/TotalDeCostaRicenses, "%")
    ImprimirInformes(LimonNiño)
    print("Total de adolescentes en Puntarenas:  ", len(LimonAdolescente),"Equivale a un:",len(LimonAdolescente)/TotalDeCostaRicenses, "%")
    ImprimirInformes(LimonAdolescente)
    print("Total de Adultos en Puntarenas:  ", len(LimonAdulto),"Equivale a un:",len(LimonAdulto)/TotalDeCostaRicenses, "%")
    ImprimirInformes(LimonAdulto)
 #se imprimen informes por provincia de cada uno de sus grupos etarios,para hacerlo se utiliza un len para leer la cantidad de personas por edad que hay en cada provincia eso se divide entre el total de costarricenses y se imprime el resultado.

    print("Total de personas en San José:  ",SanJose, "%",SanJose/TotalDeCostaRicenses) 
    print("Total de personas en Alajuela:  ",Alajuela, "%",Alajuela/TotalDeCostaRicenses)
    print("Total de personas en Cartago:  ",Cartago, "%",Cartago/TotalDeCostaRicenses)
    print("Total de personas en Heredia:  ",Heredia, "%",Heredia/TotalDeCostaRicenses)
    print("Total de personas en Puntarenas:  ",Puntarenas, "%",Puntarenas/TotalDeCostaRicenses)
    print("Total de personas en Guanacaste:  ",SanJose, "%",SanJose/TotalDeCostaRicenses)
    print("Total de personas en Limon:  ", Limon, "%",Limon/TotalDeCostaRicenses)
 #se imprime el porcentaje de habitantes que tiene cada provincia dividiendo el total de personas de la provincia entre el total de costarricenses.

    Fe=0
    Tri=0
    Ser=0
    Ind=0
    Eno=0
    Tem=0
    Ezt=0
    #se declaran variables para hacer informes sobre las emociones.
    for Emo in Datos[0]["Emociones" ] : #con un ciclo for se recorre Datos[0]["Emociones" ] mediante la variable "Emo"
        if Emo == 0:
            Fe=Fe+1
        elif Emo == 1:
            Tri=Tri+1
        elif Emo == 2:
            Ser=Ser+1
        elif Emo == 3:
            Ind=Ind+1
        elif Emo == 4:
            Eno=Eno+1
        elif Emo == 5:
            Tem=Tem+1
        elif Emo == 6:
            Ezt=Ezt+1
     #se hace un if y para seleccionar la emoción que pertenece a la persona, pasando una por una hasta encontrarla y cada vez que pasa por una emoción le suma uno al contador.
    TotalesBebes=len(SanJoseBebe)+len(AlajuelaBebe)+len(CartagoBebe)+len(HerediaBebe)+len(PuntarenasBebe)+len(GuanacasteBebe)+len(LimonBebe)
    TotalesNiños=len(SanJoseNiño)+len(AlajuelaNiño)+len(CartagoNiño)+len(HerediaNiño)+len(PuntarenasNiño)+len(GuanacasteNiño)+len(LimonNiño)
    TotalesAdolescentes=len(SanJoseAdolescente)+len(AlajuelaAdolescente)+len(CartagoAdolescente)+len(HerediaAdolescente)+len(PuntarenasAdolescente)+len(GuanacasteAdolescente)+len(LimonAdolescente)
    TotalesAdultos=len(SanJoseAdulto)+len(AlajuelaAdulto)+len(CartagoAdulto)+len(HerediaAdulto)+len(PuntarenasAdulto)+len(GuanacasteAdulto)+len(LimonAdulto)
    print("Total de bebes en CR",TotalesBebes, "Porcentaje",TotalesBebes/TotalDeCostaRicenses)
    print("Total de niños en CR",TotalesNiños, "Porcentaje",TotalesNiños/TotalDeCostaRicenses)
    print("Total de adolescentes en CR",TotalesAdolescentes, "Porcentaje",TotalesAdolescentes/TotalDeCostaRicenses)
    print("Total de adultos en CR",TotalesAdultos, "Porcentaje",TotalesAdultos/TotalDeCostaRicenses)
 #se imprime el porcentaje total de personas por grupo etario, esto pasando con un len por cada uno de los grupos etarios iguales de cada una de las provincias y los cuales se suman.El resultado de cada uno de los grupos etarios se divide entre el total de costarricenses y ese es el pocentaje de cada uno,

    print("             Felicidad", "Tristeza", "Seriedad", "Indiferencia", "Enojo", "Temor", "Estrez")
    print("Total:      ", Fe,"       ", Tri,"      ", Ser,"      ", Ind,"          ", Eno,"   ", Tem,"   ", Ezt)
    print("Total:      ", Fe/TotalDeCostaRicenses,"     ", Tri/TotalDeCostaRicenses,"    ", Ser/TotalDeCostaRicenses,"    ", Ind/TotalDeCostaRicenses,"       ", Eno/TotalDeCostaRicenses,"  ", Tem/TotalDeCostaRicenses,"   ", Ezt/TotalDeCostaRicenses)
    #se imprimen los porcentajes de las diferentes emociones de las personas esto se hace,dividiendo cada una de las variables de las emociones entre el total de costarricenses y ese es el resultado de los porcentajes de cada una de las emociones.
    menu() #regresa al menú
    return #se returna la función Informes

# class will be created

class FormaOjos(): #"Forma de ojos" class is created
    def __init__(self):
        self.IDFormaOjos=0
        self.nombreFormaOjos=""
    def setformaOjos(self, x):
        self.IDFormaOjos=x
        self.nombreFormaOjos=Rostros[x]
    def getIDFormaOjos(self):
        return self.IDFormaOjos
    def getIDnombreFormaOjoss(self):
        return self.nombreFormaOjos
# attributes are granted with the set and get method

class ColorOjos():#"ColorOjos" class is created
    def __init__(self):
        self.IDColorOjos=0
        self.nombreColorOjos=""
    def setColorOjos(self, x):
        self.IDColorOjos=x
        self.nombreColorOj=Color[x]
    def getIDColorOjos(self):
        return self.IDColorOjos
    def getnombreColorOjos(self):
        return self.nombreColorOjos
#attributes are granted with the set and get method

class Ojos():#"Ojos" class is created
    def __init__(self):
        self.IDOjos=0
        self.Forma=[]
        self.Color=[]
    def setOjos(self, x, y):
        self.IDOjos=0
        self.Forma=x
        self.Color=y
    def getIDOjos(self):
        return self.IDOjos
    def getForma(self):
        return self.Forma
    def getColor(self):
        return self.Color
#attributes are granted with the set and get method

class Emocion():#"Emocion" class is created
    def __init__(self):
        self.IDEmocion=0
        self.nombreEmocion=""
    def setEmocion(self, x):
        self.IDEmocion=x
        self.nombreEmocion=Emociones[x]
    def getIDEmocion(self):
        return self.IDEmocion
    def getnombreEmocion(self):
        return self.nombreEmocion
#attributes are granted with the set and get method

class Genero():#"Genero" class is created
    def __init__(self):
        self.IDGenero=0
        self.nombreGenero=""        
    def setGenero(self, x):
        self.IDGenero=x
        self.nombreGenero=Generos[x]
    def getIDGenero(self):
        return self.IDGenero
    def getnombreGenero(self):
        return self.nombreGenero
#attributes are granted with the set and get method

class Provincias():#"Provincias" class is created
    def __init__(self):
        self.IDProvincia=0
        self.nombreProvincia=""
    def setProvincia(self, x):
        self.IDProvincia=x
        self.nombreProvincia=Provincia[x]
    def getIDProvincia(self):
        return self.IDProvincia
    def getnombreProvincia(self):
        return self.nombreProvincia 
#attributes are granted with the set and get method

class TexturaCabello():#"TexturaCabello" class is created
    def __init__(self):
        self.IDTexturaCabello=0
        self.nombreTexturaCabello=""
    def setTexturaCabello(self, x):
        self.IDTexturaCabello=x
        self.nombreTexturaCabello=Textura[x]
    def getIDTexturaCabello(self):
        return self.IDTexturaCabello
    def getnombreTexturaCabello(self):
        return self.nombreTexturaCabello
#attributes are granted with the set and get method

class DensidadCabello():#"DensidadCabello" class is created
    def __init__(self):
        self.IDDensidadCabello=0
        self.nombreDensidadCabello=""
    def setDensidadCabello(self, x):
        self.IDDensidadCabello=x
        self.nombreDensidadCabello=Densidad[x]
    def getIDDensidadCabello(self):
        return self.IDDensidadCabello
    def getnombreDensidadCabello(self):
        return self.nombreDensidadCabello
#attributes are granted with the set and get method

class ColorDePelo():#"ColorDePelo" class is created
    def __init__(self):
        self.IDColorDePelo=0
        self.nombreColorDePelo=""
    def setColorDePelo(self, x):
        self.IDColorDePelo=x
        self.nombreColorDelPelo=ColorDelPelo[x]
    def getIDColorDePelo(self):
        return self.IDColorDePelo
    def getnombreColorDelPelo(self):
        return self.nombreColorDelPelo
#attributes are granted with the set and get method

class Pelo(): #"Pelo" class is created
    def __init__(self):
        self.IDPelo=0
        self.TexturaCabello=[]
        self.DensidadCabello=[]
        self.ColorDePelo=[]
    def setPelo(self, XXX, YYY, ZZZ):
        self.IDPelo=0
        self.ColorDePelo=XXX
        self.DensidadCabello=YYY
        self.TexturaCabello=ZZZ
    def getTexturaCabello(self):
        return   self.TexturaCabello
    def getDensidadCabello(self):
        return   self.DensidadCabello
    def getColorDePelo(self):
        return   self.ColorDePelo
#attributes are granted with the set and get method

class Formadecara ():#"Formadecara" class is created
    def __init__(self):
        self.IDFormadecara=0
        self.nombreFormadecara=""
    def setFormadecara(self, x):
        self.IDFormadecara=x
        self.nombreFormadecara=Rostros[x]
    def getIDFormadecara(self):
        return self.IDFormadecara
    def getnombreFormadecara(self):
        return self.nombreFormadecara
#attributes are granted with the set and get method

class ColorDePiel ():#"ColorDePiel" class is created
    def __init__(self):
        self.IDColorDePiel=0
        self.nombreColorDePiel=""
    def setColorDePiel(self, x):
        self.IDColorDePiel=x
        self.nombreColorDePiel=Piel[x]
    def getIDColorDePiel(self):
        return self.IDColorDePiel
    def getnombreColorDePiel(self):
        return self.nombreColorDePiel
#attributes are granted with the set and get method

class Accesorio():#"Accesorio" class is created
    def __init__(self):
        self.IDAccesorios=0
        self.nombreAccesorios=""
    def setAccesorios(self, x):
        self.IDAccesorio=x
        self.nombreAccesorios=Accesorios[x]
    def getIDAccesorio(self):
        return self.IDAccesorio
    def getnombreAccesorios(self):
        return self.nombreAccesorios
#attributes are granted with the set and get method

class Ropas():#"Ropas" class is created
    def __init__(self):
        self.IDRopa=0
        self.nombreRopa=""
    def setRopa(self, x):
        self.IDRopa=x
        self.nombreRopa=Ropa[x]
    def getIDRopa(self):
        return self.IDRopa
    def getnombreRopa(self):
        return self.nombreRopa
#attributes are granted with the set and get method

class Calzados ():#"Calzados" class is created
    def __init__(self):
        self.IDCalzado=0
        self.nombeCalzado=""
    def setCalzado(self, x):
        self.IDCalzado=0
        self.nombeCalzado= Calzado[x]
    def getIDCalzado(self):
        return self.IDCalzado
    def getnombeCalzado(self):
        return self.nombeCalzado
#attributes are granted with the set and get method

class Vestuario():#"Vestuario" class is created
    def __init__(self):
        self.IDVestuario=0
        self.Accesorio=[]
        self.Ropa=[]
        self.Calzado=[]
    def setVestuario(self, XXX, YYY, ZZZ):
        self.IDVestuario=0
        self.Accesorio=XXX
        self.Ropa=YYY
        self.Calzado=ZZZ
    def getAccesorio(self):
        return   self.Accesorio
    def getRopa(self):
        return   self.Ropa
    def getCalzado(self):
        return   self.Calzado
#attributes are granted with the set and get method

class PersonaPOO():#"PersonaPoo" class is created
    def __init__(self):
        self.Cedula=0
        self.Edad=0
        self.Vestuario=[]
        self.Ojos=[]
        self.Cabello=[]
        self.ColordePiel=[]
        self.Genero=[]
        self.FormadecaraEmocion=[]
        self.Provincia=[]
        self.Vestuario=[]
    def setPersonaPOO(self,ced,ed,obj1,obj2,obj3,obj4,obj5,obj6,obj7,obj8): #"setPersonaPOO" function is created
        self.Cedula=ced
        self.Edad=ed
        self.Emocion=obj1
        self.Ojos=obj2
        self.Cabello=obj3
        self.ColordePiel=obj4
        self.Genero=obj5
        self.Formadecara=obj6
        self.Provincia=obj7
        self.Vestuario=obj8
    def getCedula(self):#"getCedula" function is created
        return   self.Cedula
    def getEdad(self):#"getEdad" function is created
        return self.Edad
    def getEmocion(self):#"getEmocion" function is created
        return self.Emocion
    def getOjos(self):#"getojos" function is created
        return self.Ojos
    def getCabello(self):#"getCabello" function is created
        return self.Cabello
    def getColordePiel(self):#"getColordePiel" function is created
        return self.ColordePiel
    def getGenero(self):#"getGenero" function is created
        return self.Genero
    def getFormadecara(self):#"getFormadecara" function is created
        return self.Formadecara
    def getProvincia(self):#"getProvincia" function is created
        return self.Provincia
    def getVestuario(self):#"getVestuario" function is created
        return self.Vestuario
#The "PersonaPoo" class is used to create functions that contain parameters and methods to create objects

DatosPOO=[{"PersonasPOO":[],"cedula":[], "FormaDeRostro":[], "Piel":[], "Emociones":[], "Genero":[], "Grupo":[], "Accesorios":[], "Cabello":[], "Ojos":[], "Provincia":[], "Vestuario":[]}] 
#The DatosPoo list is created, which has a dictionary, where the data will be stored

def CreaDatosPOO():#"CreaDatosPOO" function is created
    for ced in Datos[0]["cedula"]:#with a for loop, the adress Datos[0]["cedula"] is traversed
        C=Datos[0]["cedula"].index(ced)
     #with an .index the data of the "cedula" is accessed

        listaOjos=[]
        FO=FormaOjos()
        FO.setformaOjos(Datos[0]["Ojos"][C][0])
        listaOjos.append(FO)

        CO=ColorOjos()
        CO.setColorOjos(Datos[0]["Ojos"][C][1])
        listaOjos.append(CO)

        Ojs=Ojos()
        Ojs.setOjos(listaOjos[0], listaOjos[1])
        DatosPOO[0]["Ojos"].append(Ojs)

        Emo=Emocion()
        Emo.setEmocion(Datos[0]["Emociones"][C])
        DatosPOO[0]["Emociones"].append(Emo)

        Gen=Genero()
        Gen.setGenero(Datos[0]["Genero"][C])
        DatosPOO[0]["Genero"].append(Gen)

        Prov=Provincias()
        Prov.setProvincia(Datos[0]["Provincia"][C])
        DatosPOO[0]["Provincia"].append(Prov)

        listaCabello=[]

        ColCab=ColorDePelo()
        ColCab.setColorDePelo(Datos[0]["Cabello"][C][0])
        listaCabello.append(ColCab)

        DensCab=DensidadCabello()
        DensCab.setDensidadCabello(Datos[0]["Cabello"][C][1])
        listaCabello.append(DensCab)


        TexCab=TexturaCabello()
        TexCab.setTexturaCabello(Datos[0]["Cabello"][C][2])
        listaCabello.append(TexCab)

        Cabello=Pelo()
        Cabello.setPelo(listaCabello[0], listaCabello[1], listaCabello[2])

        DatosPOO[0]["Cabello"].append(Cabello)

        FDC=Formadecara()
        FDC.setFormadecara(Datos[0]["FormaDeRostro"][C])
        DatosPOO[0]["FormaDeRostro"][C].append(FDC)
    
        ColP=ColorDePiel()
        ColP.setColorDePiel(Datos[0]["Piel"][C])
        DatosPOO[0]["Piel"][C].append(ColP)

        CDP=ColorDePiel()
        CDP.setColorDePiel(Datos[0]["Piel"][C])
        DatosPOO[0]["Piel"][C].append(CDP)


        listaVestuario=[]

        Acce=Accesorio()
        Acce.setAccesorios(Datos[0]["Accesorios"][C])
        listaVestuario.append(Acce)

        Rop=Ropas()
        Rop.setRopa(Datos[0]["Ropa"][C])
        listaVestuario.append(Rop)


        Calz=Calzados ()
        Calz.setCalzado(Datos[0]["Calzado"][C])
        listaVestuario.append(Calz)

        Vestuario=Vestuario()
        Vestuario.setVestuario(listaVestuario[0], listaVestuario[1], listaVestuario[2])

        DatosPOO[0]["Vestuario"].append(Vestuario)
  return
#one by one the characteristics that people will have are created and stored at the list "DatosPOO".

def CreaPersonaPOO():#"CreaPersonaPOO" function is created
    for ced in Datos[0]["cedula"]:
        c=Datos[0]["cedula"].index(ced)#with an .index the data of the "cedula" is accessed
        Pers=PersonaPOO()
        Pers.setPersonaPOO(ced, Datos[0]["Edad"][c], DatosPOO[0]["Emociones"][c], DatosPOO[0]["Ojos"][c], DatosPOO[0]["Cabello"][c], DatosPOO[0]["Piel"][c], DatosPOO[0]["Genero"][c], DatosPOO[0]["FormaDeRostro"][c], DatosPOO[0]["Provincia"][c], DatosPOO[0]["Vestuario"][c])
        #with the pers variable and the set method we convert the data into objects
    return

def ConsultarPersonaPoo():



   


def menu(): #se define la función menu

    Login=Inicio()
     

    print("¿Que desea hacer? ")
    E=int(input("1.Crear persona aleatoriamente 2.Crear persona manualmente 3.Para consultar una persona 4.Para modificar persona 5.Para ver informes 6.para cambiar de login 7.Para terminar:   "))
    if E==1:

        if  Login == "Administrador":
            contador=int(input("Cuantas personas desea Crear:   "))
            CrearPersonaAleatoria(contador)
            CreaDatosPOO()
            CreaPersonaPOO()
        else:
            print("Esta funcion es para administradores")
    elif E==2:
        if  Login=="Administrador":
            CreaPersonajeManualmente()
        else :
            print("Esta funcion es para administradores")
    elif E==3:
        if  Login=="Usuario":
             ConsultarPersona()
        else :
            print("Esta funcion es para Usuarios")
    elif E==4:
        if  Login=="Usuario":
            ModificarPersona()
        else :
            print("Esta funcion es para Usuarios")
    elif E==5:
        if  Login=="Analista":
            informes()
        else :
            print("Esta funcion es para Analistas")
    elif E==6:
        Login=Inicio()
    elif E==7:
        sys.exit()
    else:
        pass


 #se usa un if para crear un menú de opciones que permite ser administrador,analista o usuario y dependiendo de la opción que seleccione tiene diferentes funciones a las que puede acceder.
    return #returna la función menu
    
menu() #regresa al menu
