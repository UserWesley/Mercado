import menu
#Teste vefica se a lista de produtos é nulo
def teste_funcao_verifica_nulo():
    lista_vazia = []
    lista_com_elementos = ['teste'] 
    if menu.lista_verifica_nulo(lista_vazia):
        print("Passou")
    if not menu.lista_verifica_nulo(lista_com_elementos):
        print("Passou")


teste_funcao_verifica_nulo()