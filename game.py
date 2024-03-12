from models.calcular1 import Calcular


def principal() -> None:
    ponto: int = 0
    jogando(ponto)


def jogando(ponto: int) -> None:
    dificuldade: int = int(input('Informe o nivel de dificuldade [1,2,3 ou 4] : '))
    calc: Calcular = Calcular(dificuldade)

    print('Informe o resuldado da seguinte operação:   ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        ponto += 1
        print(f'Voce tem {ponto} ponto(s)')

    continuar: int = int(input('Voce deseja continuar com o jogo? [ 1- Sim , 0 - Não] : '))

    if continuar:
        jogando(ponto)
    else:
        print(f'Voce terminou o jogo com {ponto} ponto(s)')
        print('Até a proxima meu caro ')


if __name__ == '__main__':
    principal()
