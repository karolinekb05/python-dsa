print('**************** Calculadora em Python *****************')
print('\n')
print('Selecione a opção desejada:')
print('\n')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('\n')

opcao = int(input('Digite a opção (1/2/3/4): '))
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('\n')

def calculadora():
    if opcao == 1:
        soma = n1 + n2
        print('%r + %r = %r' %(n1, n2, soma))
    elif opcao == 2:
        sub = n1 - n2
        print('%r - %r = %r' %(n1, n2, sub))
    elif opcao == 3:
        mult = n1 * n2
        print('%r * %r = %r' %(n1, n2, mult))
    elif opcao == 4:
        div = n1 / n2
        print('%r / %r = %r' %(n1, n2, div))
    else:
        print('Operação inválida! Tente novamente.')

calculadora()