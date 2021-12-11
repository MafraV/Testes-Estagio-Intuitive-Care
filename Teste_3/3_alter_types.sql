ALTER TABLE "Despesas" ALTER COLUMN "DATA" TYPE date USING ("DATA"::date); /*Changes the "DATA" column from the "Despesas" table to date type*/
ALTER TABLE "Despesas" ALTER COLUMN "VL_SALDO_FINAL" TYPE numeric USING replace("VL_SALDO_FINAL",',','.')::numeric; /*Changes the "VL_SALDO_FINAL" column from the "Despesas" table to numeric type*/
ALTER TABLE "Despesas" ALTER COLUMN "REG_ANS" TYPE numeric USING ("REG_ANS"::numeric); /*Changes the "REG_ANS" column from the "Despesas" table to numeric type*/
ALTER TABLE "Registro" ALTER COLUMN "Registro_ANS" TYPE numeric USING replace("Registro_ANS",'"',' ')::numeric; /*Changes the "Registro_ANS" column from the "Registro" table to numeric type*/
