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
        if a>=maior:
            maior=a
            print(maior)
            x=x+1
        elif a<menor:
            menor=a
            print(menor)
            x=x+1

        print(x)
    print("maior valor digitado:",maior,
          "menor valor digitado:",menor)
#===================================================

    
