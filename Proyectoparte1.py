import random

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

print(Login)

Datos=[{"cedula":[], "Edad":[], "FormaDeRostro":[], "Piel":[], "Emociones":[], "Genero":[], "Grupo":[], "Accesorios":[], "Cabello":[], "Ojos":[], "Provincia":[]}]

def CrearPersonaAleatoria():
    CreaCedula()
    #print(Datos[0]["cedula"])
  
    #CreaEdad()
  #CreaRostro()
  #CreaPiel()
  #CreaEmociones()
  #CreaGenero()
  #CreaGrupo()
  #CreaAccesorios()
  #CreaCabello()
  #CreaOjos()
  #CreaProvincia()
    return


CrearPersonaAleatoria()
def CreaEdad():
    for c in range (1920,2021):
        print(c)
        Años=c

    for i in range (1,13):
        print(i)
        Meses=i
       
    for d in range (1,30):
        print(d)
        Dias=d
    
    EdadPersona=[Años,Meses,Dias]
    Datos[0]["Edad"].append(EdadPersona)

    return CreaEdad







 
