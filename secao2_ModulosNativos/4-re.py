import re 

text = "Udemy - uma plataforma com muitos curso"
# 1 - Índice inicial e final de palavras
# O r significa uma raw string (string bruta)
match = re.search(r'uma plataforma', text)
print(f"Índice inicial: {match.start()}")
print(f"Índice final: {match.end()}")

# 2 - Buscando o indice que possui o ponto
site = 'https://udemy.com'
match = re.search(r'\.', site)
print(match)

# 3 - Buscando uma Lista de caracteres dentro de uma frase
pattern = "[g-m]"
result = re.findall(pattern, text)
print(result)

# 4 - Verificando o inicio de um string
rule = r'^A'
phrases = ['A casa está suja', 'O dia esta lindo', 'Vamos passear']
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não Corresponde: {f}")    

# 5- Verificando o final de uma string

rule_end = r'!$'
phrase2 = "O dia esta lindo!" 
match = re.search(rule_end, phrase2)
if match:
    print("Sim, corresponde")
else:
    print("Não Corresponde")    
        