import pdfplumber
import pandas as pd

pdf_path = r"C:\Users\Beatriz Pelicano\Desktop\Projetos\relatorio_dados-e-numeros-ca-mama-2023.pdf"

# Função para processar o texto bruto e organizar os dados
def processar_tabela_pagina4(texto):
    linhas = texto.split('\n') # Quebra de texto em linha
    dados = [] # Armazenar os dados extraidos
    iniciar_processamento = False # Ponto de partida para começar a processar após encontrar "Região Norte"
    final_processamento = False # Ponto final para encerrar o processo após encontrar "*Taxas ajustadas"
    
    for linha in linhas:
        # Identifica o início dos dados relevantes
        if "Região Norte" in linha:
            iniciar_processamento = True
        
        # Identifica o final do processo
        if "*Taxas ajustadas" in linha:
            final_processamento = True
        
        if iniciar_processamento and not final_processamento:
            partes = linha.split()
            # Linhas válidas devem ter ao menos 4 partes.
            if len(partes) >= 4:
                regiao = " ".join(partes[:-3])  # Nome da região
                casos = partes[-3]             # Número de casos
                taxa_bruta = partes[-2]        # Taxa bruta
                taxa_ajustada = partes[-1]     # Taxa ajustada
                dados.append([regiao, casos, taxa_bruta, taxa_ajustada])
            else:
                # Ignorar linhas que não se encaixam na estrutura
                continue
    
    return dados

# Função para processar o texto bruto e organizar os dados
def processar_tabela_pagina10(texto):
    linhas = texto.split('\n') # Quebra de texto em linha
    dados = [] # Armazenar os dados extraidos
    iniciar_processamento = False # Ponto de partida para começar a processar após encontrar "Norte"
    final_processamento = False # Ponto final para encerrar o processo após encontrar "Fonte: Ministério"

    for linha in linhas:
        # Identificar o inicio dos dados
        if 'Norte' in linha:
            iniciar_processamento = True
        
        # Identificar o final do processo
        if 'Fonte: Ministério' in linha:
            final_processamento = True
    
        if iniciar_processamento and not final_processamento:
            partes = linha.split()
            # Linhas válidas devem ter ao menos 4 partes
            if len(partes) >= 4:
                regiao = " ".join(partes[:-3]) # Nome da Região
                mamografia = partes[-3]  # Números de mamografia
                rastreamento = partes[-2] # Números de rastreamento
                total = partes[-1] # Total por região
                dados.append([regiao, mamografia, rastreamento, total])
            else:
                # Ignorar linhas que não se encaixam na estrutura
                continue

    return dados

# Função para processar o texto bruto e organizar os dados
def processar_tabela_pagina12(texto):
    linhas = texto.split('\n') # Quebra de texto em linha
    dados = [] # Armazenar dados na lista
    iniciar_processamento = False # Ponto para iniciar o processo após encontrar o "Norte"
    final_processamento = False # Ponto final para encerrar o processo após encontrar o "Fonte: Ministério"

    for linha in linhas:
        # Identificar o inicio dos dados
        if 'Norte' in linha:
            iniciar_processamento = True
        # Encontrar o final do processo
        if 'Fonte: Ministério' in linha:
            final_processamento = True
        
        # Processar apenas as linhas relevantes
        if iniciar_processamento and not final_processamento:
            partes = linha.split() # Dividir a linha em partes com base em espaços
            # Linhas válidas devem ter ao menos 6 partes
            if len(partes) >= 6:
                regiao = " ".join(partes[:-5]) # Nome da Região
                ano_2018 = partes[-5] # Dados de 2018
                ano_2019 = partes[-4] # Dados de 2019
                ano_2020 = partes[-3] # Dados de 2020
                ano_2021 = partes[-2] # Dados de 2021
                ano_2022 = partes[-1] # Dados de 2022
                dados.append([regiao, ano_2018, ano_2019, ano_2020, ano_2021, ano_2022]) # Adicionar os dados extraidos em uma lista
    return dados # Retorna a lista de dados extraidos

# Função para processar o texto bruto e organizar os dados
def processar_tabela_pagina13(texto):
    linhas = texto.split('\n') # Quebra de texto em linha
    dados = [] # Armazenar dados na lista
    iniciar_processamento = False # Ponto para iniciar o processo após encontrar o "Norte"
    final_processamento = False # Ponto final para encerrar o processo após encontrar o "Fonte: Ministério"

    for linha in linhas:
        # Identificar o inicio dos dados
        if 'Norte' in linha:
            iniciar_processamento = True
        # Encontrar o final do processo
        if 'Fonte: Ministério' in linha:
            final_processamento = True
        
        # Processar apenas as linhas relevantes
        if iniciar_processamento and not final_processamento:
            partes = linha.split() # Dividir a linha em partes com base em espaços
            # Linhas válidas devem ter ao menos 6 partes
            if len(partes) >= 6:
                regiao = " ".join(partes[:-5]) # Nome da Região
                anos_35_39 = partes[-5] # Dados faixa etaria
                anos_40_49 = partes[-4]
                anos_50_69 = partes[-3]
                anos_70 = partes[-2]
                total = partes[-1] # totais
                dados.append([regiao, anos_35_39, anos_40_49, anos_50_69, anos_70, total]) # Adicionar os dados extraidos em uma lista
    return dados # Retorna a lista de dados extraidos

# Função para processar o texto bruto e organizar os dados
def processar_tabela_pagina14(texto):
    linhas = texto.split('\n') # Quebra de texto em linha
    dados = [] # Armazenar dados na lista
    iniciar_processamento = False # Ponto para iniciar o processo após encontrar o "Norte"
    final_processamento = False # Ponto final para encerrar o processo após encontrar o "Fonte: Ministério"

    for linha in linhas:
        # Identificar o inicio dos dados
        if 'Norte' in linha:
            iniciar_processamento = True
        # Encontrar o final do processo
        if 'Fonte: Ministério' in linha:
            final_processamento = True
        
        # Processar apenas as linhas relevantes
        if iniciar_processamento and not final_processamento:
            partes = linha.split() # Dividir a linha em partes com base em espaços
            # Linhas válidas devem ter ao menos 6 partes
            if len(partes) >= 6:
                regiao = " ".join(partes[:-5]) # Nome da Região
                ano_2018 = partes[-5] # Dados 2018
                ano_2019 = partes[-4] # Dados 2019
                ano_2020 = partes[-3] # Dados 2020
                ano_2021 = partes[-2] # Dados 2021
                ano_2022 = partes[-1] # Dados 2022
                dados.append([regiao, ano_2018, ano_2019, ano_2020, ano_2021, ano_2022]) # Adicionar os dados extraidos em uma lista
    return dados # Retorna a lista de dados extraidos

# Função para processar o texto bruto e organizar os dados
def processar_tabela_pagina15(texto):
    linhas = texto.split('\n') # Quebra de texto em linha
    dados = [] # Armazenar dados na lista
    iniciar_processamento = False # Ponto para iniciar o processo após encontrar o "Norte"
    final_processamento = False # Ponto final para encerrar o processo após encontrar o "Fonte: Ministério"

    for linha in linhas:
        # Identificar o inicio dos dados
        if 'Norte' in linha:
            iniciar_processamento = True
        # Encontrar o final do processo
        if 'Fonte: Ministério' in linha:
            final_processamento = True
        
        # Processar apenas as linhas relevantes
        if iniciar_processamento and not final_processamento:
            partes = linha.split() # Dividir a linha em partes com base em espaços
            # Linhas válidas devem ter ao menos 8 partes
            if len(partes) >=8:
                regiao = " ".join(partes[:-7]) # Nome da Região
                anos_30 = partes[-7] # Dados das faixas etarias
                anos_30_39 = partes[-6]
                anos_40_49 = partes[-5]
                anos_50_59 = partes[-4]
                anos_60_69 = partes[-3]
                anos_70 = partes[-2]
                total = partes[-1] # total
                dados.append([regiao, anos_30, anos_30_39, anos_40_49, anos_50_59, anos_60_69, anos_70, total]) # Adicionar os dados extraidos em uma lista
    return dados # Retorna a lista de dados extraidos

# Função principal para abrir e extrair as informação das tabelas do PDF
def extrair_tabelas(pdf_path):
    with pdfplumber.open(pdf_path) as pdf: # Abre o PDF
        # Processa a página 4
        page_4 = pdf.pages[4]
        texto_bruto_pagina4 = page_4.extract_text()  # Extrai todo o texto bruto da página

        dados_limpos_pagina4= processar_tabela_pagina4(texto_bruto_pagina4)

        # Processa a página 10
        page_10 = pdf.pages[10]
        texto_bruto_pagina10 = page_10.extract_text()
        
        dados_limpos_pagina10 = processar_tabela_pagina10(texto_bruto_pagina10)

        # Processa a página 12
        page_12 = pdf.pages[12]
        texto_bruto_pagina12 = page_12.extract_text()

        dados_limpos_pagina12 = processar_tabela_pagina12(texto_bruto_pagina12)

        # Processa a página 13
        page_13 = pdf.pages[13]
        texto_bruto_pagina13 = page_13.extract_text()

        dados_limpos_pagina13 = processar_tabela_pagina13(texto_bruto_pagina13)

        # Processa a página 14
        page_14 = pdf.pages[14]
        texto_bruto_pagina14 = page_14.extract_text()

        dados_limpos_pagina14 = processar_tabela_pagina14(texto_bruto_pagina14)

        # Processa a página 15
        page_15 = pdf.pages[15]
        texto_bruto_pagina15 = page_15.extract_text()

        dados_limpos_pagina15 = processar_tabela_pagina15(texto_bruto_pagina15)

        # Criar os DataFrames para cada página 
        df_pagina4 = pd.DataFrame(dados_limpos_pagina4, columns=["Região / Unidade da Federação", "Nº de casos", "Taxa bruta", "Taxa ajustada"])
        df_pagina10 = pd.DataFrame(dados_limpos_pagina10, columns=["Região / Tipo de mamografia", "Mamografia*", "Mamografia de rastreamento", "Total"])
        df_pagina12 = pd.DataFrame(dados_limpos_pagina12, columns=["Região/UF", "2018", "2019", "2020", "2021", "2022"])
        df_pagina13 = pd.DataFrame(dados_limpos_pagina13, columns=["Região/UF", "35 a 39 anos", "40 a 49 anos", "50 a 69 anos", "> 70 anos", "Total"])
        df_pagina14 = pd.DataFrame(dados_limpos_pagina14, columns=["Região/UF", "2018", "2019", "2020", "2021", "2022"])
        df_pagina15 = pd.DataFrame(dados_limpos_pagina15, columns=["Região/UF", "< 30 anos", "30 a 39 anos", "40 a 49 anos", "50 a 59 anos", "60 a 69 anos", "> 70 anos", "Total"])

        # Retorna os DataFrames gerados
        return df_pagina4, df_pagina10, df_pagina12, df_pagina13, df_pagina14, df_pagina15

# Chama a função para processar o PDF e extrair as tabelas
df_pagina4, df_pagina10, df_pagina12, df_pagina13, df_pagina14, df_pagina15 = extrair_tabelas(pdf_path)

# Cria um arquivo e salva os DataFrames extraidos por abas correspondentes.
with pd.ExcelWriter('output_tabelas.xlsx') as writer:
    df_pagina4.to_excel(writer, sheet_name='Pagina 4', index=False)
    df_pagina10.to_excel(writer, sheet_name='Pagina 10', index=False)
    df_pagina12.to_excel(writer, sheet_name='Pagina 12', index=False)
    df_pagina13.to_excel(writer, sheet_name='Pagina 13', index=False)
    df_pagina14.to_excel(writer, sheet_name='Pagina 14', index=False)
    df_pagina15.to_excel(writer, sheet_name="Pagina 15", index=False)

    # Exibe uma mensagem informando que o arquivo foi gerado 
    print('Tabelas salvas')
