from colorama import Fore , Style, init
from dados import doces, respostas
from time import sleep

valorUsuario = 0
continuar = True
count = 0
init()
def menu_inicial():
    print(Fore.CYAN + '=-'*26 + '\n{:^52}\n'.format('Maquina de Venda') + '=-'*26)
    for d in doces:
        if valorUsuario < d['valor']:
            print(Fore.RED + f'{d["nome"]}\t\t\t\t{"R${:,.2f}".format(float(d["valor"]))}')
        else:
            print(Fore.GREEN + f'{d["nome"]}\t\t\t\t{"R${:,.2f}".format(float(d["valor"]))}')
    print(Fore.YELLOW +'{:^52}'.format('Valor do usuario: {:,.2f}'.format(float(valorUsuario))))
    print(Fore.CYAN + '=-'*26 + '\n{:^52}\n'.format('Comandos') + '=-'*26)
    print(Fore.MAGENTA + '{Inserir} e o tipo de moeda ou nota:\n1 - Moeda de 1 real\n2 - Nota de 2 reais\t3 - Nota de 5 reais')
    print('{Comprar} e o tipo de doce disponivel\n1 - Doce A\t2 - Doce B\t3 - Doce C')
    print('{Sair}' + Style.RESET_ALL)

def tres_pontos():
    for x in range(0,3):
        print(Fore.CYAN + '.' + Style.RESET_ALL)
        sleep(1)

def inserir(resp):
    adicionar = 0
    if '1' in resp:
        adicionar += 1
        print(Fore.GREEN + 'Inserido 1 real em moeda com sucesso!!' + Style.RESET_ALL)
    elif '2' in resp:
        adicionar+=2
        print(Fore.GREEN + 'Inserido 2 reais com sucesso!!' + Style.RESET_ALL)
    elif '3' in resp:
        adicionar+=5
        print(Fore.GREEN + 'Inserido 5 reais com sucesso!!' + Style.RESET_ALL)
    return adicionar

def comprar(valorUsuario, resp):
    if 'a' == resp[-1] or '1' in resp:
        for d in doces:
            if d['nome'] == 'Doce A' and d['valor'] > valorUsuario:
                print(Fore.YELLOW + 'Você não tem valor o suficiente, insira mais', d['valor'] - valorUsuario, 'real/reais' + Style.RESET_ALL)
                return False
            elif d['nome'] == 'Doce A' and d['valor'] <= valorUsuario:
                tres_pontos()
                print(Fore.GREEN + '=-'*26 + '\n{:^52}\n'.format('Sua compra') + '=-'*26)
                print(f'{d["nome"]}\t\t\t\t{"Seu troco: R${:,.2f}".format(float(valorUsuario - d["valor"]))}' + Style.RESET_ALL)
                return True
    elif 'b' == resp[-1] or '2' in resp:
        for d in doces:
            if d['nome'] == 'Doce B' and d['valor'] > valorUsuario:
                print(Fore.YELLOW + 'Você não tem valor o suficiente, insira mais', d['valor'] - valorUsuario, 'real/reais' + Style.RESET_ALL)
                return False
            elif d['nome'] == 'Doce B' and d['valor'] <= valorUsuario:
                tres_pontos()
                print(Fore.GREEN + '=-'*26 + '\n{:^52}\n'.format('Sua compra') + '=-'*26)
                print(f'{d["nome"]}\t\t\t\t{"Seu troco: R${:,.2f}".format(float(valorUsuario - d["valor"]))}' + Style.RESET_ALL)
                return True
    elif 'c' == resp[-1] or '3' in resp:
        for d in doces:
            if d['nome'] == 'Doce C' and d['valor'] > valorUsuario:
                print(Fore.YELLOW + 'Você não tem valor o suficiente, insira mais', d['valor'] - valorUsuario, 'real/reais' + Style.RESET_ALL)
                return False
            elif d['nome'] == 'Doce C' and d['valor'] <= valorUsuario:
                tres_pontos()
                print(Fore.GREEN + '=-'*26 + '\n{:^52}\n'.format('Sua compra') + '=-'*26)
                print(f'{d["nome"]}\t\t\t\t{"Seu troco: R${:,.2f}".format(float(valorUsuario - d["valor"]))}' + Style.RESET_ALL)
                return True

menu_inicial()
while continuar is True:
    resp = input('Digite:').lower().strip()
    count = 0
    for r in respostas:
        if resp in r['resps']:
            if r['nome'] == 'Inserir':
                valorUsuario += inserir(resp)
                tres_pontos()
                menu_inicial()
            elif r['nome'] == 'Sair':
                continuar = False
            elif r['nome'] == 'Comprar':
                if comprar(valorUsuario=valorUsuario, resp=resp):
                    continuar = False
        if resp not in r['resps']:
            count += 1
            if count == 3:
                print(Fore.RED + '...Comando incorreto, digite {Inserir 1,2 ou 3} ou {Comprar 1,2 ou 3}' + Style.RESET_ALL)
                sleep(2)