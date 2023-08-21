"""
Formatação básica de strings
s - string
d e i - int
f - float
.<número de dígitos>f - float com n dígitos de precisão
x e X - hexadecimal (ABCDEF0123456789)
(Caractere) (> ou < ou ^) (Quantidade) (Tipo - s, d ou f)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal (+ ou -)
Ex.: 0>100,.1f
Conversion flags - !r (repr), !s (str), !a (ascii)
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')