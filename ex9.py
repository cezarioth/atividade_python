class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprovado(self):
        return self.calcular_media() >= 7

aluno1 = Aluno("Maria", [8, 7.5, 9])
aluno2 = Aluno("João", [5, 6, 6.5])

print(f"{aluno1.nome} - Média: {aluno1.calcular_media():.2f} - Aprovado: {aluno1.aprovado()}")
print(f"{aluno2.nome} - Média: {aluno2.calcular_media():.2f} - Aprovado: {aluno2.aprovado()}")

