# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 11:07:17 2022

@author: jujum
"""

# Importação de dados dos arquivos txt
arquivo_dias = open("SN_d_tot_V2.0.txt")
arquivo_media = open("SN_m_tot_V2.0.txt")
linhas_media = arquivo_media.readlines()
lista_media = []
for linha in linhas_media:
    substring_media = linha.split(' ')
    substring_media = list(filter(len, substring_media))
    lista_media.append(substring_media)
dicionario_media = {}
for dado in lista_media:
    dicionario_media[str(dado[0])] = dicionario_media.get(str(dado[0]),dict())
    dicionario_media[str(dado[0])][str(dado[1])] = dicionario_media[str(dado[0])].get(str(dado[1]),[dado[3], dado[4], dado[5]])
linha_dias = arquivo_dias.readlines()  
lista_dia = []
for linha in linha_dias:
    substring_dia = linha.split(' ')
    substring_dia = list(filter(len, substring_dia))
    lista_dia.append(substring_dia)   
dicionario_dia = {}   
for dado in lista_dia:
    dicionario_dia[str(dado[0])] = dicionario_dia.get(str(dado[0]),dict())
    dicionario_dia[str(dado[0])][str(dado[1])] = dicionario_dia[str(dado[0])].get(str(dado[1]),dict())
    dicionario_dia[str(dado[0])][str(dado[1])][str(dado[2])] = dicionario_dia[str(dado[0])][str(dado[1])].get(str(dado[2]), [dado[3], dado[4], dado[5], dado[6]])
#Funções
def funcao_1(ano):
    '''
    Função que contar os dias em que n~ao foram observadas manchas solares em cada mês, para um dado ano.

    Parameters
    ----------
    ano : int. Ano que se deseja contar os dias.
    

    Returns
    -------
    str_saida_dias_sem_mancha : str. Informações de saída.

    '''
    if int(ano) < 1818 or int(ano) > 2018:
        variavel_de_validacao = 0
        while variavel_de_validacao == 0:
            print('\n')
            print('Infelizmente houve um erro.')
            ano = str(input('Favor inserir um ano entre 1818 e 2018: '))
            if int(ano) >= 1818 and int(ano) <= 2018:
                variavel_de_validacao += 1
    soma_janeiro = 0
    soma_fevereiro = 0
    soma_marco = 0
    soma_abril = 0
    soma_maio = 0
    soma_junho = 0
    soma_julho = 0
    soma_agosto = 0
    soma_setembro = 0
    soma_outubro = 0
    soma_novembro = 0
    soma_dezembro = 0
    ano_dicionario = dicionario_dia[ano]
    for mes in ano_dicionario:
        if mes == '1':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '0':
                    soma_janeiro += 1
        if mes == '2':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '0':
                    soma_fevereiro += 1
        if mes == '3':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '0':
                    soma_marco += 1
        if mes == '4':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '0':
                    soma_abril += 1
        if mes == '5':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '0':
                    soma_maio += 1
        if mes == '6':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '0':
                    soma_junho += 1
        if mes == '7':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '0':
                    soma_julho += 1
        if mes == '8':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '0':
                    soma_agosto += 1
        if mes == '9':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '0':
                    soma_setembro += 1
        if mes == '10':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '0':
                    soma_outubro += 1
        if mes == '11':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '0':
                    soma_outubro += 1
        if mes == '12':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '0':
                    soma_dezembro += 1
    str_saida_dias_sem_mancha = f'No mês de Janeiro, de {ano}, houve {soma_janeiro} dias em que não houve observações.\nNo mês de Fevereiro, de {ano}, houve {soma_fevereiro} dias em que não houve observações.\nNo mês de Março, de {ano}, houve {soma_marco} dias em que não houve observações.\nNo mês de Abril, de {ano}, houve {soma_abril} dias em que não houve observações.\nNo mês de Maio, de {ano}, houve {soma_maio} dias em que não houve observações.\nNo mês de Junho, de {ano}, houve {soma_junho} dias em que não houve observações.\nNo mês de Julho, do {ano}, houve {soma_julho} dias em que não houve observações.\nNo mês de Agosto, do {ano}, houve {soma_agosto} dias em que não houve observações.\nNo mês de Setembro, do {ano}, houve {soma_setembro} dias em que não houve observações.\nNo mês de Outubro, do {ano}, houve {soma_outubro} dias em que não houve observações.\nNo mês de Novembro, de {ano}, houve {soma_novembro} dias em que não houve observações.\nNo mês de Dezembro, de {ano}, houve {soma_dezembro} dias em que não houve observações.'
    return str_saida_dias_sem_mancha
def funcao_1_1(ano):
    '''
    Função que conta os dias que não foram coletados dados sobre manchas solares.

    Parameters
    ----------
    ano : int. Ano que se deseja contar os dias.
    

    Returns
    -------
    str_saida_dias_sem_mancha : str. Informações de saída.

    '''
    if int(ano) < 1818 or int(ano) > 2018:
        variavel_de_validacao = 0
        while variavel_de_validacao == 0:
            print('\n')
            print('Infelizmente houve um erro.')
            ano = str(input('Favor inserir um ano entre 1818 e 2018: '))
            if int(ano) >= 1818 and int(ano) <= 2018:
                variavel_de_validacao += 1
    soma_janeiro = 0
    soma_fevereiro = 0
    soma_marco = 0
    soma_abril = 0
    soma_maio = 0
    soma_junho = 0
    soma_julho = 0
    soma_agosto = 0
    soma_setembro = 0
    soma_outubro = 0
    soma_novembro = 0
    soma_dezembro = 0
    ano_dicionario = dicionario_dia[ano]
    for mes in ano_dicionario:
        if mes == '1':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '-1':
                    soma_janeiro += 1
        if mes == '2':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '-1':
                    soma_fevereiro += 1
        if mes == '3':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '-1':
                    soma_marco += 1
        if mes == '4':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '-1':
                    soma_abril += 1
        if mes == '5':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '-1':
                    soma_maio += 1
        if mes == '6':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '-1':
                    soma_junho += 1
        if mes == '7':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '-1':
                    soma_julho += 1
        if mes == '8':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '-1':
                    soma_agosto += 1
        if mes == '9':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '-1':
                    soma_setembro += 1
        if mes == '10':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '-1':
                    soma_outubro += 1
        if mes == '11':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '-1':
                    soma_outubro += 1
        if mes == '12':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] == '-1':
                    soma_dezembro += 1
    str_saida_dias_sem_mancha = f'No mês de Janeiro, de {ano}, houve {soma_janeiro} dias em que não se coletaram dados.\nNo mês de Fevereiro, de {ano}, houve {soma_fevereiro} dias em que não se coletaram dados.\nNo mês de Março, de {ano}, houve {soma_marco} dias em que não se coletaram dado.\nNo mês de Abril, de {ano}, houve {soma_abril} dias em que não se coletaram dados.\nNo mês de Maio, de {ano}, houve {soma_maio} dias em que não se coletaram dados.\nNo mês de Junho, de {ano}, houve {soma_junho} dias em que não se coletaram dados.\nNo mês de Julho, do {ano}, houve {soma_julho} dias em que não se coletaram dados.\nNo mês de Agosto, do {ano}, houve {soma_agosto} dias em que não se coletaram dados.\nNo mês de Setembro, do {ano}, houve {soma_setembro} dias em que não se coletaram dados.\nNo mês de Outubro, do {ano}, houve {soma_outubro} dias em que não se coletaram dados.\nNo mês de Novembro, de {ano}, houve {soma_novembro} dias em que não se coletaram dados.\nNo mês de Dezembro, de {ano}, houve {soma_dezembro} dias em que não se coletaram dados.'
    return str_saida_dias_sem_mancha
def funcao_2():

    '''
    Função que Determinar o ano e o mês que tiveram mais dias sem manchas solares.
    
    Parameters
    ----------
    mes_sem_dado: str. Mês que possui menos manchas solares.
    ano_mes_sem_dados: str. Ano do mês que possui menos manchas solares.
    soma_mes: int. Número de dias sem manchas solares de um mês.
    soma_mes_sem_dado: int. Número do mês com mais dias sem manchas solares.
    lista_mes : list. Lista com os meses com as menores vizualizações.
    lista_ano : list. Lista com os anos respectivos aos meses da lista_mes
    lista_mes_final : list. Lista com os meses escritos por extenso.
    
    Returns
    -------
    str_saida : str. Saída formatada de dados indicando o mês com menor número de manchas solares e o 
    ano com menor número de manchas solares.

    '''
    mes_sem_dado = 0
    ano_mes_sem_dado = 0
    soma_mes = 0
    soma_mes_sem_dado = 0
    lista_mes = []
    lista_ano = []
    lista_mes_final = []
    for ano in dicionario_media:
        for mes in dicionario_media[ano]:
            soma_mes = float(dicionario_media[ano][mes][0])
            if soma_mes <= soma_mes_sem_dado:
                soma_mes_sem_dado = soma_mes
                mes_sem_dado = int(mes)
                lista_mes.append(mes_sem_dado)
                ano_mes_sem_dado = ano
                lista_ano.append(ano_mes_sem_dado)
    for mes in lista_mes:
        if mes == 1:
            lista_mes_final.append('Janeiro')
        if mes == 2:
            lista_mes_final.append('Fevereiro')
        if mes == 3:
            lista_mes_final.append('Março')
        if mes == 4:
            lista_mes_final.append('Abril')
        if mes == 5:
            lista_mes_final.append('Maio')
        if mes == 6:
            lista_mes_final.append('Junho')
        if mes == 7:
            lista_mes_final.append('Julho')
        if mes == 8:
            lista_mes_final.append('Agosto')
        if mes == 9:
            lista_mes_final.append('Setembro')
        if mes == 10:
            lista_mes_final.append('Outubro')
        if mes == 11:
            lista_mes_final.append('Novembro')
        if mes == 12:
            lista_mes_final.append('Dezembro')
    print('Os meses com menores observação de manchas solares foram:')
    for i in range(len(lista_ano)):
        str_saida = f'- {lista_mes_final[i]} de {lista_ano[i]}.'
        print(str_saida)
    return ('\n')
def funcao_3():
    '''
    Função que determinar o ano e o mês que tiveram mais manchas solares.

    Parameters
    ----------
    mes_mais_dado: int. Mês com o maior número de manchas solares.
    anos_mes_mais_dado: str. Ano do mês com maior número de manchas solares.
    soma_mes: int. Número de manchas solares por mês.
    soma_mes_mais_dado: int. Número de manchas solares do mês com mais manchas solares.
    
    
    Returns
    -------
    str_saida : str. String com as informações de formatadas de saída.

    '''
    mes_mais_dado = 0
    ano_mes_mais_dado = 0
    soma_mes = 0
    soma_mes_mais_dado = 0
    for ano in dicionario_media:
        for mes in dicionario_media[ano]:
            soma_mes = float(dicionario_media[ano][mes][0])
            if soma_mes >= soma_mes_mais_dado:
                soma_mes_mais_dado = soma_mes
                mes_mais_dado = int(mes)
                ano_mes_mais_dado = ano
    if mes_mais_dado == 1:
        mes_saida = 'Janeiro'
    if mes_mais_dado  == 2:
        mes_saida = 'Fevereiro'
    if mes_mais_dado == 3:
        mes_saida = 'Março'
    if mes_mais_dado == 4:
        mes_saida = 'Abril'
    if mes_mais_dado == 5:
        mes_saida = 'Maio'
    if mes_mais_dado == 6:
        mes_saida = 'Junho'
    if mes_mais_dado == 7:
        mes_saida = 'Julho'
    if mes_mais_dado == 8:
        mes_saida = 'Agosto'
    if mes_mais_dado == 9:
        mes_saida = 'Setembro'
    if mes_mais_dado == 10:
        mes_saida = 'Outubro'
    if mes_mais_dado == 11:
        mes_saida = 'Novembro'
    if mes_mais_dado == 12:
        mes_saida = 'Dezembro'
    print('O mês com maior observação de manchas solares foi:')
    str_saida = f'{mes_saida} de {ano_mes_mais_dado} com {soma_mes_mais_dado} manchas observadas.'
    return str_saida
def funcao_4(inicio,fim):
   '''
   Função que determina o máximo e o mínimo de manchas solares em um período.

   Parameters
   ----------
   inicio : str. Data de início do período.
   fim : str. Data de fim do período.

   Returns
   -------
   str_saida : str. Saída formatada dos dados de entrada.

   '''
   mes_fim = 0
   mes_fim = 0
   if inicio[:2] == 'Ja' or inicio[:2] == 'ja':
       mes_inicio = '1'
   if inicio[:2] == 'Fe' or inicio[:2] == 'fe':
       mes_inicio = '2'
   if inicio[:2] == 'Mar' or inicio[:2] == 'mar':
       mes_inicio = '3'
   if inicio[:2] == 'Ab' or inicio[:2] == 'ab':
       mes_inicio = '4'
   if inicio[:2] == 'Mai' or inicio[:2] == 'mai':
       mes_inicio = '5'
   if inicio[:2] == 'Jun' or inicio[:2] == 'jun':
       mes_inicio = '6'
   if inicio[:2] == 'Jul' or inicio[:2] == 'jul':
       mes_inicio = '7'
   if inicio[:2] == 'Ag' or inicio[:2] == 'ag':
       mes_inicio = '8'
   if inicio[:2] == 'Se' or inicio[:2] == 'se':
       mes_inicio = '9'
   if inicio[:2] == 'Ou' or inicio[:2] == 'ou':
       mes_inicio = '10'
   if inicio[:2] == 'No' or inicio[:2] == 'no':
       mes_inicio = '11'
   if inicio[:2] == 'De' or inicio[:2] == 'de':
       mes_inicio = '12'
   ano_inicio = int(inicio[-4:])
   if fim[:2] == 'Ja' or fim[:2] == 'ja':
       mes_fim = '1'
   if fim[:2] == 'Fe' or fim[:2] == 'fe':
       mes_fim = '2'
   if fim[:2] == 'Mar' or fim[:2] == 'mar':
       mes_fim = '3'
   if fim[:2] == 'Ab' or fim[:2] == 'ab':
       mes_fim = '4'
   if fim[:2] == 'Mai' or fim[:2] == 'mai':
       mes_fim = '5'
   if fim[:2] == 'Jun' or fim[:2] == 'jun':
       mes_fim = '6'
   if fim[:2] == 'Jul' or fim[:2] == 'jul':
       mes_fim = '7'
   if fim[:2] == 'Ag' or fim[:2] == 'ag':
       mes_fim = '8'
   if fim[:2] == 'Se' or fim[:2] == 'se':
       mes_fim = '9'
   if fim[:2] == 'Ou' or fim[:2] == 'ou':
       mes_fim = '10'
   if fim[:2] == 'No' or fim[:2] == 'no':
       mes_fim = '11'
   if fim[:2] == 'De' or fim[:2] == 'de':
       mes_fim = '12'
   ano_fim = int(fim[-4:])
   maximo_periodo = []
   minimo_periodo = []
   lista_mancha = []
   for ano in range(ano_inicio,ano_fim+1):
       for mes in dicionario_media[str(ano)]:
           mancha_mes = float(dicionario_media[str(ano)][mes][0])
           lista_mancha.append(mancha_mes)
   if int(mes_inicio) > 1:
       for i in range(1, int(mes_inicio)):
           del lista_mancha[i]
   for i in range(12 - int(mes_fim)):
       del lista_mancha[(12-i)]
   maximo_periodo = max(lista_mancha)
   minimo_periodo = min(lista_mancha)
   str_saida = f'O máximo de mancha solares no período foi {maximo_periodo}.\nO mínimo de manchas solares no período foi {minimo_periodo}'            
   return str_saida
def funcao_5(ano):
    '''
    Função que calcula a média mensal de cada mês, para um dado ano.

    Parameters
    ----------
    ano : str. Ano que se deseja saber a média por mês das manchas solares.
    variavel_de_validacao: int. Variável que valida se o ano de entrada corresponde a 
    um ano dentro do banco de dados.
    lista_mes_janeiro: list. Lista que contém as observações diárias de manchas solares, quando existem.
    lista_mes_fevereiro: list. Lista que contém as observações diárias de manchas solares, quando existem.
    lista_mes_marco: list. Lista que contém as observações diárias de manchas solares, quando existem.
    lista_mes_abril: list. Lista que contém as observações diárias de manchas solares, quando existem.
    lista_mes_maio: list. Lista que contém as observações diárias de manchas solares, quando existem.
    lista_mes_junho: list. Lista que contém as observações diárias de manchas solares, quando existem.
    lista_mes_julho: list. Lista que contém as observações diárias de manchas solares, quando existem.
    lista_mes_agosto: list. Lista que contém as observações diárias de manchas solares, quando existem.
    lista_mes_setembro: list. Lista que contém as observações diárias de manchas solares, quando existem.
    lista_mes_outubro: list. Lista que contém as observações diárias de manchas solares, quando existem.
    lista_mes_novembro: list. Lista que contém as observações diárias de manchas solares, quando existem.
    lista_mes_dezembro list. Lista que contém as observações diárias de manchas solares, quando existem.
    dias_mes_janeiro: int. Número de dias do mês indicado.
    dias_mes_fevereiro: list. Lista que contém as observações diárias de manchas solares, quando existem.
    dias_mes_marco: list. Lista que contém as observações diárias de manchas solares, quando existem.
    dias_mes_abril: list. Lista que contém as observações diárias de manchas solares, quando existem.
    dias_mes_maio: list. Lista que contém as observações diárias de manchas solares, quando existem.
    dias_mes_junho: list. Lista que contém as observações diárias de manchas solares, quando existem.
    dias_mes_julho: list. Lista que contém as observações diárias de manchas solares, quando existem.
    dias_mes_agosto: list. Lista que contém as observações diárias de manchas solares, quando existem.
    dias_mes_setembro: list. Lista que contém as observações diárias de manchas solares, quando existem.
    dias_mes_outubro: list. Lista que contém as observações diárias de manchas solares, quando existem.
    dias_mes_novembro: list. Lista que contém as observações diárias de manchas solares, quando existem.
    dias_mes_dezembro: list. Lista que contém as observações diárias de manchas solares, quando existem.
    soma_mes_janeiro: int. Número de manchas solares de todas as manchas solares do mês indicado.
    soma_mes_fevereiro: int. Número de manchas solares de todas as manchas solares do mês indicado.
    soma_mes_marco: int. Número de manchas solares de todas as manchas solares do mês indicado.
    soma_mes_abril: int. Número de manchas solares de todas as manchas solares do mês indicado.
    soma_mes_maio: int. Número de manchas solares de todas as manchas solares do mês indicado.
    soma_mes_junho: int. Número de manchas solares de todas as manchas solares do mês indicado.
    soma_mes_julho: int. Número de manchas solares de todas as manchas solares do mês indicado.
    soma_mes_agosto: int. Número de manchas solares de todas as manchas solares do mês indicado.
    soma_mes_setembro: int. Número de manchas solares de todas as manchas solares do mês indicado.
    soma_mes_outubro: int. Número de manchas solares de todas as manchas solares do mês indicado.
    soma_mes_novembro: int. Número de manchas solares de todas as manchas solares do mês indicado.
    soma_mes_dezembro: int. Número de manchas solares de todas as manchas solares do mês indicado.
    media_janeiro: int. Média de manchas solares do mês indicado.
    media_fevereiro: int. Número de manchas solares de todas as manchas solares do mês indicado.
    media_marco: int. Número de manchas solares de todas as manchas solares do mês indicado.
    media_abril: int. Número de manchas solares de todas as manchas solares do mês indicado.
    media_maio: int. Número de manchas solares de todas as manchas solares do mês indicado.
    media_junho: int. Número de manchas solares de todas as manchas solares do mês indicado.
    media_julho: int. Número de manchas solares de todas as manchas solares do mês indicado.
    media_agosto: int. Número de manchas solares de todas as manchas solares do mês indicado.
    media_setembro: int. Número de manchas solares de todas as manchas solares do mês indicado.
    media_outubro: int. Número de manchas solares de todas as manchas solares do mês indicado.
    media_novembro: int. Número de manchas solares de todas as manchas solares do mês indicado.
    media_dezembro: int. Número de manchas solares de todas as manchas solares do mês indicado.
    
    Returns
    -------
    str_saida : str. Saída de dados formatados.

    '''
    if int(ano) < 1818 or int(ano) > 2018:
        variavel_de_validacao = 0
        while variavel_de_validacao == 0:
            print('\n')
            print('Infelizmente houve um erro.')
            ano = str(input('Favor inserir um ano entre 1818 e 2018: '))
            if int(ano) >= 1818 and int(ano) <= 2018:
                variavel_de_validacao += 1
    lista_mes_janeiro = []
    lista_mes_fevereiro = []
    lista_mes_marco = []
    lista_mes_abril = []
    lista_mes_maio = []
    lista_mes_junho = []
    lista_mes_julho = []
    lista_mes_agosto = []
    lista_mes_setembro = []
    lista_mes_outubro = []
    lista_mes_novembro = []
    lista_mes_dezembro = []
    dias_mes_janeiro = 0
    dias_mes_fevereiro = 0
    dias_mes_marco = 0
    dias_mes_abril = 0
    dias_mes_maio = 0
    dias_mes_junho = 0
    dias_mes_julho = 0
    dias_mes_agosto = 0
    dias_mes_setembro = 0
    dias_mes_outubro = 0
    dias_mes_novembro = 0
    dias_mes_dezembro = 0
    ano_dicionario = dicionario_dia[ano]
    for mes in ano_dicionario:   
        if mes == '1':
            for dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] != None:
                    dias_mes_janeiro +=1
                if  dicionario_dia[ano][mes][dia][1] != '-1':
                    mancha_dia = int(dicionario_dia[ano][mes][dia][1])
                    lista_mes_janeiro.append(mancha_dia)
        if mes == '2':
            for  dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] != None:
                    dias_mes_fevereiro += 1
                if  dicionario_dia[ano][mes][dia][1] != '-1':
                    mancha_dia = int(dicionario_dia[ano][mes][dia][1])
                    lista_mes_fevereiro.append(mancha_dia)
        if mes == '3':
            for  dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] != None:
                    dias_mes_marco += 1
                if  dicionario_dia[ano][mes][dia][1] != '-1':
                    mancha_dia = int(dicionario_dia[ano][mes][dia][1])
                    lista_mes_marco.append(mancha_dia)
        if mes == '4':
            for  dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] != None:
                    dias_mes_abril += 1
                if  dicionario_dia[ano][mes][dia][1] != '-1':
                    mancha_dia = int(dicionario_dia[ano][mes][dia][1])
                    lista_mes_abril.append(mancha_dia)
        if mes == '5':
            for  dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] != None:
                    dias_mes_maio += 1
                if  dicionario_dia[ano][mes][dia][1] != '-1':
                    mancha_dia = int(dicionario_dia[ano][mes][dia][1])
                    lista_mes_maio.append(mancha_dia)
        if mes == '6':
            for  dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] != None:
                    dias_mes_junho += 1
                if  dicionario_dia[ano][mes][dia][1] != '-1':
                    mancha_dia = int(dicionario_dia[ano][mes][dia][1])
                    lista_mes_junho.append(mancha_dia)
        if mes == '7':
            for  dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] != None:
                    dias_mes_julho += 1
                if  dicionario_dia[ano][mes][dia][1] != '-1':
                    mancha_dia = int(dicionario_dia[ano][mes][dia][1])
                    lista_mes_julho.append(mancha_dia)
        if mes == '8':
            for  dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] != None:
                    dias_mes_agosto += 1
                if  dicionario_dia[ano][mes][dia][1] != '-1':
                    mancha_dia = int(dicionario_dia[ano][mes][dia][1])
                    lista_mes_agosto.append(mancha_dia)
        if mes == '9':
            for  dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] != None:
                    dias_mes_setembro += 1
                if  dicionario_dia[ano][mes][dia][1] != '-1':
                    mancha_dia = int(dicionario_dia[ano][mes][dia][1])
                    lista_mes_setembro.append(mancha_dia)
        if mes == '10':
            for  dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] != None:
                    dias_mes_outubro += 1
                if  dicionario_dia[ano][mes][dia][1] != '-1':
                    mancha_dia = int(dicionario_dia[ano][mes][dia][1])
                    lista_mes_outubro.append(mancha_dia)
        if mes == '11':
            for  dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] != None:
                    dias_mes_novembro += 1
                if  dicionario_dia[ano][mes][dia][1] != '-1':
                    mancha_dia = int(dicionario_dia[ano][mes][dia][1])   
                    lista_mes_outubro.append(mancha_dia)
        if mes == '12':
            for  dia in dicionario_dia[ano][mes]:
                if dicionario_dia[ano][mes][dia][1] != None:
                    dias_mes_dezembro += 1
                if  dicionario_dia[ano][mes][dia][1] != '-1':
                    mancha_dia = int(dicionario_dia[ano][mes][dia][1])   
                    lista_mes_dezembro.append(mancha_dia)               
    soma_mes_janeiro = sum(lista_mes_janeiro)
    media_janeiro = round(soma_mes_janeiro/dias_mes_janeiro, 2)
    soma_mes_fevereiro = sum(lista_mes_fevereiro)
    media_fevereiro = round(soma_mes_fevereiro/dias_mes_fevereiro, 2)
    soma_mes_marco = sum(lista_mes_marco)
    media_marco = round(soma_mes_marco/dias_mes_marco, 2)
    soma_mes_abril = sum(lista_mes_abril)
    media_abril = round(soma_mes_abril/dias_mes_abril, 2)
    soma_mes_maio = sum(lista_mes_maio)
    media_maio = round(soma_mes_maio/dias_mes_maio, 2)
    soma_mes_junho = sum(lista_mes_junho)
    media_junho = round(soma_mes_junho/dias_mes_junho, 2)
    soma_mes_julho = sum(lista_mes_julho)
    media_julho = round(soma_mes_julho/dias_mes_julho, 2)
    soma_mes_agosto = sum(lista_mes_agosto)
    media_agosto = round(soma_mes_agosto/dias_mes_agosto, 2)
    soma_mes_setembro = sum(lista_mes_setembro)
    media_setembro = round(soma_mes_setembro/dias_mes_setembro, 2)
    soma_mes_outubro = sum(lista_mes_outubro)
    media_outubro = round(soma_mes_outubro/dias_mes_outubro, 2)
    soma_mes_novembro = sum(lista_mes_novembro)
    media_novembro = round(soma_mes_novembro/dias_mes_novembro, 2)
    soma_mes_dezembro = sum(lista_mes_dezembro)
    media_dezembro = round(soma_mes_dezembro/dias_mes_dezembro, 2)
    str_saida = f'Em {ano}, foram observadas em média de manchas solares:\n -{media_janeiro} em Janeiro.\n-{media_fevereiro} em Fevereiro.\n-{media_marco} em Março.\n-{media_abril} em Abril.\n-{media_maio} em Maio.\n-{media_junho} em Junho.\n-{media_julho} em Julho.\n-{media_agosto} em Agosto.\n-{media_setembro} em Setembro.\n-{media_outubro} em Outubro.\n-{media_novembro} em Novembro.\n-{media_dezembro} em Dezembro. '
    return str_saida
def funcao_6():
    '''
    Função que calcular o desvio padrão mensal a partir das observações diárias do mês pela fórmula
    dada no arquivo dos dados de observações mensais.

    Parameters
    ----------
    mes : str. Mês a ser calculado o desvio padrão.
    ano : str. Ano do mês a ser calculado o desvio padrão.

    Returns
    -------
    str_desvio : str. Saída de dados de formatação desejada.

    '''
    
    ano = str(input('Insira o ano que se deseja calcular o desvio padrão: '))
    if int(ano) < 1818 or int(ano) > 2018:
        variavel_de_validacao = 0
        while variavel_de_validacao == 0:
            print('\n')
            print('Infelizmente houve um erro.')
            ano = str(input('Favor inserir um ano entre 1818 e 2018: '))
            if int(ano) >= 1818 and int(ano) <= 2018:
                variavel_de_validacao += 1
    mes = str(input('Insira o número do mês que se deseja calcular o desvio padrão: '))
    if mes[:2] != 'ja' and mes[:2] != 'Ja' and mes[:2] != 'JA' and mes[:2] != 'fe' and mes[:2] !='FE' and mes[:2] != 'Fe' and mes[:3] != 'mar' and mes[:3] != 'MAR' and mes[:3] != 'Mar' and mes[:2] != 'Ab' and mes[:2] != 'ab' and mes[:2] != 'AB' and mes[:3] != 'Mai' and mes[:3] != 'mai' and mes[:3] !='MAI' and mes[:3] !=  'jun' and mes[:3] != 'JUN' and mes[:3] != 'Jun' and mes[:3] != 'jul' and mes[:3] != 'JUL' and mes[:3] != 'Jul' and mes[:2] != 'Ag' and mes[:2] != 'AG' and mes[:2] != 'ag' and mes[:2] != 'SE' and mes[:2] != 'Se' and mes[:2] != 'se' and mes[:2] != 'ou' and mes[:2] != 'Ou' and mes[:2] != 'OU' and mes[:2] !='No' and mes[:2] !='no' and mes[:2] != 'NO' and mes[:2] != 'De' and mes[:2] != 'DE' and mes[:2] != 'de':
        variavel_de_validacao = 0
        while variavel_de_validacao == 0:
            print('\n')
            print('Infelizmente houve um erro.')
            mes = str(input('Favor escrever um mês do ano: '))
            if mes[:2] == 'ja' or mes[:2] == 'Ja' or mes[:2] == 'JA' or mes[:2] == 'fe' or mes[:2] =='FE' or mes[:2] == 'Fe' or mes[:3] == 'mar' or mes[:3] == 'MAR' or mes[:3] == 'Mar' or mes[:2] == 'Ab' or mes[:2] == 'ab' or mes[:2] == 'AB' or mes[:3] == 'Mai' or mes[:3] == 'mai' or mes[:3] =='MAI' or mes[:3] ==  'jun' or mes[:3] == 'JUN' or mes[:3] == 'Jun' or mes[:3] == 'jul' or mes[:3] == 'JUL' or mes[:3] == 'Jul' or mes[:2] == 'Ag' or mes[:2] == 'AG' or mes[:2] == 'ag' or mes[:2] == 'SE' or mes[:2] == 'Se' or mes[:2] == 'se' or mes[:2] == 'ou' or mes[:2] == 'Ou' or mes[:2] == 'OU' or mes[:2] =='No' or mes[:2] =='no' or mes[:2] == 'NO' or mes[:2] == 'De' or mes[:2] == 'DE' or mes[:2] == 'de':
                variavel_de_validacao += 1
    if mes[:2] == 'ja' or mes[:2] == 'Ja' or mes[:2] == 'JA':
        mes_saida = '1'
        print(mes_saida)
        mes_str = 'Janeiro'
    if mes[:2] == 'fe' or mes[:2] =='FE' or mes[:2] == 'Fe':
        mes_saida = '2'
        mes_str = 'Fevereiro'
    if mes[:3] == 'mar' or mes[:3] == 'MAR' or mes[:3] == 'Mar':
        mes_saida = '3'
        mes_str = 'Março'
    if mes[:2] == 'Ab' or mes[:2] == 'ab' or mes[:2] == 'AB':
        mes_saida = '4'
        mes_str = 'Abril'
    if mes[:3] == 'Mai' or mes[:3] == 'mai' or mes[:3] =='MAI':
        mes_saida = '5'
        mes_str = 'Maio'
    if mes[:3] ==  'jun' or mes[:3] == 'JUN' or mes[:3] == 'Jun':
        mes_saida = '6'
        mes_str = 'Junho'
    if mes[:3] == 'jul' or mes[:3] == 'JUL' or mes[:3] == 'Jul':
        mes_saida = '7'
        mes_str = 'julho'
    if mes[:2] == 'Ag' or mes[:2] == 'AG' or mes[:2] == 'ag':
        mes_saida = '8'
        mes_str = 'Agosto'
    if mes[:2] == 'SE' or mes[:2] == 'Se' or mes[:2] == 'se':
        mes_saida = '9'
        mes_str = 'Setembro'
    if mes[:2] == 'ou' or mes[:2] == 'Ou' or mes[:2] == 'OU':
        mes_saida = '10'
        mes_str = 'Outubro'
    if mes[:2] =='No' or mes[:2] =='no' or mes[:2] == 'NO':
        mes_saida = '11'
        mes_str = 'Novembro'
    if mes[:2] == 'De' or mes[:2] == 'DE' or mes[:2] == 'de':
        mes_saida = '12'
        mes_str = 'Dezembro'
    lista_sigma_d = []
    lista_n_d = []
    lista_aux_1 = []
    observacoes_diarias = 0
    desvio_diario = 0
    for ANO in dicionario_dia:
        if ANO == ano:
            for MES in dicionario_dia[ANO]:
                if MES == mes_saida: 
                    for dia in dicionario_dia[ANO][MES]:
                        if dicionario_dia[ANO][MES][dia][1] != '0' and dicionario_dia[ANO][MES][dia][1] != '-1':
                            observacoes_diarias = int(dicionario_dia[ANO][MES][dia][1])
                            lista_n_d.append(observacoes_diarias)
                        if dicionario_dia[ANO][MES][dia][2] != '0.0' and dicionario_dia[ANO][MES][dia][2] != '-1.0':
                            desvio_diario = float(dicionario_dia[ANO][MES][dia][2])
                            lista_sigma_d.append(desvio_diario)                    
    lista_aux_1 = list(map(lambda x,y: x*y ,lista_n_d,lista_sigma_d))
    variavel_aux = sum(lista_aux_1)
    n_d = sum(lista_n_d)
    if n_d == 0:
        n_d = 1
    variavel_aux_1 = variavel_aux / n_d
    desvio = round((variavel_aux_1)**(0.5), 2)
    str_desvio = f'O desvio padrão de {mes_str} de {ano} é {desvio}.'
    return (str_desvio)   
def funcao_7(ciclo):
    '''
    Função que retorna informação sobre os ciclos solares.

    Parameters
    ----------
    ciclo : int. Número do cliclo que se deseja obter informações.
    variavel_de_validacao : int. Variável que verifica se o int de entrada está dentro dos ciclos disponíveis.
    inicio_ciclo : str. Data de início do ciclo solar.
    fim_ciclo : str. Data de fim do ciclo solar.
    duracao_ciclo : str. Duração do ciclo solar em anos.
    extra : str. Informação complementar sobre o ciclo solar.


    Returns
    -------
    str_saida : str. Informações de saída sobre o ciclo solar escolhido.

    '''
    if ciclo < 1 or ciclo > 25:
        variavel_de_validacao = 0
        while variavel_de_validacao == 0:
            print('Infelizmente houve um erro.')
            ciclo = int(input('Favor inserir um ciclo entre 1 e 25: '))
            if ciclo >= 1 and ciclo <= 25:
                variavel_de_validacao += 1
    print('\n')
    if ciclo == 1:
        inicio_ciclo = 'Fevereiro de 1755'
        fim_ciclo = 'Junho de 1766'
        duracao_ciclo = '11,3'
        extra = 'foi o primeiro ciclo solar desde o início do extenso registro da atividade das manchas solares.'
    if ciclo == 2:
        inicio_ciclo = 'Junho de 1766'
        fim_ciclo = 'Junho de 1775'
        duracao_ciclo = '9'
        extra = 'observações de manchas solares por Alexander Wilson durante este período estabeleceram o efeito Wilson.'
    if ciclo == 3:
        inicio_ciclo = 'Junho de 1775'
        fim_ciclo = 'Setembro de 1784'
        duracao_ciclo = '9,3'
        extra = 'William Herschel começou a observar manchas solares durante este período.'
    if ciclo == 4:
        inicio_ciclo = 'Setembro de 1784'
        fim_ciclo = 'Abril de 1798'
        duracao_ciclo = '13,6'
        extra = 'existem algumas especulações recentes de que o ciclo 4, o ciclo solar mais longo desde 1755, foi na verdade dois ciclos, com base no aparecimento de novas manchas solares em altas latitudes solares em 1793-1796 e uma reconstrução do diagrama borboleta de manchas solares para os ciclos 3 e 4, embora os números totais de manchas solares mostrem apenas uma distribuição de pico único. '
    if ciclo == 5:
        inicio_ciclo = 'Abril de 1798'
        fim_ciclo = 'Agosto de 1810'
        duracao_ciclo = '12,3'
        extra = 'este foi segundo mais baixo de qualquer ciclo até hoje, atrás do ciclo solar 6, como resultado de ser parte do Mínimo de Dalton.'
    if ciclo == 6:
        inicio_ciclo = 'Agosto de 1810'
        fim_ciclo = 'Maio de 1823'
        duracao_ciclo = '12,8'
        extra = 'o número máximo de manchas solares observado durante o ciclo solar foi de 81,2, em maio de 1816 (o mais baixo de qualquer ciclo até hoje, como resultado de fazer parte do Mínimo de Dalton), e o mínimo inicial foi de 0,0.'
    if ciclo == 7:
        inicio_ciclo = 'Maio de 1823'
        fim_ciclo = 'Novembro de 1833'
        duracao_ciclo = '10,5'
        extra = 'o número máximo de manchas solares observado durante o ciclo solar foi de 119,2 (novembro de 1829), e o mínimo inicial foi de 0,2. '
    if ciclo == 8:
        inicio_ciclo = 'Novembro de 1833'
        fim_ciclo = 'Julho de 1843'
        duracao_ciclo = '9,7'
        extra = 'o ciclo solar 8 terminou em 1843, ano em que Heinrich Schwabe descobriu o ciclo das manchas solares.'
    if ciclo == 9:
        inicio_ciclo = 'Julho de 1843'
        fim_ciclo = 'Dezembro de 1855'
        duracao_ciclo = '12,4'
        extra = 'durante este ciclo, Edward Sabine, Rudolf Wolf e outros cientistas reconheceram que os distúrbios solares afetaram o ambiente magnético da Terra, de modo que os ciclos solares são idênticos aos ciclos geomagnéticos da Terra.'
    if ciclo == 10:
        inicio_ciclo = 'Dezembro de 1855'
        fim_ciclo = 'Março de 1867'
        duracao_ciclo = '11,3'
        extra = 'as primeiras observações de erupções solares, por Richard Carrington e Richard Hodgson (de forma independente), ocorreram durante este ciclo.'
    if ciclo == 11:
        inicio_ciclo = 'Março de 1867'
        fim_ciclo = 'Dezembro de 1878'
        duracao_ciclo = '11,8'
        extra = 'fortes exibições de auroras foram observadas em outubro de 1870, fevereiro de 1872 e agosto de 1872.'
    if ciclo == 12:
        inicio_ciclo = 'Dezembro de 1878'
        fim_ciclo = 'Março de 1890'
        duracao_ciclo = '11,3'
        extra = 'durante o trânsito mínimo do ciclo solar 12 a 13, houve um total de 736 dias sem manchas solares.'
    if ciclo == 13:
        inicio_ciclo = 'Março de 1890'
        fim_ciclo = 'Janeiro de 1902'
        duracao_ciclo = '11,8'
        extra = 'houve uma série de eventos intensos de prótons solares durante o ciclo solar 13, bem como tempestades geomagnéticas, como em setembro de 1898, que afetaram as linhas de telégrafo.'
    if ciclo == 14:
        inicio_ciclo = 'Janeiro de 1902'
        fim_ciclo = 'Julho de 1913'
        duracao_ciclo = '11,5'
        extra = 'tempestades geomagnéticas em novembro de 1903, março de 1905 e setembro de 1909 afetaram as linhas telegráficas. '
    if ciclo == 15:
        inicio_ciclo = 'Julho de 1913'
        fim_ciclo = 'Agosto de 1923'
        duracao_ciclo = '10,1'
        extra = 'tempestades geomagnéticas em março de 1918, agosto de 1919, outubro de 1919 e março de 1920 afetaram as linhas telegráficas, enquanto uma erupção solar em 13 de maio de 1921 também afetou o sinal ferroviário e os equipamentos de comutação, no que ficou conhecido como a "Tempestade Ferroviária de Nova York".'
    if ciclo == 16:
        inicio_ciclo = 'Agosto de 1923'
        fim_ciclo = 'Setembro de 1933'
        duracao_ciclo = '10,1'
        extra = 'reportagens de jornais durante este período notam efeitos nos sistemas de telégrafo, mas também (em março de 1924, janeiro de 1926, outubro de 1926 e outubro de 1927) na transmissão de rádio.'
    if ciclo == 17:
        inicio_ciclo = 'Setembro de 1933'
        fim_ciclo = 'Fevereiro de 1944'
        duracao_ciclo = '10,4'
        extra = 'uma grande aurora foi vista por toda a Europa em 25 de janeiro de 1938, até o sul de Portugal e Sicília, assustando muitas pessoas. Alguns pensavam que o brilho vermelho indicava grandes incêndios, enquanto outros o ligavam às profecias de Fátima. Uma aurora foi visível sobre Nova York em 3 de abril de 1940.'
    if ciclo == 18:
        inicio_ciclo = 'Fevereiro de 1944'
        fim_ciclo = 'Abril de 1954'
        duracao_ciclo = '10,2'
        extra = 'O ciclo 18 foi caracterizado por manchas solares "gigantes". A gravação do fluxo de rádio solar de 10,7 cm (2800 MHz) começou parcialmente durante este ciclo, e os valores do fluxo solar durante este ciclo revelaram-se particularmente elevados.'
    if ciclo == 19:
        inicio_ciclo = 'Abril de 1954'
        fim_ciclo = 'Outubro de 1964'
        duracao_ciclo = '10,5'
        extra = 'Uma tempestade geomagnética em fevereiro de 1956 interferiu nas comunicações de rádio e levou a uma busca pelo submarino britânico Acheron depois que ele perdeu o contato de rádio.'
    if ciclo == 20:
        inicio_ciclo = 'Outubro de 1964' 
        fim_ciclo = 'Março de 1976'
        duracao_ciclo = '11,4'
        extra = 'Os dados do ciclo solar 20 foram usados ​​para construir o modelo de fluência de prótons solares K-1974, usado para planejar missões espaciais durante o ciclo solar 21.'
    if ciclo == 21:
        inicio_ciclo = 'Março de 1976'
        fim_ciclo = 'Setembro de 1986'
        duracao_ciclo = '10,5'
        extra = 'este ciclo solar marcou o início do monitoramento sistemático da irradiância solar total do espaço.'
    if ciclo == 22:
        inicio_ciclo = 'Setembro de 1986'
        fim_ciclo = 'Agosto de 1996'
        duracao_ciclo = '9,9'
        extra = 'durante março de 1989, uma forte tempestade geomagnética causou o colapso do sistema de transmissão de eletricidade da Hydro-Québec.'
    if ciclo == 23:
        inicio_ciclo = 'Agosto de 1996'
        fim_ciclo = 'Dezembro de 2008'
        duracao_ciclo = '12,3'
        extra = 'uma das primeiras grandes exibições de auroras do ciclo solar 23 ocorreu em 6 de abril de 2000, com auroras vermelhas brilhantes visíveis até o sul da Flórida e do sul da Europa.'
    if ciclo == 24:
        inicio_ciclo = 'Dezembro de 2008'
        fim_ciclo = 'Dezembro de 2019'
        duracao_ciclo = '11'
        extra = 'segundo a NASA , a intensidade das tempestades geomagnéticas durante o Ciclo Solar 24 pode ser elevada em algumas áreas onde o campo magnético da Terra é mais fraco do que o esperado. '
    if ciclo == 25:
        inicio_ciclo = 'Dezembro de 2019'
        fim_ciclo = 'atualmente'
        duracao_ciclo = 'mais de 3'
        extra = 'espera-se que continue até cerca de 2030.'
    str_saida = f'O ciclo solar {ciclo} se iniciou em {inicio_ciclo} e se encerrou em {fim_ciclo}.\nEste ciclo teve duração de {duracao_ciclo} anos.\nÉ interessante observar que {extra}'
    return str_saida    
#Interface do programa
import time
print('Olá humano!\n\nEu sou um programa de computador responsável pela computação de dados sobre manchas solares.\n')
time.sleep(4)
print('Você sabe o que são manchas solares?')
resposta1 = str(input('(Sim/Não): '))
if resposta1[0] == 'N' or resposta1[0] == 'n':
    resposta_1 = True
elif resposta1[0] == 's' or resposta1[0] == 'S':
    resposta_1 = None
if resposta_1 == True:
    print('\nBem, manchas solares são regiões na superfície do Sol com temperatura menor do que a média local e, por isso mesmo, em comparação com a superfície da nossa estrela, parecem ser mais escuras.\n')
    time.sleep(6)
    print('As manchas solares apresentam grande concentração de campo magnético.\n ')
    time.sleep(4)
    print('Este campo magnético concentrado aprisiona matéria na forma de plasma, ou seja, gás muito quente e ionizado e eletricamente carregado.\n')
    time.sleep(6.5)
    print('Se as linhas de campo magnético se rompem, matéria pode ser lançada para o espaço em eventos que chamamos de ejeção de massa coronal.')
    time.sleep(5)
    print('\nNeste caso, inúmeras partículas são arremessadas no espaço e muitas delas podem atingir a Terra.')
    time.sleep(4)
    print('\nAs auroras boreais e austrais resultam da chegada dessas partículas que interagem com a atmosfera terrestre. ')
    time.sleep(4)
if resposta_1 == None:
    print('\n')
    print('Okay sabichão!')
    time.sleep(3)

print('\n')
print('\nAgora, sabia que eu posso te informar vários dados sobre as manchas solares de TODA A HISTÓRIA\n')
time.sleep(1)
print('(que tiveram os dados computados)\n')
time.sleep(1)
print('DA RAÇA HUMANA?\n')
time.sleep(2)
print('SIMMMMM!!!!!')
time.sleep(2)
print('\nEnfim, agora vamos ao trabalho.\n')
time.sleep(3)

print('\n')
print('Você gostaria de saber quais dias, de um determinado ano, não foram observadas manchas solares?')
resposta2 = str(input('(Sim/Não): '))
resposta_2 = None
while resposta2[0] != 'S' and resposta2[0] != 's' and resposta2[0] != 'N' and resposta2[0] != 'n':
    variavel_de_validacao = 0
    while variavel_de_validacao == 0:
        print('\n')
        print('Infelizmente houve um erro.')
        resposta2 = str(input('Favor inserir uma resposta válida, sim ou não: '))
        if resposta2[0] == 'S' or resposta2[0] == 's' or resposta2[0] == 'N' or resposta2[0] == 'n':
            variavel_de_validacao += 1
if resposta2[0] == 'S' or resposta2[0] == 's':
    resposta_2 = True
elif resposta2[0] == 'N' or resposta2[0] == 'n':
    resposta_2 = False
if resposta_2 == True:
    print('\nTemos dados disponívels de 1818 até 2018.')
    time.sleep(4)
    ano = str(input('Insira o ano que deseja se obter os dados desejados: '))
    print(funcao_1(ano))
elif resposta_2 == False:
    print('\nOkay...')    

time.sleep(3)
print('\n')
print('Você gostaria de saber quais dias, de um determinado ano, não foram coletados dados sobre manchas solares?')
resposta21 = str(input('(Sim/Não): '))
if resposta21[0] == 'S' or resposta21[0] == 's':
    resposta_21 = True
elif resposta21[0] == 'N' or resposta21[0] == 'n':
    resposta_21 = False
if resposta_21 == True:
    print('\nTemos dados disponívels de 1818 até 2018.')
    time.sleep(4)
    ano = str(input('Insira o ano que deseja se obter os dados desejados: '))
    print(funcao_1_1(ano))
elif resposta_21 == False:
    print('\nOkay...') 

time.sleep(3)
print('\n')
print('\nVocê gostaria de saber os anos e os meses que tiveram menos manchas solares?')
resposta3 = str(input('(Sim/Não): '))
if resposta3[0] == 'S' or resposta3[0] == 's':
    resposta_3 = True
elif resposta3[0] == 'N' or resposta3[0] == 'n':
    resposta_3 = False
if resposta_3 == True:
    print(funcao_2())
elif resposta_3 == False:
    print('\nOkay...')

time.sleep(3)
print('\n')    
print('\nVocê gostaria de saber qual o mês que teve mais manchas solares?')
resposta4 = str(input('(Sim/Não): '))
if resposta4[0] == 'S' or resposta4[0] == 's':
    resposta_4 = True
elif resposta4[0] == 'N' or resposta4[0] == 'n':
    resposta_4 = False
if resposta_4 == True:
    print(funcao_3())
elif resposta_4 == False:
    print('\nOkay...')

time.sleep(3)
print('\n')    
print('Você deseja determinar o máximo e o mínimo de manchas solares de um determinado período?')
resposta5 = str(input('(Sim/Não): '))
if resposta5[0] == 'S' or resposta5[0] == 's':
    resposta_5 = True
elif resposta5[0] == 'N' or resposta5[0] == 'n':
    resposta_5 = False
if resposta_5 == True:
    print('Insira o início do período a ser considerado.')
    inicio = str(input('(*mês escrito por extenso* de *ano*): '))
    print('Insira o fim do período a ser considerado.')
    fim = str(input('(*mês escrito por extenso* de *ano*): '))
    print(funcao_4(inicio,fim))
elif resposta_5 == False:
    print('\nOkay...')

time.sleep(3)
print('\n')
print('Você gostaria de calcular a média mensal de manchas solares de um determinado ano?')
resposta6 = str(input('(Sim/Não): '))
if resposta6[0] == 'S' or resposta6[0] == 's':
    resposta_6 = True
elif resposta6[0] == 'N' or resposta6[0] == 'n':
    resposta_6 = False
if resposta_6 == True:
    ano = str(input('Insira o ano que se deseja calcular as médias: '))
    print(funcao_5(ano))
elif resposta_6 == False:
    print('\nOkay...')

time.sleep(3)
print('\n')
print('Você deseja calcular o desvio padrão mensal dos dados de observações diárias?')
resposta7 = str(input('(Sim/Não): '))
if resposta7[0] == 'S' or resposta7[0] == 's':
    resposta_7 = True
elif resposta7[0] == 'N' or resposta7[0] == 'n':
    resposta_7 = False
if resposta_7 == True:
    print(funcao_6())
elif resposta_7 == False:
    print('\nOkay...')

time.sleep(3)
print('\n')    
print('Você deseja saber um pouco sobre ciclos solares?')
resposta8 = str(input('(Sim/Não): '))
if resposta8[0] == 'S' or resposta8[0] == 's':
    resposta_8 = True
elif resposta8[0] == 'N' or resposta8[0] == 'n':
    resposta_8 = False
if resposta_8 == True:
    print('Ciclo Solar de Schwabe, conhecido popularmente apenas como ciclo solar, é o ciclo com uma série de fenômenos determinados do Sol.')
    time.sleep(4)
    print('Foram contabilizados, até a atualidade, 25 deles.')
    time.sleep(2)
    print('Sobre qual deles você deseja mais informações?')
    ciclo = int(input('Insira um número de 1 a 25: '))
    print(funcao_7(ciclo))
elif resposta_8 == False:
    print('\nOkay...')

time.sleep(3)
print('Foi um prazer te informar sobre manchas solares.')
print('\n')
print('Caso deseje alguma nova infomação, reinicie o programa.')
print('\n')
print('Até mais!')