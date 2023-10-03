
def menu():
    print()
    print("----- Sistema de Ouvidoria -----")
    print("\n1) Listar Ocorrências\n2) Cadastrar Ocorrência\n3) Alterar Ocorrência\n4) Excluir Ocorrência\n5) Sair\n")
    print("--------------------------------")
    print()

def cadastro(conn, novaOcorrencia):
    if novaOcorrencia:
        sqlInsert = "insert into ocorrencias (ocorrencia) values (%s)"
        dados = [novaOcorrencia]
        if insertNoBancoDados(conn, sqlInsert, dados):
            print("--------------------------------")
            print("-Ocorrência adicionada com sucesso!")
        else:
            print("-Erro ao adicionar ocorrência no banco de dados")
    else:
        print("-Nenhuma ocorrência informada")

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
    atualizarBancoDados(conn, sqlUpdate, dados)
    print("-Mensagem alterada com sucesso!")

def delete(conn, codigoPesquisado):
    print("--------------------------------------------")
    sqldelete = "delete from ocorrencias where codigo = %s"
    dados = [codigoPesquisado]
    excluirBancoDados(conn, sqldelete, dados)
    print("\n-Ocorrência removida com sucesso!")
      
