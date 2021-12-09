SELECT "Despesas"."REG_ANS", "Registro"."Razao_Social", SUM("Despesas"."VL_SALDO_FINAL") as despesa_total_2020
	FROM "Despesas"
	JOIN "Registro"
		ON "Despesas"."REG_ANS" = "Registro"."Registro_ANS"
WHERE (("DESCRICAO" LIKE 'EVENTOS%') and ("DESCRICAO" LIKE '%HOSPITALAR '))
	AND ("DATA" BETWEEN '01/01/2020' AND '31/12/2020')
	AND ("VL_SALDO_FINAL" < 0)
GROUP BY "REG_ANS", "Razao_Social" 
ORDER BY despesa_total_2020
LIMIT 10;