import pandas as pd
import numpy as np
import datetime
y = datetime.datetime.now()
table = pd.DataFrame()
j=(y.day)
m=(y.month)
a=(y.year)
nome=[]
mori=[]
mdes=[]
vori=[]
vcom=[]
taxa=[]
s5=['Libra','Euro','Dollar','Peso','Real'] #aqui se encontra as siglas das notas
nomes1=['Libra','Euro','Dollare','Peso','Real']
s0 = ['Libras', 'Euros', 'Dollares', 'Pesos', 'Reais']  # aqui se encontra as siglas das notas
nomes = ['Libras', 'Euros', 'Dollares', 'Pesos', 'Reais']
#nomes das notas
notas=[7.38,6.34,5.22,0.056,1.00] #valores das notas
p='S'
while p =='S':
    n=str(input("qual seu nome? "))
    print("\n  conversora de moedas baseada no real brasileiro\n"
          " 0 para LIBRA ESTERLINA  :  £  7,38\n"
          " 1 para EURO             :  €  6,34\n"
          " 2 para DOLLAR AMERICANO : USD 5,22\n"
          " 3 para PESO ARGENTINO   : ARS 0,056\n"
          " 4 para REAL BRASILEIRO  : BRL 1,00\n")
    v1 = int(input("digite a moeda de origem de 0 á 4 : "))
    v2 = int(input("digite a moeda de destino de 0 á 4 : "))
    d = float(input("digite o valor em dinheiro: "))
    n1 = nomes[v1]
    s1 = s0[v2]
    n2 = nomes1[v1]
    s2 = s5[v2]
    t1 = notas[v1]
    t2 = notas[v2]
    t3 = t1 / t2
    tf = t3 * d
    des = tf * 10/100
    desf=float('{:.2f}'.format(des))
    tfc= tf - (tf * 10 / 100)
    tfcd='{:.2f}'.format(tfc)
    nome.append(n)
    mori.append(n2)
    mdes.append(s2)
    vori.append(d)
    vcom.append(tfcd)
    taxa.append(desf)
    def somal(taxa):
        soma=0
        for i in taxa:
            soma= soma +i
        return soma
    soma = somal(taxa)
    print('\n A conversão com desconto de 10% no valor de: {:.2f} {} para {} é de: {:.2f} {}\n'.format(d, n1, nomes[v2], tfc, s1))
    p=input('digite S para fazer outra operação ou N para mostrar a tabela de operações ja ralizadas:\n').upper()
table["nome"] = (nome)
table["m.origem"] = (mori)
table["m.destino"] = (mdes)
table["dia"] = j
table["mês"] = m
table["ano"] = a
table["v.original"] = (vori)
table["v.convertido"] = (vcom)
table["taxa"] = (taxa)
print(table)
print("\nsoma total de taxas cobradas é de: {:.2f}".format(soma))