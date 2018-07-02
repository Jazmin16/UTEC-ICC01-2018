lista=[]
def suma(lista):
    a=sum(lista)
    return a
def resta(lista):
    resta = 0
    for i in range (len(lista)):
        resta = resta - lista[i]
    return resta
def promedio(lista):
    p = sum(lista)/len(lista)
    return p


for i in range(3):
    a=int(input())
    lista.append(a)
s = suma(lista)
r = resta(lista)
p = promedio(lista)
ma = mayor(lista)
mu = multiplicacion(lista)
print ("suma: ", s, " resta: ", r, " promedio: ", p, " mayor: ", ma, " multplicacion: ", mu)
input()
