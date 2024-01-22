valorDivida = float(input("Digite o valor da dívida: "))
taxa = float(input('Taxa de juros mensal(Ex: 3 -> 3%): '))
pagamentoMensal = float(input("Valor de pagamento mensal: "))
mes = 1

if((valorDivida * taxa/100) > pagamentoMensal):
    print("A divida nunca será paga")
else:
    saldo = valorDivida
    juros_pago = 0

    while saldo > pagamentoMensal:
        juros = saldo * (taxa/100)
        juros_pago = juros_pago + juros

        saldo = saldo + juros - pagamentoMensal

        print(f"O saldo da sua divida no mês {mes} é de R${saldo:6.2f}.")

        mes+=1

    print(f"O numero de meses apra pagar é {mes -1}")
    print(f"O total pago foi {valorDivida+juros_pago:6.2f}, sendo o total de juros pago {juros_pago:8.2f}")
    print(f"No último mês, você teria um saldo residual de R${saldo:8.2f} a pagar.")
        
