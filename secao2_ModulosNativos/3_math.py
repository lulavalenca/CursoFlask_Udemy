import math

# 1 - Acessar o numero PI
print(math.pi)
print(f"{math.pi:.2f}")

# 2 - Acessar o numero de Euler
print(math.e)
print(f"{math.e:.2f}")

# 3 - Arrendondamento mumeros para cima e para baixo
num = 10.4
print(math.ceil(num))
print(math.floor(num))

# 4 - Fatorial de um numero
num2 = int(input("digite um numero:\n"))
print(math.factorial(num2))

# 5 - Potência de Numeros 
print(math.pow(5, 5))

# 6 -  Raiz quadrada de um numero
print(math.sqrt(169))

# 7 - MDC
mdc = math.gcd(20, 100)
print(mdc)

# 8 - Logaritmo
print(math.log(10))