# Testes de Nivelamento - Estágio Desenvolvimento de Software - Intuitive Care
*   Este repositório foi criado para a execução de testes de nivelamento do processo seletivo "Estágio Desenvolvimento de Software", da empresa Intuitive Care.
*   Autor: Victor Mafra de Holanda Ferraz 
*   email: vmhf@ic.ufal.br 
*   links: [LinkedIn](https://www.linkedin.com/in/victor-mafra-de-holanda-ferraz-b7a813200/) [github](https://github.com/MafraV) 


## Teste 1 - WebScraping
*   Neste primeiro teste, o desafio é baixar o arquivo pdf mais atualizado (novembro de 2021) do componente organizacional do Padrão TISS no [site da ANS (Agência Nacional de Saúde)](https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss).
*   Para realizar este desafio, utilizei a linguagem de programação Python e algumas de suas bibliotecas especializadas no processo de *web scraping*.
*   Requerimentos:
    -   python >= 3.7.0
    2.   requests >= 2.25.1
    3.   bs4 (beautifulsoup4) >= 4.9.3


## Teste 2 - Transformação de dados
*   Neste segundo teste, o desafio é:
    1.   Extrair do [pdf](https://www.gov.br/ans/pt-br/arquivos/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-tiss/padrao-tiss/padrao-tiss_componente-organizacional_202111.pdf) do teste anterior os dados dos quadro 30, 31 e 32;
    2.   Salvar os dados em tabelas estruturadas, em arquivos .csv;
    3.   Por último, zipar todos os arquivos em um arquivo .zip.
*   Para a realização deste desafio, utilizei novamente a linguam de programação Python e algumas de suas bibliotecas especializadas em lidar com tabelas e arquivos .zip.
*   Requerimentos:
    1.   python >= 3.7.0
    2.   pandas >= 1.1.5
    3.   tabula-py >= 2.3.0


* Tabela estruturada do quadro 30 - Tabela de Tipo do Demandante

|    |   Código | Descrição da categoria   |
|---:|---------:|:-------------------------|
|  0 |        1 | Operadora                |
|  1 |        2 | Prestador                |
|  2 |        3 | Consumidor               |
|  3 |        4 | Gestor                   |
|  4 |        5 | ANS                      |


* Tabela estruturada do quadro 31 - Tabela de Categoria do Padrão TISS

|     |   Código | Descrição da categoria                                                                            |
|----:|---------:|:--------------------------------------------------------------------------------------------------|
|   0 |        1 | Componente Organizacional                                                                         |
|   1 |        2 | Componente de Conteúdo e Estrutura                                                                |
|   2 |        3 | Componente de Representação de Conceitos em Saúde                                                 |
|   3 |        4 | Componente de Comunicação                                                                         |
|   4 |        5 | Componente de Segurança e Privacidade                                                             |
|   5 |       18 | Terminologia de diárias, taxas e gases medicinais                                                 |
|  ... |       ... | ...                                                                                             |
| 132 |      163 | Guia de recurso de glosa odontológica                                                             |
| 133 |      164 | Guia de resumo de internação                                                                      |
| 134 |      165 | Guia de serviços profissionais/serviço auxiliar de diagnóstico e terapia                          |
| 135 |      166 | Guia de solicitação de internação                                                                 |
| 136 |      167 | Guia de solicitação de prorrogação de internação ou complementação do tratamento                  |
| 137 |      168 | Guia de tratamento odontológico                                                                   |

* Tabela estruturada do quadro 32 - Tabela de Tipo do Solicitação

|    |   Código | Descrição da categoria   |
|---:|---------:|:-------------------------|
|  0 |        1 | Alteração                |
|  1 |        2 | Inclusão                 |
|  2 |        3 | Exclusão                 |


## O Jupyter Notebook para a execução facilitada dos código dos testes 1 e 2 está presente no repositório e pode ser acessado no Google Colab através deste [link](https://colab.research.google.com/drive/1jp87mR7BkT7RuoxNjlG5sXAT8awm_yJl?usp=sharing).

## Teste 3 - Banco de Dados

*   Neste terceiro teste, o desafio é:
    1.   Baixar os arquivos referentes aos anos de 2020 e 2021 no [repositório público](http://ftp.dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/) (feito manualmente);
    2.   Baixar csv do mesmo [link](https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss) do teste 1. Porém, eu não encontrei o arquivo em questão no link fornecido, portanto, procurando no google encontrei o tal arquivo csv referente ao registro na ANS das operadoras de planos de saúde ativas neste [link](https://dados.gov.br/dataset/operadoras-de-planos-privados-de-saude);
    3.   Criar as queries para carregar o conteúdo dos arquivos obtidos anteriormente num banco MySQL ou Postgres;
    4. Montar uma query analítica que traga a resposta para a pergunta: Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre (3º trimestre de 2021)?
     5. Montar uma query analítica que traga a resposta para a pergunta: Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último ano (2020)?

*  Para a realização deste desafio, utilizei o banco de dados PostgreSQL 14.1.

* Resultado obtido com a primeira query analítica:

![Query 1 Results](https://user-images.githubusercontent.com/32077156/145493665-cfc408e6-4a71-4295-9dc2-054824b3820f.png)

* Resultado obtido com a segunda query analítica:

![Query 2 Results](https://user-images.githubusercontent.com/32077156/145493673-0cbed7dc-22aa-4ac2-aa4f-56deeea0c262.png)

