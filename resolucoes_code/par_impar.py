def verificar_par_ou_impar():
    numero_par = int(input("Digite um número para verificar se é PAR: "))
    numero_impar = int(input("Digite um número para verificar se é ÍMPAR: "))

    # Verifica PAR
    if numero_par % 2 == 0:
        print(f"O número {numero_par} é par.")
    else:
        print(f"O número {numero_par} NÃO é par.")

    # Verifica ÍMPAR
    if numero_impar % 2 != 0:
        print(f"O número {numero_impar} é ímpar.")
    else:
        print(f"O número {numero_impar} NÃO é ímpar.")


if __name__ == "__main__":
    verificar_par_ou_impar()
  