# Maria pegou um empréstimo de 1.000.000 para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi 20/12/2020 e o vencimento de
# cada parcela é n odia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o vlaor de cada parcela
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos
valor_parcela = valor_total / 60
nro_parcela = 1

for parcela in range(1, 61):
    data_parcela = data_emprestimo + relativedelta(months=parcela)
    print(
        f'Parcela nº{nro_parcela} ({data_parcela.strftime("%d/%m/%Y")}) = '
        f'R${valor_parcela:,.2f}'
    )
    nro_parcela += 1

print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({nro_parcela-1} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)
