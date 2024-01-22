total_digitado = 0
soma = 0

while True:
    valor_digitado = float(input(f"Digite um numero para somar ou 0 para sair: "))

    if(valor_digitado==0):
        break
    else:
        total_digitado+= 1
        soma = soma + valor_digitado

media = soma/total_digitado
print(f"Total digitado {total_digitado}")
print(f"Soma: {soma}")
print(f"Media artimetica dos valores digitados é: {media:.2f}")