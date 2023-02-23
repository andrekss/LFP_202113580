class Cargar: 
    def __init__(self,nombre, actores, año,género):
        self.nombre = nombre
        self.actores = actores
        self.año= año
        self.género = género

    def LeerArchivo(self, arreglo):
     #ruta = "/Users/gmg/Desktop/usac 2023/practica 1 LFP/prueba.lfp"
     ruta = input("escriba la ruta exacta del archivo: ")
     archivo = open(ruta, 'r') #abrimos el archivo y leemos con r de read
     ListaLineas = archivo.readlines() #leemos linea por linea, y crea un arreglo de lineas del archivo
     for i in ListaLineas: #recorremos las lineas
        contador = 1
        i=i.split(";") # separamos por punto y coma para hacer el arreglo  por linea
        
        for j in i: 
            if contador == 1:
                self.nombre = j
            elif contador == 2:
                j = [x.strip() for x in j.split(",")] # con sprit eliminamos espacios en blanco de las esquinas y se las pasamos a cada elemento de la lista j.split
                self.actores = [x.strip() for x in j] #aqui se lo asignamos a cada variable la lista sin espacios
            elif contador ==3:
                self.año=j
            elif contador ==4:
                self.género= j.strip()
            contador +=1

        Existe = False
        for i in arreglo:
            if i.nombre == self.nombre:  #en la segunda iteración de ListaLineas verifica
                Existe = True  #si algún elemento es igual del arreglo, si lo es entonces no permite agregarlo a la lista principal
                break
                
        if Existe == False:
            lica = Cargar(self.nombre,self.actores,self.año,self.género)    
            arreglo.append(lica) #agregamos al arreglo 
     archivo.close()
        

        


    
    def imprimirDatos(self):
         print("\nNombre: ", self.nombre,"\nActores: ", self.actores, "\nAño: ", self.año, "\nGénero: ", self.género)    

    def imprimirPeliculas(self,a):
        if a == True:
           print(self.nombre+":")
        elif a == False:
            print(self.nombre) 

    def imprimirActores(self):
        print(self.actores)    

    def imprimirActores1(self,arr,aa):
        nuevo = []
        for i in range(len(arr)):
            for j in range(len(arr[i].actores)): 
                 nuevo.append(arr[i].actores[j])
        self.menuDefinitivo = list(set(nuevo))

        if aa == True:
         for k in range(len(self.menuDefinitivo)):
          print(str(k+1)+")"+self.menuDefinitivo[k])         
    
    def imprimirLica(self,arr2,entrada):
        a=1
        for i in range(len(arr2)):
            for j in range(len(arr2[i].actores)):
                if self.menuDefinitivo[entrada] ==arr2[i].actores[j]:
                    if a==1:
                     print("\npeliculas en las que a participó "+arr2[i].actores[j]+":")  
                    print(arr2[i].nombre)
                    a+=1 


    def imprimirAños(self,arr1):
      nuevo1 = []
      for i in range(len(arr1)):
          nuevo1.append(arr1[i].año)
      
      self.menuDefinitivo1 = list(set(nuevo1))

      for j in range(len(self.menuDefinitivo1)):
          print(str(j+1)+")"+str(self.menuDefinitivo1[j]))

    def printNombreYGenero(self,arr3,entrar):
        b=1
        for i in range(len(arr3)):
            if self.menuDefinitivo1[entrar] == arr3[i].año:
               if b==1:
                   print("\nnombre y género de las peliculas del año "+arr3[i].año+":")

               print("\nNombres: "+arr3[i].nombre+"\nGénero: "+arr3[i].género+"\n")  
               b+=1    

    def imprimirGeneros(self,arr4):
        nuevo2 = []
        for i in range(len(arr4)):
            nuevo2.append(arr4[i].género)

        self.menuDefinitivo2 = list(set(nuevo2))

        for n in range(len(self.menuDefinitivo2)):
            print(str(n+1)+")"+str(self.menuDefinitivo2[n]))    
    
    def printLicasXgenero(self,arr5,entra):
        c=1
        for i in range(len(arr5)):
            if self.menuDefinitivo2[entra] == arr5[i].género:
                if c==1:
                    print("\nnombres de las peliculas con el género de "+arr5[i].género+":")
                print("\n"+arr5[i].nombre+"\n")  
                c+=1    