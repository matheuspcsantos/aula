sim = True 
nao = False 

if sim: 
    print("Entrou no if") 
else: 
    print("Não entrou") 

# ---------------------------------------------------------------
resto = 5%2 
print(resto)
# --------------------------------------------------------------- 
# imprimir: numero Par
# --------------------------------------------------------------- 
numero = int(input("Digite um numero: ")) 
resultado = numero%2

if resultado == 0: 
    print("Numero Par")
else:
    print("Numero Impar") 
# --------------------------------------------------------------- 
# == igual á 
# != diferente de 
# < menor que 
# > maior que 
# <= menor ou igual
# >= maior ou igual 
# --------------------------------------------------------------- 
# a, b, c, d
a = 3 
b = 1.5  
c = 12 
d = 8.10 
# --------------------------------------------------------------- 
if a > b: 
    print("A é maior que B") 
elif a == b: 
    print("O valor de A  é o mesmo que de B")
elif a != c: 
    print("A e C são iguais") 
elif a < b: 
    print ("A é menor que B") 
