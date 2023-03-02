class compromisso:
    data = None
    hora = None
    duracao = None
    descricao = None

agenda = []#Vetor que armazena os compromissos

#Funções
def incluir():
    while 1:
        print(agenda)
        c = compromisso()
        c.data = input("\nData: ")
        c.hora = input("Hora: ")
        c.duracao = input("Duração: ")
        c.descricao = input("Descrição: ")
        for i in range(len(agenda)):
            if c.data in agenda[i].data and c.hora in agenda[i].hora:
                opc = int(input("\nJá existem compromissos marcados para a data e horário informados. Salvar mesmo assim?\n(1)Sim\n(2)Não\n"))
                if opc == 1:
                    agenda.append(c)
                    break
                elif opc == 2:
                    pass
                else:
                    print("ERRO: Opção inválida.")
                    break
            else:
                continue 
        opt = int(input("\nIncluir outro compromisso?\n(1)Sim\n(2)Não\n"))
        if opt == 1:
            continue
        elif opt == 2:
            break
        else:
            print("ERRO: Opção inválida.")
            break

#def consultar():
    
#def alterar():
    
#def excluir():
    
#def listar():


while 1:
    op = int(input("\nAgenda de compromissos\nSelecione uma opção:\n(1)Incluir\n(2)Consultar\n(3)Alterar\n(4)Excluir\n(5)Listar todos\n(6)Sair\n"))
    if op == 1:
        incluir()
    else:
        break