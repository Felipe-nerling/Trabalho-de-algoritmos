class compromisso:
    data = None
    hora = None
    duracao = None
    descricao = None

#Funções
def incluir():
    while 1:
        print("--INCLUIR COMPROMISSO--")
        c = compromisso()
        c.data = input("\nData: ")
        c.hora = input("Hora: ")
        c.duracao = input("Duração: ")
        c.descricao = input("Descrição: ")
        cont = 0
        for i in range(len(agenda)):
            if c.data in agenda[i].data and c.hora in agenda[i].hora:
                cont = cont+1
            else:
                continue
        if cont > 0:
            opc = int(input("\nJá existem compromissos marcados para a data e horário informados. Salvar mesmo assim?\n(1)Sim\n(2)Não\n"))
            if opc == 1:
                agenda.append(c)
            elif opc == 2:
                pass
            else:
                print("\nERRO: Opção inválida.")
        else:
            agenda.append(c)
        opt = int(input("\nIncluir outro compromisso?\n(1)Sim\n(2)Não\n"))
        if opt == 1:
            continue
        elif opt == 2:
            break
        else:
            print("\nERRO: Opção inválida.")
            break

def consultardata():
    while 1:
        print("--CONSULTAR POR DATA--")
        dt = input("\nDigite a data a ser consultada:\n")
        cont = 0
        for i in range(len(agenda)):
            if agenda[i].data == dt:
                print("Descrição: ", agenda[i].descricao, "\tHorário: ", agenda[i].hora, "\tDuração: ", agenda[i].duracao)
                cont = 1
            else:
                if i == (len(agenda))-1 and cont == 0:
                    print("Agenda Vazia!")
        opt = int(input("\nConsultar outra data?\n(1)Sim\n(2)Não\n"))
        if opt == 1:
            continue
        elif opt == 2:
            break
        else:
            print("\nERRO:Opção inválida.")
            break

def consultardh():
    while 1:
        print("--CONSULTAR POR DATA E HORA--")
        dt = input("\nDigite a data a ser consultada:\n")
        hr = input("\nDigite a hora a ser consultada:\n")
        cont = 0
        for i in range(len(agenda)):
            if agenda[i].data == dt and agenda[i].hora == hr:
                print("Descrição: ", agenda[i].descricao, "\tHorário: ", agenda[i].hora, "\tDuração: ", agenda[i].duracao)
                cont = 1
            else:
                if i == (len(agenda))-1 and cont == 0:
                    print("Agenda Vazia!")
        opt = int(input("\nConsultar outra data?\n(1)Sim\n(2)Não\n"))
        if opt == 1:
            continue
        elif opt == 2:
            break
        else:
            print("\nERRO: Opção inválida.")
            break

def alterar():
    while 1:
        print("--ALTERAR COMPROMISSOS--")
        dt = input("\nDigite a data do compromisso:\n")
        hr = input("\nDigite a hora do compromisso:\n")
        ind = []
        for i in range(len(agenda)):
            if agenda[i].data == dt and agenda[i].hora == hr:
                print("Descrição: ", agenda[i].descricao, "\tHorário: ", agenda[i].hora, "\tDuração: ", agenda[i].duracao)
                ind.append(i)
            else:
                if i == (len(agenda))-1 and len(ind) == 0:
                    print("Compromisso não encontrado!")
        if len(ind) == 1:
            agenda[ind[0]].descricao = input("\nDigite a nova descrição:\n")
            agenda[ind[0]].duracao = input("\nDigite a nova duração:\n")
        elif len(ind) > 1:
            x = input("\nExistem 2 ou mais compromissos agendados nesse horário.\nDigite a descrição do compromisso a ser alterado:\n")
            for i in range(len(ind)):
                if agenda[ind[i]].descricao == x:
                    agenda[ind[i]].descricao = input("\nDigite a nova descrição:\n")
                    agenda[ind[i]].duracao = input("\nDigite a nova duração:\n")
                    break
                elif i == (len(ind))-1:
                    print("\nERRO: Descrição não encontrada")
        opt = int(input("\nAlterar outro compromisso?\n(1)Sim\n(2)Não\n"))
        if opt == 1:
            continue
        elif opt == 2:
            break
        else:
            print("\nERRO: Opção inválida.")
            break

def excluir():
    while 1:
        print("--EXCLUIR COMPROMISSOS--")
        dt = input("\nDigite a data do compromisso:\n")
        hr = input("\nDigite a hora do compromisso:\n")
        ind = []
        for i in range(len(agenda)):
            if agenda[i].data == dt and agenda[i].hora == hr:
                print("Descrição: ", agenda[i].descricao, "\tHorário: ", agenda[i].hora, "\tDuração: ", agenda[i].duracao)
                ind.append(i)
            else:
                if i == (len(agenda))-1 and len(ind) == 0:
                    print("Compromisso não encontrado!")
        if len(ind) == 1:
            agenda.pop(ind[0])
            print("\nCompromisso removido com sucesso!")
        elif len(ind) > 1:
            x = input("\nExistem 2 ou mais compromissos agendados nesse horário.\nDigite a descrição do compromisso a ser excluído:\n")
            for i in range(len(ind)):
                if agenda[ind[i]].descricao == x:
                    agenda.pop(ind[i])
                    print("\nCompromisso removido com sucesso!")
                    break
                elif i == (len(ind))-1:
                    print("\nERRO: Descrição não encontrada")
        opt = int(input("\nExcluir outro compromisso?\n(1)Sim\n(2)Não\n"))
        if opt == 1:
            continue
        elif opt == 2:
            break
        else:
            print("\nERRO: Opção inválida.")
            break
    
#def listar():

agenda = []#Vetor que armazena os compromissos

while 1:
    op = int(input("\nAgenda de compromissos\nSelecione uma opção:\n(1)Incluir\n(2)Consultar\n(3)Alterar\n(4)Excluir\n(5)Listar todos\n(6)Sair\n"))
    if op == 1:
        incluir()
    elif op == 2:
        op2 = int(input("\nConsultar agenda:\n(1)Por data\n(2)Por data e hora\n"))
        if op2 == 1:
            consultardata()
        elif op2 == 2:
            consultardh()
        else:
            print("\nERRO: Opção inválida.")
    elif op == 3:
        alterar()
    elif op == 4:
        excluir()
    else:
        break