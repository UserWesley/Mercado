#Lista de funcionario em tipo dicionario com atributos
lista_funcionario = [
    {
        "nome_funcionario" : "João",
        "idade" : "15",
        "cpf" : "12345678",
        "cargo" :"Gerente"
 
    },


    {
        "nome_funcionario" : "Pedro",
        "idade" : "29",
        "cpf" : "12345678",
        "cargo" :"Padeiro"       
    }

]
  
#Flag para executar o menu repetidas vezes
rodar_programa = True

#Metodo que verifica se o valor existe dentro do indice

def verifica_valor_indice(numero_indice):
    
    if numero_indice >=0 and numero_indice < len(lista_funcionario):
        return True
    
    return False

#Verifica entrada de usuário se é vazia
def verifica_entrada_usuario_vazia(entrada_usuario):
    if entrada_usuario == "":
        return True

    return False

#Metodo para recebido de dados do usuario
def entrada_dado_usuario_texto_para_inteiro(entrada_texto):

    try:
        entrada_valor = int(entrada_texto)
        return True, entrada_valor

 #Erro de conversão de texto para inteiro
    except ValueError:
        erro = "\nPor favor digite um número !\n\n"
        return False, erro
    

    #Erro desconhecido
    except Exception:
        erro = "\nErro desconhecido !\n\n"
        return False, erro
    
    #Função para exibir valor cadastrado
def exibir_funcionario_adicionado(nome_funcionario, idade, cpf, cargo):
    print("\n\nfuncionario cadastrado \n")
    print("Nome do funcionario cadastrado:", nome_funcionario,"\n")
    print("idade:", idade,"\n")
    print("cpf:", cpf, "\n")
    print("cargo:", cargo, "\n")


#Função para conferir entrada correta de valor do funcionario
def verifica_entrada_idade_funcionario(idade_funcionario):

    try:
        nova_idade_funcionario = int(idade_funcionario)
        print(nova_idade_funcionario)
        return True, nova_idade_funcionario

#Erro de conversão de texto para float
    except ValueError:
        erro = "\nPor favor digite um número !\n\n"
        return False, erro
    
    #Erro desconhecido
    except Exception:
        erro = "\nErro desconhecido !\n\n"
        return False, erro

#Função para adiocionar funcionario
def adcionar_funcionario(nome_funcionario, idade, cpf, cargo):
    novo_funcionario = {'nome_funcionario' : nome_funcionario, 'idade' : idade, 'cpf' : cpf, 'cargo' : cargo}
    if lista_funcionario.append(novo_funcionario):
        return False

    return True

#Função lista funcionario com enumerate
def lista_funcionario_enumerate(lista_funcionario):

    print("\n#############################\nListar funcionario",end="\n\n")

 #listando todos os funcionarios da lista
    for indice, funcionario_elemento in enumerate(lista_funcionario):
        print("Código :",indice,"\nNome do funcionario :",funcionario_elemento["nome_funcionario"], 
              "\nidade funcionario : R$", funcionario_elemento['idade'],
              "\ncpf do funcionario :", funcionario_elemento['cpf'],
              "\ncargo do funcionario:", funcionario_elemento['cargo'], "\n##############")


#Função verifica lista funcionario esta nulo ou não 
def lista_verifica_nulo(lista_funcionario):

    if not lista_funcionario:
        return True
    
    return False

#Função apagar todas elementos
def excluir_todos_elementos(lista_funcionario):
    
    #limpando a lista
    lista_funcionario.clear()

    if not lista_funcionario:
        return True
    
    return False

#Método para verficar se funcionario já existe na lista
def verifica_funcionario_lista(nome_funcionario):
    if nome_funcionario in lista_funcionario:
        return True
    return False

#Metodo para alterar valor da lista
def alterar_funcionario(codigo_funcionario, novo_nome_funcionario):
    
    lista_funcionario[codigo_funcionario] = novo_nome_funcionario
    if novo_nome_funcionario is not None:
        return True
    
    return False

#Remover funcionario
def remover_funcionario(codigo_funcionario_excluido_inteiro):
    #Adicionando indice para ajudar na removoção e evitar erros de digitação 
    #pop retorna valor tipo string Del não tem retorno
    #Produto por valor na lista e removendo
    del lista_funcionario[codigo_funcionario_excluido_inteiro]
    return True

#Função menu de funcionario
def exibir_menu_funcionario():

#lista menu funcionario

    print("#########################\n","Digite seu Escolha",end ="\n\n")
    print("1 - Cadastrar funcionario")
    print("2 - Listar funcionarios")
    print("3 - Excluir funcionario ")
    print("4 - Excluir funcionario especifico")
    print("5 - Atualizar funcionario")
    print("6 - Sair", end="\n\n")

#Executando enquanto variável for True
while rodar_programa: 


    #Chamanado método para exibir menu de funcionarios
    exibir_menu_funcionario()

    #Escolha do usuário - Observo que o retorno é tipo string
    escolha_menu = input("Digite sua escolha : ")

    #Validar entrada do usuário
    verificacao_entrada_usuario = entrada_dado_usuario_texto_para_inteiro(escolha_menu)

#Verifica entrada do usuário
    if verificacao_entrada_usuario[0]:

        #Descompactar dados
        *_, escolha_numero = verificacao_entrada_usuario

    else:
        print(verificacao_entrada_usuario[1])
        continue


        #Condição para cadastrar funcionario -- Programar para evitar itens duplicados
    if(escolha_numero == 1):

         #Recebendo do usuário o nome do funcionario
        nome_funcionario = input("Digite o nome do funcionario:")



        #Recebendo a idade do funcionario
        idade_funcionario = input("Digite a idade do funcionario:")


        #recebendo o cpf do funcionario
        cpf_funcionario = input("digite o cpf do funcionario")

        #recebendo o cargo do funcionario
        cargo_funcionario = input("digite o cargo do funcionario")

        if (verifica_entrada_usuario_vazia(nome_funcionario)) or (verifica_entrada_usuario_vazia(idade_funcionario)) or (verifica_entrada_usuario_vazia(cpf_funcionario)) or (verifica_entrada_usuario_vazia(cargo_funcionario)):
                    print("\nAlgum campo vazio! Digite um  nome de funcionario válido, idade, cpf e cargo !\n")
                    continue

        #Adicionado o nome do funcionario a lista
        if verifica_funcionario_lista(nome_funcionario):
            print("funcionario já existe !",end="\n")
            continue

        idade_valida, nova_idade = verifica_entrada_idade_funcionario(idade_funcionario)

        if not idade_valida:
            print("Nomeaclatura da idade errada !",end="\n")
            continue
                
        adcionar_funcionario(nome_funcionario, idade_funcionario, cpf_funcionario, cargo_funcionario)
        exibir_funcionario_adicionado(nome_funcionario, idade_funcionario, cargo_funcionario, cargo_funcionario)

    #COndição para lista funcionario
    elif(escolha_numero == 2):
        if lista_verifica_nulo(lista_funcionario):
            print('Lista vazia !\n')

        else:
            lista_funcionario_enumerate(lista_funcionario)

    #COndição para remover funcionario
    elif(escolha_numero == 3):

        if excluir_todos_elementos(lista_funcionario):
            print("Todos elementos excluidos")
        else:
            print("Não excluido !")

    
    #COndição para excluir funcionario selecionado
    #Verificar a duplicidade de código e como orientado a objetos ou funções ajudam 
    elif(escolha_numero == 4):

        if lista_verifica_nulo(lista_funcionario):
            print("Lista Vazia !")

        else:

            #Chamando função para exibir lista de funcionarios
            lista_funcionario_enumerate(lista_funcionario)

            print("Excluir funcionario Selecionado",end="\n\n")

            #Recebendo valor em string do código do funcionario
            codigo_funcionario_excluido = input("Digite o código do funcionario que você deseja excluir :")

            #Tentando converter tipo string para int 
            codigo_funcionario_excluido_inteiro = entrada_dado_usuario_texto_para_inteiro(codigo_funcionario_excluido)

            #Desempacotar
            resultado_dado_verificado, codigo_funcionario = codigo_funcionario_excluido_inteiro

            if resultado_dado_verificado:
                
                #Verifica se o código do funcionario recebido é maior do que a lista
                if verifica_valor_indice(codigo_funcionario):

                    if remover_funcionario(codigo_funcionario):
                        print("funcionario Excluido")
                    else :
                        print("funcionario não excluido")
                else:
                    print("Digite um código válido")
                    continue
            else:
                print(codigo_funcionario)
                continue
    #Condição para atualizar funcionario
    elif(escolha_numero == 5):

        #Verificando se a lista esta vazia   
         if not lista_funcionario:
            print("lista vazia")
         
         else:
             
             #Chamando função para lista funcionario
            lista_funcionario_enumerate(lista_funcionario)

            print("\nAtualizar funcionario\n\n")


             #recebendo codigo do funcionario que deseja alterar 
            codigo_funcionario = input("digite o valor do codigo que deseja alterar:")

            codigo_funcionario_inteiro = entrada_dado_usuario_texto_para_inteiro(codigo_funcionario)

            #Desempacotar
            dado_valido, codigo_funcionario =codigo_funcionario_inteiro

            if dado_valido:

                #verificando se o valor do indice existe
                if verifica_valor_indice(codigo_funcionario):
                    novo_nome_funcionario = input("Digite um novo nome para o funcionario :")
                    
                    if verifica_entrada_usuario_vazia(novo_nome_funcionario):
                        print("Campo vazio")
                        continue
                    else:
                        if alterar_funcionario(codigo_funcionario, novo_nome_funcionario):
                            print("funcionario alterado !")
                        else:
                            print("funcionario não alterado")
                else:
                    print("valor codigo não existe")
                    continue
            else:
                print(codigo_funcionario)
                continue 

     #COndição para sair
    elif(escolha_numero == 6):
        print("Sair",end="\n\n")
        rodar_programa = False
    
    #COndição digitados fora do esperado
    else:
        print("Digite um valor dentro das opções !",end="\n\n")

        