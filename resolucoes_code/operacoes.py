def calcular_operacoes():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    if numero2 != 0:
        divisao = numero1 / numero2
    else:
        divisao = "Divisão por zero!"

    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")

if __name__ == "__main__":
    calcular_operacoes()
