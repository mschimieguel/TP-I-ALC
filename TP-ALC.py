import numpy as np
e  = 2.718281828459045235360287
π  = 3.141592653589793238462643
pi = π

function = "Fx = " + input("Digite a funcao:\n")

n = int(input ("Digite o numero de pontos:\n"))
a = float(input ("Digite os limites de integraçao:\n"))
b = float(input())

Jn = np.zeros((n,n))

for i in range (1,n):
	Jn[i,i-1] = np.sqrt( (i**2)/(4*(i**2)-1) )
	Jn[i-1,i] = np.sqrt( (i**2)/(4*(i**2)-1) )

EigenValues,EigenVectors = np.linalg.eig(Jn)

W = 2*(EigenVectors[0]**2)
X = ((b-a)/2)*(EigenValues + 1) + a

exec(function)
print (((b-a)/2)*(W @ Fx))