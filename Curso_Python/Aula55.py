"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

num1 = decimal.Decimal('0.1')
num2 = decimal.Decimal('0.7')
num3 = num1 + num2
print(num3)
print(f'{num3:.2f}')
print(round(num3, 3))