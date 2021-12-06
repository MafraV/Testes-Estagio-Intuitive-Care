#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Victor Mafra de Holanda Ferraz
# Created Date: 06/12/2021 - 16:12
# version ='1.0'
# ---------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup

#Function that finds a specific link in a html page using two sub-strings that are present in the target url as parameters
def find_link(url, condition1, condition2):
    read = requests.get(url) #Reads the url
    html_content = read.content #Gets the content from the html page
    soup = BeautifulSoup(html_content, "html.parser") #Creates a BeautifulSoup object with the html content
    l = soup.find_all('a') #Finds all the <a> tags in the html page code
    for link in l: #Goes through all the <a> tags found previously
        new_link = link.get('href') #Gets only the link that is inside the current <a> tag
        if (condition1 in new_link) and (condition2 in new_link): #Tests if the condition1 and condition2 sub-strings are present in the current link
            return new_link #Returns the target url

#Function that downloads a pdf file from a url page
def download_pdf(url, path):
    response = requests.get(url) #Reads the url
    with open(path, 'wb') as f: #Open the PDF file
        done = f.write(response.content) #Write the content of the PDF to the path
        if done: print('PDF downloaded with success!') #If the PDF is successfully downloaded, prints a message to inform it
        else: print('PDF download failed!') #Else, prints a message to inform that the download have failed