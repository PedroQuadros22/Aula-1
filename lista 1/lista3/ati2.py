x=1
while x==1:
    print('MENU:')
    print('1-Converter um número decimal para binário')
    print('2-Converter um número binário para decimal')
    print('28092023-Encerrar')
    opcao=int(input('qual das opcões acima vc deseja realizar? '))
    if opcao==1:
        decimal=int(input('Digite um número decimal: '))
        d=decimal
        bin=decimal%2
        decimal=decimal//2
        while decimal>=1:
            valor=decimal%2
            decimal=decimal//2
            bin=str(valor)+str(bin)
        print(f'O valor decimal {d} representa o valor binário {bin}')
    if opcao==2:
        binario=int(input('Digite um número binário: '))
        b=binario
        valor=0
        x=binario
        y=0
        z=0
        bin=0
        while x>9:
            x=x//10
            y+=1
            print(y)
        z=y
        while binario>0:
            if binario%10==0:
                bin=0
                binario=binario//10
                z-=1
            if binario%10==1:
                bin=1
                exp=bin*(2**(y-z))
                binario=binario//10
                z-=1
                valor=valor+exp
        print(f'O numero binario {b} representa o valor decimal: {valor}')
    if opcao==28092023:
        print('sessão encerrada')
        x+=1
    else:
        print('ERRO!')
        print("escolha uma das opcões disponiveis abaixo:")
        

        