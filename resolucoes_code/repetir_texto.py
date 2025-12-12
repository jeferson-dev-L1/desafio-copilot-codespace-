def repetir_texto():
    texto = input("Digite um texto para repetir: ")
    vezes = int(input("Quantas vezes deseja repetir o texto? "))

    # 1) Um do lado do outro
    junto = " ".join([texto] * vezes)

    # 2) Cada um embaixo
    embaixo = "\n".join([texto] * vezes)

    print("\n=== Resultado lado a lado ===")
    print(junto)

    print("\n=== Resultado um embaixo do outro ===")
    print(embaixo)

if __name__ == "__main__":
    repetir_texto()
