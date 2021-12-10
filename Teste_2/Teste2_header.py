#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Victor Mafra de Holanda Ferraz
# Created Date: 07/12/2021 - 10:49
# version ='1.0'
# ---------------------------------------------------------------------------

import pandas as pd
from zipfile import ZipFile

#Function that builds a structured pandas DataFrame from a dictionary receiving the disctionary and the key to the data as parameters
def build_table_from_dict(d,key):
    code, desc = [], []

    #Save each value from the discionary at two separated lists, that represents the two columns of the final DataFrame
    for value in d[key].values():
        splitted = value.split() #Split the value into two separeted strings, because the intire row came merged into a single string
        code.append(splitted[0]) #Save the 'Código' value at the code list
        desc.append(splitted[1]) #Save the 'Descrição da categoria' value at the disc list

    final_d = {'Código': code, #Creates a structures disctionary with the separated lists
               'Descrição da categoria': desc}

    df = pd.DataFrame(final_d, columns=['Código', 'Descrição da categoria']) #Create the DataFrame from the structured dictionary

    return df

#Function that builds a structured pandas DataFrame from a list of DataFrame objects
def build_table_from_tables(tables):
    code, desc = [], []

    d = tables[0].to_dict() #Transform the first table of the list into a dictionary

    #Save each value from the two discionaries at two separated lists, that represents the two columns of the final DataFrame
    for (value1,value2) in zip(d['Tabela de Categoria do Padrão TISS'].values(),d['Unnamed: 0'].values()):
        desc.append(value1) #Save the 'Código' value at the code list
        code.append(value2) #Save the 'Descrição da categoria' value at the disc list
        
    del desc[0] #Remove the header of the table from the desc list
    del code[0] #Remove the header of the table from the code list

    #Save the values from all the remaining tables into the two lists
    for table in tables[1:]:
        d = table.to_dict() #Transform the table into a dictionary
        header = list(d.keys()) #Get the header of the table
        code.append(int(header[0])) #Save the header to the two lists because the 'Quadro 31' goes through many pages, 
        desc.append(header[1])      #so each page was considered a separated table and the first row was considered the header
        #Save each value from the first dictionary to the code list
        for value in table[header[0]]:
            code.append(value)
        #Save each value from the second dictionary to the disc list
        for value in table[header[1]]:
            if '\r' in value: #Checks if there are line break at the string
                value = value.replace('\r', ' ') #Replace the line brack special characters to a blank space
            desc.append(value)

    final_d = {'Código': code, #Creates a structures disctionary with the separated lists
               'Descrição da categoria': desc}

    df = pd.DataFrame(final_d,columns=['Código', 'Descrição da categoria']) #Create the DataFrame from the structured dictionary

    return df

#Function that saves the pandas DataFrame into a CSV file at the desired path
def save_csv(df, path):
    df.to_csv(path)
    print('CSV successfully saved at path: '+path)

#Function that compress the CSVs files into a ZIP file at the desired path
def zip_csvs(zip_path, csv_path):
    zip = ZipFile(zip_path,'w')
    for path in csv_path:
        zip.write(path)
    zip.close()
    print('CSVs successfully zipped at path: '+zip_path)
