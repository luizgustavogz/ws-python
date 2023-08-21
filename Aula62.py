"""
Cálculo do segundo dígito do CPF

CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF + o primeiro dígito
multiplicando cada um dos valores por uma contagem regressiva começando de 11

Ex.: 746.824.890-70 (746824890)
    11 10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0  7 <-- Primeiro dígito
    77  40 54 64 14 24 40 36 0 14

Somar todos os resultados:
77 + 40 + 54 + 64 + 14 + 24 + 40 + 36 + 0 + 14 = 363

Multiplicar o resultado anterior por 10:
363 * 10 = 3630

Obter o resto da divisão da conta anterior por 11
3630 % 11 = 3

Se o resultado anterior for maior que 9:
    O primeiro dígito verificador é 0
Contrarío disso:
    O primeiro dígito verificador é o resultado anterior

O segundo dígito do CPF é 0
"""
# cpf = '36440847007' # Esse CPF gera o primeiro dígito como 10 (0)
cpf_digitado = '74682489070'
cpf_digitado = input('Digite seu CPF (apenas números): ')
nove_digitos = cpf_digitado[:-2]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0


cpf_validado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_digitado == cpf_validado:
    print(f'{cpf_digitado} é válido')
else:
    print('CPF inválido')
