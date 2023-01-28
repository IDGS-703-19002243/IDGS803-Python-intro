
class operasbas():
    #Definir propiedades de clases
    num1 = 0
    num2 = 0
    res = 0
    def __init__(self,a,c):
        self.num1=a
        self.num2=c
    def suma(self):
            self.res=self.num1+self.num2
    def resta(self):
            self.res=self.num1-self.num2
    
    #Definir constructor de clases
    
    #Definimos los metodos de la clase
    def suma(self,a,b):
        self.num1=a
        self.num2=b
        return a+b
    
    obj=operasbas()
    