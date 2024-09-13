import json
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Exemplo de JSON com faturamento diário
faturamento = '''
[
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0}, 
    {"dia": 5, "valor": 0.0}, 
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0}
]
'''

dados = json.loads(faturamento)

# Filtra os dias com faturamento
faturamentos_validos = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Calcula menor e maior valor
menor_valor = min(faturamentos_validos)
maior_valor = max(faturamentos_validos)

# Calcula média
media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)

# Dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamentos_validos if valor > media_mensal)

# Imprime os resultados formatados
print(f"Menor valor de faturamento: {locale.currency(menor_valor, grouping=True)}")
print(f"Maior valor de faturamento: {locale.currency(maior_valor, grouping=True)}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
