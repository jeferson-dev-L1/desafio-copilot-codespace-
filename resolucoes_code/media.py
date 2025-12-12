def calcular_media():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    numero3 = float(input("Digite o terceiro número: "))
    numero4 = float(input("Digite o quarto número: "))
    media = (numero1 + numero2 + numero3 + numero4) / 4
    return media
if __name__ == "__main__":
    resultado_media = calcular_media()
    print("A média dos números é:", resultado_media)
# media.py