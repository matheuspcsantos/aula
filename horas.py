valor_hora = float(input("Digite o valor hora: ")) 
horas_trabalhadas = float (input("Digite as horas trabalhadas")) 

if "horas_trabalhadas" > 40:
    horas_extras = "horas_trabalhadas" - 40
    salario_base = 40 * "valor_hora"
    adicional = horas_extras * "valor_hora" * 1.5
    salario_total = salario_base + adicional
else:
    salario_total = "horas_trabalhadas * valor_hora" 

print("O salario total é R$", salario_total)
