def verificar_palindromo():
    print("="*40)
    print("VERIFICADOR DE PALÍNDROMO")
    print("="*40)
    
    for i in range(1, 4):
        texto = input(f"\nDigite a {i}ª palavra: ").replace(" ", "").lower()
        if texto == texto[::-1]:
            print(f'✓ "{texto}" é um palíndromo!')
        else:
            print(f'✗ "{texto}" NÃO é um palíndromo!')
    
    print("\n" + "="*40)
if __name__ == "__main__":
    verificar_palindromo()