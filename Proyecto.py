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
      print("Esa opcioon no está")
    

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