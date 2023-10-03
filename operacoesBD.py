import mysql.connector

def abrirBancoDados(endereco,usuario, senha, bancodedados):
      return mysql.connector.connect(
  host=endereco,user=usuario, password=senha,database=bancodedados)

def encerrarBancoDados(connection):
      connection.close()

def insertNoBancoDados(connection,sql,dados):
      cursor = connection.cursor()
      cursor.execute(sql, dados)
      connection.commit()
      id = cursor.lastrowid
      cursor.close()
      return id

def listarBancoDados(connection,sql):
      cursor = connection.cursor()
      cursor.execute(sql)
      results = cursor.fetchall()
      cursor.close()
      return results

def atualizarBancoDados(connection,sql, dados):
      cursor = connection.cursor()
      cursor.execute(sql, dados)
      connection.commit()
      linhasAfetadas = cursor.rowcount
      cursor.close()
      return linhasAfetadas

def excluirBancoDados(connection,sql,dados):
      cursor = connection.cursor()
      cursor.execute(sql, dados)
      connection.commit()
      linhasAfetadas = cursor.rowcount
      cursor.close()
      return linhasAfetadas

def menu():
    print()
    print("----- Sistema de Ouvidoria -----")
    print("\n1) Listar Ocorrências\n2) Cadastrar Ocorrência\n3) Alterar Ocorrência\n4) Excluir Ocorrência\n5) Sair\n")
    print("--------------------------------")
    print()

def cadastro(conn, novaOcorrencia):
    if novaOcorrencia:
        sqlInsert = "INSERT INTO ocorrencias (ocorrencia) VALUES (%s)"
        dados = [novaOcorrencia]
        if insertNoBancoDados(conn, sqlInsert, dados):
            print("--------------------------------")
            print("- Ocorrência adicionada com sucesso!")
        else:
            print("- Erro ao adicionar ocorrência no banco de dados")
    else:
        print("- Nenhuma ocorrência informada")

def listagem(sqlListagem):
    if len(sqlListagem) == 0:
        print("-Sem ocorrências, adicione uma primeiro")
    else:
        print("-Lista de ocorrências:")
        for ocorrencia in sqlListagem:
            print("-", ocorrencia[1])

def listagemIndice(sqlListagem):
    if len(sqlListagem) == 0:
        print("-Sem ocorrências, adicione uma usando a Opção 2")
    else:
        print("-As ocorrências cadastradas no sistema são:\n")
        for codigo, ocorrencia in sqlListagem:
            print("-Código", codigo, "corresponde a ocorrência: ", ocorrencia)

def update(conn, ocorrenciaUpdate, codigoAlterar):
    print("-----------------------------------------------------")
    sqlUpdate = "update ocorrencias set ocorrencia = %s where codigo = %s"
    dados = [ocorrenciaUpdate, codigoAlterar]
    metodoUpdate = atualizarBancoDados(conn, sqlUpdate, dados)
    print("-Mensagem alterada com sucesso!")

def delete(conn, codigoPesquisado):
    print("--------------------------------------------")
    sqldelete = "delete from ocorrencias where codigo = %s"
    dados = [codigoPesquisado]
    metodoDelete = excluirBancoDados(conn, sqldelete, dados)
    print("\n-Ocorrência removida com sucesso!")