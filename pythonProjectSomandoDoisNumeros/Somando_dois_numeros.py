# Função para somar dois números
def soma(n1, n2):
    return n1 + n2

# Solicita os números do usuário
try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
except ValueError:
    print("Por favor, insira números válidos.")
else:
    # Calcula a soma e imprime o resultado
    resultado = soma(numero1, numero2)
    print(f"A soma de {numero1} e {numero2} é {resultado}")

