#Lista de produto em tipo dicionario com atributos
lista_produto = [
    {
        'nome_produto' : 'Feijão',
        'preco' : '10.00'
    },
    {
        'nome_produto': "Arroz",
        'preco' : '11.00'
    }
]

#Flag para executar o menu repetidas vezes
rodar_programa = True

#Metodo que verifica se o valor existe dentro do indice
def verifica_valor_indice(numero_indice):
    
    if numero_indice >=0 and numero_indice < len(lista_produto):
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
    except ValueError as erro:
        mensagem_erro = "\nPor favor digite um número !"
        nome_erro = erro.__class__.__name__
        descricao_erro  = erro
        
        return False, mensagem_erro,nome_erro,descricao_erro
        
    #Erro desconhecido
    except Exception:
        erro = "\nErro desconhecido !\n\n"
        return False, erro

#Função para exibir valor cadastrado
def exibir_produto_cadastrado(nome_produto, novo_preco):
    print("\n\nProduto Cadastrado \n")
    print("Nome do Produto cadastrado:", nome_produto,"\n")
    print("Preço R$:", novo_preco,"\n")

#Função para conferir entrada correta de valor do produto
def verifica_entrada_preco_produto(preco_produto):

    try:
        novo_preco_produto = float(preco_produto)
        print(novo_preco_produto)
        return True, novo_preco_produto
        
    #Erro de conversão de texto para float
    except ValueError as erro:
        mensagem_erro = "\nPor favor digite neste padrão 12.12 !"
        nome_erro = erro.__class__.__name__
        descricao_erro  = erro
        
        return False, mensagem_erro,nome_erro,descricao_erro
        
    #Erro desconhecido
    except Exception:
        erro = "\nErro desconhecido !\n\n"
        return False, erro

#Função para adiocionar produtos
def cadastrar_produtos(produto,preco):
    novo_produto = {'nome_produto' : produto, 'preco' : preco}
    if lista_produto.append(novo_produto):
        return False
    
    return True

#Função lista produtos com enumerate
def lista_produtos_enumerate(lista_produto):
    
    print("\n#############################\nListar Produtos",end="\n\n")
    #listando todos os produtos da lista
    for indice,produto_elemento in enumerate(lista_produto):
        print("Código :",indice,"\nNome do Produto :",produto_elemento['nome_produto'], 
              "\nPreço do Produto : R$", produto_elemento['preco'],"\n#############\n")

#FUnção verifica lista produto esta nulo ou não 
def lista_verifica_nulo(lista_produto):

    if not lista_produto:
        return True
    
    return False

#Função apagar todas elementos
def apagar_todos_elementos(lista_produto):
    
    #limpando a lista
    lista_produto.clear()

    if not lista_produto:
        return True
    
    return False

#Método para verficar produto já existe na lista
def verifica_produto_lista(nome_produto):
    if nome_produto in lista_produto:
        return True
    return False

#Metodo para alterar valor da lista
def alterar_produto(codigo_produto,novo_nome_produto, novo_preco):
    
    lista_produto[codigo_produto]['nome_produto'] = novo_nome_produto
    lista_produto[codigo_produto]['preco'] = novo_preco
    
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
    escolha_menu = input("Digite sua escolha : ")

    #Validar entrada do usuário
    verificacao_entrada_usuario = entrada_dado_usuario_texto_para_inteiro(escolha_menu)

    #Verifica entrada do usuário
    if verificacao_entrada_usuario[0]:

        #Descompactar dados
        *_, escolha_numero = verificacao_entrada_usuario

    else:
        #Desempacotar dados
        *_, mensagem_usuario, nome_erro, descricao_erro = verificacao_entrada_usuario
        print(mensagem_usuario)
        print("Nome do Erro :",nome_erro)
        print("Descrição do Erro :",descricao_erro)
        continue

    #Condição para cadastrar Produto -- Programar para evitar itens duplicados
    if(escolha_numero == 1):
        
        #Recebendo do usuário o nome do produto
        nome_produto = input("Digite o nome do Produto:")

        #Recebendo o preço do nome do produto
        preco_produto = input("Digite o preço do produto (11.11) R$ :")
        
        if (verifica_entrada_usuario_vazia(nome_produto)) or (verifica_entrada_usuario_vazia(preco_produto)):
            print("\nAlgum campo vazio! Digite um  nome de produto válido e preço !\n")
            continue

        #Adicionado o nome do produto a lista
        if verifica_produto_lista(nome_produto):
            print("Produto já existe !",end="\n")
            continue
        
        #primeiro valor da lista, True or False para resultado valido
        valida_entrada_preco_produto = verifica_entrada_preco_produto(preco_produto)
        
        if valida_entrada_preco_produto[0]:

            #Descompactar dados
            *_, preco_produto = valida_entrada_preco_produto

        else:
            print(preco_produto)
            *_, mensagem_usuario, nome_erro, descricao_erro = valida_entrada_preco_produto
            print(mensagem_usuario)
            print("Nome do Erro :",nome_erro)
            print("Descrição do Erro :",descricao_erro)
            continue

        print(preco_produto)
        cadastrar_produtos(nome_produto, preco_produto)
        exibir_produto_cadastrado(nome_produto, preco_produto)

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
            codigo_produto_excluido_inteiro = entrada_dado_usuario_texto_para_inteiro(codigo_produto_excluido)

            #Desempacotar
            resultado_dado_verificado, codigo_produto = codigo_produto_excluido_inteiro

            if resultado_dado_verificado:
                
                #Verifica se o código do produto recebido é maior do que a lista
                if verifica_valor_indice(codigo_produto):

                    if remover_produto(codigo_produto):
                        print("Produto Excluido")
                    else :
                        print("Produto não excluido")
                else:
                    print("Digite um código válido")
                    continue
            else:
                print(codigo_produto)
                continue

    #Condição para atualizar produto
    elif(escolha_numero == 5):
       
        #Verificando se a lista esta vazia   
         if not lista_produto:
            print("lista vazia")
         
         else:
            #Chamando função para lista produtos
            lista_produtos_enumerate(lista_produto)

            print("\nAtualizar Produto\n\n")
            
            #recebendo codigo do produto que deseja alterar 
            codigo_do_produto = input("digite o valor do codigo que deseja alterar:")

            validacao_dado_usuario_alteracao = entrada_dado_usuario_texto_para_inteiro(codigo_do_produto)

            #Primeiro valor do indice diz se é True para dado correto 
            if validacao_dado_usuario_alteracao[0]:

                #Desempacotar
                dado_valido, codigo_produto = validacao_dado_usuario_alteracao

                if dado_valido:
            
                    #verificando se o valor do indice existe
                    if verifica_valor_indice(codigo_produto):
                        novo_nome_produto = input("Digite um novo nome para o produto :")
                        
                        #Recebendo o preço do nome do produto
                        preco_produto = input("Digite o preço do produto (11.11) R$ :")
                        
                        if verifica_entrada_usuario_vazia(novo_nome_produto) or verifica_entrada_usuario_vazia(preco_produto):
                            print("Campo vazio do nome ou preço vazio")
                            continue
                        
                        valida_entrada_preco_produto = verifica_entrada_preco_produto(preco_produto)

                        #Valida retorno True numero correto
                        if valida_entrada_preco_produto[0]:
                            *_,novo_preco = valida_entrada_preco_produto 
                            alterar_produto(codigo_produto, novo_nome_produto, novo_preco)
                            print("Produto alterado !")
                        
                        else:
                            *_, mensagem_usuario, nome_erro, descricao_erro = valida_entrada_preco_produto
                            print(mensagem_usuario)
                            print("Nome do Erro :",nome_erro)
                            print("Descrição do Erro :",descricao_erro)
                            continue
            else:
                #Desempacotar dados
                *_, mensagem_usuario, nome_erro, descricao_erro = validacao_dado_usuario_alteracao
                print(mensagem_usuario)
                print("Nome do Erro :",nome_erro)
                print("Descrição do Erro :",descricao_erro)
                continue
                
    #COndição para sair
    elif(escolha_numero == 6):
        print("Sair",end="\n\n")
        rodar_programa = False
    
    #COndição digitados fora do esperado
    else:
        print("Digite um valor dentro das opções !",end="\n\n")
