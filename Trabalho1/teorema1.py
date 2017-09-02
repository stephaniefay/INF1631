import sys
import math
import time

def quociente(x,y,k):
	if k == 1:
		return 1 # para quando q[k-1] = 1
	return x**(k-1) + (y * quociente(x,y,k-1)) # q[k] = x^(k-1)+ y*q[k-1]

print ("\nTeorema 1: pow(x, n) - pow(y, n) eh divisivel por x - y para quaisquer x e y inteiros e todos valores de n inteiros e maiores do que zero.\n")

x = int(input(" x: "))
y = int(input(" y: "))
n = int(input(" n: "))

q = quociente(x, y, n)

print ("q[%d] = %d" % (n,q))

print ("\nVamos repetir varias vezes ate completar 5 segundos. Desta forma podemos observar quantas execucoes houveram por segundo.\n")

t = 5
quantidadePorLoop = 0
inicio = time.time()
temp0 = 1

while(time.time() - inicio < t):
	quantidadePorLoop = quantidadePorLoop + 1
	q = quociente(x, y, n)
	
	temp = time.time()
	if ((round(temp0)) != (round(temp))):
		temp0 = round(temp)
		temp2 = (round(temp)) - (round(inicio))
		if ((6 - temp2) != 6):
			print("Faltam %d segundos..." % (6 - temp2))

fim = time.time()
tempoExecucao = fim - inicio

print ("\nExecucoes: %d\nTempo: %.8f segundos\nExecucoes por segundo: %.8f\n" % (quantidadePorLoop, tempoExecucao, quantidadePorLoop/tempoExecucao))
