total_itens = 0
total_spend = 0

while(True):

    code = int(input("Select the product code: "))
   
    
    if(code == 0):
        print("Saindo...")
        break
    elif(code == 1 or code==2 or code==3 or code==5 or code==9):

        amount = int(input("How much do you want to buy?"))

        total_itens = total_itens + amount

        match code:
            case 1:
                preco = 0.50
                total_spend = total_spend + preco*amount
            case 2:
                preco = 1
                total_spend = total_spend + preco*amount
            case 3:
                preco = 5
                total_spend = total_spend + preco*amount
            case 5:
                preco = 7
                total_spend = total_spend + preco*amount
            case 9:
                preco = 0.50
                total_spend = total_spend + preco*amount
    else:
        print("Code Error")


print(f"Total gasto: R${total_spend:.2f}")
print(f"Total de itens: {total_itens}")

