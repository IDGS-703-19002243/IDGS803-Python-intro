import os

class operasbas:
    # declaración de las propiedades

    # declaración de constructor
        #def _init_(self):
        #pass
    # declaración de métodos

    def suma(self, num1, num2):
        res = num1 + num2
        return res

    def resta(self, num1, num2):
        res = num1 - num2
        return res

    def multi(self, num1, num2):
        res = num1 * num2
        return res

    def div(self, num1, num2):
        res = num1 / num2
        return res
def main():
    obj = operasbas()
    opt = -1
    res = 0
    while (opt != 0):
        opt = int(
            input('1.- Suma\n2.- Resta\n3.- Multiplicación\n4.- División\n0.- Salir'))
        if (opt == 0):
            break
        os.system('clear')
        num1 = int(input('Ingresa el primer número:'))
        num2 = int(input('Ingresa el segundo número:'))
        if (opt == 1):
            res = obj.suma(num1, num2)
        elif (opt == 2):
            res = obj.resta(num1, num2)
        elif (opt == 3):
            res = obj.multi(num1, num2)
        elif (opt == 4):
            res = obj.div(num1, num2)
        print('El resultado es: {}'.format(res))
        
#if _name_ == "_main_":
#   main()