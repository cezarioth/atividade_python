class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}"

    def __eq__(self, other):
        if isinstance(other, Produto):
            return self.preco == other.preco
        return False


p1 = Produto("Mouse", 50.0)
p2 = Produto("Teclado", 50.0)
p3 = Produto("Monitor", 700.0)

print(p1) 
print(p2) 
print(p3) 

print(p1 == p2) 
print(p1 == p3)
