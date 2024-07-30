from sklearn.metrics import mean_absolute_error
from math import e,factorial,sqrt,sin
from numpy import pi
from scipy.stats import linregress


# Função que define o pesos de ambas metologias, PMA e Choquet
def height(window,type):
  sum = 0
  sum_e = 0
  sum_h = 0
  vector = []

  for i in range(1,window+1):
    sum += i
    sum_e += e**i
    sum_h += 1/i

  if type == "PMA":
    for i in range(1,window+1):
      poisson = ((((window)**i)*(e**-(window)))/factorial(i))
      vector.append(poisson*2)

    return vector

#Função PMA
def PMA(v,window):
  peso = height(window,'PMA')
  soma = 0
  for i in range(len(v)):
    soma += v[i]*peso[i]

  return soma

# Função de ordenação de Choquet
def ordem_choquet(v,type):
  janela = []
  peso_1 = []

  if type == "PMA":
    peso = height(len(v),"PMA")

  for i in range(len(v)):
    janela.append(v[i])

  janela.sort()

  for i in range(len(v)):
    for j in range(len(v)):
      if v[j] == janela[i]:
        peso_1.append(peso[j])

  return janela,peso_1


# Função de choquet
def choquet(v,type,style):
  vetor,peso = ordem_choquet(v,type)
  soma = 0
  x_norm = []
  s_norm = sum(v)

  for i in range(len(v)):
    x_norm.append(vetor[i]/s_norm)


  if style == 0: # Algebraic Product
    for i in range(len(v)):
      if i == 0:
        soma += (x_norm[i] - 0)*sum(peso)

      else:
        soma += (abs(x_norm[i] - x_norm[i-1]))*sum(peso)

      peso.pop(0)

  return soma*s_norm

# Função que verifica sinais de atenção. Onde 1.65 equivale a 65%
def verificar_atencao(valor_atual, valor_predito):
    atencao = 0
    erro = 1.65

    if valor_predito > erro * valor_atual:
        atencao = 1

    elif valor_atual > erro * valor_predito:
        atencao = 1

    return atencao