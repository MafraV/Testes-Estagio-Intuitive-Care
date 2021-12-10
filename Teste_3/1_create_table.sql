CREATE TABLE public."Despesas"
(
    "DATA" text COLLATE pg_catalog."default", 
    "REG_ANS" text COLLATE pg_catalog."default",
    "CD_CONTA_CONTABIL" text COLLATE pg_catalog."default",
    "DESCRICAO" text COLLATE pg_catalog."default", 
    "VL_SALDO_FINAL" text COLLATE pg_catalog."default"
);

CREATE TABLE public."Registro"
(
    "Registro_ANS" text NOT NULL,
    "CNPJ" text COLLATE pg_catalog."default",
    "Razao_Social" text COLLATE pg_catalog."default",
    "Nome_Fantasia" text COLLATE pg_catalog."default",
    "Modalidade" text COLLATE pg_catalog."default",
    "Logradouro" text COLLATE pg_catalog."default",
    "Numero" text COLLATE pg_catalog."default",
    "Complemento" text COLLATE pg_catalog."default",
    "Bairro" text COLLATE pg_catalog."default",
    "Cidade" text COLLATE pg_catalog."default",
    "UF" text COLLATE pg_catalog."default",
    "CEP" text COLLATE pg_catalog."default",
    "DDD" text COLLATE pg_catalog."default",
    "Telefone" text COLLATE pg_catalog."default",
    "Fax" text COLLATE pg_catalog."default",
    "Endereco_eletronico" text COLLATE pg_catalog."default",
    "Representante" text COLLATE pg_catalog."default",
    "Cargo_Representante" text COLLATE pg_catalog."default",
    "Regiao_de_Comercializacao" text COLLATE pg_catalog."default",
    "Data_Registro_ANS" text COLLATE pg_catalog."default",
    CONSTRAINT "Registro_ANS" PRIMARY KEY ("Registro_ANS")
);
