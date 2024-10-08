import math

class calculadora:

    @staticmethod

    def suma (num1, num2):
        return (num1, num2)
    
    @staticmethod

    def suma (num1, num2):
        return float(num1 + num2)
    
    @staticmethod

    def resta (num1, num2):
        return float(num1 - num2)
    
    @staticmethod

    def multi (num1, num2):
        return float(num1 * num2)
    
    @staticmethod

    def dividir (num1, num2):
        return float(num1 / num2)
    

num1 = float(input("introdueix el primer numero: " ))
num2 = float(input("introdueix el segon numero: " ))

print(calculadora.suma(num1, num2))
print(calculadora.resta(num1, num2))
print(calculadora.multi(num1, num2))
print(calculadora.dividir(num1, num2))