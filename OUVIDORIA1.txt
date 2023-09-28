from operacoesbd import *

conn = abrirBancoDados("127.0.0.1", "root", "011198", "ouvidoriabd")

opcao = 0
ocorrencias = []

while opcao != 5:
    print("----- Sistema de Ouvidoria -----")
    print("1) Listar Ocorrências")
    print("2) Cadastrar Ocorrência")
    print("3) Pesquisar Ocorrência por Código")
    print("4) Excluir Ocorrência")
    print("5) Sair")
    print("--------------------------------")
    opcao = int(input("-Quais das opções você deseja realizar? "))
    print("--------------------------------")

    resultadoConsulta = "select ocorrencia from ouvidoria"
    ocorrencias = listarBancoDados(conn, resultadoConsulta)

    if opcao == 1:
        if len(ocorrencias) > 0:
            print("-Ocorrências Cadastradas no Sistema:")
            for o in ocorrencias:
                print("-", o[0])
        else:
            print("-Nenhuma ocorrência cadastrada ainda")
    elif opcao == 2:

        novaOcorrencia = input("Digite sua ocorrência: ")
        sqlinsertBD = "insert into ouvidoria (ocorrencia) values (%s)"
        dados = [novaOcorrencia]
        insertNoBancoDados(conn, sqlinsertBD, dados)
        if len(novaOcorrencia) > 0:
            print("-Ocorrência cadastrada com sucesso!")
        else:
            print("-Inválido, cadastre uma ocorrência válida")

    elif opcao == 3:
        if len(ocorrencias) > 0:
            codigoPesquisa = input("-Digite o código da ocorrência para pesquisa: ")
            sqlPesquisa = "select * from ouvidoria where codigo = " + codigoPesquisa
            codigoPesquisado = listarBancoDados(conn, sqlPesquisa)
            print("-A ocorrência pesquisada foi: ")
            for i in codigoPesquisado:
                print("Código", i[0], "corresponde a ocorrência:", i[1])
        else:
            print("-Nenhuma ocorrência cadastrada ainda")
    elif opcao == 4:
        if len(ocorrencias) > 0:
            codigoDigitado = int(input("-Digite o código da ocorrencia para exclusao: "))
            sqlDelBD = "Delete from ouvidoria where codigo = (%s)"
            delete = [codigoDigitado]
            exclusaoOcorrencia = excluirBancoDados(conn, sqlDelBD, delete)
        else:
            print("-Nenhuma ocorrência cadastrada ainda")
    elif opcao != 5:
        print("Opção Inválida")
encerrarBancoDados(conn)
print()
print("-----Programa Encerrado-----")
print()
