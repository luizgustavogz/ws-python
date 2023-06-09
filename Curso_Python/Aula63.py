import re
import sys

# cpf_digitado = '746.824.890-70'.replace('.', '').replace('-', '').replace(' ', '')
# cpf_digitado = input('Digite seu CPF (apenas números): ').replace('.', '') \
    # .replace('-', '').replace(' ', '')
cpf_digitado = re.sub(r'[^0-9]', '', input('Digite seu CPF (apenas números): '))

entrada_sequencial = cpf_digitado == cpf_digitado[0] * len(cpf_digitado)

if entrada_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

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
