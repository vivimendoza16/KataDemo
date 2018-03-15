__author__= 'Vivian'

class Calculadora:
    def sumar(self,cadena):
        suma = 0
        if cadena=="":
            return 0
        elif "," in cadena or "&" in cadena or ":" in cadena:
            cadena = cadena.replace("&",",")
            cadena = cadena.replace(":", ",")
            numeros = cadena.split(",")
            print suma
            for num in numeros:
                suma = suma + int(num)
                print suma
            return suma
        else:
            return int(cadena)