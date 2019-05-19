numeros = [-2,-2,-2,0,0,5,5,5,5,5]

class Unidimencional4:
    __numeros_positivos = int(0)
    __numeros_negativos = int(0)
    __ceros = int(0)
    __media1 = float(0)
    __media2 = float(0)

    def Ejer4(self):
        b = int(0)
        c = int(0)
        d = int(0)
        for a in range(0,len(numeros)):
            if numeros[a] > 0:
                b = b + 1
                self.__numeros_positivos = self.__numeros_positivos + numeros[a]
                self.__media1 = self.__numeros_positivos / b
            if numeros[a] < 0:
                c = c + 1
                self.__numeros_negativos = self.__numeros_negativos + numeros[a]
                self.__media2 = self.__numeros_negativos / c
            elif numeros[a] == 0:
                d = d + 1
                self.__ceros = d

    def getmedia1(self):
        return self.__media1

    def getmedia2(self):
        return self.__media2

    def getceros(self):
        return self.__ceros

if __name__ == '__main__':
    main = Unidimencional4()
    main.Ejer4()
    print('media 1: ',main.getmedia1())
    print('media 2: ',main.getmedia2())
    print('ceros: ',main.getceros())
