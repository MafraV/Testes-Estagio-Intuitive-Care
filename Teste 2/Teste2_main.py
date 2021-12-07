#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Victor Mafra de Holanda Ferraz
# Created Date: 07/12/2021 - 11:49
# version ='1.0'
# ---------------------------------------------------------------------------

import tabula
import Teste2_header as h

pdf_file = "LatestPadraoTiss/padrao-tiss_componente-organizacional_202111.pdf" #PDF file path

#Reads the tables that are in the pages 114 to 120, where 'Quadro 30' is in page 114, 
#'Quadro 31' goes through page 115 to page 120 and 'Quadro 32' is in page 120 
tables = tabula.read_pdf(pdf_file, pages=(114,115,116,117,118,119,120), multiple_tables=True) 

d_30 = tables[0].to_dict() #Transforms the first table of the list into a dictionary
del d_30['Tabela de Tipo do Demandante'][0] #Removes the header from the dictionary

d_32 = tables[-1].to_dict() #Transforms the last table of the list into a dictionary
del d_32['Tabela de Tipo de Solicitação'][0] #Removes the first header from the dictionary
del d_32['Tabela de Tipo de Solicitação'][1] #Removes the second header from the dictionary
del d_32['Tabela de Tipo de Solicitação'][4] #Removes a None value from the dictionary

df_30 = h.build_table_from_dict(d_30,'Tabela de Tipo do Demandante') #Calls the function that build the table of 'Quadro 30'
df_31 = h.build_table_from_tables(tables[1:-1]) #Calls the function that build the table of 'Quadro 31'
df_32 = h.build_table_from_dict(d_32,'Tabela de Tipo de Solicitação') #Calls the function that build the table of 'Quadro 32'

dfs=[df_30,df_31,df_32] #Creates a list with all the returned DataFrames
csv_paths=['CSVs/Tabela_de_tipo_do_Demandante.csv','CSVs/Tabela_de_categoria_do_Padrão_TISS.csv','CSVs/Tabela_de_tipo_de_Solicitação.csv'] #Creates a list with all the csv desired paths

#Save each DataFrame to its related path
for (df,path) in zip(dfs,csv_paths):
    h.save_csv(df,path) #Call the function that saves the DataFrame as a CSV file at the desired path

h.zip_csvs('ZIP/Teste_{Victor Mafra de Holanda Ferraz}.zip', csv_paths) #Calls the function that zip the CSVs files to a desired path