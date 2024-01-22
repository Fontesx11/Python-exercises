valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50 
apagar = valor

while True:
    if atual <= apagar:
        apagar-=atual
        cedulas+=1
     
    else:

        print(f"{cedulas} cedulas de R${atual}")
       
        if apagar == 0:
            break
     

        match atual:
            
            case 50:
                
                atual = 20
            case 20:
                
                atual = 10
            case 10:
               
                atual = 5
            case 5:
               
                atual = 1
            
        cedulas = 0
