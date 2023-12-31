#--------------Clase Padre--------------
class ConversorNumerico():
    def _init_(self):
        self.__numero=None

    def setNumero(self,numero:int):
        numero=input(int('Escriba el numero a convertir: '))
        self.__numero=numero

    def getNumero(self):
        return self.__numero
    
#--------------Clase hijo Decimal-------------
class Decimal(ConversorNumerico):
    def _init_(self,numero:int, decbin:int, dechex:int):
        super()._init_(numero)
        self.__decbin=decbin
        self.__dechex=dechex

#--------------Decimal a binario--------------
    def setDecbin(self,decbin:int):
        convercion = []
        while numero > 0:
            residuo = numero%2
            numero = numero//2
            convercion.append(residuo)
        convercion.reverse()
        resultado=str(convercion).replace(",","").replace("[","").replace("]","").replace(" ","")
        print(resultado)
        self.__decbin=decbin

    def getDecbin(self):

        return self.__decbin

    
#--------------Decimal a Hexadecimal--------------
    def setDechex(self,dechex:int):
        convercion = []
        while numero > 0:
            residuo = numero%16
            numero = numero//16
            if residuo == 10:
                residuo = "A"
            elif residuo == 11:
                residuo = "B"
            elif residuo == 12:
                residuo = "C"
            elif residuo == 13:
                residuo = "D"
            elif residuo == 14:
                residuo = "E"
            elif residuo == 15:
                residuo = "F"
            convercion.append(residuo)
        convercion.reverse()
        resultado=str(convercion).replace(",","").replace("[","").replace("]","").replace(" ","")
        print(resultado)
        self.__dechex=dechex

    def getDechex(self):
        return self.__dechex
    
    def resultadoDecbin(self):
        return f'El numero decimal {self.getNumero} es {self.getDecbin} en binario'
    
    def resultadoDechex(self):
        return f'El numero decimal {self.getNumero} es {self.getDechex} en binario'
    
#--------------Clase Hijo Binario--------------
class Binario(ConversorNumerico):
    def _init_(self,numero:int, bindec:int):
        super()._init_(numero)
        self.__bindec=bindec

    def setBindec(self,bindec:int):
        numero=str('numero')
        convercion=[]
        tot=[]
        for i in numero:
            convercion.append(i)
        for j in range(len(convercion)):
                tot.append(int(convercion[j])(2*(len(convercion)-int(j+1))))
        print(sum(tot))
        self.__bindec=bindec

    def getBindec(self):
        return self.__bindec
    
#--------------Clase Hijo Hexadecimal--------------
class Hexadecimal(ConversorNumerico):
    def _init_(self,numero:int, hexadecimal:int):
        super()._init_(numero)
        self.__hexadecimal=hexadecimal

    def setHexadecimal(self,hexadecimal:int):
        numero=str(numero)
        convercion = []
        tot = []
        for i in numero:
            if i == "a":
                i = 10
            elif i == "b":
                i = 11
            elif i == "c":
                i = 12
            elif i == "d":
                i = 13
            elif i == "e":
                i = 14
            elif i == "f":
                i = 15
            convercion.append(i)
        for j in range(len(convercion)):
                tot.append(int(convercion[j])(16*(len(convercion)-int(j+1))))
        print(sum(tot))
        self.__hexadecimal=hexadecimal

    def getHexadecimal(self):
        return self.__hexadecimal

def main():
    while True:
        convertir=ConversorNumerico()
        print('--------------Sistema de conversion numerico--------------\n\
            1.Conversion Decimal a Binario \n\
            2.Conversion Decimal a Hexadecimal \n\
            3.Conversion Binario a Decimal \n\
            4.Conversion Hexadecimal a Decimal\n')
        
        Op=input('¿Que conversion desea realizar?: ')
        if Op=="1":
            decimal=Decimal()
            print(f'El numero decimal {ConversorNumerico.getNumero()} es {Decimal.getDecbin}')

        elif Op== "2":
            decimal=Decimal()
            print(f'El numero decimal {ConversorNumerico.getNumero()} es {Decimal.getDechex}')
                
        elif Op=="3":
            binario=Binario()
            print(f'El numero Binario {ConversorNumerico.getNumero()} es {Binario.getBindec}')
        
        elif Op=="4":
            hexa=Hexadecimal()
            print(f'El numero Hexadecimal {ConversorNumerico.getNumero()} es {Hexadecimal.getHexadecimal}')
            break
        else:
            print('opcion invalida')
            

if __name__=="_main_":
    main()