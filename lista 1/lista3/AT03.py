questao=int(input("digite o número da questao: "))
if questao==8:
    x=1
    soma=0
    num=0
    while x<=10:
        a=int(input("digite um numero: "))
        if a>=0:
            soma=soma+a
            x+=1
            num+=1
        else:
            x+=1
    media=soma/num
    print(media)
#===================================================
if questao==9:
    x=1
    b=int(input("digite um numero: "))
    maior=b
    menor=b
    while x<=9:
        a=int(input("digite um numero: "))
        if a>maior:
            maior=a
            x=x+1
        elif a<menor:
            menor=a
            x=x+1
        else:
            x+=1

    print(f"maior valor digitado: {maior}. E o menor valor digitado foi: {menor}")
#===================================================
if questao==10:
    a=int(input("digite um numero: "))
    b=1
    while b<=a:
        print (b)
        b+=2
#===================================================
if questao==11:
    x=1
    b=0
    soma=0
    while x<=50:
        b+=2
        soma=soma+b
        x+=1
    print(soma)
#===================================================
if questao==12:
    a=int(input("digite um numero: "))
    fatorial=1
    while 1<=a:
        fatorial=fatorial*a
        a-=1
    print(fatorial)
#===================================================
if questao==13:
    a=int(input("digite um numero: "))
    b=a
    while 1<=a:
        if b%a==0:
           print(a)
           a-=1
        else:
            a-=1
#===================================================
if questao==14:
    a=int(input("digite um numero: "))
    b=a
    c=0
    while 1<=a:
        if b%a==0:
           a-=1
           c+=1
        else:
            a-=1
    if c==2:
        print("o número é primo")
    else:
        print('o número não é primo')
#===================================================
if questao==15:
    quantidade=int(input("digite a quantidade de números que serão lidos: "))
    c=1
    primeiro=int(input("digite um numero: "))
    b=primeiro
    while 1<quantidade:
        a=int(input("digite um numero: "))
        if a>b:
            b=a
            quantidade-=1
        elif a==b:
            c+=1
            quantidade-=1
        else:
            quantidade-=1
    if c==1:
        print(f'o maior numero digitado foi {b} e ele foi digitado {c} vez')
    else:
        print(f'o maior numero digitado foi {b} e ele foi digitado {c} vezes')
#===================================================
if questao==16:
    print('ainda n fiz')
#===================================================
if questao==17:
    a=int(input("digite um numero: "))
    x=a
    b=int(input("digite um segundo numero: "))
    soma=0
    multiplicacao=1
    if a%2==0:
        while a<=b:
            soma=soma+a
            a+=2
        print(f'a soma dos numeros impares = {soma}')
        x+=1
        while x<=b:
            multiplicacao=multiplicacao*x
            x+=2
        print(f'a multiplicacao dos numeros impares = {multiplicacao}')
    else:
        a+=1
        while a<=b:
            soma=soma+a
            a+=2
        print(f'a soma dos numeros impares = {soma}')
        while x<=b:
            multiplicacao=multiplicacao*x
            x+=2
        print(f'a multiplicacao dos numeros impares = {multiplicacao}')
#===================================================
if questao==18:
    x=0
    while x==0:
        print('adicao=1\nsubtracao=2\nmultiplicacao=3\ndivisao=4\nsair=5')
        escolha=int(input('escolha uma das opcoes acima: '))
        if escolha == 1:
            print("voce escolheu adicao")
            a=int(input("digite um numero: "))
            b=int(input("digite um segundo numero: "))
            soma=a+b
            print(f"{a}+{b}={soma}")
        if escolha == 2:
            print("voce escolheu subtracao")
            a=int(input("digite um numero: "))
            b=int(input("digite um segundo numero: "))
            subtracao=a-b
            print(f"{a}-{b}={subtracao}")
        if escolha == 3:
            print("voce escolheu multiplicacao")
            a=int(input("digite um numero: "))
            b=int(input("digite um segundo numero: "))
            multiplicacao=a*b
            print(f"{a}*{b}={multiplicacao}")
        if escolha == 4:
            print("voce escolheu divisao")
            a=int(input("digite um numero: "))
            b=int(input("digite um segundo numero: "))
            divisao=a/b
            print(f"{a}/{b}={divisao}")
        if escolha ==5:
            x+=1
    print("sessao finalizada")
#===================================================
if questao==19:
    a=int(input('digite um valor: '))
    b=a
    soma=-a
    while 1<=a:
        if b%a==0:
            soma=soma+a
            a-=1
        else:
            a-=1
    print(f"a soma de todos os divisoresde {b} = {soma}")
#===================================================
if questao==20:
    soma=0
    mil=1000
    while 1<=mil:
        if (mil%3==0 or mil%5==0):
            soma+=mil
            mil-=1
        else:
            mil-=1
    print(soma)
#===================================================
if questao==21:
    num=int(input('digite um numero: '))
    n=1
    soma=1
    while n<=num:
        soma=soma+(1/n)
        n+=1
    print(soma)
#===================================================
if questao==22:
    num=int(input('digite um numero: '))
    n=1
    soma=1
    mult=1
    nume=num
    while n<=num:
        b=nume
        while b>0:
            print(b)
            mult=mult*b
            b-=1
        nume=nume-1
        print(mult)
        soma=soma+(1/mult)
        mult=1
        n+=1
    print(soma)
    #===================================================
if questao==23:
    soma=1
    impar=1
    uni=1
    while uni<=50:
        impar+=2
        uni+=1
        soma+=(impar/uni)
    print(soma)
#===================================================
if questao==25:
    a=int(input("digite um numero: "))
    maior=a
    menor=a
    while a>=0:
        a=int(input("digite um numero: "))
        if a>=0:
            if a>maior:
                maior=a
            elif a<menor:
                menor=a
        else:
            a=-1
    print(f'maior= {maior} e menor: {menor}')
#===================================================
if questao==26:
    saque=int(input("digite o valor do saque em reais: "))
    cem=saque//100
    resto=saque%100
    cinq=resto//50
    resto=resto%50
    print(cem,cinq)