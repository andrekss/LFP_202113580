from cargarArchivo import *
from graphviz import *

carga = Cargar("","",0,"")

Peliculas = [] # arreglo contendrá todas las peliculas

print("\nLenguajes Formales y de Programación")
print("Andrés Alejandro Agosto Méndez 202113580 sección B+")
print("------------------Menú principal-------------------")

Entrada = int(input("pulse 1 para ir al menú principal: "))

if Entrada == 1:
   aviso = False
   while aviso == False:
    aviso = False
    a=1
    print("\nMenú principal")
    print("1) Cargar archivo de entrada")
    print("2) Gestionar películas")
    print("3) Filtrado")
    print("4) Gráfica")
    print("5) Salir")
    
    Entrada1 = int(input("ingrese una opción: "))
        
    
    if Entrada1==1:
        carga.LeerArchivo(Peliculas)
        
        print("\nCargado Exitósamente")        
    elif Entrada1 == 2:
       aa= True
       while aa==True: 
        a=1
        print("\n1) Mostrar películas")
        print("2) Mostrar actores")
        print("3) regresar")
        Entrada2= int(input("ingrese una opción: "))

        if Entrada2 == 1:
         print("\nInformación sobre las películas:")
         for i in Peliculas:
           i.imprimirDatos()
        elif Entrada2 == 2:
          for i in Peliculas:  #impresión del menú
           print(str(a)+")",end=" ")
           i.imprimirPeliculas(False)
           a+=1
          print("presione 0 para regresar")

          entrada3= int(input("ingrese una opción: "))
          if entrada3 == 0:
            pass
          else:
           print ("Actores de la película ",end="")
           Peliculas[entrada3-1].imprimirPeliculas(True)

           Peliculas[entrada3-1].imprimirActores()
        elif Entrada2 == 3:
          aa = False 
    elif Entrada1 == 3:
     h= True
     while h == True:
      print("\n1) Filtrado por actor")
      print("2) Filtrado por año")
      print("3) Filtrado por género")
      print("4) regresar")

      Entrada4= int(input("ingrese la opción: "))
      if Entrada4 == 1:
         carga.imprimirActores1(Peliculas,True)
         entrada5 = int(input("elija un actor: "))
         carga.imprimirLica(Peliculas,entrada5-1)

      elif Entrada4 == 2:
          carga.imprimirAños(Peliculas)
          entrada6 = int(input("elija un año: "))
          carga.printNombreYGenero(Peliculas,entrada6-1)
      elif Entrada4 == 3:
         carga.imprimirGeneros(Peliculas) 
         entrada7 = int(input("elija un género: "))
         carga.printLicasXgenero(Peliculas,entrada7-1)
      elif Entrada4 == 4:
        h= False   
    elif Entrada1 == 4:
       
     dot = Digraph(comment='Tablas guías', format='pdf') # diagraph es toda la plantilla donde irán los nodos
     dot.attr('node', shape='plaintext')  #establece la forma de los nodos como texto plano
     
     for i in range(len(Peliculas)):
      dot.node(f'tabla{i}', 
f'''<<table border="1" cellborder="1" cellspacing="0">
       <tr><td colspan ="2" bgcolor="red">{Peliculas[i].nombre}</td></tr>
       <tr><td>{Peliculas[i].año}</td><td>{Peliculas[i].género}</td></tr>     
   </table>>''')
     for i in range(len(carga.menuDefinitivo)):
      dot.node(f'tabla{i+100}',  #inicializar el arreglo menú definitivo y dar un salto de línea
f'''<<table border="1" cellborder="1" cellspacing="0">
       <tr><td colspan ="2" bgcolor="yellow">{carga.menuDefinitivo[i]}</td></tr>    
   </table>>''')
      
     for i in range(len(carga.menuDefinitivo)):
          for j in range(len(Peliculas)):
             for k in range(len(Peliculas[j].actores)):
              if carga.menuDefinitivo[i] == Peliculas[j].actores[k]:
                dot.edge(f'tabla{j}', f'tabla{i+100}', dir="back")  
# Renderizamos todo
     dot.render('tablas', view=True)
    elif Entrada1 == 5:
       print("\nHasta la próxima . . .\n")
       exit()