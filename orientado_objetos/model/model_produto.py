#Classe que representa o modelo de produto
class Produto:

    #Semelhante ou igual ao construtor em java
    def __init__(self):
        self._id = id
        self._nome = "nome"
        self._marca = "Marca"
        self._preco = 0.0

    #Getter do id
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self):
        self._id = id
    




    #Método para cadastrar produto
    def cadastrar_produto(self):
        ...
    
    #Método para listar produtos 
    def listar_produto(self):
        ...

    #Método para alterar produtos
    def alterar_produto(self):
        ...

    #Métoo para remover produtos
    def remover_produto(self):
        ...

    def log_cadastro_produto_json(self):
        ...



p1 = Produto()
p1.nome = "Nomess"
p1.preco = 12.1
print(p1.nome)

p2 = Produto()
p2.nome = "Nomes"
p2.preco = 12.1
print(p2.nome)

leite = Produto()
leite.nome= "Caneca"
leite.preco = 1.1
print(leite.nome)


print(leite.__dict__)
print(vars(leite))