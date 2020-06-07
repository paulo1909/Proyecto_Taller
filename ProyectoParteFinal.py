import random
import sys

Rostros=["Redondo", "Alargado", "Corazón", "Cuadrado", "Ovalado", "Rectangular"]
Piel=["Negra", "Marrón", "Morena", "Clara", "Blanca"]
Emociones=["Felicidad", "Tristeza", "Seriedad", "Indiferencia", "Enojo", "Temor", "Estrez"]
Generos=["Masculino", "Femenino"]
Accesorios=["lentes", "Aretes", "Percing", "Tatuajes", "Collar", "Ninguno", "Ninguno", "Ninguno", "Ninguno", "Ninguno"]
ColorDelPelo=["negro", "rubio", "café", "castaño", "gris", "invisible"]
Densidad=["Escaso", "Moderado", "Abundante","","","invisible"]
Textura=["lacio", "Ondulado", "Rizado","","","invisible"]
Forma=["almendrados", "separados", "redondos", "caídos", "saltones", "juntos", "profundos", "asiático"]
Color=["negro", "castaño", "ámbar", "avellana", "verde", "azul", "gris"]
Provincia=["","San José", "Alajuela", "Cartago", "Heredia", "Puntarenas", "Guanacaste", "Limón"]
def Inicio():

    N=int(input("Digite el numero correspondiente si desea iniciar sesion como: 1.Administrador 2.Analista 3.Usuario:  "))
    if N == 1 :
      Login="Administrador"
    elif N == 2:
      Login="Analista"
    elif N == 3 :
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

def CreaEdad ():
    c=random.randint(1920,2020)
    Años=c
            
             
    i=random.randint(1,12)
    Meses=i
     
             
    d=random.randint(1,30)
    Dias=d

    EdadPersona= [ Años,Meses,Dias]
    Datos[0]["Edad"].append(EdadPersona) 
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

def GrupoEtario(edad):
    if edad[0]>=2019:
        etario="Bebe"
    elif edad[0]<2019 and edad[0]>=2008:
        etario="Niño"
    elif edad[0]<2008 and edad[0]>=2002:
        etario="Adolecente"
    elif edad[0]<2002:
        etario="Adulto"
    return etario
        


def CreaProvincia():

    Datos[0]["Provincia"].append(random.randint(1, 7))
    return

Datos=[{"cedula":[], "Edad":[], "FormaDeRostro":[], "Piel":[], "Emociones":[], "Genero":[], "Grupo":[], "Accesorios":[], "Cabello":[], "Ojos":[], "Provincia":[]}]

def CrearPersonaAleatoria(Contador):
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
        X=X+1
    menu()
    return


def CreaPersonajeManualmente():


    CreaCedula()
    Fecha=[]
    Fecha.append(int(input("Digite su año de nacimieto:  ")))
    Fecha.append(int(input("Digite su mes de nacimieto:  ")))
    Fecha.append(int(input("Digite su dia de nacimieto:  ")))
    Datos[0]["Edad"].append(Fecha)
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



def ColsuntarPersona():
    for ced in Datos[0]["cedula"]:
        print(ced)
 
    contador=Datos[0]["cedula"].index(int(input("Digite la cedula de la persona que desea consultar")))

    print(ced) 
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


def ModificarPersona():
    for ced in Datos[0]["cedula"]:
        print(ced)

    C=Datos[0]["cedula"].index(int(input("Digite la cedula de la persona que desea cambiar:  ")))
    Datos[0]["Provincia"][C]=int(input("Digite el numero correspondiente a su nueva provincia: 1.San José 2.Alajuela 3.Cartago 4.Heredia 5.Puntarenas 6.Guanacaste 7.Limón:   "))
    Datos[0]["Emociones"][C]=int(input("Digite el numero de la emocion correspondiente: 0.Felicidad 1.Tristeza 2.Seriedad 3.Indiferencia 4.Enojo 5.Temor 6.Estrez"))
    menu()
    return

def ImprimirInformes(Lista):
    for ced in Lista:
       contador=Datos[0]["cedula"].index(ced)
       print(ced) 
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


def informes():
    SanJose=0
    SanJoseBebe=[]
    SanJoseNiño=[]
    SanJoseAdolecente=[]
    SanJoseAdulto=[]
    Alajuela=0
    AlajuelaBebe=[]
    AlajuelaNiño=[]
    AlajuelaAdolecente=[]
    AlajuelaAdulto=[]
    Cartago=0
    CartagoBebe=[]
    CartagoNiño=[]
    CartagoAdolecente=[]
    CartagoAdulto=[]
    Heredia=0
    HerediaBebe=[]
    HerediaNiño=[]
    HerediaAdolecente=[]
    HerediaAdulto=[]
    Limon=0
    LimonBebe=[]
    LimonNiño=[]
    LimonAdolecente=[]
    LimonAdulto=[]
    Guanacaste=0
    GuanacasteBebe=[]
    GuanacasteNiño=[]
    GuanacasteAdolecente=[]
    GuanacasteAdulto=[]
    Puntarenas=0
    PuntarenasBebe=[]
    PuntarenasNiño=[]
    PuntarenasAdolecente=[]
    PuntarenasAdulto=[]
    for persona in Datos[0]["cedula"]:

        if Datos[0]["Provincia"][Datos[0]["cedula"].index(persona)] == 1:
            SanJose=SanJose+1
            if GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Bebe":
               SanJoseBebe.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Niño":
                SanJoseNiño.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adolecente":
                SanJoseAdolecente.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adulto":
                SanJoseAdulto.append(persona)
        elif Datos[0]["Provincia"][Datos[0]["cedula"].index(persona)] == 2:
            Alajuela=Alajuela+1
            if GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Bebe":
                AlajuelaBebe.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Niño":
                AlajuelaNiño.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adolecente":
                AlajuelaAdolecente.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adulto":
                AlajuelaAdulto.append(persona)
        elif Datos[0]["Provincia"][Datos[0]["cedula"].index(persona)] == 3:
            Cartago=Cartago+1
            if GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Bebe":
                CartagoBebe.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Niño":
                CartagoNiño.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adolecente":
                CartagoAdolecente.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adulto":
                CartagoAdulto.append(persona)
        elif Datos[0]["Provincia"][Datos[0]["cedula"].index(persona)] == 4:
            Heredia=Heredia+1
            if GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Bebe":
                HerediaBebe.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Niño":
                HerediaNiño.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adolecente":
                HerediaAdolecente.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adulto":
                HerediaAdulto.append(persona)
        elif Datos[0]["Provincia"][Datos[0]["cedula"].index(persona)] == 5:
            Puntarenas=Puntarenas+1
            if GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Bebe":
                PuntarenasBebe.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Niño":
                PuntarenasNiño.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adolecente":
                PuntarenasAdolecente.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adulto":
                PuntarenasAdulto.append(persona)
        elif Datos[0]["Provincia"][Datos[0]["cedula"].index(persona)] == 6:
            Guanacaste=Guanacaste+1
            if GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Bebe":
                GuanacasteBebe.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Niño":
                GuanacasteNiño.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adolecente":
                GuanacasteAdolecente.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adulto":
                GuanacasteAdulto.append(persona)
        elif Datos[0]["Provincia"][Datos[0]["cedula"].index(persona)] == 7:
            Limon=Limon+1
            if GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Bebe":
                LimonBebe.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Niño":
                LimonNiño.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adolecente":
                LimonAdolecente.append(persona)
            elif GrupoEtario(Datos[0]["Edad"][Datos[0]["cedula"].index(persona)]) == "Adulto":
                LimonAdulto.append(persona)
    

    TotalDeCostaRicenses=len(Datos[0]["cedula"])
    print("Total de bebes en San Jose:  ", len(SanJoseBebe),"Equivale a un:", len(SanJoseBebe)/TotalDeCostaRicenses, "%")
    ImprimirInformes(SanJoseBebe)
    print("Total de niños en San Jose:  ", len(SanJoseNiño),"Equivale a un:",len(SanJoseNiño)/TotalDeCostaRicenses, "%")
    ImprimirInformes(SanJoseNiño)
    print("Total de adolecentes en San Jose:  ", len(SanJoseAdolecente),"Equivale a un:",len(SanJoseAdolecente)/TotalDeCostaRicenses, "%")
    ImprimirInformes(SanJoseAdolecente)
    print("Total de Adultos en San Jose:  ", len(SanJoseAdulto),"Equivale a un:",len(SanJoseAdulto)/TotalDeCostaRicenses, "%")
    ImprimirInformes(SanJoseAdulto)
    print("Total de bebes en Alajuela:  ", len(AlajuelaBebe),"Equivale a un:",len(AlajuelaBebe)/TotalDeCostaRicenses, "%")
    ImprimirInformes(AlajuelaBebe)
    print("Total de niños en Alajuela:  ", len(AlajuelaNiño),"Equivale a un:",len(AlajuelaNiño)/TotalDeCostaRicenses, "%")
    ImprimirInformes(AlajuelaNiño)
    print("Total de adolecentes en Alajuela:  ", len(AlajuelaAdolecente),"Equivale a un:","Equivale a un:",len(AlajuelaAdolecente)/TotalDeCostaRicenses, "%")
    ImprimirInformes(AlajuelaAdolecente)
    print("Total de Adultos en Alajuela:  ", len(AlajuelaAdulto),"Equivale a un:",len(AlajuelaAdulto)/TotalDeCostaRicenses, "%")
    ImprimirInformes(AlajuelaAdulto)    
    print("Total de bebes en Cartago:  ", len(CartagoBebe),"Equivale a un:",len(CartagoBebe)/TotalDeCostaRicenses, "%")
    ImprimirInformes(CartagoBebe)
    print("Total de niños en Cartago:  ", len(CartagoNiño),"Equivale a un:",len(CartagoNiño)/TotalDeCostaRicenses, "%")
    ImprimirInformes(CartagoNiño)
    print("Total de adolecentes en Cartago:  ", len(CartagoAdolecente),"Equivale a un:",len(CartagoAdolecente)/TotalDeCostaRicenses, "%")
    ImprimirInformes(CartagoAdolecente)
    print("Total de Adultos en Cartago:  ", len(CartagoAdulto),"Equivale a un:",len(CartagoAdulto)/TotalDeCostaRicenses, "%")
    ImprimirInformes(CartagoAdulto)
    print("Total de bebes en Heredia:  ", len(HerediaBebe),"Equivale a un:",len(HerediaBebe)/TotalDeCostaRicenses, "%")
    ImprimirInformes(HerediaBebe)
    print("Total de niños en Heredia:  ", len(HerediaNiño),"Equivale a un:",len(HerediaNiño)/TotalDeCostaRicenses, "%")
    ImprimirInformes(HerediaNiño)
    print("Total de adolecentes en Heredia:  ", len(HerediaAdolecente),"Equivale a un:",len(HerediaAdolecente)/TotalDeCostaRicenses, "%")
    ImprimirInformes(HerediaAdolecente)
    print("Total de Adultos en Heredia:  ", len(HerediaAdulto),"Equivale a un:",len(HerediaAdulto)/TotalDeCostaRicenses, "%")
    ImprimirInformes(HerediaAdulto)
    print("Total de bebes en Puntarenas:  ", len(PuntarenasBebe),"Equivale a un:",len(PuntarenasBebe)/TotalDeCostaRicenses, "%")
    ImprimirInformes(PuntarenasBebe)
    print("Total de niños en Puntarenas:  ", len(PuntarenasNiño),"Equivale a un:",len(PuntarenasNiño)/TotalDeCostaRicenses, "%")
    ImprimirInformes(PuntarenasNiño)
    print("Total de adolecentes en Puntarenas:  ", len(PuntarenasAdolecente),"Equivale a un:",len(PuntarenasAdolecente)/TotalDeCostaRicenses, "%")
    ImprimirInformes(PuntarenasAdolecente)
    print("Total de Adultos en Puntarenas:  ", len(PuntarenasAdulto),"Equivale a un:",len(PuntarenasAdulto)/TotalDeCostaRicenses, "%")
    ImprimirInformes(PuntarenasAdulto)
    print("Total de bebes en Puntarenas:  ", len(PuntarenasBebe),"Equivale a un:",len(PuntarenasBebe)/TotalDeCostaRicenses, "%")
    ImprimirInformes(GuanacasteBebe)
    print("Total de niños en Puntarenas:  ", len(GuanacasteNiño),"Equivale a un:",len(GuanacasteNiño)/TotalDeCostaRicenses, "%")
    ImprimirInformes(GuanacasteNiño)
    print("Total de adolecentess en Puntarenas:  ", len(GuanacasteAdolecente),"Equivale a un:",len(GuanacasteAdolecente)/TotalDeCostaRicenses, "%")
    ImprimirInformes(GuanacasteAdolecente)
    print("Total de Adultos en Puntarenas:  ", len(GuanacasteAdulto),"Equivale a un:",len(GuanacasteAdulto)/TotalDeCostaRicenses, "%")
    ImprimirInformes(GuanacasteAdulto)
    print("Total de bebes en Puntarenas:  ", len(LimonBebe),"Equivale a un:",len(LimonBebe)/TotalDeCostaRicenses, "%")
    ImprimirInformes(LimonBebe)
    print("Total de niños en Puntarenas:  ", len(LimonNiño),"Equivale a un:",len(LimonNiño)/TotalDeCostaRicenses, "%")
    ImprimirInformes(LimonNiño)
    print("Total de adolecentes en Puntarenas:  ", len(LimonAdolecente),"Equivale a un:",len(LimonAdolecente)/TotalDeCostaRicenses, "%")
    ImprimirInformes(LimonAdolecente)
    print("Total de Adultos en Puntarenas:  ", len(LimonAdulto),"Equivale a un:",len(LimonAdulto)/TotalDeCostaRicenses, "%")
    ImprimirInformes(LimonAdulto)


    print("Total de personas en San José:  ",SanJose, "%",SanJose/TotalDeCostaRicenses)
    print("Total de personas en Alajuela:  ",Alajuela, "%",Alajuela/TotalDeCostaRicenses)
    print("Total de personas en Cartago:  ",Cartago, "%",Cartago/TotalDeCostaRicenses)
    print("Total de personas en Heredia:  ",Heredia, "%",Heredia/TotalDeCostaRicenses)
    print("Total de personas en Puntarenas:  ",Puntarenas, "%",Puntarenas/TotalDeCostaRicenses)
    print("Total de personas en Guanacaste:  ",SanJose, "%",SanJose/TotalDeCostaRicenses)
    print("Total de personas en Limon:  ", Limon, "%",Limon/TotalDeCostaRicenses)
    Fe=0
    Tri=0
    Ser=0
    Ind=0
    Eno=0
    Tem=0
    Ezt=0
    for Emo in Datos[0]["Emociones" ] :
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
    TotalesBebes=len(SanJoseBebe)+len(AlajuelaBebe)+len(CartagoBebe)+len(HerediaBebe)+len(PuntarenasBebe)+len(GuanacasteBebe)+len(LimonBebe)
    TotalesNiños=len(SanJoseNiño)+len(AlajuelaNiño)+len(CartagoNiño)+len(HerediaNiño)+len(PuntarenasNiño)+len(GuanacasteNiño)+len(LimonNiño)
    TotalesAdolecentes=len(SanJoseAdolecente)+len(AlajuelaAdolecente)+len(CartagoAdolecente)+len(HerediaAdolecente)+len(PuntarenasAdolecente)+len(GuanacasteAdolecente)+len(LimonAdolecente)
    TotalesAdultos=len(SanJoseAdulto)+len(AlajuelaAdulto)+len(CartagoAdulto)+len(HerediaAdulto)+len(PuntarenasAdulto)+len(GuanacasteAdulto)+len(LimonAdulto)
    print("Total de bebes en CR",TotalesBebes, "Porcentaje",TotalesBebes/TotalDeCostaRicenses)
    print("Total de niños en CR",TotalesNiños, "Porcentaje",TotalesNiños/TotalDeCostaRicenses)
    print("Total de adolecentes en CR",TotalesAdolecentes, "Porcentaje",TotalesAdolecentes/TotalDeCostaRicenses)
    print("Total de adultos en CR",TotalesAdultos, "Porcentaje",TotalesAdultos/TotalDeCostaRicenses)


    print("             Felicidad", "Tristeza", "Seriedad", "Indiferencia", "Enojo", "Temor", "Estrez")
    print("Total:      ", Fe,"       ", Tri,"      ", Ser,"      ", Ind,"          ", Eno,"   ", Tem,"   ", Ezt)
    print("Total:      ", Fe/TotalDeCostaRicenses,"     ", Tri/TotalDeCostaRicenses,"    ", Ser/TotalDeCostaRicenses,"    ", Ind/TotalDeCostaRicenses,"       ", Eno/TotalDeCostaRicenses,"  ", Tem/TotalDeCostaRicenses,"   ", Ezt/TotalDeCostaRicenses)
    menu()
    return

def menu():
    Login=Inicio()
    print("¿Que desea hacer? ")
    E=int(input("1.Crear persona aleatoriamente 2.Crear persona manualmente 3.Para consultar una persona 4.Para modificar persona 5.Para ver informes 6.Para terminar:   "))
    if E==1:

        if Login == "Administrador":
            contador=int(input("Cuantas personas desea Crear:   "))
            CrearPersonaAleatoria(contador)
        else:
            print("Esta funcion es para administradores")
    elif E==2:
        if Login=="Administrador":
            CreaPersonajeManualmente()
        else :
            print("Esta funcion es para administradores")
    elif E==3:
        if Login=="Usuario":
            ColsuntarPersona()
        else :
            print("Esta funcion es para Usuarios")
    elif E==4:
        if Login=="Usuario":
            ModificarPersona()
        else :
            print("Esta funcion es para Usuarios")
    elif E==5:
        if Login=="Analista":
            informes()
        else :
            print("Esta funcion es para Analistas")
    elif E==6:
        print("fin")
        sys.exit()

    return
    
menu()
