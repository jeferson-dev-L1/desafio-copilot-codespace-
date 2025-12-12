def verificar_par_ou_impar():
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")    

if __name__ == "__main__":
    verificar_par_ou_impar()    