import random

# 1 - Seleciona valor aleatorio de uma lista
list1 = [7, 6, 5, 4, 3, 2, 1]
print(random.choice(list1))

# 2 - Gera um numero aleatorio em um intervalo de valores
r1 = random.randint(5, 15)
print(r1)

# 3 - Seleciona caractere aleatorio de uma string
name = "Curso Python"
r2 = random.choice(name)
print(r2)

# 4 - Seleciona mais de um valor aleatório
#random.sample(senquencia, tamanho)
print(random.sample(list1, 2))
print(random.sample(list1, 3))
s = "Olá mundo"
print(random.sample(s, 2))

# 5 - Programa de Sorteio
done = False
while not done:
    print("O que você deseja fazer?")
    print("1. Advinhar o numero")
    print("2. Sair")

    choice = input(">")
    if choice == "1":
        print("========================Advinhe um numero de 1 a 10:======================\n")
        number = int(input("Digite um numero de 1 a 10:\n"))
        result = random.randint(1, 10)
        if number == result:
            print("Parabéns. Você acertou!")
        else:
            print(f"Tente novamente. O numero sorteado foi: {result}")
    elif choice == "2":
        done = True
    else:
        print("Opção Inválida. Escolha a opção 1 ou 2.")            
