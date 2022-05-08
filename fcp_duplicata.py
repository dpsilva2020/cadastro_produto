#CONTAS A  PAGAR 


def cadastro_duplicata():
    dupli_numero=int(input("Numero da duplicata: "))
    cd_pessoa=int(input("Fornecedor: "))
    dt_emissao=input("Data Emissao: ")
    dt_vecimento_original=input("Data Vencimento: ")
    dt_vencimento=dt_vecimento_original
    dupli_valor=float(input("Valor: "))
    dupli_desconto=float(input("Desconto: "))
    dupli_juros=float(input("Juros: "))
    dupli_obs=input("obs: ")
    dupli_valor_liquido=dupli_valor+dupli_juros-dupli_desconto
    print(f"Duplicata:{dupli_numero}\nFornecedor:{cd_pessoa}\nData Emissao:{dt_emissao}\nData Vencimento Original:{dt_vecimento_original} \n Data Vencimento{dt_vencimento} \nValor:{dupli_valor}")
    cod_dupli=int(input("Gravar Duplicata: 1-Sim ou 2-Não:"))
    if cod_dupli==1:
        import sqlite3
        banco= sqlite3.connect('sistema.db')
        cursor=banco.cursor()
        cursor.execute(f"INSERT INTO FCP_DUPLICATA (DUPLICATA,CD_FORNECEDOR,DT_EMISSAO,DT_VECTO_ORIGINAL,DT_VENCTO,OBS,DUP_VALOR,DUP_DESCONTO,DUP_JUROS,DUP_VALOR_LIQ,DUP_VL_PAGO) VALUES ('{dupli_numero}','{cd_pessoa}','{dt_emissao}','{dt_vecimento_original}','{dt_vencimento}','{dupli_obs}','{dupli_valor}','{dupli_desconto}','{dupli_juros}','{dupli_valor_liquido}','0')")
        banco.commit()
    else:
            print("Saindo...")

def alterar_duplicata():
    dupli_numero=int(input("Numero Duplicata: "))
    import sqlite3
    banco= sqlite3.connect('sistema.db')
    cursor=banco.cursor()
    cursor.execute(f"SELECT * FROM FCP_DUPLICATA WHERE NDUPLI={dupli_numero}")
    print(cursor.fetchall)
    dt_vencimento=("Data Vencimento: ")
    cursor=banco.cursor()
    cursor.execute(f"UPDATE FCP_DUPLICATA SET DT_VENCTO={dt_vencimento} WHERE NDUPLI={dupli_numero}")


def baixar_duplicata():
    dupli_numero=int(input("NUMERO DA DUPLICATA: "))
    import sqlite3
    banco= sqlite3.connect('sistema.db')
    cursor=banco.cursor()
    cursor.execute(f"SELECT * FROM FCP_DUPLICATA WHERE NDUPLI={dupli_numero}")
    print(cursor.fetchall)
    duplicata=cursor.execute(f"SELECT duplicata FROM FCP_DUPLICATA WHERE NDUPLI={dupli_numero}")
    cd_fornecedor=cursor.execute(f"SELECT cd_fornecedor FROM FCP_DUPLICATA WHERE NDUPLI={dupli_numero}")
    dt_pagamento=input("DATA PAGAMENTO: ")
    vl_baixar=float(input('VALOR PAGO: '))
    import sqlite3
    banco= sqlite3.connect('sistema.db')
    cursor=banco.cursor()
    cursor.execute(f"UPDATE FCP_DUPLICATA SET DUP_VL_PAGO={vl_baixar} WHERE NDUPLI={dupli_numero}")
    cursor.execute(f"INSERT INTO FCP_DUPLICATA_PGTO (NDUPLI,DUPLICATA,DT_PAGAMENTO,CD_FORNECEDOR,VL_PAGO) VALUES ('{dupli_numero}','{duplicata}','{dt_pagamento}','{cd_fornecedor}','{vl_baixar}')")
    banco.commit()




