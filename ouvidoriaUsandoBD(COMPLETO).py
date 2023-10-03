from operacoesBD import *

conn = abrirBancoDados("127.0.0.1", "root", "011198", "ouvidoria_final")

opcao = 0

while opcao != 5:
    menu()
    opcao = int(input("-Qual das opções você deseja realizar? "))

    sqlconsulta = "select codigo, ocorrencia from ocorrencias"
    sqlListagem = listarBancoDados(conn, sqlconsulta)

    if opcao == 1:
        listagem(sqlListagem)

    elif opcao == 2:
        ocorrenciadigitada = input("-Digite sua ocorrência: ")
        nova_ocorrencia = ocorrenciadigitada
        cadastro(conn, nova_ocorrencia)

    elif opcao == 3:
        listagemIndice(sqlListagem)
        codigoAlterar = input("-Digite o código da ocorrência que você quer alterar: ")
        ocorrenciaUpdate = input("-Digite a ocorrência atualizada: ")
        update(conn, ocorrenciaUpdate, codigoAlterar)

    elif opcao == 4:
        listagemIndice(sqlListagem)
        codigoPesquisado = int(input("-Digite o código da ocorrência para remover: "))
        delete(conn, codigoPesquisado)

    elif opcao != 5:
        print("-Opção Inválida. Escolha uma opção válida.")

encerrarBancoDados(conn)
print("------ Programa Encerrado ------\n")
