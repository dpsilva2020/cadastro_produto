

def opcoes():
    if opcoes_entrada==1:
        data_produto=input('Data de Cadastro: ')
        tipo_produto=input('Tipo de Produto: ')
        marca=input('Marca: ')
        modelo=input('Modelo: ')
        cor=input('Cor: ')
        produto_nome=tipo_produto+' '+marca+' '+modelo+' '+cor
        nome_produto=input(f'{produto_nome} ')        
        valor_custo=float(input('Valor de Custo: '))
        valor_venda=float(input('Valor Venda: '))
        lucro_venda=valor_venda-valor_custo
        margem_de_lucro=((lucro_venda/valor_venda)*100)
        print('-'*30)
        print('FICHA DE PRODUTO')
        print('-'*30)
        print(f'Data:{data_produto} \n Marca: {marca} \n Modelo: {modelo} \n Nome do Produto: {nome_produto} \n Tipo Produto: {tipo_produto} \n Valor Custo: {valor_custo} \n Valor Venda: {valor_venda} \n Margem de Lucro: {lucro_venda}\n Margem de Lucro: {margem_de_lucro}')
        gravar=int(input('Deseja Gravar esse produto? \n 1-Sim ou 2-Não \n Resposta: '))
        if gravar==1:
            import sqlite3
            banco= sqlite3.connect('sistema.db')
            cursor=banco.cursor()
            cursor.execute(F"INSERT INTO PRD_PRODUTO (DATA_PRODUTO,MARCA,MODELO,NOME_PRODUTO,TIPO_PRODUTO,VALOR_CUSTO,VALOR_VENDA) VALUES  ('{data_produto}','{marca}','{modelo}','{produto_nome}','{tipo_produto}','{valor_custo}','{valor_venda}')") 
            banco.commit()
            print('Produto cadastrado!')
        else:
            print('O produto não foi cadastrado.')
            
    elif opcoes_entrada==2:
        import sqlite3
        banco= sqlite3.connect('sistema.db')
        cursor=banco.cursor()
        cursor.execute("SELECT * FROM PRD_PRODUTO")
        print(cursor.fetchall())
        item_alterar=int(input('Informar o cd_produto desejado para alteração: '))
        tipo_alteracao=input("informe a o nome da coluna='o que deseja alterar'")
        cursor.execute(F"UPDATE PRD_PRODUTO SET {tipo_alteracao} WHERE CD_PRODUTO='{item_alterar}' ")
        banco.commit()
        cursor.execute("SELECT * FROM PRD_PRODUTO")
        print(cursor.fetchall())
        print('Produto Alterado!')
    elif opcoes_entrada==3:
        import sqlite3
        banco= sqlite3.connect('sistema.db')
        cursor=banco.cursor()
        cursor.execute("SELECT * FROM PRD_PRODUTO")
        print(cursor.fetchall())
        cd_prd_deletar=int(input('Informe o cd_produto que será deletado: '))
        cursor.execute(f"DELETE FROM PRD_PRODUTO WHERE CD_PRODUTO='{cd_prd_deletar}'")
        banco.commit()
        print(f'O produto {cd_prd_deletar} foi deletado!')
    elif opcoes_entrada==4:
        print('-'*30)
        print('MOVIMENTAÇÕES DE ESTOQUE')
        print('-'*30)
        estoque_opcoes=int(input('1-Entrada \n 2-Saida \n 3-Consultar'))
        if estoque_opcoes==1:
                import sqlite3
                banco= sqlite3.connect('sistema.db')
                cursor=banco.cursor()
                cd_produto=int(input('Codigo do produto: '))
                cursor.execute(f"SELECT * FROM PRD_PRODUTO WHERE CD_PRODUTO={cd_produto}")
                print(cursor.fetchall())
                dt_mov=input('Data de Movimentação: ')
                qtde_produto=int(input('Quantidade Entrada: '))
                cursor.execute(f"INSERT INTO PRD_ESTOQUE (CD_PRODUTO,QUANTIDADE,TIPO,DT_MOV) VALUES ('{cd_produto}','{qtde_produto}','E','{dt_mov}')")
                banco.commit()
                print(f'Foram adicionados {qtde_produto} do produto {cd_produto}')
        elif estoque_opcoes==2:
                import sqlite3
                banco= sqlite3.connect('sistema.db')
                cursor=banco.cursor()
                cd_produto=int(input('Codigo do produto: '))
                cursor.execute(f"SELECT * FROM PRD_ESTOQUE WHERE CD_PRODUTO={cd_produto}")
                print(cursor.fetchall())
                dt_mov=input('Data de Movimentação: ')
                qtde_produto=int(input('Quantidade saida: '))
                qtde_produto_saida=qtde_produto*-1
                cursor.execute(f"INSERT INTO PRD_ESTOQUE (CD_PRODUTO,QUANTIDADE,TIPO,DT_MOV) VALUES ('{cd_produto}','{qtde_produto_saida}','S','{dt_mov}')")
                banco.commit()
                print(f'Foram RETIRADOS {qtde_produto} do produto {cd_produto}')
        elif estoque_opcoes==3:
                import sqlite3
                banco= sqlite3.connect('sistema.db')
                cursor=banco.cursor()
                cd_produto=int(input('Codigo do produto: '))
                cursor.execute(f"SELECT E.CD_PRODUTO AS CODIGO,P.NOME_PRODUTO,SUM(E.QUANTIDADE) AS SALDO,MAX(E.DT_MOV) AS DATA_MOVIMENTACOES FROM PRD_ESTOQUE E LEFT JOIN PRD_PRODUTO P ON E.CD_PRODUTO=P.CD_PRODUTO WHERE E.CD_PRODUTO={cd_produto}")
                print(cursor.fetchall())
        else:
            print('-'*50)
            print('FIM')
            print('-'*50)
    else:
        print('Nenhuma Opção foi selecionada!')


opcoes_entrada=int(input('O que deseja fazer? \n 1-Cadastrar um produto \n 2-Alterar um Cadastro \n 3-Excluir um cadastro\n 4-Estoque \n Resposta:   '))
opcoes()
opcoes_entrada=int(input('O que deseja fazer? \n 1-Cadastrar um produto \n 2-Alterar um Cadastro \n 3-Excluir um cadastro\n 4-Estoque \n Resposta:   '))
opcoes()
