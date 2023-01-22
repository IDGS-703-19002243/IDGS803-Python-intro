num1=0
num2=0
op=0
menu=0


def pedir():
    num1
    num2
    num1=int(input("Dame el primer numero: "))
    num2=int(input("Dame el segundo numero: "))

def sum(pedir):
    num1+num2
    
def res(pedir):
    num1-num2
    
def mul(pedir):
    num1*num2
    
def div(pedir):
    num1/num2


def menu():
    op=(int(input(("Ingrese la opción el proceso que desea realizar: "))))
if (op == 1):
    sum()
elif (op == 2):
    res()
elif (op == 3):
    mul()
elif (op == 4):
    div()
    
menu()