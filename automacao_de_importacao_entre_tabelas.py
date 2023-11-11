# Importando o Pandas para manipular as tebelas
import pandas as pd

tabela_1 = pd.read_excel('nome_da_tabela.xlsx')
tabela_2 = pd.read_excel('nome_da_tabela.xlsx', header=4) # o header serve para eliminar cabeçalhos personalizados das planilhas

# selecionando as 5 primeiras linhas para analisar os tipos de dados
tabela_1_cinco = tabela_1.head(5)
tabela_2_cinco = tabela_2.head(5)
display(tabela_1_cinco)
display(tabela_2_cinco)

# definindo quais são as colunas correspondetes por meio de estrutura de lista
nome_coluna_destino = ["Cliente * (Razão Social, Nome Fantasia, CNPJ ou CPF)", 'Categoria *', 'Conta Corrente *', 'Valor da Conta *', 'Data de Registro *', 'Data de Vencimento *']
nome_coluna_origem = ["Nome do cliente", 'Categoria 1','Conta bancária', 'Valor original da parcela (R$)', 'Data de competência', 'Data de vencimento']

# criando um for para enviar os dados de uma planilha a outra
for i in tabela_1:
    tabela_2[nome_coluna_destino] = tabela_1[nome_coluna_origem]

# definindo o nome do arquivo final
nome_arquivo_saida = "tabela_teste.xlsx"

# transformando o data frame em xlsx novamente
tabela_2.to_excel(nome_arquivo_saida, index=False)

# printando o resultado final como forma de garantia que funcionou
print(f'DataFrame tabela_2 exportado para {nome_arquivo_saida}')