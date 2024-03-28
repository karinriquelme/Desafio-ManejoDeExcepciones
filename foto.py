from error import DimensionError
import os


class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        try:
            if ancho < 1 or ancho > self.MAX:
                raise DimensionError("El ancho",ancho,self.MAX)
            self.__ancho = ancho
        except DimensionError as e:
            print(e)

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        try:
            if alto<1 or alto > self.MAX:
                raise DimensionError("El alto",alto,self.MAX)
            self.__alto = alto
        except DimensionError as e:
            print(e)
            

foto1=Foto(0,3000,"mifoto.jpg")



try:
    os.system('cls') if os.name == 'nt' else os.system('clear')
    print("ingrese el tamaño de sus fotos:\n\n")
    foto1.ancho=int(input("ingrese el ancho de su foto: ")) 
    foto1.alto=int(input("ingrese el alto de su foto: "))
except:
    print()
    
finally:
    print (f"el tamaño de su foto es: {foto1.ancho} X {foto1.alto}")