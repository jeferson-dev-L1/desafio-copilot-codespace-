# concatenar.py

# Função para receber dois dados do usuário e concatená-los
def concatenar_dados():
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    resultado = dado1 + " " + dado2
    return resultado

if __name__ == "__main__":
    resultado_final = concatenar_dados()
    print("Resultado da concatenação:", resultado_final)