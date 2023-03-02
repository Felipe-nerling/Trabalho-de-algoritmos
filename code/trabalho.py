class compromisso:
    data = None
    hora = None
    duracao = None
    descricao = None

#Funções
def incluir():
    while 1:
        x = compromisso()
        x.data = input("Data: ")
        x.hora = input("Hora: ")
        if x.data in agenda and x.hora in agenda: #Verifica se existem outros compromissos na mesma data e horario
            op = input("\nJá existem compromissos marcados para a data e horário informados. Salvar mesmo assim?\n(1)Sim\n(2)Não\n")
            if op == 1:
                continue
            elif op == 2:
                pass
            else:
                print("ERRO: Opção inválida.")
                break
        x.duracao = input("Duração: ")
        x.descricao = input("Descrição: ")            
        agenda.append(x)
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

agenda = []#Vetor que armazena os compromissos