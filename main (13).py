#Ap 4

def circulo(radio):
    return 3.141592 * radio * radio
    
def cuardrado(lado):
    return  lado * lado 

def rectangulo(base, altura):
    return base * altura/2
    
def trapecio(bmayor, bmenor, altura):
    return (bmayor - bmenor)* altura / 2
    
def menu():
    print ("areas de figuras geometricas")
    print("")
    print("1. circulo")
    print("2. cuadrado")
    print("3. rectangulo")
    print("4. triangulo")
    print("5. trapecio")
    print("elige una opcion")
    
    menu() 
    