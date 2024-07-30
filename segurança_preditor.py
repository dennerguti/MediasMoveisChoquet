# PREDITOR
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from funcoes import *

dataframe = pd.read_csv('compilado.csv')
x = dataframe.iloc[:, 1].tolist()


# Definição de todas variáveis usadas
# Variaveis de execução geral
vetor_janela = []
window = 27
vetor_janela.append(window)
atencao_geral = 0
ataque_geral = 0
incrementos_consecutivos_geral = 0
last = 0
sequencia = 3

# Variaveis de PMA
prediction_PMA = []
vetor_dpma = []
prediction_choquet_PMA0 = []
prediction_PMA_val = 0
pred_choquet_PMA0 = 0
atencao_PMA = 0
ataque_PMA = 0
incrementos_consecutivos_PMA = 0

# Variaveis de Choquet
vetor_pma0 = []
atencao_PrAl = 0
ataque_PrAl = 0
incrementos_consecutivos_PrAl = 0


# Aplicação do sistema de janela deslizantee
sliding_window = [x[i] for i in range(window)]
prediction = [x[i] for i in range(window, len(x))]

for j in range(len(prediction)):
  length = len(sliding_window)
  test_window = [sliding_window[i] for i in range(length - window, length)]
  penultimo = last
  last = test_window[-1]

  # Verificação de ataques da base de dados
  if penultimo != 0 and last != 0:
    atencao_anterior = atencao_geral
    atencao_geral += verificar_atencao(penultimo, last)

    if atencao_geral > atencao_anterior:
      incrementos_consecutivos_geral += 1
    else:
      incrementos_consecutivos_geral = 0

    if incrementos_consecutivos_geral >= sequencia:
      ataque_geral += 1

  # Predição de ataques do modelo PMA
  if prediction_PMA_val != 0:
    atencao_anterior = atencao_PMA
    atencao_PMA += verificar_atencao(last, prediction_PMA_val)

    if atencao_PMA > atencao_anterior:
      incrementos_consecutivos_PMA += 1
    else:
      incrementos_consecutivos_PMA = 0

    if incrementos_consecutivos_PMA >= sequencia:
      ataque_PMA += 1

  # Predição de ataques do modelo Choquet
  if pred_choquet_PMA0 != 0:
    atencao_anterior = atencao_PrAl
    atencao_PrAl += verificar_atencao(last, pred_choquet_PMA0)

    if atencao_PrAl > atencao_anterior:
      incrementos_consecutivos_PrAl += 1
    else:
      incrementos_consecutivos_PrAl = 0

    if incrementos_consecutivos_PrAl >= sequencia:
      ataque_PrAl += 1

  prediction_PMA_val = round(PMA(test_window, window))
  pred_choquet_PMA0 = round(choquet(test_window, 'PMA', 0))

  prediction_PMA.append(prediction_PMA_val)
  prediction_choquet_PMA0.append(pred_choquet_PMA0)

  sliding_window.append(prediction[j])


# Tabela de alarmes
dados = {
    'Atenção Geral': [atencao_geral],
    'Atenção PMA': [atencao_PMA],
    'Atenção TM': [atencao_PrAl]
}

df = pd.DataFrame(dados)
print(df)


# Tabela de ataques
infos = {
    'Ataque Geral': [ataque_geral],
    'Ataque PMA': [ataque_PMA],
    'Ataque TM': [ataque_PrAl],
}

# Criando o DataFrame
data = pd.DataFrame(infos)
print(data)

# Matriz confusão do modelo PMA 
verdadeiros_positivos_geral = ataque_geral
falsos_negativos_geral = atencao_geral - ataque_geral

verdadeiros_positivos_PMA = ataque_PMA
falsos_negativos_PMA = atencao_PMA - ataque_PMA

print("Matriz de Confusão:")
print(f"                  | Predito Ataque | Predito Não Ataque |")
print(f"------------------|----------------|--------------------|")
print(f"Atual Ataque      | {verdadeiros_positivos_geral:<14} | {falsos_negativos_geral:<18} |")
print(f"Atual Não Ataque  | {verdadeiros_positivos_PMA:<14} | {falsos_negativos_PMA:<18} |")
print('\n')

TVP = verdadeiros_positivos_geral / (verdadeiros_positivos_geral + falsos_negativos_geral)
TVN = verdadeiros_positivos_PMA / (verdadeiros_positivos_PMA + falsos_negativos_PMA)

print(f"TVP {TVP:.2f}")
print(f"TVN {TVN:.2f}")


# Matriz confusão do modelo Choquet
verdadeiros_positivos_geral2 = ataque_geral
falsos_negativos_geral2 = atencao_geral - ataque_geral

verdadeiros_positivos_choquet = ataque_PrAl
falsos_negativos_choquet = atencao_PrAl - ataque_PrAl

print("Matriz de Confusão:")
print(f"                  | Predito Ataque | Predito Não Ataque |")
print(f"------------------|----------------|--------------------|")
print(f"Atual Ataque      | {verdadeiros_positivos_geral2:<14} | {falsos_negativos_geral2:<18} |")
print(f"Atual Não Ataque  | {verdadeiros_positivos_choquet:<14} | {falsos_negativos_choquet:<18} |")
print('\n')

TVP = verdadeiros_positivos_geral2 / (verdadeiros_positivos_geral2 + falsos_negativos_geral2)
TVN = verdadeiros_positivos_choquet / (verdadeiros_positivos_choquet + falsos_negativos_choquet)

print(f"TVP {TVP:.2f}")
print(f"TVN {TVN:.2f}")