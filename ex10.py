class Funcionario:
    empresa = "Empresa Riot Games" 

    def __init__(self, nome):
        self.nome = nome

    @classmethod
    def alterar_empresa(cls, novo_nome):
        cls.empresa = novo_nome

f1 = Funcionario("Ana")
f2 = Funcionario("Carlos")

print(f1.nome, "-", f1.empresa) 
print(f2.nome, "-", f2.empresa) 

Funcionario.alterar_empresa("Empresa Steam")

print(f1.nome, "-", f1.empresa) 
print(f2.nome, "-", f2.empresa)  