def leer_archivo(nombre_archivo):
    archivo = []
    with open(nombre_archivo, "r") as file:
        for line in file:
            archivo.append(line.strip())
    return archivo

def escribir_archivo(nombre_archivo,lista):
    archivo=open(nombre_archivo,"w")
    archivo.write(str(lista))
    archivo.close()

class Elemento:
    def __init__(self, var1, var2):
        self.nombre=var1
        self.peso=var2
    def __str__(self):
        return self.nombre + " pesa " + str(self.peso)
    
    def __repr__(self):
        return self.nombre

class Maleta:
    def __init__(self,var1,var2):
        self.propietario=var1
        self.color=var2
        self.elementos=[]

    def agregar_elementos(self,var1):
        self.nuevo_elemento=var1
        self.elementos.append(self.nuevo_elemento)
    
    def quitar_elemento(self):
        mayor=0
        pos=0
        for i in range(len(self.elementos)):
            if self.elementos[i].peso>mayor:
                mayor=self.elementos[i].peso
                pos=i
        self.elementos.pop(pos)
    
    def calcular_peso(self):
        total=0
        for x in self.elementos:
            total=float(x.peso)+total
        return total

    def __str__(self):
        return "Maleta de " + self.propietario + " es de color " + self.color

class Pasajero:
    def __init__(self,var1,var2,var3,var4):
        self.nombre=var1
        self.edad=var2
        self.origen=var3
        self.destino=var4
        self.maletas=[]
        self.recepcionado=False
    
    def agregar_maleta(self,var1):
        self.nueva_maleta=var1
        self.maletas.append(self.nueva_maleta)

    def __str__(self):
        return self.nombre + " va desde " + self.origen + " a " + self.destino + " y lleva"

class Aeropuerto:
    def __init__(self,var1,var2,var3):
        self.nombre=var1
        self.peso_max=var2
        self.destinos=var3
        self.lista_pasajeros=[]
    
    def recepcionar_maleta(self,var1):
        global contenido_final
        self.maleta=var1
        while self.maleta.calcular_peso()>float(self.peso_max):
            self.maleta.quitar_elemento()
            contenido_final += "El peso ha sido excedido" + "\n"
        contenido_final += "Se ha ingresado la maleta de peso " + str(self.maleta.calcular_peso()) + "\n"
        return self.maleta
    
    def recepcionar_pasajero(self,var1):
        global contenido_final
        self.pasajero=var1
        if self.pasajero.origen == self.nombre:
            if self.pasajero.destino in self.destinos:
                self.lista_pasajeros.append(self.pasajero)
                self.pasajero.recepcionado=True
                return self.pasajero.nombre + " hizo check-in en el aeropuerto " + self.nombre
            else:
                return self.pasajero.nombre + " no pudo hacer check-in"
        else:
            return self.pasajero.nombre + " no pudo hacer check-in"

contenido_final = ""

data = leer_archivo("aeropuertos.txt")
linea = 0
dimensiones_aeropuerto= data[linea].split(",")
linea+=1
info_aeropuertos=data[linea].split(";")
linea+=1
lista_aeropuertos=[]
for x in info_aeropuertos:
    x=x.split(",")
    destinos=[]
    for i in range(len(x)-2):
        destinos=destinos+[x[i+2]]
    aeropuerto=Aeropuerto(x[0],float(x[1]),destinos)
    lista_aeropuertos=lista_aeropuertos+[aeropuerto]
info_pasajeros=data[linea].split(";")
linea+=1
lista_pasajeros=[]
for x in info_pasajeros:
    x=x.split(",")
    pasajero=Pasajero(x[0],int(x[1]),x[2],x[3])
    lista_pasajeros=lista_pasajeros+[pasajero]
cantidad_maletas=int(data[linea])
linea+=1
lista_maletas=[]
for x in range(cantidad_maletas):
    info_maleta=data[linea].split(",")
    linea+=1
    maleta=Maleta(info_maleta[0],info_maleta[1])
    info_elementos=data[linea].split(";")
    linea+=1
    lista_elementos=[]
    for x in info_elementos:
        x=x.split(",")
        lista_elementos=lista_elementos+[x]
    for x in lista_elementos:
        objetos=Elemento(x[0],float(x[1]))
        maleta.agregar_elementos(objetos)
    lista_maletas=lista_maletas+[maleta]
for i in range(len(lista_aeropuertos)):
    for j in range(len(lista_pasajeros)):
        if(lista_pasajeros[j].origen==lista_aeropuertos[i].nombre):
            contenido_final += lista_aeropuertos[i].recepcionar_pasajero(lista_pasajeros[j]) + "\n"
            if lista_pasajeros[j].recepcionado==True:
                for x in lista_maletas:
                    if x.propietario==lista_pasajeros[j].nombre:
                        lista_aeropuertos[i].recepcionar_maleta(x)
                        contenido_final += str(x.elementos) + "\n"
                        
escribir_archivo("output.txt",contenido_final)
