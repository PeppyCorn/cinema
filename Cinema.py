clientes = list()

def linha():
    print('=' * 20)


def leia_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print('Digite um número inteiro válido')


def desconto(total_valor_ingressos):
    novo_valor = total_valor_ingressos - (total_valor_ingressos * 10 / 100)
    print('Desconto aplicado! (10%)')
    return novo_valor


def operacao_cliente():
    nome_cliente = input('\nDigite o nome do cliente: ').strip().title()
    while True:
        try:
            quantidade_ingressos = leia_inteiro('Quantidade de ingressos: ')
            if quantidade_ingressos <= 0:
                print('Digite um número positivo maior que zero!!')
                continue

            if quantidade_ingressos > 5:
                novo_valor_pos_desconto = desconto(quantidade_ingressos * 20)
                print(f'Total a pagar: R${novo_valor_pos_desconto:.2f}')
                clientes.append((nome_cliente, quantidade_ingressos, novo_valor_pos_desconto))
            else:
                print(f'Total a pagar: R${quantidade_ingressos * 20 :.2f}')
                clientes.append((nome_cliente, quantidade_ingressos, quantidade_ingressos * 20))
            break

        except ValueError:
            print('Digite um número inteiro válido!')


def resumo_do_dia():
    linha()
    print('Resumo do dia: ')
    linha()

    total_arrecadado = 0
    total_ingressos_vendidos = 0
    for cliente in clientes:
        if cliente[1] == 1:
            print(f'Cliente: {cliente[0]} comprou {cliente[1]} ingresso') # diferença é sem o 'S'
        else:
            print(f'Cliente: {cliente[0]} comprou {cliente[1]} ingressos')  # cliente[0] = nome_cliente
        total_ingressos_vendidos += cliente[1] # cliente[1] = quantidade_ingressos
        total_arrecadado += cliente[2] # cliente[2] = total_arrecadado

    print(f'\nTotal de ingressos vendidos: {total_ingressos_vendidos}')
    print(f'Total arrecadado: R${total_arrecadado:.2f}')

def main():
    linha()
    print('Bem vindo ao Cinema 🎬')
    linha()

    while True:
        operacao_cliente()

        while True:
            cadastrar_outro_cliente = input('\nDeseja cadastrar outro cliente? [S/N] ').upper().strip()
            if cadastrar_outro_cliente in ['S', 'N']:
                break
            print('Digite apenas S ou N')

        if cadastrar_outro_cliente == 'N':
            break

    resumo_do_dia()
    print('\nObrigado e até a próxima ^w^')
    linha()


main()
