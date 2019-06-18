import numpy as np
e = 2,718281828459045235360287

function = "Fx = "
function += input("Digite a funcao (sendo ** o operador de exponenciacao):\n")
print(function)
n = input ("Digite o numero de pontos:\n")
a = input ("Digite os limites de integraçao:\n")
b = input()
print(n)
n = int(n)
a = int(a)
b = int(b)
Jn = np.zeros((n,n))
for i in range (1,n):
	Jn[i,i-1] = np.sqrt( (i**2)/(4*(i**2)-1) )
	Jn[i-1,i] = np.sqrt( (i**2)/(4*(i**2)-1) )
#print(Jn)
EigenValues,EigenVectors = np.linalg.eig(Jn)
#print(EigenVectors[i].T @ EigenVectors[i])
#Ai = 
#print(EigenValues)
#print(EigenVectors)
W = 2*(EigenVectors[0]**2)
#print(W)
#X = ((b-a)/2)*(np.add(EigenValues,1))

X = ((b-a)/2)*(EigenValues + 1) + a
#print("x ==",X)
exec(function)
#print (Fx)
In = ((b-a)/2)*(W @ Fx) 
print (4*In)