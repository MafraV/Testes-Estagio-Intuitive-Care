ALTER TABLE "Despesas" ALTER COLUMN "DATA" TYPE date USING ("DATA"::date);
ALTER TABLE "Despesas" ALTER COLUMN "VL_SALDO_FINAL" TYPE numeric USING replace("VL_SALDO_FINAL",',','.')::numeric;
ALTER TABLE "Despesas" ALTER COLUMN "REG_ANS" TYPE numeric USING ("REG_ANS"::numeric);
ALTER TABLE "Registro" ALTER COLUMN "Registro_ANS" TYPE numeric USING replace("Registro_ANS",'"',' ')::numeric;
