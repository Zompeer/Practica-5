class Memoria:
    def __init__(self, *valores):
        self.__memoria = list()
        self.__archivos = list()
        for valor in valores:
            self.__memoria.append(valor)
            self.__archivos.append(list())
    def modificaMemoria(self, cual, cantidad):
        if cantidad >=0:
            self.__memoria[cual] += cantidad
            return True
        if self.__memoria[cual] >= abs(cantidad):
            self.__memoria[cual] += cantidad
            return True
        return False
    def guardar(self, donde, archivo):
        self.__archivos[donde].append(archivo)
    def tam(self):
        return len(self.__memoria)
    def mostrarMemoria(self):
        print("------------------------")
        print("Memoria")
        for i in range(len(self.__memoria)):
            print("Espacio "+str(i)+": "+str(self.__memoria[i])+ " kb")
            for archivo in self.__archivos[i]:
                print("\t"+archivo[0]+"   "+str(archivo[1])+" kb")
        if len(self.__memoria) == 0:
            print("Vacia")
        print("------------------------")
    def memoria(self, donde):
        return self.__memoria[donde]