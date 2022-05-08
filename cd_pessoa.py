

#funções e apis 


import requests

def consulta_rfb():
    import sqlite3

    banco= sqlite3.connect('sistema.db')

    cursor=banco.cursor()
    tipo=int(input('Qual é o tipo de pessoa: \n 1-Fisica \n 2-Juridica ? \n (Informe o numero) : '))
    cnpjcpf=input('CNPJ/CPF: ')







    if tipo==1:
        nome=input('Nome: ')
        cep=input('CEP: ')
        url_cep=f'https://viacep.com.br/ws/{cep}/json/'
        cep_api=requests.get(url_cep)
        resp_cep_api=cep_api.json()
        cep=resp_cep_api['cep']
        bairro=resp_cep_api['bairro']
        municipio=resp_cep_api['localidade']
        uf=resp_cep_api['uf'] 
        logradouro=resp_cep_api['logradouro'] 
        situacao=''
        bairro=bairro
        logradouro=logradouro
        numero=input('Nº: ')        
        print('Nome:{} \n CNPJ:{} \n Situação: {} Logradouro:{} \n N º: {} \n Bairro: {} \n CEP: {} \n Municipio: {} \n UF: {} '.format(nome,cnpjcpf,situacao,logradouro,numero,bairro,cep,municipio,uf))
        inserir=int(input('Deseja inserir essa Pessoa? \n 1-Sim 2-Não'))
        if inserir==1:
           cursor.execute(F"INSERT INTO PES_PESSOA (NOME,CPFCNPJ,DS_LOGRADOURO,BAIRRO,CEP,MUNICIPIO,UF,NUMERO) VALUES  ('{nome}','{cnpjcpf}','{logradouro}','{bairro}','{cep}','{municipio}','{uf}','{numero}')") 
           banco.commit()
           #cd_pessoa=cursor.execute(F"select cd_pessoa from PES_PESSOA WHERE CPFCNPJ={cnpjcpf}")
           print('Cadastro efetuado com sucesso! ')

    elif tipo==2:
        url_api_rfb=f'https://www.receitaws.com.br/v1/cnpj/{cnpjcpf}'
        requisicao=requests.get(url_api_rfb)
        resposta_requisicao=requisicao.json()
        nome=resposta_requisicao['nome']
        situacao=resposta_requisicao['situacao']
        bairro=resposta_requisicao['bairro']
        logradouro=resposta_requisicao['logradouro']
        numero=resposta_requisicao['numero'] 
        cep=resposta_requisicao['cep']
        municipio=resposta_requisicao['municipio']
        uf=resposta_requisicao['uf']
        print('Nome:{} \n CNPJ:{} \n Situação: {} Logradouro:{} \n N º: {} \n Bairro: {} \n CEP: {} \n Municipio: {} \n UF: {} '.format(nome,cnpjcpf,situacao,logradouro,numero,bairro,cep,municipio,uf))
        inserir=int(input('Deseja inserir essa Pessoa? \n 1-Sim 2-Não'))
        if inserir==1:
           cursor.execute(F"INSERT INTO PES_PESSOA (NOME,CPFCNPJ,DS_LOGRADOURO,BAIRRO,CEP,MUNICIPIO,UF,NUMERO) VALUES  ('{nome}','{cnpjcpf}','{logradouro}','{bairro}','{cep}','{municipio}','{uf}','{numero}')") 
           banco.commit()
           
           print('Cadastro efetuado com sucesso! ')

        else:
            print('Não foi realizado a gravação dos dados')





#variaveis
 
    



