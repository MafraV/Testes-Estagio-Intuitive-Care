#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Victor Mafra de Holanda Ferraz
# Created Date: 06/12/2021 - 17:02
# version ='1.0'
# ---------------------------------------------------------------------------

import Teste1_header as h #Imports the functions from the Teste1_header python file

url = "https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss" #url given in the task

tiss_page_url = h.find_link(url, 'tiss', '2021') #Finds the link to the latest 'Padrão Tiss' page using 'tiss' and '2021' as parameters

pdf_url = h.find_link(tiss_page_url, 'tiss', '.pdf') #Finds the link to the 'Componente Organizacional' PDF file using 'tiss' and '.pdf' aas parameters

h.download_pdf(pdf_url, 'LatestPadraoTiss/padrao-tiss_componente-organizacional_202111.pdf') #Downloads the PDF to the LatestPadraoTiss folder