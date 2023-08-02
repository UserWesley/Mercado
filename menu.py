#Lista de produto iniciando vazio
lista_produto = ["Feijao", "Arroz"]

#Flag para executar o menu repetidas vezes
rodar_programa = True

#Função para adiocionar produtos
def cadastrar_produtos(produto):
    if lista_produto.append(produto):
        return False
    else:
        return True

#Função lista produtos com enumerate
def lista_produtos_enumerate(lista_produto):
    
    print("Listar Produtos",end="\n\n")
    #listando todos os produtos da lista
    for indice,produto_elemento in enumerate(lista_produto):
        print("Código",indice,"Produto :",produto_elemento)

#FUnção verifica lista produto esta nulo ou não 
def lista_verifica_nulo(lista_produto):

    if not lista_produto:
        return True
    else:
        return False

#Função apagar todas elementos
def apagar_todos_elementos(lista_produto):
    
    #limpando a lista
    lista_produto.clear()

    if not lista_produto:
        return True
    else:
        return False

#Método para verficar produto já existe na lista
def verifica_produto_lista(nome_produto):
    if nome_produto in lista_produto:
        return True
    else:
        return False

#Metodo para alterar valor da lista
def alterar_produto(codigo_produto,novo_nome_produto):
    
    lista_produto[codigo_produto] = novo_nome_produto
    if novo_nome_produto :
        return False
    else:
        return True
    
#Remover produto
def remover_produto(codigo_produto_excluido_inteiro):
    #Adicionando indice para ajudar na removoção e evitar erros de digitação 
    #pop retorna valor tipo string Del não tem retorno
    #Produto por valor na lista e removendo
    del lista_produto[codigo_produto_excluido_inteiro]
    return True
        
#Função menu de produtos
def exibir_menu_produtos():

    #Lista de Menu
    print("#########################\n","Digite seu Escolha",end ="\n\n")
    print("1 - Cadastrar Produto")
    print("2 - Lista Produto")
    print("3 - Excluir lista inteira Produtos")
    print("4 - Excluir produto selecionado")
    print("5 - Atualizar Produto")
    print("6 - Sair", end="\n\n")

#Executando enquanto variável for True
while rodar_programa: 
    
    #Chamanado método para exibir menu de produtos
    exibir_menu_produtos()

    #Escolha do usuário - Observo que o retorno é tipo string
    escolha = input("Digite sua escolha : ")

    #Lembra de usar corretamente tratar o erro
    try:
        #Tentando converter tipo string para int
        escolha_numero = int(escolha)

    except:
        print("Digite um valor dentro das opções!",end="\n\n")
        continue
    
    #Condição para cadastrar Produto -- Programar para evitar itens duplicados
    if(escolha_numero == 1):
        
        #Recebendo do usuário o nome do produto
        nome_produto = input("Digite o nome do Produto:")

        #Adicionado o nome do produto a lista
        if verifica_produto_lista(nome_produto):
            print("Produto já existe !",end="\n")
            continue
        
        else:
            if cadastrar_produtos(nome_produto):
                print("Nome do Produto cadastrado:", nome_produto,"\n")
            else:
                print("Produto não cadastrado")

    #COndição para lista Produtos
    elif(escolha_numero == 2):
        if lista_verifica_nulo(lista_produto):
            print('Lista vazia !\n')

        else:
            lista_produtos_enumerate(lista_produto)
    
    #COndição para excluir Produto
    elif(escolha_numero == 3):

        if apagar_todos_elementos(lista_produto):
            print("Todos elementos excluidos")
        else:
            print("Não excluido !")

    #COndição para excluir produto selecionado
    #Verificar a duplicidade de código e como orientado a objetos ou funções ajudam 
    elif(escolha_numero == 4):

        if lista_verifica_nulo(lista_produto):
            print("Lista Vazia !")

        else:

            #Chamando função para exibir lista de produtos
            lista_produtos_enumerate(lista_produto)

            print("Excluir Produto Selecionado",end="\n\n")
            
            #Recebendo valor em string do código do produto
            codigo_produto_excluido = input("Digite o código do produto que você deseja excluir :")
            
            #Tentando converter tipo string para int 
            try:
                codigo_produto_excluido_inteiro = int(codigo_produto_excluido)

            #Tratamento para coódigo em string ou outro caracter diferente !!!! EU sei que devemos tratar o erros, apenas testes
            except:
                print("Digite um código válido")
                continue

            else:
                #Verifica se o código do produto recebido é maior do que a lista
                if codigo_produto_excluido_inteiro > len(lista_produto):
                    print("Valor não existe na lista")   

                else:
                    print(codigo_produto_excluido_inteiro)
                    if remover_produto(codigo_produto_excluido_inteiro):
                        print("Produto Excluido")
                    else :
                        print("Produto não excluido")
                    

    #Condição para atualizar produto
    elif(escolha_numero == 5):
       
        #Verificando se a lista esta vazia   
         if not lista_produto:
            print("lista vazia")
         
         else:
            #Chamando função para lista produtos
            lista_produtos_enumerate(lista_produto)

            print("Atualizar Produto",end="\n\n")
            
            #recebendo codigo do produto que deseja alterar 
            codigo_do_produto = input("digite o valor do codigo que deseja aleterar:")
            try: 
                #convertendo valor do string para inteiro
                codigo_produto_inteiro= int(codigo_do_produto)
            except:
                print("digite algum valor correto")
                continue 
            
            #verificando se o valor do indice existe
            if codigo_produto_inteiro > len(lista_produto):
                print("valor codigo não existe")

            else:
                novo_nome_produto = input("Digite um novo nome para o produto :")
                if alterar_produto(codigo_produto_inteiro, novo_nome_produto):
                    print("Produto alterado !")
                else:
                    print("Produto não alterado")
                
    #COndição para sair
    elif(escolha_numero == 6):
        print("Sair",end="\n\n")
        rodar_programa = False
    
    #COndição digitados fora do esperado
    else:
        print("Digite um valor dentro das opções !",end="\n\n")
