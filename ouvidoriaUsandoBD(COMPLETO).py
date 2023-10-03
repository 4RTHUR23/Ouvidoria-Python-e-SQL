from operacoesBD import *

conn = abrirBancoDados("127.0.0.1", "root", "011198", "ouvidoria_final")

opcao = 0

while opcao != 5:
    print()
    print("----- Sistema de Ouvidoria -----")
    print("\n1) Listar Ocorrências\n2) Cadastrar Ocorrência\n3) Alterar Ocorrência\n4) Excluir Ocorrência\n5) Sair\n")
    print("--------------------------------")
    opcao = int(input("-Qual das opções você deseja realizar? "))
    print()

    sqlconsulta = "select codigo, ocorrencia from ocorrencias"
    sqlListagem = listarBancoDados(conn, sqlconsulta)

    if opcao == 1:
        if len(sqlListagem) == 0:
            print("-Sem ocorrências, adicione uma primeiro")
        else:
            print("-Lista de ocorrências:")
            for ocorrencia in sqlListagem:
                print("-", ocorrencia[1])

    elif opcao == 2:
        novaOcorrencia = input("-Digite a ocorrência: ")
        if len(novaOcorrencia) > 0:
            sqlInsert = "insert into ocorrencias (ocorrencia) values (%s)"
            dados = [novaOcorrencia]
            metodoInsert = insertNoBancoDados(conn, sqlInsert, dados)
            print("--------------------------------")
            print("-Ocorrência adicionada com sucesso!")
        else:
            print("-Nenhuma ocorrência informada")

    elif opcao == 3:
        if len(sqlListagem) == 0:
            print("-Sem ocorrências, adicione uma usando a Opção 2")
        else:
            print("-As ocorrências cadastradas no sistema são:\n")
            for codigo, ocorrencia in sqlListagem:
                print("-Código", codigo, "corresponde a ocorrência: ", ocorrencia)

            print("-----------------------------------------------------")
            codigoAlterar = input("-Digite o código da ocorrência que você quer alterar: ")
            ocorrenciaUpdate = input("-Digite a ocorrência atualizada: ")
            sqlUpdate = "update ocorrencias set ocorrencia = %s where codigo = %s"
            dados = [ocorrenciaUpdate, codigoAlterar]
            metodoUpdate = atualizarBancoDados(conn, sqlUpdate, dados)
            print("-Mensagem alterada com sucesso!")

    elif opcao == 4:
        print("-As ocorrências cadastradas no sistema são:\n")
        for codigo, ocorrencia in sqlListagem:
            print("-Código", codigo, "corresponde a ocorrência: ", ocorrencia)

        print("--------------------------------------------")
        codigoPesquisado = int(input("-Digite o código da ocorrência para remover: "))
        sqldelete = "delete from ocorrencias where codigo = %s"
        dados = [codigoPesquisado]
        metodoDelete = excluirBancoDados(conn, sqldelete, dados)
        print("\n-Ocorrência removida com sucesso!")

    elif opcao != 5:
        print("-Opção Inválida. Escolha uma opção válida.")

encerrarBancoDados(conn)
print("------ Programa Encerrado ------\n")
