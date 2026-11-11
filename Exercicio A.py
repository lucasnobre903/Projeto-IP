# Variáveis
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)

def tamanho_caixas_euclides(d, e):
    numero_maior = max(d, e)
    numero_menor = min(d, e)
    resto = numero_maior % numero_menor
    if numero_maior % numero_menor == 0:
        resto_antigo = numero_menor
        return resto_antigo
    return tamanho_caixas_euclides(numero_menor, resto)

def calculo_cateto(producao, expo):
    if expo == 0:
        return 1
    return producao * calculo_cateto(producao, expo-1)

# Programa
valor_duendes = int(input())
producao_duendes = fatorial(valor_duendes)
valor_elfos = int(input())
producao_elfos = fatorial(valor_elfos)
if producao_duendes > producao_elfos:
    print('Os duendes se superaram dessa vez.')
elif producao_elfos > producao_duendes:
    print('É, os elfos tiveram um resultado melhor.')
else:
    print('Ué, houve um empate.')

tamanho_caixas = tamanho_caixas_euclides(producao_duendes, producao_elfos)
if tamanho_caixas > 10:
    print('Caixas gigantes! O Papai Noel vai precisar de um guindaste para empacotar tudo.')
else:
    print('Caixas compactas e organizadas perfeitamente.')

divisor_estabilidade = (producao_duendes + producao_elfos) // 2 + tamanho_caixas
if divisor_estabilidade > 50:
    print('Atenção: O divisor de estabilidade está altíssimo!')
else:
    print('Divisor calculado com sucesso. A rampa está equilibrada.')

print('Calculando a inclinação geométrica do canhão...')
cateto1_quadrado = calculo_cateto(producao_duendes, 2)
cateto2_quadrado = calculo_cateto(producao_elfos, 2)
hipotenusa_geometrica = cateto1_quadrado + cateto2_quadrado

if hipotenusa_geometrica % divisor_estabilidade != 0:
    print('Lançamento autorizado!')
else:
    print('Lançamento não autorizado!')